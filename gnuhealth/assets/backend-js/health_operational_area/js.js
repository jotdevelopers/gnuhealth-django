//alert(csrftoken);
$("#search-results-operational").ready(function () {
	operationalAreaSearch();
});

function operationalAreaSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-operational-area/searchOperationalArea/" + $('#operational-area-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccess,
        datatype: 'html'
    });
}

function searchSuccess(data, textStatus, jqXHR) {
    $('#search-results-operational').html(data);
}