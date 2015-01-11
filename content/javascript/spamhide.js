$(function() {
    $('#mail').replaceWith(function() {
        var s = $(this).text().replace(' [at] ', '@').replace(' [dot] ', '.').replace(' [dot] ','.');
        return '<a href="mailto:' + s + '">' + s + '</a>';
    });
});
