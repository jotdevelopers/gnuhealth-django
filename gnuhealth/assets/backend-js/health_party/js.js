//alert(csrftoken);
$("#search-results-ethnicity").ready(function () {
	ethnicitySearch();
});

function ethnicitySearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-party/searchEthnicity/" + $('#ethnicity-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccess,
        datatype: 'html'
    });
}

function searchSuccess(data, textStatus, jqXHR) {
    $('#search-results-ethnicity').html(data);
}

$("#search-results-citizenship").ready(function () {
	citizenshipSearch();
});

function citizenshipSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-party/searchCitizenship/" + $('#citizenship-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessCitizenship,
        datatype: 'html'
    });
}

function searchSuccessCitizenship(data, textStatus, jqXHR) {
    $('#search-results-citizenship').html(data);
}