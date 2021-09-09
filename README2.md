# ProjectL PinPlace

🔍 [![Netlify Status](https://api.netlify.com/api/v1/badges/a219f92e-0912-4232-808e-746b42373a08/deploy-status)](https://pinplace.netlify.app/) 🚀 ![AWS]()
## Add a deployed status thing above for AWS
## Add a gif & remove this title

PinPlace is a recommendations organisation application built in full stack with react, django REST framework connected to PostgreSQL database deployed on AWS and netlify. Users can create an account, quickly search, add, organise & view recommendations they have added with a friendly UI. Interaction with the app allows the user to view recommendations as geolocations and share these with other users (friends)

## Description
PinPlace is an Application to help customers solve the problem of disorganised location wish-lists, using our unique Social Media Inspired platform. Unlike our competitors, we offer a quick alternative to share, sort & maintain recommendations with friends.

# Installation and Usage
Clone or download this repo.

To start up the server:
`pipenv shell`
`pipenv install`
`cd pinplace`
`pipenv run dev`


To start up the PostgreSQL database in a docker container, open another terminal and input:
`docker compose up`

It should load on: http://127.0.0.1:8000/

To start up our client: 

`cd front-end`
`npm install`
`npm run dev`

It should load on: http://localhost:8080

# Technologies
- HTML, CSS, Pythin, JavaScript, docker, PostgreSQL

### Dependencies
- Server: django, django REST framework

- Client: react, router-dom, react-router-dom, tailwind, axios, react-icons

### DevDependencies
- Server: psycopg2

- Client: necessary loaders, webpack, babel, jest, react testing library, dotenv-webpack

# Process
1. Project Plan! We used the MoSCoW method to prioritise features & created a Github organisation for version control
2. Designed & mocked up out app using Figma
3. Set up file structure and boilerplate for react and Django 
4. Defined our routes to link the front and back end together
5. Set up to do lists with flexible time frames to ensure completion of work but also a relaxed env
6. Deploy front and back end & trigger auto deploy to welcome new changes merged to main Git branch
7. Open huddle policy for collaboration a call could be opened at any point in the day

## ChangeLog
### Django-API
1. Install django - start project 'pinplace' and create app for users, pins and locations
2. Explicitely created 
3. Issues linking models 
4. Add [Django REST Framework](https://www.django-rest-framework.org/)
5. Recreated user app & merged pins & locations app
6. Add JWT auth via [simplejwt] (https://github.com/jazzband/djangorestframework-simplejwt)
7. Add test suite to test end points

### React-Client
1. Set up react file structure
2. Install dependencies and devdependencies
3. Add components:
4. Set up routing
5. 
6. 
7. Install test devdependencies & add setup for test suite
8. Fetch from our Django API. Rendering data in correct components and ages

## Bugs
- [x] Heroku settings with django prevented full successful deployment & persisting data. Switched to AWS
- [x] Newly added required fields for db added with incorrect type of data causing the app to crash. Migrations were deleted and reapplied.
- [x] DB schema required slight reconfiguration to allow for essential db relationships
- [x]
- []
- []

# Wins & Challenges

### Wins
- Having a detailed plan from early in the dev process and open communication within the team
- Successful deployment of frontend to Netlify & backend to AWS
- Production ready UI utilising Tailwind 
- Dynamic nature of react provides a responsive feeling app

### Challenges
- Persisting data issues when deployed to Heroku
- Django build - lots of configuration alongside trial and error
- Django rest framework was not implemented immediatly and cost the backend dev some time
- Editing model followed by migrations cause internal issues for Django

# Future Features
- Adding other users as friends
- Search for other users
- Sharing of lists between users
- Mobile application using react native

# Slide Deck

