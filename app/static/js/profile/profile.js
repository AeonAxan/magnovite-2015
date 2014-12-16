var app = app || {};
app.profile = {};

(function() {
	'use strict';

    var $list, $container;
    var currentView = 'profile-view';


	app.profile.init = function() {
        $('#profile-form').on('submit', formSubmit);

        $container = $('.profile-page .right-container');
        $list = $('.js-profile-nav');

        $list.on('click', 'li', function(e) {
            choseView($(e.target).data('class'));
        });

        if (window.location.hash !== '') {
            choseView(window.location.hash.substring(1));
        }
	};

    function choseView(view) {
        if (view.indexOf('-view') === -1) {
            view = view + '-view';
        }

        if (view === currentView) {
            return;
        }

        $list.find('li').removeClass('selected');

        $list.find('li[data-class=' + view + ']').addClass('selected');
        $container.removeClass(currentView);
        $container.addClass(view);
        currentView = view;
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
