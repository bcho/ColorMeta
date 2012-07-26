(function() {
    $(document).ready(function() {
        $(window).onresize = function() {
            $('iframe').width($(this).width());
            $('iframe').height($(this).height());
        }
        $('iframe').width($(window).width());
        $('iframe').height($(window).height());
        $('.color').each(function() {
            var color = $(this).attr('color-data');
            $(this).css({background: color, color: color});
        });
    });
})();
