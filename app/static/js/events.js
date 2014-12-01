var app = app || {};
app.events = {};

(function() {
    'use strict';

    var cultural = true;
    var technical = true;
    var $events;

    app.events.init = function() {
        $events = document.querySelector('.events');

        var hash = window.location.hash;
        if (hash === '#technical' || hash === '#cultural') {
            $events.classList.remove('filter-technical', 'filter-cultural');
            $events.classList.add('filter-' + hash.substring(1));
        }

        document.querySelector('.js-technical')
            .addEventListener('click', technicalToggle);

        document.querySelector('.js-cultural')
            .addEventListener('click', culturalToggle);

        ['.js-cse', '.js-civil', '.js-mech', '.js-ec'].forEach(function(cls) {
            document.querySelector(cls).addEventListener('click', technicalSubToggle);
        });

        document.querySelector('.pane').addEventListener('click', tagClicked);

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

    function tagClicked(e) {
        if (!e.target.classList.contains('tag')) {
            return;
        }

        $events.classList.remove.apply($events.classList, [
            'filter-cse', 'filter-ec',
            'filter-civil', 'filter-mech',
            'filter-cultural'
        ]);

        $events.classList.add('filter-' + e.target.classList[1]);
    }

    function culturalToggle(e) {
        $events.classList.toggle('filter-cultural');
        cultural = !cultural;
    }

    function technicalToggle(e) {
        var fn;

        if (technical) {
            fn = $events.classList.remove;
        } else {
            fn = $events.classList.add;
        }

        fn.apply($events.classList, [
            'filter-cse', 'filter-ec',
            'filter-civil', 'filter-mech',
            'filter-technical'
        ]);

        technical = !technical;
    }

    function technicalSubToggle(e) {
        var li;

        if (e.target.tagName === 'LI') {
            li = e.target;
        } else {
            li = e.target.parentElement;
        }

        var filter;
        Array.prototype.slice.call(li.classList).forEach(function(cls) {
            if (cls.indexOf('js') !== -1) {
                filter = cls.substring(3);
            }
        });

        $events.classList.toggle('filter-' + filter);
    }

})();
