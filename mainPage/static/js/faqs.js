function searchFAQ() {
    // Obtén el valor ingresado en el campo de búsqueda
    var searchQuery = document.getElementById("searchInput").value.toLowerCase();
    
    // Obtén todas las preguntas y respuestas
    var faqs = document.querySelectorAll(".accordion-body");
    
    // Inicializa una variable para almacenar los resultados de la búsqueda
    var searchResults = "";
    
    // Recorre todas las preguntas y respuestas para buscar coincidencias
    for (var i = 0; i < faqs.length; i++) {
        var faqText = faqs[i].textContent.toLowerCase();
        if (faqText.includes(searchQuery)) {
            // Agrega la pregunta y respuesta coincidente a los resultados de búsqueda
            i=i+1;
            searchResults += "<h3>Respuesta N° "+i+" :</h3>"+ faqText;
            i=i-1;
        }
    }
    
    // Muestra los resultados de la búsqueda en el contenedor
    document.getElementById("searchResults").innerHTML = searchResults;
}
function resetPage() {
    // Recarga la página actual
    location.reload();
}