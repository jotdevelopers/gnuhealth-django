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

$("#search-results-residence").ready(function () {
	residenceSearch();
});

function residenceSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-party/searchResidence/" + $('#residence-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessResidence,
        datatype: 'html'
    });
}

function searchSuccessResidence(data, textStatus, jqXHR) {
    $('#search-results-residence').html(data);
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

$("#search-results-occupation").ready(function () {
	occupationSearch();
});

function occupationSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-party/searchOccupation/" + $('#occupation-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessOccupation,
        datatype: 'html'
    });
}

function searchSuccessOccupation(data, textStatus, jqXHR) {
    $('#search-results-occupation').html(data);
}



$("#search-results-du").ready(function () {
	duSearch();
});

function duSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-party/searchDU/" + $('#du-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessDU,
        datatype: 'html'
    });
}

function searchSuccessDU(data, textStatus, jqXHR) {
    $('#search-results-du').html(data);
}