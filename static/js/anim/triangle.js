var anim = anim || {};

(function() {
    'use strict';

    // highlight fade speeds
    var fadeInSpeed = 0.01;
    var fadeOutSpeed = 0.005;
    var bumpAlpha = 0.3;

    var colors = [
        {
            fill: '#313886',
            highlight: 'rgba(151, 158, 236, '
        },
        {
            fill: '#1d226e',
            highlight: 'rgba(80, 85, 161, '
        },
        {
            fill: '#0e145d',
            highlight: 'rgba(65, 71, 144, '
        },
        {
            fill: '#2e347c',
            highlight: 'rgba(97, 103, 175,'
        }
    ];

    function Triangle(vertices, triangle) {
        var $this = this;
        this.cordinates = [
            vertices[triangle[0]],
            vertices[triangle[1]],
            vertices[triangle[2]]
        ];

        var rand = Math.floor(Math.random() * colors.length);
        this.color = colors[rand];

        this.highlightAlpha = 0;
        this.fading = 'null';

        // delay for the fading
        this.delay = 0;
    }

    Triangle.prototype.getCallback = function() {
        var $this = this;

        return function(atom) {
            $this.highlightAlpha = Math.min($this.highlightAlpha + bumpAlpha, 1);
            $this.fading = 'in';

            $this.updateHighlight();
        };
    };

    Triangle.prototype.updateHighlight = function() {
        if (this.fading === 'in') {
            this.highlightAlpha = Math.min(this.highlightAlpha + fadeInSpeed, 1);
        } else if (this.fading === 'out') {
            this.highlightAlpha = Math.max(this.highlightAlpha - fadeOutSpeed, 0);
        }

        if (this.highlightAlpha === 0) {
            this.fading = 'null';
        } else if (this.highlightAlpha === 1) {
            this.fading = 'out';
        }
    };

    Triangle.prototype.draw = function(context) {
        if (this.delay > 0) {
            this.delay -= 15;
            return;
        }

        var cord = this.cordinates;
        context.save();

        context.beginPath();
        context.moveTo(cord[0][0], cord[0][1]);
        context.lineTo(cord[1][0], cord[1][1]);
        context.lineTo(cord[2][0], cord[2][1]);
        context.closePath();

        context.fillStyle = this.color.fill;
        context.fill();

        if (this.highlightAlpha > 0) {
            context.fillStyle = this.color.highlight + this.highlightAlpha + ')';
            context.fill();

            this.updateHighlight();
        }

        context.restore();
    };

    anim.Triangle = Triangle;

})();
