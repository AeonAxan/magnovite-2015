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
        document.body.classList.add('modal-loading');
        window.setTimeout(function() {
            document.body.classList.add('modal-active');
        }, 50);

        document.querySelector('.login-modal')
            .addEventListener('click', function(e) {
                if (e.target.classList.contains('login-modal') ||
                    e.target.classList.contains('close')) {
                    closeModal();
                }
            });
    }

    /**
     * Hide the LogIn Modal
     */
    function closeModal() {
        document.body.classList.remove('modal-active');
        window.setTimeout(function() {
            document.body.classList.remove('modal-loading');
        }, 50);
    }

})();
