$(function () {
    $('#datepicker').datetimepicker({
        inline: true,
        sideBySide: true,
        format: 'YY-MM-DD'
    })
    .on("dp.change", function (e) {
        var x = document.getElementsByClassName("datepicker");
        for (var i = 0; i < x.length; i++) {
            x[i].value = e.date.format('YYYY-MM-DD');
            console.log(x[i].value);
        }
    });
});

$(function () {
    $('div[name="timepicker"]').datetimepicker({
        inline: true,
        sideBySide: true,
        format: 'hh:mm a'
    });
});

$(function () {
    $('#start_timepicker').on("dp.change", function(e) {
        var start_time = document.getElementsByClassName("start_timepicker")[0];
        start_time.value = e.date.format('HH:mm');
        console.log(start_time.value);
    });
});

$(function () {
    $('#finish_timepicker').datetimepicker().on("dp.change", function(e) {
        var finish_time = document.getElementsByClassName("end_timepicker")[0];
        finish_time.value =e.date.format('HH:mm');
        console.log(finish_time.value);
    });
});
