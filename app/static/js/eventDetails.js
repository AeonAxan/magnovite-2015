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

        if (isIndividual) {
            if (isRegistered) {
                unregisterSingle();
            } else {
                registerSingle();
            }
        } else {
            if (isRegistered) {
                unregisterTeam();
            } else {
                registerTeam();
            }
        }
    }

    /**
     * Handle unregistration for a single person event
     */
    function unregisterSingle() {
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
                app.notification.notify({
                    text: 'Could not unregister at this time. Please try again later',
                    type: 'error'
                });
            })
            .always(function() {
                NProgress.done();
                inProgress = false;
            });
    }

    /**
     * Handle registration for a single person event
     */
    function registerSingle() {
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
                    app.notification.notify({
                        text: 'Something went wrong! Please try again later',
                        type: 'error'
                    });
                    return;
                }

                if (obj.errorCode === 'profile_incomplete') {
                    // issue a message and a redirect
                    app.notification.notify({
                        text: 'You cannot register without completing your profile!',
                        action: 'Complete Now',
                        type: 'error',
                        persistant: true,
                        actionCallback: function() {
                            window.location.replace('/profile/');
                        }
                    });
                    return;
                }

                app.notification.notify({
                    text: obj.errorMessage,
                    type: 'error'
                });
            })
            .always(function() {
                NProgress.done();
                inProgress = false;
            });
    }

    function unregisterTeam() {
        var $modal = $('#team-detail');

        app.modal.show('#team-detail', function() {
            $modal.off('click', '.js-leave');
        });

        $modal.on('click', '.js-leave', function(e) {
            NProgress.start();
            inProgress = true;

            $.post('/events/api/unregister/' + eventID + '/')
                .done(function() {
                    $registerButton.removeClass('registered');
                    $registerButton.find('.js-text').text('Register');

                    isRegistered = false;
                    app.modal.hide();
                })
                .fail(function(err) {
                    var obj = err.responseJSON;

                    app.notification.notify({
                        text: obj.errorMessage,
                        type: 'error'
                    });
                })
                .always(function() {
                    NProgress.done();
                    inProgress = false;
                });
        });
    }

    function registerTeam() {
        var $modal = $('#team-register');

        app.modal.show('#team-register', function() {
            $modal.off('click', '.js-new-team');
            $modal.off('click', '.js-join-team');

            $modal.removeClass('has-error');
        });

        $modal.on('click', '.js-new-team', handleSubmission);
        $modal.on('click', '.js-join-team', handleSubmission);

        function handleSubmission(e) {
            var $input, id = '';

            var url = '/events/api/register/' + eventID + '/';

            if ($(e.target).hasClass('js-join-team')) {
                $input = $modal.find('input[name=teamId]');

                id = $input.val();
                if (!id || id.length !== 5) {
                    $input.focus();
                    $modal.addClass('has-error');
                    return;
                }

                url = url + id + '/';
            }

            $.post(url)
                .done(function(data) {
                    // populate team detail modal
                    var $teamDetail = $('#team-detail');
                    var $members = $teamDetail.find('.members');

                    $teamDetail.find('.team-id').text(data.teamId);

                    var html = '';
                    $.each(data.members, function(i, val) {
                        if (val.me) {
                            html += '<li class="me">';
                        } else {
                            html += '<li>';
                        }

                        html += val.name + '</li>';
                    });

                    $members.html(html);

                    $registerButton.addClass('registered');
                    $registerButton.find('.js-text').text('View Team');

                    // show the team detail modal
                    app.modal.hide();
                    unregisterTeam();

                    isRegistered = true;
                })
                .fail(function(err) {
                    if (err.status === 404) {
                        // invalid team code
                        $input.focus();
                        $modal.addClass('has-error');
                        return;
                    }

                    var obj = err.responseJSON;

                    if (obj.errorCode === 'profile_incomplete') {
                        app.notification.notify({
                            text: 'You cannot register without completing your profile!',
                            action: 'Complete Now',
                            type: 'error',
                            persistant: true,
                            actionCallback: function() {
                                window.location.replace('/profile/');
                            }
                        });

                        return;
                    }

                    app.notification.notify({
                        text: obj.errorMessage,
                        type: 'error'
                    });
                })
                .always(function() {
                    NProgress.done();
                    inProgress = false;
                });
        }
    }

})();
