/*Template(modelo) de Ajax server para várias requisições*/
function utilizouhoraextra(id){
    console.log("funcionou também");
    console.log(id);
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
