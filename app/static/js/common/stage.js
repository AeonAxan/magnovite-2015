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
    } else {
        selectView('profile-scene');
    }

    $menu.on('click', 'li', function(e) {
        var target = $(e.target).closest('li');

        if (!target.data('scene')) {
            return;
        }

        selectView(target.data('scene'));
    });

    function selectView(view) {
        $scene.removeClass(scenes.join(' '));
        $scene.addClass(view + '-on');

        $menu.find('li').removeClass('selected');
        $menu.find('li[data-scene=' + view + ']').addClass('selected');
    }

})();
