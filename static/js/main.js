$(document).ready(function($) {
    $(".table-row").click(function() {
        if($(".table-row").is(':checked'))
            alert('checked');
        else
        {
            // When any item in the list is selected, disable row on click
            window.document.location = $(this).data("href");
        }
    });
});
