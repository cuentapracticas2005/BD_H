// Funcion para cargar el modal m_email.html y agregarlos al DOM
document.addEventListener("DOMContentLoaded", function () {
  // Cargar el contenido del modal
  fetch("./modals/modal_email/m_email.html")
    .then(response => response.text())
    .then(data => {
      document.getElementById("modalEmail").innerHTML = data;
    });
});