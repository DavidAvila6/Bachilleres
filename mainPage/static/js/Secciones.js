function agregarFavorito() {
    // Puedes agregar más lógica aquí si es necesario antes de enviar el formulario
    document.getElementById("favoritoForm").submit();
}

document.addEventListener('DOMContentLoaded', function () {
    const rightNavbar = document.querySelector('.right-navbar');

    // Agregar evento hover
    rightNavbar.addEventListener('mouseenter', function () {
        // Cambiar la anchura del menú en hover
        this.style.width = '250px'; // O el ancho deseado en hover
    });

    // Agregar evento de salida del hover
    rightNavbar.addEventListener('mouseleave', function () {
        // Cambiar la anchura del menú cuando se sale del hover
        this.style.width = '50px'; // Anchura mínima cuando no está en hover
    });
});







