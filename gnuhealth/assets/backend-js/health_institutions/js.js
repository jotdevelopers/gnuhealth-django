//alert(csrftoken);
$("#search-results-institution").ready(function () {
    institutionSearch();
});

function institutionSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-institutions/searchInstitution/" + $('#institution-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessInstitution,
        datatype: 'html'
    });
}

function searchSuccessInstitution(data, textStatus, jqXHR) {
    $('#search-results-institution').html(data);
}
