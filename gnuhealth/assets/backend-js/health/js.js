//alert(csrftoken);
$("#search-results-person").ready(function () {
    personSearch();
});

function personSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health/searchPerson/" + $('#person-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessPerson,
        datatype: 'html'
    });
}

function searchSuccessPerson(data, textStatus, jqXHR) {
    $('#search-results-person').html(data);
}

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
        url: "/health/searchInstitution/" + $('#institution-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessInstitution,
        datatype: 'html'
    });
}

function searchSuccessInstitution(data, textStatus, jqXHR) {
    $('#search-results-institution').html(data);
}

$("#search-results-condition").ready(function () {
	conditionSearch();
});

function conditionSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health/searchCondition/" + $('#condition-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessCondition,
        datatype: 'html'
    });
}

function searchSuccessCondition(data, textStatus, jqXHR) {
    $('#search-results-condition').html(data);
}

$("#search-results-procedure").ready(function () {
	procedureSearch();
});

function procedureSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health/searchProcedure/" + $('#procedure-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessProcedure,
        datatype: 'html'
    });
}

function searchSuccessProcedure(data, textStatus, jqXHR) {
    $('#search-results-procedure').html(data);
}