//event listeners
$('.js-submit').on('click', sendData);
$(document).delegate('.js-pack', 'click',calcPrice);
$(document).delegate('.js-group-events', 'click', calcPrice);
$(document).delegate('.js-workshop-events', 'click', calcPrice);
$(document).delegate('.js-group-events ~ .js-teamid','blur', calcPrice);
$(document).delegate('.js-teamid', 'blur', function(e) {

	//clears the error list
	$('.js-errorlist').html('');

	//valid teamid?
	if($(e.target).val() != "") {
		if(!isTeamValid($(e.target).val())) {
			//display error message
			//find the id of inputbox
			var tId = $(e.target).attr('id');
			showError(tId, ['Invalid Team Id']);
		}
	}
});

//calculates price of events
function calcPrice() {
	var packInp = $('.js-pack:checked');
	var price = 0;

	if (packInp.data('type') == 'single') {
		price = 100;
	} else if(packInp.data('type') == 'multiple') {
		price = 200;
	}

	$('.js-group-events:checked').each(function(i, el) {
		if(!$(el).siblings('.js-teamid').val()) {
			price += 500;
		}
	})

	$('.js-workshop-events:checked').each(function(i, el) {
		price += $(el).data("price");
	})

	$('.js-amount').html('Total Amount: ' + price);
}

//populates the dom with events
function populate() {

	//first radio button checked
	$('.js-radiobuttons').each(function(){
		$('input[type=radio]', this).get(0).checked = true;
	});

	$('.js-events-technical').append(renderEvents(EVENTS.technical, 'js-tech-events'));
	$('.js-events-cultural').append(renderEvents(EVENTS.cultural, 'js-cult-events'));
	$('.js-events-group').append(renderEvents(EVENTS.group, 'js-group-events'));
	$('.js-events-workshop').append(renderEvents(EVENTS.workshop, 'js-workshop-events'));
	calcPrice();
}

//returns the rendered template
function renderEvents(arrEvents, cssclass) {
	var htmlString = "";
	var singleTemp = $('#singleTemplate').html();
	var multiTemp = $('#teamTemplate').html();

	for(var i = 0; i < arrEvents.length; i++) {
		arrEvents[i].cssclass = cssclass || '';

		if(arrEvents[i].is_team) {
			htmlString += render(multiTemp, arrEvents[i])

		} else {
			htmlString += render(singleTemp, arrEvents[i])
		}
	}
	return htmlString;
}

//template rendering, key and value
function render(tempString,obj) {
	var template = tempString;

	$.each(obj, function(key,value) {
		template = template.replace(new RegExp('\\[\\[' + key + '\\]\\]','g'), value);
	})
	return template;
}

/*
	sendData()
	- does field validation
	- sends data
	- handles api errors

*/
function sendData(e) {
	e.preventDefault();
	$('.js-errorlist').html('');

	var arrInp = $('.js-events:checked').not('.js-workshop-events');
	var packInp = $('.js-pack:checked');

	var jsonObj = {};

	jsonObj.name = $('input[name="fullname"]').val();
	jsonObj.email = $('input[name="email"]').val();
	jsonObj.college = $('input[name="college"]').val();
	jsonObj.mobile = $('input[name="mobile"]').val();
	jsonObj.referred = $('input[name="referred"]').val();
	jsonObj.pack = packInp.data('type');
	jsonObj.events = [];

	if(packInp.data('type') == 'single') {
		if (arrInp.not('.js-group-events').not('.js-workshop-events').length > 1) {
			showError('pack', ['Cant register to more than one event with single pack']);
			return;
		}
	}

	for (var i = 0; i < arrInp.length; i++) {
		var eventObj = {};
		eventObj.id = makeId(arrInp[i].id);

		var teamid = $(arrInp[i]).siblings('input').val();
		if(teamid) {
			if(isTeamValid(teamid)) { //write isTeamValid()
				eventObj.teamid = teamid;
			} else {
				showError('tid-'+eventObj.id, ['Invalid Team Id']);
				$('#tid-' + eventObj.id).focus();
				return;
			}
		}

		jsonObj.events.push(eventObj);
	}

	jsonObj.workshops = [];
	$('.js-workshop-events:checked').each(function(i, el) {
		var $el = $(el);

		jsonObj.workshops.push({id: makeId($el.attr('id'))});
	})

	var validResp = isFieldValid(jsonObj);
	if(validResp === true) {

		$.post( '/internal/api/register/', JSON.stringify(jsonObj))
		.done(function(resp) {
			window.location.replace(resp.url);
		})
		.fail(function(err) {
			var obj = err.responseJSON;
			$.each(obj.errors, function(i, el) {
				showError(i, el);
			})
		});
	} else {
		showError(validResp,['this field cant be empty'])
	}
}

//checks teamid syntax
function isTeamValid(teamid) {
	var r = /^[tg][0-9a-f]{5}$/i;
	return teamid.match(r) != null;

}

//checks empty fields, returns id
function isFieldValid(jObj) {
	if (jObj.name == "") {
		return "name";
	}
	else if (jObj.email == "") {
		return "email";
	}
	else if (jObj.college == "") {
		return "college";
	}
	else if (jObj.mobile == "") {
		return "mobile";
	}
	else if (!jObj.pack) {
		showError('form',['Select a pack']);
	}
	else if (jObj.events.length == 0) {
		showError('form', ['Include Atleast One Event']);
	}
	else {
		return true;
	}
}

//display error
function showError(id, errorMsgs) {
	// general case seperately
	
	var	$el = $('#' + id).siblings('.js-errorlist');

	var html = '';
	$.each(errorMsgs, function(i, val) {
		html += '<li>' + val + '</li>';
	});

	$el.html(html);

	// scroll to the element - offsetvalue (in px)
	var scrollPos = $('#' + id).position().top - 30;
	if ($(window).scrollTop() > scrollPos) {
		$(window).scrollTop(scrollPos);	
	}
	
}

function makeId(domId) {
	var parts = domId.split('-');
	return parts[parts.length-1];
}

//initial call
$(function() {
	populate();
})
