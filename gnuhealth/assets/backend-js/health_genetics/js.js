//alert(csrftoken);
$("#search-results-varient").ready(function () {
	varientSearch();
});

function varientSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-genetics/searchVarient/" + $('#varient-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessVarient,
        datatype: 'html'
    });
}

function searchSuccessVarient(data, textStatus, jqXHR) {
    $('#search-results-varient').html(data);
}

$("#search-results-gene").ready(function () {
	geneSearch();
});

function geneSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-genetics/searchGene/" + $('#gene-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessGene,
        datatype: 'html'
    });
}

function searchSuccessGene(data, textStatus, jqXHR) {
    $('#search-results-gene').html(data);
}

$("#search-results-phenotype").ready(function () {
	phenotypeSearch();
});

function phenotypeSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-genetics/searchPhenotype/" + $('#phenotype-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessPhenotype,
        datatype: 'html'
    });
}

function searchSuccessPhenotype(data, textStatus, jqXHR) {
    $('#search-results-phenotype').html(data);
}

$("#search-results-doc").ready(function () {
	docSearch();
});

function docSearch() {
    $.ajax({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        type: "POST",
        url: "/health-genetics/searchDoc/" + $('#doc-search').val() + "/",
        data: 'csrfmiddlewaretoken=' + csrftoken,
        success: searchSuccessDoc,
        datatype: 'html'
    });
}

function searchSuccessDoc(data, textStatus, jqXHR) {
    $('#search-results-doc').html(data);
}