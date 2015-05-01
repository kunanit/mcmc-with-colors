$(document).ready(function(){

	$('#color-left').click(function(){
		$('.alert').css('display','none')
		$('.alert-success').css('display','block');
	});

	$('#color-right').click(function(){
		$('.alert').css('display','none')
		$('.alert-danger').css('display','block');
	});
})
