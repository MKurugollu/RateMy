$(document).ready(function() {
		// JQuery code to be added in here.
		$('#followers').click(function(){
		var catid;
		catid = $(this).attr("data-catid");
		$.get('/ratemy/follow_category/', {category_id: catid}, function(data){
			$('#follower_count').html(data);
			$('#followers').hide();
		})
	})})
