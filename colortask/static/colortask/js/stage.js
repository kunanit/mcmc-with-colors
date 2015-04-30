var main = function(){

	var maxQuestions = 60
	var questionNumber = 1
	var previousColor

	$('#max-questions').text(maxQuestions);

	// initialize a color
	var previousColor = $.get('/colortask/initialize', function(data){
		return data;
	});


	// initialize question
	refreshColors(previousColor);


	// repeated task
	$('.color-square').click(function(){
		alert('new question');
		refreshColors(previousColor);
		// display question number
		questionNumber++;
		$('#counter-value').text(questionNumber);
	})
	

}

$(document).ready(main)

var refreshColors = function(previousColor){
	// get proposal based on previous color
	// var proposalColor
	var proposalColor = $.get('/colortask/proposal',{prevcolor:previousColor}, function(data){
		return data;
	});

	// shuffle left/right color display
	var colors = Math.random()<0.5 ? [previousColor,proposalColor] : [proposalColor,previousColor]

	// set colors on display
	$('#color-left').css('background-color',colors[0])
	$('#color-right').css('background-color',colors[1])

}
