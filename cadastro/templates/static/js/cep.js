// Auto completar pelo CEP
$(document).ready(function () {
    $('#id_cep').focusout(function () {

        var cep = $('#id_cep').val();
        var urlcep = 'https://viacep.com.br/ws/' + cep + '/json/';

        $.ajax({
            url: urlcep,
            type: 'get',
            dataType: 'json',
            success: function (data) {
                console.log(data);
                $('#id_logradouro').val(data.logradouro)
                $('#id_bairro').val(data.bairro)
                $('#id_cidade').val(data.localidade)
                $('#id_estado').val(data.uf)
            },
            error: function (erro) {
                console.log(erro);
            }
        });
    });
});

// Remove o placeholder de cada campo.
// O placeholder foi introduzido pelo form Django
for (var i = 0; i < 11; i++) {
    document.getElementsByClassName('form-control')[i].placeholder='';
}