$(document).ready(function() {
		// JQuery code to be added in here.

    $('#unfollow').hide();
	$('#followers').click(function(){

	    var catid;
	    var b_id;


		catid = $(this).attr("data-catid");
		b_id= $(this).attr("id");

		$.get('/ratemy/follow_category/', {category_id: catid, button_id:b_id}, function(data){
			$('#follower_count').html(data);
			$('#unfollow').show();
			$('#followers').hide();

		})
	})

	$('#unfollow').click(function(){
		var catid;
		var b_id;

		catid = $(this).attr("data-catid");
		b_id = $(this).attr("id");

		$.get('/ratemy/follow_category/', {category_id: catid, button_id:b_id}, function(data){
			$('#follower_count').html(data);
			$('#followers').show();
			$('#unfollow').hide();

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


	$(window).on('popstate', function() {
      location.reload(true);
   })

})
