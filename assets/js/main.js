const copiarBtn = document.getElementById('copiarBtn')
const textoParaCopiar = document.getElementById('textoParaCopiar')

copiarBtn.addEventListener('click', async () => {
    try {
        await navigator.clipboard.writeText(textoParaCopiar.textContent)
        mostrarNotificacion('¡Texto copiado!')
    } catch (err) {
        console.error('Error al copiar el texto:', err)
    }
})
function mostrarNotificacion(mensaje) {
    const notificacion = document.createElement('div')
    notificacion.style.cssText = `
                                          position: fixed;
                                          top: 10px;
                                          right: 10px;
                                          padding: 10px;
                                          background-color: #F0F0F0;
                                          border: 1px solid #CCC;
                                          border-radius: 5px;
                                          z-index: 9999;
                                        `
    notificacion.textContent = mensaje
    setTimeout(() => {
        notificacion.parentNode.removeChild(notificacion)
    }, 2000)
    document.body.appendChild(notificacion)
}