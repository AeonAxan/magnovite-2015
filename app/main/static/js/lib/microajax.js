/**
 * http://code.google.com/p/microajax/source/browse/trunk/microajax.js
 * Note, this code has been modified and is not the same as the original
 */

var app = app || {};

app.ajax = function(method, url, callbackFunction) {
    'use strict';

    var postBody = (arguments[2] || "");

    var stateChange = function (object) {
        if (this.request.readyState===4) {
            callbackFunction(request.responseCode, request.responseText);
        }
    };

    var request = (function() {
        if (window.ActiveXObject) {
            return new ActiveXObject('Microsoft.XMLHTTP');
        }
        else if (window.XMLHttpRequest) {
            return new XMLHttpRequest();
        }
        return false;
    })();

    if(request) {
        request.onreadystatechange = stateChange;

        if (method === "POST") {
            request.open("POST", url, true);
            request.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
            request.setRequestHeader('X-CSRFToken', 'token');
        } else {
            request.open("GET", url, true);
        }

        request.send(postBody);
    }
};
