document.addEventListener("DOMContentLoaded", function (){
    fetch('../../components/modal_editar_user/m_editar_user.html')
    .then(Response => Response.text())
    .then(html => {

        const container = document.getElementById('modalContainerEditar');
        if (container) {
            container.innerHTML = html;
        }
    });
})

//funcion para mostrar el modal
function mostrarModalEditar() {
    const modal = document.getElementById('modalEditar');
    if (modal) {
        modal.classList.remove('hidden');
    }
}