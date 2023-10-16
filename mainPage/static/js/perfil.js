// perfil.js
document.addEventListener("DOMContentLoaded", function () {
    var body = document.body;
  
    // Verifica si hay un estado almacenado en localStorage
    var isChanged = localStorage.getItem("isChanged") === "true";
  
    // Aplica la clase "cambiado" si es necesario
    if (isChanged) {
      body.classList.add("cambiado");
    }
  
    // Agrega un evento al botón para cambiar el fondo
    document.getElementById("cambiarImagen").addEventListener("click", function () {
      // Cambia el estado y la clase del cuerpo
      isChanged = !isChanged;
      body.classList.toggle("cambiado", isChanged);
  
      // Almacena el estado en localStorage
      localStorage.setItem("isChanged", isChanged.toString());
    });
  });
  