var app = app || {};
app.profile = {};

(function() {
	'use strict';

	app.profile.init = function() {
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
            ['name', 'active_email', 'mobile', 'college']
                .forEach(function(key) {
                    if ($('input[name=' + key + ']').val() === '') {
                        filled = false;
                    }
                });

            $('.profile-scene').toggleClass('show-warn', !filled);

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

})();
