(function() {
    'use strict';

    $(document).ready(function() {
        if (app.DEBUG) {
            setTimeout(function() {
                $(document.body).removeClass('page-loading');
                $(document.body).addClass('page-loaded');
            }, 1500);
        } else {
            $(document.body).removeClass('page-loading');
            $(document.body).addClass('page-loaded');
        }
   });
})();
