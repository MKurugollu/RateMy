$(document).ready(function() {
		// JQuery code to be added in here.
    // Hide button until follow is clicked
    $('#unfollow').hide();

    //Gets data from button and sends it to the views_ajax.py file and adds a follower then replaces the button to unfollow
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

    //if clicked it takes away one from follower count and hides the unfollow button and shows the follow button
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


    //works in simillar fasion to the above functions
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
