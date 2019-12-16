//alert(csrftoken);
$("#search-results-prof").ready(function () {
    profSearch();
});

function profSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-health-professionals/searchProf/" + $('#prof-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessProf,
        datatype: 'html'
    });
}

function searchSuccessProf(data, textStatus, jqXHR) {
    $('#search-results-prof').html(data);
}

$("#search-results-institution-prof").ready(function () {
	institutionSearchProf();
});

function institutionSearchProf() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-health-professionals/searchInstitutionProf/" + $('#institution-search-prof').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessInstitutionProf,
        datatype: 'html'
    });
}

function searchSuccessInstitutionProf(data, textStatus, jqXHR) {
    $('#search-results-institution-prof').html(data);
}
