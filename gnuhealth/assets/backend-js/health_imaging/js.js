//alert(csrftoken);
$("#search-results-patient-imaging").ready(function () {
    patientSearchImaging();
});

function patientSearchImaging() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health_imaging/searchPatient/" + $('#patient-search-imaging').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessPatient,
        datatype: 'html'
    });
}

function searchSuccessPatient(data, textStatus, jqXHR) {
    $('#search-results-patient-imaging').html(data);
}

$("#search-results-doctor-imaging").ready(function () {
	doctorSearchImaging();
});

function doctorSearchImaging() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health_imaging/searchDoctor/" + $('#doctor-search-imaging').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessDoctor,
        datatype: 'html'
    });
}

function searchSuccessDoctor(data, textStatus, jqXHR) {
    $('#search-results-doctor-imaging').html(data);
}


$("#search-results-test-imaging").ready(function () {
	testSearchImaging();
});

function testSearchImaging() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health_imaging/searchTest/" + $('#test-search-imaging').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessTest,
        datatype: 'html'
    });
}

function searchSuccessTest(data, textStatus, jqXHR) {
    $('#search-results-test-imaging').html(data);
}
