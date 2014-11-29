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

        // scroll listener to add fixed
        var top = document.querySelector('.banner').clientHeight;
        window.addEventListener('scroll', function(e) {
            if (window.scrollY > top) {
                $events.classList.add('fixed-left');
            } else if (window.scrollY < top) {
                $events.classList.remove('fixed-left');
            }
        });
    };

})();
