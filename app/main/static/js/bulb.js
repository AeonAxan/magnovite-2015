var app = app || {};
app.bulb = {};

(function() {
    'use strict';

    var $hexagon = document.querySelector('.hexagon');
    var $bulbSection = document.querySelector('.bulb-section');

    // the classList last added
    var lastClicked = 'default';
    var lastOutClass;

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

        // set up bulb section hovers
        var $circles = Array.prototype.slice.call($hexagon.querySelectorAll('.circle'));
        $circles.forEach(function(circle) {
            circle.addEventListener('mouseover', handleClick);
        });

        return hexLines + hexM + splitPane;
    };

    function handleClick(e) {
        var target = e.target;
        var el = target;

        if (target.classList.contains('cover')) {
            el = target.parentElement;
        }

        var sectionClass = el.dataset.type;
        if (sectionClass === lastClicked) {
            return;
        }

        if (lastClicked) {
            $bulbSection.classList.remove(lastClicked);

            if (lastOutClass) {
                $bulbSection.classList.remove(lastOutClass);
            }

            $bulbSection.classList.add(lastClicked + '-out');
            lastOutClass = lastClicked + '-out';
        }

        lastClicked = sectionClass;
        $bulbSection.classList.add(sectionClass);
    }

})();
