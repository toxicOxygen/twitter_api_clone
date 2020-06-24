# twitter_api_clone
This is a project attempts to imitate the twitter API. Per the settings of the project you must be authenticated before you can use this API

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
