(function() {
    'use strict';

    // guard block
    if (!$(document.body).hasClass('stage-view')) {
        return;
    }

    var $menu = $('.js-scene-menu');
    var $scene = $('.s-right');

    var scenes = [];
    $menu.find('li').each(function(i, li) {
        scenes.push($(li).data('scene') + '-on');
    });

    $menu.on('click', 'li', function(e) {
        var target = $(e.target).closest('li');

        if (!target.data('scene')) {
            return;
        }

        $scene.removeClass(scenes.join(' '));
        $scene.addClass(target.data('scene') + '-on');

        $menu.find('li').removeClass('selected');
        target.addClass('selected');
    });

})();
