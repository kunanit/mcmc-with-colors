// Main script for color task


// number of questions
// var maxQuestions = 10 // defined from context

var main = function(){

	// initial color retrieved from html context data
	var previousColor = initialColor

	// initialize question
	refreshColors(previousColor);
	var currentQuestion = 1

	$('#max-questions').text(maxQuestions);

	// Repeated task
	$('.color-square').click(function(){
		// save data
		var selectedColor = $(this).css('background-color')
		saveQuestionData(currentQuestion,selectedColor)

		// refresh colors if question limit not reached
		if (currentQuestion<maxQuestions){
			refreshColors(selectedColor);
			currentQuestion++;
			$('#counter-value').text(currentQuestion);
		}
		
		
	})
}

var refreshColors = function(previousColor){
	
	// retrieve proposal color with ajax request
	$.get('/colortask/proposal/',{prevcolor:previousColor,proposalSD:proposalSD}, function(data){
		var proposalColor = data

		// shuffle left/right color display
		var colors = Math.random()<0.5 ? [previousColor,proposalColor] : [proposalColor,previousColor]

		// set colors on display
		$('#color-left').css('background-color',colors[0]);
		$('#color-right').css('background-color',colors[1]);

	});
}

var saveQuestionData = function(currentQuestion,selectedColor){
	var color0 = $('#color-left').css('background-color')
	var color1 = $('#color-right').css('background-color')
	$.get('/colortask/saveQuestionData/',{
		userid:userid,
		currentQuestion:currentQuestion,
		color0:color0,
		color1:color1,
		selectedColor:selectedColor,
	},function(){
		if (currentQuestion>=maxQuestions){
			// redirect after recording participant completed questions
			saveParticipantData();
		}
	});
}

var saveParticipantData = function(){
	$.get('/colortask/saveParticipantData/',{userid:userid},function(){
		// redirect to debrief page
		window.location.href = '/colortask/conclusion/'
	});
}

$(document).ready(main);