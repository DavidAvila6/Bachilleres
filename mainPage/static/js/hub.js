window.addEventListener('load', function() {
    // Verificar si el modal ya ha sido mostrado
    if (!localStorage.getItem('modalMostrado')) {
        // Si no ha sido mostrado, mostrar el modal
        document.getElementById('container-modal').style.display = 'block';
        // Marcar el modal como mostrado en el almacenamiento local
        localStorage.setItem('modalMostrado', 'true');
    }
})

/* window.addEventListener('load', function() {
    document.getElementById('container-modal').style.display = 'block';
});*/





