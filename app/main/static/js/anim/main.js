var anim = anim || {};

(function() {
    'use strict';

    var mCanvas = document.getElementById('canvas');
    var mContext = mCanvas.getContext('2d');

    var mPointer;
    var mTouching;

    var mMode = 'logo';
    var mDrawFn;

    /**
     * Entry point for the landing page animation
     * This is the only external function
     * that needs to be called
     */
    function init() {
        if (!Modernizr.canvas) {
            window.alert('blah');
        }

        if (window.innerWidth < 767) {
            anim.mobile = true;
        } else {
            anim.desktop = true;
        }

        if (Modernizr.touch) {
            anim.touch = true;
        }

        if (!anim.mobile) {
            // if not mobile, set landings height to browser
            // height, in mobile canvas is equal to browser height
            var landing = document.getElementsByClassName('landing')[0];
            landing.style.height = window.innerHeight + 'px';
        }

        if (document.readyState === "complete" || document.readyState === "loaded") {
            app.main();
        } else {
            document.addEventListener('DOMContentLoaded', _ready);
        }
    }

    /**
     * The DOM ready callback
     */
    function _ready() {
        if (anim.touch) {
            mPointer = anim.util.captureTouch(mCanvas);

            // add a 300 ms delay to touch so scrolling smoothly works
            var touchstart;
            mCanvas.addEventListener('touchstart', function() {
                touchstart = new Date();
            });

            mCanvas.addEventListener('touchend', function() {
                mTouching = false;
                touchstart = undefined;
            });

            mCanvas.addEventListener('touchmove', function(e) {
                if (touchstart && (new Date() - touchstart) > 300) {
                    mTouching = true;
                    e.preventDefault();
                }
            });

        } else {
            mPointer = anim.util.captureMouse(mCanvas);
        }

        // set up canvas
        var height = window.innerHeight;
        if (anim.desktop) {
            // we have a 250height timer on desktop
            height -= 250;
        }

        mCanvas.setAttribute('width', window.innerWidth);
        mCanvas.setAttribute('height', height);

        // show the logo
        mDrawFn = anim.logo.main(mCanvas, mContext);
        window.requestAnimationFrame(loop);
    }

    /**
     * This will get called on requestAnimationFrame
     */
    function loop() {
        window.requestAnimationFrame(loop);
        mDrawFn();
    }

    function changeMode(mode) {
        if (mode === 'game') {
            mDrawFn = anim.game.main(mCanvas, mContext);

        } else if (mode === 'logo') {
            mDrawFn = anim.logo.main(mCanvas, mContext);
        }
    }

    /**
     * Returns undefined or an object with x,y cords
     */
    function getPointer() {
        if (anim.touch && !mTouching) {
            return undefined;
        }

        return mPointer;
    }

    // external interface
    anim.init = init;
    anim.changeMode = changeMode;
    anim.getPointer = getPointer;

})();
