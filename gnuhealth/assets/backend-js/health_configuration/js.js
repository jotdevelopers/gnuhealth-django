alert(csrftoken);

$('input.select2-search__field').on('keyup', function() {
      alert($(this).val()); // it alerts with the string that the user is searching
 });


function countrySearch()

{

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


      var input, filter, ul, li, a, i, txtValue;
      input = document.getElementById('country-search');
      filter = input.value.toUpperCase();
      ul = document.getElementById("search-results");
      li = ul.getElementsByTagName('li');

      // Loop through all list items, and hide those who don't match the search query
      for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          li[i].style.display = "";
        } else {
          li[i].style.display = "none";
        }
        }

}


function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}