var app = app || {};
app.eventDetails = {};

(function() {
    'use strict';

    var isRegistered;
    var isIndividual;

    // make sure we dont send more than one request at a time
    var inProgress = false;

    // app.CURRENT_EVENT_ID must be set before this script
    var eventID;

    var $registerButton;

    app.eventDetails.init = function() {
        $registerButton = $('.register-button');

        $registerButton.on('click', handleRegister);
        isRegistered = $(document.body).hasClass('registered') || false;
        isIndividual = $(document.body).hasClass('individual') || false;
        eventID = app.CURRENT_EVENT_ID;
    };

    /**
     * Handles the registration logic
     * @param  {EventObject} e Event object
     */
    function handleRegister(e) {
        if (inProgress) {
            return;
        }

        if (isRegistered) {
            unregister();
        } else {
            register();
        }
    }

    function unregister() {
        NProgress.start();
        inProgress = true;

        $.post('/events/api/unregister/' + eventID + '/')
            .done(function() {
                $registerButton.removeClass('registered');
                $registerButton.find('.js-text').text('Register');

                isRegistered = false;
            })
            .fail(function() {
                // alert failure TODO: FIXME
                alert('Could not unregister at this time');
            })
            .always(function() {
                NProgress.done();
                inProgress = false;
            });
    }

    function register() {
        if (isIndividual) {
            // simple registration

            NProgress.start();
            inProgress = true;

            $.post('/events/api/register/' + eventID + '/')
                .done(function() {
                    $registerButton.addClass('registered');
                    $registerButton.find('.js-text').text('Unregister');

                    isRegistered = true;
                })
                .fail(function(err) {
                    var obj = err.responseJSON;
                    if (!obj) {
                        alert('Something went wrong! Please try again later');
                        return;
                    }

                    if (obj.error_code === 'profile_incomplete') {
                        // issue a message and a redirect
                        alert('Complete profile first');
                        return;
                    }

                    alert(obj.error_message);
                })
                .always(function() {
                    NProgress.done();
                    inProgress = false;
                });

            return;
        }

        teamRegister();
    }

    function teamRegister() {
        app.modal.show('#team-register');
    }

})();
