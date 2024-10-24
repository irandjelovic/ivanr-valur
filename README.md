## Prerequisites
* Install docker
* Optional for tests and local run of the application:\
** Install python\
** Install python requirements from the root folder using command:\
  `pip install -r requirements.txt`\
** Install node.js and npm

## Application
Run application by building and running docker containers *api* and *web* using command:\
  `docker-compose up -d --build`

Application can be accessed from the browser using url:
  `http://localhost:3009/`

Locally, these can be run with:
* **api**: `python manage.py runserver` in backend folder (the only endpoint is at http://localhost:8000/api/multiply)
* **web**: `npm run dev` in frontend folder and accessed at http://0.0.0.0:3000/
## API tests
* Located in module *~/backend/api/tests.py*
* Tests can be run from the backend folder using command:\
  `python manage.py test`

## UI tests using Playwright
* Located in folder *~/frontend/tests*
* Test can be run from frontend folder using command:\
  `npm run test`