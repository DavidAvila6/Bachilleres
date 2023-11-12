import calendar
from datetime import date, datetime, timedelta
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils.safestring import mark_safe
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.decorators import login_required
from cal.forms import EventForm



from .models import *
from .utils import Calendar

def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

@login_required
def event(request, event_id=None):
    instance = Event()

    if event_id:
        instance = get_object_or_404(Event, pk=event_id)

    form = EventForm(request.user, request.POST or None, instance=instance)

    if request.method == 'POST' and form.is_valid():
        form.save()
        user = request.user

        # Renderizar el contenido HTML desde la plantilla de correo electrónico
        context = {'user': user, 'event': instance}
        html_content = render_to_string('cal/nuevo_evento.html', context)

        # Enviar correo electrónico de confirmación con contenido HTML
        subject = 'Nuevo evento creado'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]

        send_mail(subject, '', from_email, recipient_list, fail_silently=True, html_message=html_content)
        return redirect('cal:calendar')

    return render(request, 'cal/event.html', {'form': form})


def nuevo_evento(request):
    # Lógica para la vista nuevo_evento, si es necesaria
    return render(request, 'cal/nuevo_evento.html')
