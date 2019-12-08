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

$("#search-results-varient-config").ready(function () {
	varientSearchConfig();
});

function varientSearchConfig() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-configuration/searchVarient/" + $('#varient-search-config').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessVarientConfig,
        datatype: 'html'
    });
}

function searchSuccessVarientConfig(data, textStatus, jqXHR) {
    $('#search-results-varient-config').html(data);
}

$("#search-results-phenotype-config").ready(function () {
	phenotypeSearchConfig();
});

function phenotypeSearchConfig() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-configuration/searchPhenotype/" + $('#phenotype-search-config').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessPhenotypeConfig,
        datatype: 'html'
    });
}

function searchSuccessPhenotypeConfig(data, textStatus, jqXHR) {
    $('#search-results-phenotype-config').html(data);
}

$("#search-results-gene-config").ready(function () {
	geneSearchConfig();
});

function geneSearchConfig() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-configuration/searchGene/" + $('#gene-search-config').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessGeneConfig,
        datatype: 'html'
    });
}

function searchSuccessGeneConfig(data, textStatus, jqXHR) {
    $('#search-results-gene-config').html(data);
}