async function enviarMensagem() {
    const form = document.getElementById('form-contato')
    const dados = new FormData(form)

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
    if (resultado.status === 'success') {
        alert('Mensagem enviada com sucesso!')
        form.reset()
    }
}