//alert(csrftoken);
$("#search-results-patient").ready(function () {
    patientSearch();
});

function patientSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health_lab/searchPatient/" + $('#patient-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessPatient,
        datatype: 'html'
    });
}

function searchSuccessPatient(data, textStatus, jqXHR) {
    $('#search-results-patient').html(data);
}

$("#search-results-type").ready(function () {
	typeSearch();
});

function typeSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health_lab/searchType/" + $('#type-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessType,
        datatype: 'html'
    });
}

function searchSuccessType(data, textStatus, jqXHR) {
    $('#search-results-type').html(data);
}

$("#search-results-doctor").ready(function () {
	doctorSearch();
});

function doctorSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health_lab/searchDoctor/" + $('#doctor-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessDoctor,
        datatype: 'html'
    });
}

function searchSuccessDoctor(data, textStatus, jqXHR) {
    $('#search-results-doctor').html(data);
}
