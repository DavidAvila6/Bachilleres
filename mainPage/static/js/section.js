
const accordion = document.getElementsByClassName('AcordeonContainer');

for (i=0; i<accordion.length; i++) {
  accordion[i].addEventListener('click', function () {
    this.classList.toggle('active')
  })
}

document.addEventListener('DOMContentLoaded', function() {
  var labels = document.querySelectorAll('.AcordeonLabel h2');
  labels.forEach(function(label) {
    label.addEventListener('click', function() {
      var content = this.nextElementSibling;
      content.classList.toggle('active');
    });
  });
});