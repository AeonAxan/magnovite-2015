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

    if (window.location.hash !== '') {
        var view = window.location.hash.substring(1);
        if (!(view === 'profile' || view === 'schedule' || view === 'help')) {
            view = 'profile';
        }

        selectView(view + '-scene');
        $menu.find('li').removeClass('selected');
        $menu.find('li[data-scene=' + view + '-scene]').addClass('selected');
    } else {
        selectView('profile-scene');
        $menu.find('li').removeClass('selected');
        $menu.find('li[data-scene=profile-scene]').addClass('selected');
    }

    $menu.on('click', 'li', function(e) {
        var target = $(e.target).closest('li');

        if (!target.data('scene')) {
            return;
        }

        selectView(target.data('scene'));
        $menu.find('li').removeClass('selected');
        target.addClass('selected');
    });

    function selectView(view) {
        $scene.removeClass(scenes.join(' '));
        $scene.addClass(view + '-on');
    }

})();
