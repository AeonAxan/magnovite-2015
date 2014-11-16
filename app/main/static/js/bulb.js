var app = app || {};
app.bulb = {};

(function() {
    'use strict';

    var $hexagon = document.querySelector('.hexagon');
    var $bulbSection = document.querySelector('.bulb-section');

    /**
     * Initializes the bulb
     * @return {number} number of ms bulb needs to initialize
     */
    app.bulb.init = function() {
        // time needed for hexagon animations
        var hexLines = 400 * 2;
        var hexM = 2000;

        // time needed for pane split animation
        var splitPane = 300 + 600;

        $hexagon.classList.add('hex-load');

        setTimeout(function() {
            $bulbSection.classList.remove('preload');
            $bulbSection.classList.add('loaded');

        }, hexLines + hexM);

        return hexLines + hexM + splitPane;
    };

})();
