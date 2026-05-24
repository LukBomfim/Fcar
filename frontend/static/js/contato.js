async function enviarMensagem() {
    const form = document.getElementById('form-contato')
    const dados = new FormData(form)
    const msgErro = document.getElementById('msg-erro')


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
        alert('Mensagem enviada com sucesso!')
        msgErro.innerText = ''
        form.reset()
    }
}

function digitar(event){
    const input = document.getElementById(event.target.id)
    input.style.border = ''
}