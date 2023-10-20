document.addEventListener("DOMContentLoaded", function () {
    var body = document.body;

    // Verifica si hay un estado almacenado en localStorage
    var modoOscuroActivado = localStorage.getItem("modoOscuro") === "true";

    // Aplica la clase "modo-oscuro" si es necesario
    if (modoOscuroActivado) {
        body.classList.add("modo-oscuro");
    }

    // Agrega un evento al botón en la barra de navegación para cambiar el modo
    document.getElementById("toggleModoOscuroNav").addEventListener("click", function () {
        // Cambia el estado y la clase del cuerpo
        modoOscuroActivado = !modoOscuroActivado;
        body.classList.toggle("modo-oscuro", modoOscuroActivado);

        // Almacena el estado en localStorage
        localStorage.setItem("modoOscuro", modoOscuroActivado.toString());
    });

    // Agrega un evento al botón en el pie de página para cambiar el modo
    document.getElementById("toggleModoOscuroFooter").addEventListener("click", function () {
        // Cambia el estado y la clase del cuerpo
        modoOscuroActivado = !modoOscuroActivado;
        body.classList.toggle("modo-oscuro", modoOscuroActivado);

        // Almacena el estado en localStorage
        localStorage.setItem("modoOscuro", modoOscuroActivado.toString());
    });
});
