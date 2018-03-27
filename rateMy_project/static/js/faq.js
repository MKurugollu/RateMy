$(document).ready(function(){
    $(".a").hide();
	$(".q").click(function(){
        $(this).next().slideToggle();
    });
});