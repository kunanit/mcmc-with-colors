$(document).ready(function(){

	$('#color-left').click(function(){
		$('.alert').css('display','none')
		$('.alert-success').css('display','block');
	});

	$('#color-right').click(function(){
		$('.alert').css('display','none')
		$('.alert-danger').css('display','block');
	});

	// can use arrow keys to select instead of clicking
	$(document).keydown(function(e) {
		switch(e.which) {
			case 37: // left
				$('#color-left').trigger('click');
				break;

			case 39: // right
				$('#color-right').trigger('click');
				break;

			default: return; // exit this handler for other keys
		}
		e.preventDefault(); // prevent the default action (scroll / move caret)
	});
})
