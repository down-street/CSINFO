$(document).ready(function () {
    var visibleDates = 3;
    var totalDates = $(".date-item").length;
    var currentIndex = 0;

    var daysOfWeek = {
        'Monday': '星期一',
        'Tuesday': '星期二',
        'Wednesday': '星期三',
        'Thursday': '星期四',
        'Friday': '星期五',
        'Saturday': '星期六',
        'Sunday': '星期天'
    };

    // Convert the day of the week to Chinese
    $(".date-item span:last-child").each(function() {
        var dayOfWeek = $(this).text();
        $(this).text(daysOfWeek[dayOfWeek]);
    });

    function updateDateVisibility() {
        var offset = -currentIndex * ($(".date-item").outerWidth(true));

        // Add extra spacing to the left when at the first date
        if (currentIndex === 0) {
            offset = 0;
        }

        // Add extra spacing to the right when at the last date
        if (currentIndex >= totalDates - visibleDates) {
            offset = -(totalDates - visibleDates) * $(".date-item").outerWidth(true);
        }

        $(".date-item-wrapper").css("transform", "translateX(" + offset + "px)");
    }

    $(".date-item").on("click", function () {
        $(".date-item").removeClass("selected");
        $(this).addClass("selected");
        filterMatches($(this).data("date"));
    });

    function filterMatches(date) {
        $(".match-item").hide();
        $(".match-item[data-date='" + date + "']").show();
    }

    // Center today's date
    function centerToday() {
        var todayIndex = $(".date-item[data-date='" + today + "']").index();
        currentIndex = todayIndex - Math.floor(visibleDates / 2);

        if (currentIndex < 0) {
            currentIndex = 0;
        } else if (currentIndex > totalDates - visibleDates) {
            currentIndex = totalDates - visibleDates;
        }

        updateDateVisibility();
    }

    // Initial filtering of today's matches
    filterMatches(today);
    $(".date-item[data-date='" + today + "']").addClass("selected");

    $(".left-arrow").on("click", function () {
        if (currentIndex > 0) {
            currentIndex--;
            updateDateVisibility();
        }
    });

    $(".right-arrow").on("click", function () {
        if (currentIndex < totalDates - visibleDates) {
            currentIndex++;
            updateDateVisibility();
        }
    });

    // Initialize date position
    centerToday();
});
