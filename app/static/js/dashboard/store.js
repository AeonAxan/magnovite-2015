var app = app || {};
app.dashboard = app.dashboard || {};
app.dashboard.store = {};

(function() {
    'use strict';

    var cache = {};

    /**
     * Gets the event ids from the global DASH
     * @return {Array} array of ids
     */
    function eventIds() {
        var ids = [];
        window.DASH['events'].forEach(function(event) {
            ids.push(event.id);
        });

        return ids;
    }

    /**
     * Comperator for dates in the format 'day/month/year'
     */
    function dateComperator(a, b) {
        var as = a.split('/');
        var bs = b.split('/');

        for (var i = 2; i >= 0; i--) {
            var val = parseInt(as[i], 10) - parseInt(bs[i], 10);
            if (val !== 0) {
                return val > 0 ? 1 : -1;
            }
        }

        return 0;
    }

    function buildCache(raw) {
        // build summary data
        var out = {
            dates: [],
            events: {},
        };

        var summary = {
            registrations: [],
            views: [],
        };

        raw.sort();

        raw.forEach(function(day) {
            out.dates.push(day.date);
            summary.registrations.push(0);
            summary.views.push(0);

            day.events.forEach(function(event) {
                if (!out.events[event.title]) {
                    out.events[event.title] = {
                        registrations: [],
                        views: []
                    };
                }

                var obj = out.events[event.title];

                obj.registrations.push(event.registrations);
                obj.views.push(event.views);

                summary.registrations[summary.registrations.length-1]
                    += event.registrations;
                summary.views[summary.views.length-1]
                    += event.views;
            });
        });

        summary.dates = out.dates;

        // cache
        cache['time'] = new Date();
        cache['raw'] = raw;
        cache['data'] = out;
        cache['summary'] = summary;
    }

    /**
     * Returns summaryData
     * @param  {Function} callback callback on success
     * @param  {boolean}   noCache  if true, cache will not be used
     */
    app.dashboard.store.summaryData = function(callback, noCache) {
        if (!noCache && cache['summary']) {
            return cache['summary'];
        }

        app.dashboard.api.getAnalytics(eventIds(), function(data) {
            buildCache(data);

            callback(cache['summary']);
        });
    }

})();
