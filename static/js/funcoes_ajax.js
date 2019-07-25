/*Template(modelo) de Ajax server para várias requisições*/
function utilizouhoraextra(id){

    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    
    $.ajax({
        type: "post",
        url: '/horas/utilizou/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function(result){
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.Horas)
            
        }
    });
}

function desfazerutilizouhoraextra(id){

    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: "post",
        url: '/horas/naoutilizou/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,

        },
        success: function(result){
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.Horas)
            
        }
    });
}