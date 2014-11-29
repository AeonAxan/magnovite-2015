var app = app || {};
app.events = {};

(function() {
    'use strict';

    app.events.init = function() {
        var $events = document.querySelector('.events');

        var hash = window.location.hash;
        if (hash === '#technical' || hash === '#cultural') {
            $events.classList.remove('filter-technical', 'filter-cultural');
            $events.classList.add('filter-' + hash.substring(1));
        }

        document.querySelector('.js-technical')
            .addEventListener('click', function(e) {
                $events.classList.toggle('filter-technical');
            });

        document.querySelector('.js-cultural')
            .addEventListener('click', function(e) {
                $events.classList.toggle('filter-cultural');
            });
    };

})();
