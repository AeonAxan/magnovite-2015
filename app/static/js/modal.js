var app = app || {};
app.modal = {};

(function() {
    'use strict';

    var currentModal;

    /**
     * Shows the modal with given id and will handle
     * its close events
     * @param  {string} id DOM id of the modal
     */
    app.modal.show = function(id) {
        if (currentModal) {
            if (currentModal.attr('id') !== id) {
                app.modal.hide();
            } else {
                return;
            }
        }

        currentModal = $(id);
        currentModal.addClass('modal-loading');
        window.setTimeout(function() {
            currentModal.addClass('modal-active');
        }, 50);

        currentModal.on('click', function(e) {
            if ($(e.target).hasClass('modal') || $(e.target).hasClass('close')) {
                app.modal.hide();
            }
        });

    };

    /**
     * Hides the currently visible modal,
     * does nothing if no modal is open
     */
    app.modal.hide = function() {
        if (!currentModal) {
            return;
        }

        currentModal.removeClass('modal-active');
        window.setTimeout(function() {
            currentModal.removeClass('modal-loading');
            currentModal = undefined;
        }, 50);
    };

})();
