var app = app || {};
app.events = {};

(function() {
    'use strict';

    var cultural = true;
    var technical = true;
    var $events;

    app.events.init = function() {
        $events = $('.events-page');

        var hash = window.location.hash;
        if (hash === '#technical' || hash === '#cultural') {
            $events.removeClass('filter-technical', 'filter-cultural');
            $events.addClass('filter-' + hash.substring(1));
        }

        $('.js-technical').on('click', technicalToggle);
        $('.js-cultural').on('click', culturalToggle);

        ['.js-cse', '.js-civil', '.js-mech', '.js-ec'].forEach(function(cls) {
            $(cls).on('click', technicalSubToggle);
        });

        $('.s-right').on('click', tagClicked);
    };

    function tagClicked(e) {
        if (!$(e.target).hasClass('tag')) {
            return;
        }

        $events.removeClass.apply($events, [
            'filter-cse', 'filter-ec',
            'filter-civil', 'filter-mech',
            'filter-cultural'
        ]);

        $events.addClass('filter-' + e.target.classList[1]);
    }

    function culturalToggle(e) {
        $events.toggleClass('filter-cultural');
        cultural = !cultural;
    }

    function technicalToggle(e) {
        var fn;

        if (technical) {
            fn = $events.removeClass;
        } else {
            fn = $events.addClass;
        }

        fn.call($events, 'filter-cse filter-ec filter-civil filter-mech filter-technical');

        technical = !technical;
    }

    function technicalSubToggle(e) {
        var li = $(e.target).closest('li');

        var filter;
        li.attr('class').split(' ').forEach(function(cls) {
            if (cls.indexOf('js') !== -1) {
                filter = cls.substring(3);
            }
        });

        $events.toggleClass('filter-' + filter);
    }

})();
