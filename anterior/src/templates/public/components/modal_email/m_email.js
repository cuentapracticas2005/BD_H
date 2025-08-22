// Funcion para cargar el modal m_email.html y agregarlos al DOM
document.addEventListener("DOMContentLoaded", function () {
  // Cargar el contenido del modal
  fetch("src/templates/public/components/modal_email/m_email.html")
    .then(response => response.text())
    .then(html => {
      //Insercion del modal en el contenedor
      const container = document.getElementById('modalContainer');
      if (container) {
        container.innerHTML = html;
      }
    });
});

//Funcion para mostrar el modal
function mostrarModalEmail() {
  const modal = document.getElementById('modalEmail');
  if (modal) {
    modal.classList.remove('hidden');
  }
}