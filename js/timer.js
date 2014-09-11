var app = app || {};

(function() {
    var magnoviteDate = new Date(2015, 2, 17);

    app.Timer = function() {
        this.tick();
        setInterval(this.tick, 1000);
    }

    /**
     * Returns num as a binary string of length 6
     */
    function toBinary(num) {
        var bin = num.toString(2);

        var padding = 6 - bin.length;
        var output = '';
        for (var i = 0; i < padding; i++) {
            output += '0';
        }

        return output + bin;
    }

    /**
     * Update number on the column
     * {arg binCol} dom node to column
     * {arg value} the value to set, must be a digit
     */
    function updateNum(binCol, value) {
        var dots = binCol.getElementsByClassName('dot');
        dots = Array.prototype.slice.call(dots, 0).reverse();

        var bin = toBinary(value).split('').reverse().join('');
        for (var i = 0; i < dots.length; i++) {
            if (i < bin.length) {
                dots[i].classList.toggle('on', bin[i] === '1');
            } else {
                dots[i].classList.remove('on');
            }
        }
    }

    /**
     * Updates the timer block, given a DOM reference
     * to the block and the value to update to
     */
    function updateTimerBlock(block, value, type) {
        var el = block.getElementsByClassName('numeric')[0];
        el.innerHTML = value;

        // update binary block
        var cols = block.getElementsByClassName('bin-col');
        if (type === 'months') {
            updateNum(cols[0], value);
        } else {
            // two digits
            updateNum(cols[1], value % 10);
            updateNum(cols[0], Math.floor(value / 10));
        }
    }

    /**
     * Updates the seconds and minutes
     */
    app.Timer.prototype.tick = function() {
        var diff = countdown(magnoviteDate);

        var blocks = document.getElementsByClassName('timer-block');
        updateTimerBlock(blocks[0], diff.months, 'months');
        updateTimerBlock(blocks[1], diff.days);
        updateTimerBlock(blocks[2], diff.hours);
        updateTimerBlock(blocks[3], diff.minutes);
        updateTimerBlock(blocks[4], diff.seconds);
    }

 })();
