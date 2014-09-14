var anim = anim || {};

(function() {
    'use strict';

    /**
     * Game constructor, this will switch to the game mode
     */
    function Game(canvas, context) {
        this.canvas = canvas;
        this.context = context;

        window.requestAnimationFrame(this.draw.bihnd(this));
    }

    Game.prototype.draw = function() {
        var context = this.context;


    };

})();
