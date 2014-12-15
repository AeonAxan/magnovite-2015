var app = app || {};
app.profile = {};

(function() {
	'use strict';

	app.profile.init = function() {
        // do the height hack only on desktop
        if (app.desktop) {
            fixHeight();
        }

        $('#profile-form').on('submit', formSubmit);
	};

    function clearErrors() {
        $('.errorlist').html('');
    }

    function formSubmit(e) {
        e.preventDefault();
        NProgress.start();

        var form = $(e.target);

        $.post(
            form.attr('action'),
            form.serialize()

        ).done(function(data) {
            clearErrors();

            // if everything is filled make sure the show-warn
            // class is removed
            var filled = true;
            ['name', 'active_email', 'mobile', 'college', 'year']
                .forEach(function(key) {
                    if ($('input[name=' + key + ']').val() === '') {
                        filled = false;
                    }
                });

            $('.profile-right-panel').toggleClass('show-warn', !filled);

        }).fail(function(err) {
            clearErrors();
            var data = err.responseJSON;
            $.each(data.errors, function(key, val) {
                var el = $('input[name=' + key + ']');
                window.el = el;
                el.next('.errorlist').append('<li>' + val[0] + '</li>');
            });

        }).always(function() {
            NProgress.done();
        });
    }

    /**
     * Sets the height to the browser height
     * and hides the scroll bar , if desktop
     */
    function fixHeight() {
        var $page = document.querySelector('.profile-page');
        var $banner = document.querySelector('.banner');
        var height = window.innerHeight - $banner.clientHeight;
        $page.style.height = height + 'px';

        document.body.classList.add('profile-body');
    }

})();
