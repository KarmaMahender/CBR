/**
 * Created by Nemesis on 21-09-2015.
 */
$(document).ready(function () {
    $(document).keypress(function (e) {
        if (e.which == 13) {
            search();
        }
    });
    $("#btnSearch").click(function () {
        search();
    });
    function setloadingimage() {
        $("#iSearch").removeClass();
        $("#iSearch").addClass("fa fa-spinner fa-spin");
    }

    function clearLoadingImage() {
        $("#iSearch").removeClass();
        $("#iSearch").addClass("fa fa-search");
    }

    function search() {
        setloadingimage();
        var ajax_url = 'search/?q=';
        var q = $('input[name="q"]').val();
        if (!!q) {
            q = encodeURI(q);
            $.get(ajax_url + q, function (data) {
                $("#divSearchResuls").html(data);
                $("#searchbar").removeClass("searchbox");
                $("#searchbar").addClass("searchboxTop");
                clearLoadingImage();
            });
            return false;
        }
        else {
            return false;
        }
    }

});
