window.addEventListener('load', function() {
    var modal = document.getElementById('container-modal');
    var btnModal = document.getElementById('btn-modal');

    // Verificar si la cookie 'modalMostrado' está presente
    var modalMostrado = localStorage.getItem('modalMostrado');

    if (!modalMostrado) {
        // Si la cookie no está presente, mostrar el modal
        modal.style.display = 'block';
    }

    // Asignar un evento al botón de cerrar
    document.getElementById('btn-cerrar').addEventListener('click', function() {
        modal.style.display = 'none';
        
        // Al cerrar el modal, establecer la cookie 'modalMostrado' para evitar que se muestre nuevamente
        localStorage.setItem('modalMostrado', 'true');
    });

    // Asignar un evento al botón de siguiente
    document.getElementById('btn-siguiente').addEventListener('click', function() {
        window.location.href = 'recursos';
    });
});

/* window.addEventListener('load', function() {
    document.getElementById('container-modal').style.display = 'block';
});*/





