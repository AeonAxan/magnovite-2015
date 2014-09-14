var anim  = anim || {};

anim.common = {

    /**
     * Layout letters, all letter should be of height 240
     */
    createLetters: function(canvas, text) {
        'use strict';

        var letterSpacing = 30;

        var letters = [];

        // calculate width needed
        var totalWidth = 0;
        text.split('').forEach(function(c) {
            totalWidth += anim.shapeData[c].width;
            totalWidth += letterSpacing;
        });
        totalWidth -= letterSpacing;

        var letterX = (canvas.width / 2) - (totalWidth / 2);
        text.split('').forEach(function(c) {
            var shape = anim.shapeData[c];

            var letterY = (canvas.height / 2) - (shape.height / 2);
            letters.push(new anim.Letter(letterX, letterY, shape));

            letterX += shape.width + letterSpacing;
        });

        return letters;
    }
};
