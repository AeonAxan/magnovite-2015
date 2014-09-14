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
    },

    /**
     * Draws a line between two atoms based on the distance
     * {Self Contained}
     * {args atomA} : Object of class {Atom}
     * {args atomB} : Object of class {Atom}
     */
    energyLine: function(context, atomA, atomB, baseAlpha) {
        'use strict';

        var energyMinDist = 100;

        var dx, dy, dist, alpha;

        if (atomA.id === atomB.id) {
            return;
        }

        dx = atomB.x - atomA.x;
        dy = atomB.y - atomA.y;
        dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < energyMinDist) {
            alpha = (1 - dist / energyMinDist) * (baseAlpha || 0.2);
            context.strokeStyle = 'rgba(255, 255, 255, ' + alpha + ')';
            context.beginPath();
            context.moveTo(atomA.x, atomA.y);
            context.lineTo(atomB.x, atomB.y);
            context.stroke();
        }
    }
};
