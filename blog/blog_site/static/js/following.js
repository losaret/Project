function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(".follow-btn").click(function () {
    var username = $(this).attr('username');
    var follow = $(this).attr('value') != "True";
    $.ajax({
        type: "POST",
        url:  "/user/"+username+"/",
        data: { username: username , follow : follow , csrfmiddlewaretoken: getCookie('csrftoken') },
        success: function () {
            window.location.reload();
        },
        error: function () {
            alert("ERROR !!");
        }
    })
});