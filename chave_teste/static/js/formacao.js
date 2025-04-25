document.addEventListener(  "DOMContentLoaded", () => {
    const botoes = document.querySelectorAll('button[data-group]');
    const form = document.querySelector(".form_time")
    const botaoPadrao = document.querySelector('button[data-group="dupla"]');
    document.querySelector("#nome").focus();



    if (botaoPadrao) {
        botaoPadrao.classList.replace('btn-dark', 'btn-warning');
        atualizar_rota(botaoPadrao);
    }
    

    botoes.forEach((botao) => {
        botao.addEventListener('click', () =>  {
            
            botoes.forEach((b) => b.classList.replace('btn-warning', 'btn-dark'));
            
            botao.classList.replace('btn-dark', 'btn-warning');
        
            atualizar_rota(botao);

        });
    });

    function atualizar_rota(botao) {
        if (botao) {
            const nome = botao.getAttribute("data-group");

            switch (nome) {
                default:
                    form.action = "/times/dupla";
                
                case "trio":
                    form.action = "/times/trio";
                    break;
                case "seis":
                    form.action = "/times/seis";
                    break;
                case "dupla":
                    form.action = "/times/dupla";
                    break;
              
            }
        }
    }
});
