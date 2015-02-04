EVENTS = {
	"technical": [
	{
		"id": 9,
		"title": "Robitics",
		"is_team": false
	},
	{
		"id": 10,
		"title": "CAD Modelling",
		"is_team": true
	}
	],

	"cultural": [
	{
		"id": 11,
		"title": "Shipwreck",
		"is_team": true
	},
	{
		"id": 8,
		"title": "Counter Strike",
		"is_team": true
	}
	],

	"group": [
	{
		"id": 12,
		"title": "Group Dance",
		"is_team": true
	}
	],

	"workshop": [
	{
		"id": 20,
		"title": "Android WorkShop",
		"is_team": false,
		"price": 1000
	},
	{
		"id": 21,
		"title": "Windows Dev Workshop",
		"is_team": false,
		"price": 600
	},
	{
		"id": 22,
		"title": "Apple Dev Workshop",
		"is_team": false,
		"price": 1400
	}
	]
}



$('.js-submit').on('click', sendData);
$(document).delegate('.js-pack', 'click',calcPrice);
$(document).delegate('.js-group-events', 'click', calcPrice);
//listen to workshop check
//if checked find the price and adds it to the price
$(document).delegate('.js-workshop-events', 'click', calcPrice);
$(document).delegate('.js-group-events ~ .js-teamid','blur', calcPrice);
$(document).delegate('.js-teamid', 'blur', function(e) {
	//if not empty then check team id
	//clear all the errors
	$('.js-errorlist').html('');
	if($(e.target).val() != "") {
		//check for valid team id 
		//if it return false invalid team id
		if(!isTeamValid($(e.target).val())) {
			//display error message
			//find the id of inputbox
			var tId = $(e.target).attr('id');
			showError(tId, ['Invalid Team Id']);
		}
	}
});


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


function populate() {
	$('.js-radiobuttons').each(function(){
		$('input[type=radio]', this).get(0).checked = true;
	});
	$('.js-events-technical').append(renderEvents(EVENTS.technical));
	$('.js-events-cultural').append(renderEvents(EVENTS.cultural));
	$('.js-events-group').append(renderEvents(EVENTS.group, 'js-group-events'));
	$('.js-events-workshop').append(renderEvents(EVENTS.workshop, 'js-workshop-events'));
	calcPrice();
}

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

function render(tempString,obj) {
	var template = tempString;
	$.each(obj, function(key,value) {
		template = template.replace(new RegExp('\\[\\[' + key + '\\]\\]','g'), value);
	})
	return template;
}

function sendData(e) {
	e.preventDefault();
	$('.js-errorlist').html('');

	var arrInp = $('.js-events:checked');
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
		eventObj.id = arrInp[i].id;

		var teamid = $(arrInp[i]).siblings('input').val();
		if(teamid) {
			if(isTeamValid(teamid)) { //write isTeamValid()
				eventObj.teamid = teamid;
			} else {
				//display {{general error}}
				showError('tid-'+eventObj.id, ['Invalid Team Id']);
				$('#tid-' + eventObj.id).focus();
				return;
			}
		}

		jsonObj.events.push(eventObj);
	}

	var validResp = isFieldValid(jsonObj);
	if(validResp === true) {
		// call api
		
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

function isTeamValid(teamid) {
	var r = /^[tg][0-9a-f]{5}$/i;
	return teamid.match(r) != null;

}

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

function showError(id, errorMsgs) {
	// general case seperately
	var $el;
	if (id == 'form') {
		$el = $('.js-general-errors .js-errorlist');
	} else {
		$el = $('#' + id).siblings('.js-errorlist');
	}

	var html = '';
	$.each(errorMsgs, function(i, val) {
		html += '<li>' + val + '</li>';
	});

	$el.html(html);
}



$(function() {

	populate();	
})