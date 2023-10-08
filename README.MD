# Python Rest API


## Installation
1. Create .env file. Rename .env.example to .env 
2. Build a docker container
```commandline
cd your_project
docker-conpose build
docker-compose up
```

## Environment Variables
Docker Uses variables from .env file to create containers. Copy them from .env.example to make it works with docker-container only.

Postgres variables
1) POSTGRES_PORT
2) POSTGRES_HOST
3) POSTGRES_USER
4) POSTGRES_PASSWORD
5) POSTGRES_DB

App variables
1) APP_PORT - the port of application
2) SECRET_KEY - the jwt secret key (recommend to use from env.example)
3) FLASK_ENV (development or production) - variable to enable disable debug mode and production mode

## API
Use  application/json content type for the all requests/

Based on .env file:

HOST=http://0.0.0.0:5002 | http://localhost:5002

## Routes
.........
### POST {{HOST}}/users
Request Body:
```json
{
    "username": "ivan2",
    "email": "sdsdfds2f@gmao.com",
    "password": "helloworld"
}
```
Response Body:
```json
{
    "created_at": "2023-10-08 14:04:53",
    "email": "sdsdfds2f@gmao.com",
    "id": 2,
    "username": "ivan2"
}
```
.........
### POST {{HOST}}/users/login
Request Body:
```json
{
    "email": "sdsdfds2f@gmao.com",
    "password": "helloworld"
}
```
Response Body:
```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJzZHNkZmRzMmZAZ21hby5jb20iLCJ1c2VybmFtZSI6Iml2YW4yIiwiZXhwIjoxNjk2Nzc0NDAwfQ.7tMlFwKMk-3krMnymCagY_0z9u8msndCuuHAMS-1nkk"
}
```
Token lifetime is 1hour.

.........
### GET {{HOST}}/users/{username}
Headers:
```json
{
  "Authorization": "Bearer {{TOKEN}}"
}
```
Request Params:
```json
{
  "username": "current"
}
```
Can be `current` or `any_username`

Response Body:
```json
{
    "created_at": "2023-10-08 13:13:08",
    "email": "sdsdfds2f@gmao.com",
    "id": 1,
    "password_hash": "fc5e038d38a57032085441e7fe7010b0",
    "username": "ivan2"
}
```

.........
### GET {{HOST}}/posts
Headers:
```json
{
  "Authorization": "Bearer {{TOKEN}}"
}
```
Response Body:
```json
[
    {
        "author_id": 1,
        "content": "The post description",
        "created_at": "2023-10-08 13:37:11",
        "id": 2,
        "title": "Hello world"
    }
]
```

.........
### POST {{HOST}}/posts
Headers:
```json
{
  "Authorization": "Bearer {{TOKEN}}"
}
```
Request Body:
```json
{
    "title": "Hello world",
    "content": "The post description"
}
```
Response Body:
```json
{
    "author_id": 1,
    "content": "The post description",
    "created_at": "2023-10-08 13:37:11",
    "id": 2,
    "title": "Hello world"
}
```
.........
### GET {{HOST}}/posts
Headers:
```json
{
  "Authorization": "Bearer {{TOKEN}}"
}
```
Response Body:
```json
[
    {
        "author_id": 1,
        "content": "The post description",
        "created_at": "2023-10-08 13:37:11",
        "id": 2,
        "title": "Hello world"
    }
]
```
.........
### GET {{HOST}}/posts/{id}
Headers:
```json
{
  "Authorization": "Bearer {{TOKEN}}"
}
```
Request Params:
```json
{
  "id": 2
}
```
Response Body:
```json
{
    "author_id": 1,
    "content": "The post description",
    "created_at": "2023-10-08 13:37:11",
    "id": 2,
    "title": "Hello world"
}
```

.........
### POST {{HOST}}/posts/{id}/comments
Headers:
```json
{
  "Authorization": "Bearer {{TOKEN}}"
}
```
Request Params:
```json
{
  "id": 2
}
```
Response Body:
```json
{
    "author_id": 1,
    "content": "The post comment",
    "created_at": "2023-10-08 13:38:36",
    "id": 5,
    "post_id": 2
}
```
.........
### GET {{HOST}}/posts/{id}/comments
Headers:
```json
{
  "Authorization": "Bearer {{TOKEN}}"
}
```
Request Params:
```json
{
  "id": 2
}
```
Response Body:
```json
[
    {
        "author_id": 1,
        "content": "The post comment",
        "created_at": "2023-10-08 13:38:36",
        "id": 5,
        "post_id": 2
    }
]
```

