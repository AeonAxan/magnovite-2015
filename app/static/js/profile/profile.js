var app = app || {};
app.profile = {};

(function() {
	'use strict';

	app.profile.init = function() {
        $('#profile-form').on('submit', formSubmit);
        $('.js-pack-activate').on('click', activatePack);
	};

    var activationInProgress = false;
    function activatePack(e) {
        if (activationInProgress) {
            return;
        }

        activationInProgress = true;
        NProgress.start();

        var type = $(e.target).data('type');
        $.get('/payment/generate/' + type + '/')
            .done(function(data) {
                $(data).submit();

                NProgress.set(0.8);
            })
            .fail(function() {
                app.notification.notify({
                    text: 'There was an error, if the problem persists please reach out to us in Help',
                    type: 'error'
                });

                NProgress.done();
                activationInProgress = false;
            })
    }

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

})();
