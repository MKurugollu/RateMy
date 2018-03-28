# RateMy
This will be a website similar to rango and Reddit where users can create categories. In which registered users
can upload images (and maybe videos if possible) of the category and other users can upvote, comment and rate it.

# Stuff to do

<del>1 Do the Design Spec *BEFORE ANYTHING ELSE*. That includes:
    -User personas
    -ER diagram
    -Specification
    -Page layouts/wireframes
    -site walkthrough (wtf is that)
    -system architecture diagram
    
    Note: not only is this going to be submitted and worth 10%, but it will be beneficial to have a detailed plan before we start
   
<del>2) I created a django project for this so you guys need to just clone it to your computers.

<del>3) I think we should map out everything first. Ie make simple views and links to the urls so we have the foundation to build up on</del>

4) Then after we can inlude the following featuers (feel free to add anymore):

      ---------*Basic Features that should be added*---------------
      
      -Threaded comments
      
      -creating categories
      
      -posting (images or text depending on the permissions of the category
      
      -upvoting
      
      <del>- user authentication
      
      -show num. of upvotes, comments etc (similar to reddit)
      
      -(in homepage) show recently added categories, highest voted categories, posts etc
      
      -subsrcibtion to categories so they can easy find it in their homepage
      
      <del>- Simple UI design (Css)
      
      -show number of views
      
     
     
      ---------*Advanced Features that can be added after basic ones are (nearly) done. (Not compulsory)*---------------
      
      -(user login required) have a subscription page so only posts from subscripted cats are shown
      
      -reporting (if post or user gets reported too much(put a threshold) the user/post will get a temporary ban and a mod can look in          to it
      
      -linking social media accounts to the ratemy account
      
      -collapsing comment threads
      
      <del>add NSFW tags (allow users to block them via user settings ala reddit)</del>
      
      -Users enter keywords and we show cateogories which might interest them
      
      -add moderators (ie give some users the permission to ban users, remove posts, categories... etc.
      
      -doing a unique rating for the website only
      
      <del>Show similar categories before a user creates a category so there are no duplicates</del>
      
      -Have custom urls (no idea how to do) - ie ratemy.cat.pythonanywhere.com, ratemy.poo.pt....
      
      -Really nice UI design
      
      -Have a small tutorial of the site if the user has entered the site for the first time (based on cookies)
      
      -Random category selector button
      
      -added related posts or categories to the right of the page (suggested posts)
      
      -sharing posts to social media
      
      
      
      PS: Strike a line through stuff we have completed
 
 
 
 tl;dr: basically recreate a better looking reddit for rating images ;)
 
 Requirements:
 To populate the database a superuser named admin is required.
 
 External Sources:
•	Django-countries library – Used in the profile and profile registration which allows the User to select which country they are from
•	Django-registration-redux – Used for User Authentication (as in the Rango app)
•	Django-el-pagination – used to paginate when there are 10+ posts on a given page
•	Used a w3schools source code and stylesheet to create the top posts slideshow on the landing page
•	We used Bootstrap 4.0 (as in the rango app) for the navbar.

Please Note:
•	We explained why we have 1 javascript (used to hide the navbar when scrolling down) inline and not in a separate .js file in a comment on line 101 in the base_bootstrap
•	We also explained in a comment in the populate-script.py why we could only populate 1 User Profile and not anymore.

      
