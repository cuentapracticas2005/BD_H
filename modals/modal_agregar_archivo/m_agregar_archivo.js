// Función para cargar el modal desde m_agregar_archivo.html y agregarlo al DOM
document.addEventListener("DOMContentLoaded", function () {
    fetch('../modals/modal_agregar_archivo/m_agregar_archivo.html')
        .then(response => response.text())
        .then(html => {
            // Insertar el modal en el contenedor
            const container = document.getElementById('modalContainer');
            if (container) {
                container.innerHTML = html;
            }
        });
});

// Función para mostrar el modal (puedes llamarla desde un botón)
function mostrarModalAgregar() {
    const modal = document.getElementById('modalAgregar');
    if (modal) {
        modal.classList.remove('hidden');
    }
}
