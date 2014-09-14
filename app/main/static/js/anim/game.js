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
    var mPlaying = false;

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

        // dont draw energy lines during delay
        if (mEnergyDelay > 0) {
            return;
        }

        mAtoms.forEach(function(atom) {
            var tag = anim.common.handleMouse(pointer, atom, mContext);

            if (tag) {
                atom.tag(true);
            }
        });

    }

    function draw() {
        mContext.clearRect(0, 0, mCanvas.width, mCanvas.height);

        if (mEnergyDelay < 500) {
            mPlaying = true;
        }

        // handle inter atom interactions
        mAtoms.forEach(function(atomA) {
            mAtoms.forEach(function(atomB) {
                atomA.collide(atomB);
            });

            // collide with letters
            mExternalEdges.forEach(function(edge) {
                atomA.collideLine(edge);
            });
        });

        // draw atom energies
        interAtomEnergy();
        mouseEnergy();

        // draw the atoms
        mAtoms.forEach(function(atom) {
            atom.update(mContext);
        });

        // draw the letters
        mLetters.forEach(function(letter) {
            letter.draw(mContext);
        });
    }

    // external interface
    anim.game = {
        main: main
    };

})();
