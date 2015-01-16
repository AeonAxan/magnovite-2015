var app = app || {};

(function() {
    'use strict';

    if (!app.mobile) {
        return;
    }

    $('.js-drawer').on('click', function(e) {
        openDrawer();
        e.preventDefault();
    });

    function openDrawer() {
        $(document.body).addClass('slide-menu-active');
        $(document.body).on('touchmove', cancelEvent);

        $(document.body).delegate('.slide-menu a, .slide-menu-cover',
                'click', function(e) {

            closeDrawer();
        });
    }

    function closeDrawer() {
        $(document.body).removeClass('slide-menu-active');
        $(document.body).off('touchmove', cancelEvent);
    }

    function cancelEvent(e) {
        e.preventDefault();
    }
})();
