document.addEventListener(  "DOMContentLoaded", () => {
    const botoes = document.querySelectorAll('button[data-group]');
    const form = document.querySelector(".form_time")
    
    botoes.forEach((botao) => {
        botao.addEventListener('click', () =>  {
            
            botoes.forEach((b) => b.classList.replace('btn-info', 'btn-secondary'));
            
            botao.classList.replace('btn-secondary', 'btn-info');
        
            atualizar_rota(botao);
        });
    });

    function atualizar_rota(botao) {
        if (botao) {
            const nome = botao.getAttribute("data-group");

            switch (nome) {
                default:
                    form.action = "/campeonato/dupla";
                    break;
                case "trio":
                    form.action = "/campeonato/trio";
                    break;
                case "seis":
                    form.action = "/campeonato/seis";
                    break;
                case "dupla":
                    form.action = "/campeonato/dupla";
                    break;
                
            }
        }
    }
});
