/**
 * Unlike other modules init does not have to be
 * called for this. It will auto start if the
 * tag user-settings is in the DOM
 */
(function() {
    'use strict';

    var el = document.querySelector('.user-settings');
    if (!el) {
        return;
    }

    var loggedIn = el.classList.contains('logged-in');

    el.querySelector('.text')
        .addEventListener('click', function(e) {
            e.preventDefault();

            if (!loggedIn) {
                showModal();
                return;
            }

            el.classList.toggle('dropdown-active');
        });

    /**
     * Shows the LogIn dropdown
     */
    function showModal() {
        app.modal.show('#login-modal');
    }

    if (window.location.hash === '#login') {
        showModal();
    }

})();
