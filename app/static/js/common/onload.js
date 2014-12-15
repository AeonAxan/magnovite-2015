(function() {
    'use strict';

    // page-loading -> [DOMContentLoaded] -> page-loading -> 2s -> page-finished

    $(document).ready(function() {
        if (app.DEBUG) {
            setTimeout(pageLoaded, 1500);
        } else {
            pageLoaded();
        }
    });

    function pageLoaded() {
        $(document.body).removeClass('page-loading');
        $(document.body).addClass('page-loaded');

        setTimeout(function() {
            $(document.body).addClass('page-finished');
        }, 2000);
    }
})();
