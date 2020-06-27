# twitter_api_clone
This is a project attempts to imitate the twitter API. Per the settings of the project you must be authenticated before you can use this API.
After authenticating you will be assigned a token with which you will access the API

### API Endpoints
* /api/v1/rest-auth/login/
  + this endpoint only accepts **[POST]** requests. This endpoint expects
    + *email* 
    + *password*
* /api/v1/rest-auth/register/
  + this endpoint only accepts **[POST]** requests. The endpoint expects the following data
    + *email*
    + *username*
    + *password1*
    + *password2*
    
* /api/v1/posts/
  + this method accepts both **[POST]** and **[GET]** requests
      + the **[GET]** request will retreive all the tweets available
      + the **[POST]** request will create a tweet using the data sent along with the post
        + *tweet*   the String you want to post
        + *file*    the images you want to upload with tweet **(not compulsory)**
* /api/v1/posts/<int:pk>/
  + this method accepts **[GET]**, **[DELETE]** and **[PUT]** methods
* /api/v1/posts/like_post/
  + this method only accepts **[POST]** requests and it expects the following
    + *id* of the post
    + *action*  which one of the following 2 **"like"** or **"unlike"**

* /api/v1/comments/create/
  + this endpoint accepts **[POST]** requests only and expects to receive the following data
    + *post* which is the id of the post you want to comment on
    + *comment* which is the String you want add as a comment
 
* /api/v1/users/
  + this endpoint accepts only **[GET]** request and return the list of users in the application
  
* /api/v1/users/<int:pk>/
  + this endpoint is restricted; if user accessing this endpoint is the same as the user object, then **[PUT]** and **[GET]** method will be allowed otherwise **[GET]** request is the only method allowed
  
* /api/v1/users/follow/
  + this endpoint allow only **[POST]** requests and it expects the following data
    + *id* which will represent the ID of the user you want to follow
    + *action* which is one of these 2 options "follow" or "unfollow"
* /api/v1/users/current_user/
  + accepts **[GET]** request and request the detail of current user
