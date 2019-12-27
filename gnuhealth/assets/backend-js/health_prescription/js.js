//alert(csrftoken);
$("#search-results-medicament").ready(function () {
	medicamentSearch();
});

function medicamentSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-prescriptions/searchMedicament/" + $('#medicament-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessMedicament,
        datatype: 'html'
    });
}

function searchSuccessMedicament(data, textStatus, jqXHR) {
    $('#search-results-medicament').html(data);
}

$("#search-results-dose-unit").ready(function () {
	doseUnitSearch();
});

function doseUnitSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-prescriptions/searchDoseUnit/" + $('#unit-dose-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessUnit,
        datatype: 'html'
    });
}

function searchSuccessUnit(data, textStatus, jqXHR) {
    $('#search-results-dose-unit').html(data);
}
