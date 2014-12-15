/**
 * Unlike other modules init does not have to be
 * called for this. It will auto start if the
 * tag user-settings is in the DOM
 */
(function() {
    'use strict';

    var $el = $('.user-settings');
    if ($el.size() === 0) {
        return;
    }

    var loggedIn = $el.hasClass('logged-in');

    /**
     * Dropdown when you click your name on the top right
     * @type {Boolean}
     */
    var dropdownActive = false;
    var dropdownTimer = null;
    var $dropdown = $('.user-dropdown');

    $el.find('.text').on('click', function(e) {
            e.preventDefault();

            if (!loggedIn) {
                showModal();
                return;
            }

            showDropdown();
        });

    function dropdownMouseOver(e) {
        if (dropdownTimer) {
            window.clearTimeout(dropdownTimer);
            dropdownTimer = null;
        }
    }

    function dropdownMouseOut(e) {
        dropdownTimer = window.setTimeout(hideDropdown, 1000);
    }

    function hideDropdown() {
        $el.removeClass('dropdown-active');
        dropdownActive = false;

        $dropdown.off('mouseover', dropdownMouseOver);
        $dropdown.off('mouseout', dropdownMouseOut);

        if (dropdownTimer) {
            window.clearTimeout(dropdownTimer);
            dropdownTimer = null;
        }
    }

    function showDropdown() {
        $el.addClass('dropdown-active');
        dropdownActive = true;

        $dropdown.on('mouseover', dropdownMouseOver);
        $dropdown.on('mouseout', dropdownMouseOut);
    }

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
