window.addEventListener('load', function() {
    document.getElementById('container-modal').style.display = 'block';
});


function mostrarSiguiente(actual, siguiente) {
    var modalActual = document.getElementById(actual);
    var modalSiguiente = document.getElementById(siguiente);

    modalActual.style.display = "none";
    modalSiguiente.style.display = "block";
}

function mostrarAnterior(actual, anterior) {
    var modalActual = document.getElementById(actual);
    var modalAnterior = document.getElementById(anterior);

    modalActual.style.display = "none";
    modalAnterior.style.display = "block";
}



