// Función para cargar el modal desde m_create_user.html y agregarlo al DOM
document.addEventListener("DOMContentLoaded", function () {
    fetch('../../src/components/modal_create_user/m_create_user.html')
        .then(response => response.text())
        .then(html => {
            // Insertar el modal en el contenedor
            const container = document.getElementById('modalContainerCrear');
            if (container) {
                container.innerHTML = html;
            }
        });
});

// Función para mostrar el modal (puedes llamarla desde un botón)
function mostrarModalCrear() {
    const modal = document.getElementById('modalCreateUser');
    if (modal) {
        modal.classList.remove('hidden');
    }
}
