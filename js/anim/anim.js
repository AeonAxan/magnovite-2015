var anim = anim || {};

/**
 * Depends on
 * {anim.Letter}
 * {anim.Atom}
 */
(function() {

    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var mouse = anim.util.captureMouse(canvas);

    // the particles moving around
    var atoms = []
    var nAtoms = 30;
    var energyMinDist = 150;

    // mouse effect
    var mouseMaxDist = 150;
    var mouseForce = 0.05;

    // the letters
    var letters = [];

    // array of {Line}s of all external facing edges
    var externalLetterEdges = [];

    /**
     * Must be called to init the animation library
     */
    function init() {
        if (document.readyState == "complete" || document.readyState == "loaded") {
            app.main()
        } else {
            document.addEventListener('DOMContentLoaded', main);
        }
    }

    /**
     * Layout letters, all letter should be of height 240
     */
    function createLetters(text) {
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
        var letterY = (canvas.height / 2) - (240 / 2);
        text.split('').forEach(function(c) {
            var shape = anim.shapeData[c];

            letters.push(new anim.Letter(letterX, letterY, shape));

            letterX += shape.width + letterSpacing;
        });

        return letters;
    }

    /**
     * Essentially the entry point for the app
     * Called after DOM load
     */
    function main() {
        var i;

        canvas.setAttribute('width', window.innerWidth);
        canvas.setAttribute('height', window.innerHeight - 250);

        // init atoms
        for (i = 0; i < nAtoms; i++) {
            atoms.push(new anim.Atom(canvas));
        }

        // init Letters
        letters = createLetters('VTTTV');
        letters.forEach(function(letter) {
            Array.prototype.push.apply(externalLetterEdges, letter.external);
        });

        draw();
    }

    /**
     * Draws a line between two atoms based on the distance
     * {args atomA} : Object of class {Atom}
     * {args atomB} : Object of class {Atom}
     */
    function energyLine(atomA, atomB) {
        var dx, dy, dist, alpha;

        if (atomA.id === atomB.id)
            return;

        dx = atomB.x - atomA.x;
        dy = atomB.y - atomA.y;
        dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < energyMinDist) {
            alpha = (1 - dist / energyMinDist) * 0.2;
            context.strokeStyle = 'rgba(255, 255, 255, ' + alpha + ')';
            context.beginPath();
            context.moveTo(atomA.x, atomA.y);
            context.lineTo(atomB.x, atomB.y);
            context.stroke();
        }
    }

    /**
     * Make the mouse interact with the atoms
     */
    function handleMouse(atom, context) {
        var dx = mouse.x - atom.x;
        var dy = mouse.y - atom.y;
        var dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < mouseMaxDist) {
            var angle = Math.atan2(dy, dx);
            var ax = Math.cos(angle) * mouseForce;
            var ay = Math.sin(angle) * mouseForce;

            atom.vx += ax;
            atom.vy += ay;

            // mouse energy line
            var alpha = (1 - dist / mouseMaxDist) * 0.8;
            context.save()

            context.strokeStyle = 'rgba(0, 255, 0, ' + alpha + ')';
            context.lineWidth = 2;
            context.beginPath();
            context.moveTo(mouse.x, mouse.y);
            context.lineTo(atom.x, atom.y);
            context.stroke();

            context.restore();
        }
    }

    /**
     * The main draw loop
     */
    function draw() {
        window.requestAnimationFrame(draw);
        context.clearRect(0, 0, canvas.width, canvas.height);

        var buffer = 20;
        var isMouseGravityOn = false;
        if (mouse.x > 20 && mouse.x < canvas.width - buffer &&
            mouse.y > 20 && mouse.y < canvas.height - buffer)
            isMouseGravityOn = true;

        // draw energy lines
        atoms.forEach(function(atom) {
            if (isMouseGravityOn) {
                handleMouse(atom, context);
            }

            atoms.forEach(function(atomB) {
                energyLine(atom, atomB);

                // collide atoms with themselves
                atom.collide(atomB);
            });
        });

        // draw atoms
        atoms.forEach(function(atom) {
            // collide atom with letters
            externalLetterEdges.forEach(function(line) {
                atom.collideLine(line);
            });

            atom.update(context);
        });

        // draw letters
        letters.forEach(function(letter) {
            letter.draw(context);
        })

        // draw external edges seperately : // TODO: DEBUG
        // externalLetterEdges.forEach(function(line) {
        //     line.draw(context);
        // });
    }

    // set external interface
    anim.init = init;
    anim.canvas = canvas;
    anim.context = context;

})();
