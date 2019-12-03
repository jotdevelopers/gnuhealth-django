//alert(csrftoken);

//alert(csrftoken);
$("#search-results-country").ready(function () {
    countrySearchDu();
});

function countrySearchDu() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-demographics/searchCountry/" + $('#country-search-du').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessCountry,
        datatype: 'html'
    });
}

function searchSuccessCountry(data, textStatus, jqXHR) {
    $('#search-results-country').html(data);
}


$("#search-results-subdiv").ready(function () {
    subdivSearchDu();
});

function subdivSearchDu() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-demographics/searchSubdiv/" + $('#subdiv-search-du').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessSubdiv,
        datatype: 'html'
    });
}

function searchSuccessSubdiv(data, textStatus, jqXHR) {
    $('#search-results-subdiv').html(data);
}


$("#search-results-opsector").ready(function () {
    opsectorSearchDu();
});

function opsectorSearchDu() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-demographics/searchOpsector/" + $('#opsector-search-du').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessOpsector,
        datatype: 'html'
    });
}

function searchSuccessOpsector(data, textStatus, jqXHR) {
    $('#search-results-opsector').html(data);
}
