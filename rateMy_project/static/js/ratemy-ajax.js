$(document).ready(function() {
		// JQuery code to be added in here.
		$('#followers').click(function(){
		var catid;
		catid = $(this).attr("data-catid");
		$.get('/ratemy/follow_category/', {category_id: catid}, function(data){
			$('#follower_count').html(data);
			$('#followers').hide();
		})
	})

	$('#likes').click(function(){
		var postid;
		postid = $(this).attr("data-postid");
		$.get('/ratemy/like_post/', {post_id: postid}, function(data){
			$('#like_count').html(data);
			$('#likes').hide();
		})
	})})
