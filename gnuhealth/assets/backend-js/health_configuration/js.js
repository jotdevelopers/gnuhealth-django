//alert(csrftoken);
$("#search-results").ready(function () {
    countrySearch();
});

function countrySearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-configuration/searchCountry/" + $('#country-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccess,
        datatype: 'html'
    });
}

function searchSuccess(data, textStatus, jqXHR) {
    $('#search-results').html(data);
}