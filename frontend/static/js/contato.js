async function enviarMensagem() {
    const form = document.getElementById('form-contato')
    const dados = new FormData(form)
    const msgErro = document.getElementById('msg-erro')
    const btn = document.getElementById('btn-enviar')
    const spinner = document.getElementById('spinner')
    const btnTexto = document.getElementById('btn-enviar-texto')


    // VERIFICAÇÃO SE TEM ALGUM CAMPO VAZIO
    const inputs = form.querySelectorAll('input, textarea')
    let flag = false

    inputs.forEach (input => {
        if (!input.value){
            input.style.border = '1px solid red'
            flag = true
        }
    })

    if (flag){
        msgErro.innerText = 'Preencha todos os dados *'
        return
    }

    btn.disabled = true
    btnTexto.textContent = 'Enviando...'
    spinner.style.display = 'inline-block'

    try{
        const resposta = await fetch('/contato', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nome: dados.get('nome'),
                email: dados.get('email'),
                telefone: dados.get('telefone'),
                assunto: dados.get('assunto'),
                mensagem: dados.get('mensagem')
            })
            
        })

        const resultado = await resposta.json()
        if (resultado.status === 'sucesso') {
            btnTexto.textContent = 'Enviado!'
            spinner.style.display = 'none'
            msgErro.innerText = ''
            form.reset()
        }
    } catch (erro){
        btnTexto.textContent = 'Tente novamente'
        spinner.style.display = 'none'
        msgErro.innerText = erro
    } finally{
        setTimeout(() => {
            btn.disabled = false
            btnTexto.textContent = 'Enviar'
            spinner.style.display = 'none'
            msgErro.innerText = ''
        }, 3000)
    }
    

}

function digitar(event){
    const input = document.getElementById(event.target.id)
    input.style.border = ''
}