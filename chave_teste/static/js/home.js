document.addEventListener("DOMContentLoaded", () =>{
    const botoes = document.querySelectorAll("button[data-group]");


    botoes.forEach((botao) => {
        botao.addEventListener ("click", () =>{
            mudando_btn(botao);
        });
    });

    function mudando_btn(btn){
        if (btn){
            const button = btn.getAttribute("data-group");
            const form = btn.closest("form")

            switch(button){
                case "camp":
                    form.action = "/campeonato/";
                    break;
                case "amistoso":
                    form.action = "/amistoso/";
                    break;
            }

        }
    }
});