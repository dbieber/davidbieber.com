// Blokus Life Lessons
document.addEventListener('DOMContentLoaded', function () {
    $(".blokus").click(function (e) {
        $(".blokus").each(function (index, el) {
            if (el.innerHTML == "Life") $(el).text("Blokus");else if (el.innerHTML == "life") $(el).text(" Blokus");else if (el.innerHTML == "Blokus") $(el).text("Life");else if (el.innerHTML == " Blokus") $(el).text("life");
        });
    });
}, false);