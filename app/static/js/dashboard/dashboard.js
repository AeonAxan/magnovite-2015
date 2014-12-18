var app = app || {};
app.dashboard = app.dashboard || {};

(function() {
    'use strict';

    if (!$(document.body).hasClass('page-dashboard')) {
        return;
    }

    var summaryChart;
    function showSummaryPage() {
        app.dashboard.store.summaryData(function(obj) {
            window.obj = obj;
            summaryChart = c3.generate({
                bindto: '#chart-summary',
                data: {
                    x: 'x',
                    columns: [
                        ['x'].concat(obj.dates),
                        ['registrations'].concat(obj.registrations),
                        ['views'].concat(obj.views),
                    ]
                },
                axis: {
                    x: {
                        type: 'timeseries',
                        tick: {
                            format: '%d/%m'
                        }
                    }
                }
            });
        });
    }

    showSummaryPage();



})();
