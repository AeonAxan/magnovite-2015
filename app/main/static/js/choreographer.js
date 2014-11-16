/**
 * Handles scrolling,
 *
 * All scrolling is disabled on the page by hijacking
 * mouseweel events and key events (down/up/pgdown/etc)
 *
 * choreographer is also responsible for initializing the bulb
 * at the right time. Bulb's init function should return
 * how many seconds it needs to initialize (scrolling will be
 * hijacked for this time)
 *
 * choreographer also relies on the variable `anim.sectionHeight` which
 * has to be set by the anim functions, it is the height of the first section
 * (logo+timerBanner)
 */

var app = app || {};
app.choreographer = {};

(function() {
    'use strict';

    // disable scrolling
    disableScroll();

    // are we scrolling
    var scrolling = true;

    // current section
    var section = 'section-one';

    // scrollTop of sectiontwo
    var sectionTwo;

    // has the bulb been initialized (the anim)
    var bulbInit = false;

    /**
     * Initializer for choreograhper, must be called after anim
     * loads
     */
    app.choreographer.init = function() {
        document.body.scrollTop = 0;
        scrolling = false;
        sectionTwo = anim.sectionHeight;
    };

    /**
     * Stop choreographer, will disable scrollhijack
     */
    app.choreographer.stop = function() {
        enableScroll();
    };

    /**
     * Call the bulbs initizlier
     */
    function initBulb() {
        // make sure we dont scroll while the bulb is initializing
        scrolling = true;

        // bulb.init returns the ms it needs to initialize
        var timeNeeded = app.bulb.init();

        setTimeout(function() {
            scrolling = false;
        }, timeNeeded);
    }

    /**
     * Called when the user tries to scroll
     * @param  {boolean} down is the scroll down
     */
    function onScroll(down) {
        if (scrolling) {
            return;
        }

        if (down && section === 'section-one') {
            scrollTo(document.body, sectionTwo, 250);
            section = 'section-two';

        } else if (!down && section === 'section-two') {
            scrollTo(document.body, 0, 250);
            section = 'section-one';
        }
    }

    /**
     * Scroll to the offset on the given element
     * @param  {DOMElemenet} element  element to scroll in
     * @param  {number} to       offset to scroll
     * @param  {number} duration duration of the scroll
     */
    // http://stackoverflow.com/questions/4770025/how-to-disable-scrolling-temporarily
    function scrollTo(element, to, duration) {
        var start = element.scrollTop,
            change = to - start,
            currentTime = 0,
            increment = 5;

        var animateScroll = function(){
            currentTime += increment;
            var val = Math.easeInOutQuad(currentTime, start, change, duration);
            element.scrollTop = val;
            if(currentTime < duration) {
                setTimeout(animateScroll, increment);
            } else {
                scrolling = false;

                // if this is the first time we see the bulb start off
                // the bulb animation
                if (section === 'section-two' && !bulbInit) {
                    initBulb();
                }
            }
        };
        animateScroll();
    }

    // left: 37, up: 38, right: 39, down: 40,
    // spacebar: 32, pageup: 33, pagedown: 34, end: 35, home: 36
    var keys = [37, 38, 39, 40];

    function preventDefault(e) {
        e = e || window.event;
        if (e.preventDefault) {
            e.preventDefault();
        }
        e.returnValue = false;
    }

    function keydown(e) {
        for (var i = keys.length; i--;) {
            if (e.keyCode === keys[i]) {
                if (e.keyCode === 38) {
                    onScroll(false);
                } else if (e.keyCode === 40) {
                    onScroll(true);
                }

                preventDefault(e);
                return;
            }
        }
    }

    function wheel(e) {
        onScroll(e.wheelDelta < 0);
        preventDefault(e);
    }

    function disableScroll() {
      if (window.addEventListener) {
          window.addEventListener('DOMMouseScroll', wheel, false);
      }
      window.onmousewheel = document.onmousewheel = wheel;
      document.onkeydown = keydown;
    }

    function enableScroll() {
        if (window.removeEventListener) {
            window.removeEventListener('DOMMouseScroll', wheel, false);
        }
        window.onmousewheel = document.onmousewheel = document.onkeydown = null;
    }

    //t = current time
    //b = start value
    //c = change in value
    //d = duration
    // https://github.com/danro/jquery-easing/blob/master/jquery.easing.js
    Math.easeInOutQuad = function (t, b, c, d) {
        return c*(t/=d)*t*t + b;
    };
})();
