$(document).ready(function () {

    $("#form").on("submit", function (e) {
        var link = $("#pagination2 a.page-link")
        var url = $("#form").data("post-url")
        var formData = new FormData(this)
        e.preventDefault()
        $.ajax({
            type: "POST",
            url: url,

            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                $("#BlogView").empty();

                $("#BlogView").append($(response).find("#BlogView").html())
                $(".wer").empty();
                $(".wer").append($(response).find(".wer").html())
            }

        });
        if (link.hasClass("inactive") || link.parent().hasClass("current")) {} else {
            window.scrollTo(0, 650)

        }
    });

});