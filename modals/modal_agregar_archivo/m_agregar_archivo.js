// Función para cargar el modal desde m_agregar_archivo.html y agregarlo al DOM
document.addEventListener("DOMContentLoaded", function () { //Garantiza que el modal se crague despues de que la pagina este lista
    fetch('../modals/modal_agregar_archivo/m_agregar_archivo.html') //Se usa "fetch() para cargar el contenido desde un archivo HTML externo"
        //Realiza una solicitud HTTP para obtener el contenido del modal
        .then(response => response.text()) //Convierte la respuesta en texto
        .then(html => {
            // Insertar el modal en el contenedor
            const container = document.getElementById('modalContainer');
            if (container) {
                container.innerHTML = html;
            }
        }); // Funcion: Busca un elemento con ID: modalContainer, inserta el contenido del modal en el contenedor si es que este existe
});

// Función para mostrar el modal (puedes llamarla desde un botón)
function mostrarModalAgregar() {
    const modal = document.getElementById('modalAgregar');
    if (modal) {
        modal.classList.remove('hidden');
    }
}
