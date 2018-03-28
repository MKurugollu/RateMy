# RateMy
This will be a website similar to rango and Reddit where users can create categories. In which registered users
can upload images (and maybe videos if possible) of the category and other users can upvote, comment and rate it.
 
# Requirements :
 To populate the database a superuser named admin is required.
 
 External Sources:
 
-	Django-countries library – Used in the profile and profile registration which allows the User to select which country they are from
-	Django-registration-redux – Used for User Authentication (as in the Rango app)
-	Django-el-pagination – used to paginate when there are 10+ posts on a given page
-	Used a w3schools source code and stylesheet to create the top posts slideshow on the landing page
-   We used Bootstrap 4.0 (as in the rango app) for the navbar.

Please Note:

-	We explained why we have 1 javascript (used to hide the navbar when scrolling down) inline and not in a separate .js file in a comment on line 101 in the base_bootstrap
-	We also explained in a comment in the populate-script.py why we could only populate 1 User Profile and not anymore.

      
