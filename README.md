# **Building A Simple Web App with Flask and PostgreSQL Database**
This repository contains the source code and instructions to build and deploy a simple newsletter page with some basic diagnostic features, that saves the submitted user information inside a Postgres database.

## **Step 1: Prepare the Development Environment**
- Install [VS Code](https://code.visualstudio.com/download).
- Install [Docker](https://docs.docker.com/desktop/windows/install/). 
- Install [Docker extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker).

## **Step 2: Dockerize and Deploy the Application**
After cloning this repository, open the folder in VS Code. Next, open a terminal and type `docker-compose up`.
This will build and run two images:

- `postgreswebapp_backend`, the image that will create a container where the actual web application will be hosted.
- `postgres`, which will create a Postgres database called `postgres` inside a container, with the user `postgres` and user password `postgres`. These can be configured by changing the **environment** variables inside the `docker-compose.yml` file.

Once that is done loading, open another terminal and run:

`docker-compose exec backend sh`

This will open a shell inside the docker container where the web app is hosted. The following series of commands will create the tables that are required by your application. These are defined inside `main.py`. 
Run:

`python`

`from main import db`

`db.create_all()`

`exit()`

After that you can close that terminal. Now open another terminal to get a shell inside the database container. Run:

`docker-compose exec db sh`

`psql -U postgres`

`\l`

After running the last command you should see that a database named `postgres` has successfully been created inside your container. By running `\dt` you will see that the table `mailinglist` that is used by the application has also been created.

## **Step 3: Verifying That Everthing Works**
Open a browser and go to `localhost:5000`, this should open the web application. Fill in the empty fields and click submit. If the applcation is working as it should, you should be redirected to a "Thank you" page. We can verify that the user data has been saved into our database by going back to the postgres shell that we created earlier. Type in `TABLE mailinglist;`and hit enter, you should see the user info that you have typed in your browser saved in your database.

### Congratuations! You have just deployed a simple web application with Docker!
