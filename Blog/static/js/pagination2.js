function pagination() {

    $("#pagination2 a.page-link").click(function (e) {
        let page_url = $(this).attr("href");
        let clase = $(this);
        e.preventDefault()

        $.ajax({
            type: "get",
            url: page_url,
            dataType: "html",
            success: function (data) {
                $("#BlogView").empty();
                $("#BlogView").append($(data).find("#BlogView").html())
                $(".wer").empty();
                $(".wer").append($(data).find(".wer").html())
                if (clase.hasClass("inactive") || clase.parent().hasClass("current")) {} else {
                    window.scrollTo(0, 740)
                }


            }
        })


    })

}

function paginationsearch() {

    $("#paginationsearch a.page-link").click(function (e) {
        let page_url = $(this).attr("href");
        let clase = $(this);

        e.preventDefault()
        $.ajax({
            type: "get",
            url: page_url,
            dataType: "html",
            success: function (data) {
                $("#BlogView").empty();
                $("#BlogView").append($(data).find("#BlogView").html())
                $(".wer").empty();
                $(".wer").append($(data).find(".wer").html())
                if (clase.hasClass("inactive") || clase.parent().hasClass("current")) {} else {
                    window.scrollTo(0, 1)
                }
            }
        })
        /*if ($(this).hasClass("inactive") || $(this).parent().hasClass("current")) {} else {
            window.scrollTo(0, 0)

        }*/
    })

}
$(document).ready(function () {
    pagination()
    paginationsearch()


});
$(document).ajaxStop(function () {
    pagination()
});
$(document).ajaxStop(function () {
    paginationsearch()

});