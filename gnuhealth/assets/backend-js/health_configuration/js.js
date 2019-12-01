
$(document).ready(function () {
    $('#example').DataTable();
    $('.select2').select2();
});



$(function () {
    $('#datetimepicker3').datetimepicker({
        format: 'LT'
    });

function getCookie(name) {
var cookieValue = null;
if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
    $('#search').ready(function(){

        $.ajax({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            type: "POST",
            url: "/health-configuration/searchCountry/"+$('#search').val()+"/",
            data: 'csrfmiddlewaretoken={{csrf_token}}',
            success: searchSuccess,
            datatype: 'html'
        });

    });
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}