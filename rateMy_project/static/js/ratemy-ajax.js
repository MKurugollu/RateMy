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
		var b_id;

		postid = $(this).attr("data-postid");
		b_id = $(this).attr("buttonid");

		$.get('/ratemy/like_post/', {post_id: postid,button_id: b_id}, function(data){
			$('#like_count').html(data);
			$('#likes').hide();
			$('#unlike').show();
		})
	})

	$('#unlike').click(function(){
		var postid;
		var b_id;

		postid = $(this).attr("data-postid");
		b_id = $(this).attr("buttonid");
		$.get('/ratemy/like_post/', {post_id: postid,button_id: b_id}, function(data){
			$('#like_count').html(data);
			$('#unlike').hide();
			$('#likes').show()
		})

	})

})
