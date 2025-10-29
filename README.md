# LittleLemon
try these api end points wi this token where ever required : 7aa4612fe36b1cfdd62d69e4ef6a9b50c43ec4f1

login and get token : POST http://127.0.0.1:8000/api/auth/token/login/
no auth required

user logout : POST http://127.0.0.1:8000/api/auth/token/logout/
headers : Authorization: Token 7aa4612fe36b1cfdd62d69e4ef6a9b50c43ec4f1 
headers to be given in appropriate format depending on testing tool

create menu item : POST http://127.0.0.1:8000/api/restaurant/menuitem/
headers : Authorization: Token 7aa4612fe36b1cfdd62d69e4ef6a9b50c43ec4f1 
headers to be given in appropriate format depending on testing tool

create user : POST http://127.0.0.1:8000/api/auth/users/
headers : Authorization: Token 7aa4612fe36b1cfdd62d69e4ef6a9b50c43ec4f1 
headers to be given in appropriate format depending on testing tool

create booking : POST http://127.0.0.1:8000/api/restaurant/booking/bookings/
headers : Authorization: Token 7aa4612fe36b1cfdd62d69e4ef6a9b50c43ec4f1 
headers to be given in appropriate format depending on testing tool

get all menu items : GET http://127.0.0.1:8000/api/restaurant/menuitem/
headers : Authorization: Token 7aa4612fe36b1cfdd62d69e4ef6a9b50c43ec4f1 
headers to be given in appropriate format depending on testing tool

get single menu item : GET http://127.0.0.1:8000/api/restaurant/menuitem/{id}/
example :http://127.0.0.1:8000/api/restaurant/menuitem/1/
headers : Authorization: Token 7aa4612fe36b1cfdd62d69e4ef6a9b50c43ec4f1 
headers to be given in appropriate format depending on testing tool

delete single menu item : DELETE http://127.0.0.1:8000/api/restaurant/menuitem/{id}/
example :http://127.0.0.1:8000/api/restaurant/menuitem/2/
headers : Authorization: Token 7aa4612fe36b1cfdd62d69e4ef6a9b50c43ec4f1 
headers to be given in appropriate format depending on testing tool

get all bookings : GET http://127.0.0.1:8000/api/restaurant/booking/bookings/
headers : Authorization: Token 7aa4612fe36b1cfdd62d69e4ef6a9b50c43ec4f1 
headers to be given in appropriate format depending on testing tool



