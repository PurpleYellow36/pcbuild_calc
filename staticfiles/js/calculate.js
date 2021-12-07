$("#PartsTable").on('input', '.price', function () {
    var calculated_total_sum = 0;
  
    $("#PartsTable .price").each(function () {
        var get_value = $(this).val();
        if ($.isNumeric(get_value)) {
           calculated_total_sum += parseFloat(get_value);
           }                  
         });
           $("#total_sum_value").html(calculated_total_sum);
    });

function ClearPrice() {
    $("#graphic_board").val(null);
    $("#drive").val(null);
    $("#mother_board").val(null);
    $("#cooler").val(null);
    $("#case").val(null);
    $("#memory").val(null);
    $("#power").val(null);
    $("#os").val(null);

    $("#total_sum_value").html(null);
}