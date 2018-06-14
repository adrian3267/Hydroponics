 function noop() {};

 function hidefield() {
    hidefield = noop; // swap the functions

    $('.other_option').hide();

    if ($('#id_application_method').val()=="Other"){
        $('.other_option').show();
    }
}

    $(document).ready(function() {
        $('.datepicker').datepicker();
    });


$(document).ready(function(){
    hidefield();
    $('#id_application_method').on('change', function() {

        $('.other_option').hide();
        $('#' + $(this).val() ).show();

    });

});
