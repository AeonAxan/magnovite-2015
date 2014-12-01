var app = app || {};
app.profile = {};

(function() {
	'use strict';

	app.profile.init = function() {
		var $page = document.querySelector('.profile-page');
		var $banner = document.querySelector('.banner');
		var height = window.innerHeight - $banner.clientHeight;
		$page.style.height = height + 'px';

		document.body.classList.add('profile-body');
	}

})();