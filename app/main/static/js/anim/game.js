var anim = anim || {};

(function() {
    'use strict';

    var mCanvas, mContext;

    var mAtoms;
    var mNumAtoms = 30;

    var mLetters;
    var mText = 'TTVTT';
    var mExternalEdges;

    // timing delays
    var ATOM_MIN_DELAY = 1000;
    var ATOM_VAR_DELAY = 1000;
    var ENERGY_DELAY = 2000;

    var mEnergyDelay = ENERGY_DELAY;

    // game vars
    // state = ready : not playing but ready to play
    // state = playing : playing the game
    // state = paused : game is paused
    var mState = 'ready';

    /**
     * Game constructor, this will switch to the game mode
     */
    function main(canvas, context) {
        var i;

        mCanvas = canvas;
        mContext = context;

        mAtoms = [];
        mExternalEdges = [];

        // init atoms
        for (i = 0; i < mNumAtoms; i++) {
            mAtoms.push(new anim.Atom(canvas,
                ATOM_MIN_DELAY + Math.random() * ATOM_VAR_DELAY));
        }

        // init letters
        mLetters = anim.common.createLetters(canvas, mText);
        mLetters.forEach(function(letter) {
            Array.prototype.push.apply(mExternalEdges, letter.external);
        });

        document.body.classList.add('game-mode');

        return draw;
    }

    /**
     * Draws interatom energy lines,
     * Also incorporates a delay {mEnergyDelay} which
     * is used on load to animate the energy lines in
     * gradually
     */
    function interAtomEnergy() {
        if (mEnergyDelay > 0) {
            mEnergyDelay -= 15;
            return;
        }

        var alpha;
        if (mEnergyDelay > -500) {
            alpha = (mEnergyDelay / -500) * 0.2;
            mEnergyDelay -= 15;
        }

        mAtoms.forEach(function(atomA) {
            mAtoms.forEach(function(atomB) {
                if (alpha !== undefined) {
                    anim.common.energyLine(mContext, atomA, atomB, alpha);
                } else {
                    anim.common.energyLine(mContext, atomA, atomB);
                }
            });
        });
    }

    /**
     * handles mouse energy of the atoms
     */
    function mouseEnergy() {
        var pointer = anim.getPointer();
        if (!pointer) {
            return;
        }

        // sometimes mouse gets stuck to an edge, so
        // ignore mouse input if too close to edge
        var m = pointer;
        var buffer = 5;
        if (!(m && m.x > buffer && m.x < mCanvas.width - buffer &&
            m.y > buffer && m.y < mCanvas.height - buffer)) {
            return;
        }

        // dont draw energy lines during delay
        if (mEnergyDelay > 0) {
            return;
        }

        mAtoms.forEach(function(atom) {
            var caught = anim.common.handleMouse(pointer, atom, mContext);

            if (caught && mState === 'playing' || mState === 'ready') {
                atom.tag(true);

                if (mState !== 'playing') {
                    startGame();
                }
            }
        });

    }

    /**
     * Called when the game starts
     */
    function startGame() {
        if (mState !== 'ready') {
            return;
        }

        mState = 'playing';
    }

    /**
     * Called when the game is over
     */
    function gameOver() {
        mState = 'paused';
        gameOverDOM();
    }

    function draw() {
        mContext.clearRect(0, 0, mCanvas.width, mCanvas.height);

        if (mState !== 'paused') {
            // calculat and draw energies
            interAtomEnergy();
            mouseEnergy();

            mAtoms.forEach(function(atomA) {
                mAtoms.forEach(function(atomB) {
                    atomA.collide(atomB);
                });

                // collide with letters
                mExternalEdges.forEach(function(edge) {
                    var collide = atomA.collideLine(edge);
                    if (mState === 'playing' && collide && atomA.isTagged()) {
                        gameOver();
                    }
                });
            });
        }

        // draw the atoms
        mAtoms.forEach(function(atom) {
            if (mState !== 'paused') {
                atom.update(mContext);
            }

            atom.draw(mContext);
        });

        // draw the letters
        mLetters.forEach(function(letter) {
            letter.draw(mContext);
        });
    }

    /***
     * DOM Manipulators
     */
    function gameOverDOM(){
        document.body.classList.add('game-over');
    }

    // external interface
    anim.game = {
        main: main
    };

})();
