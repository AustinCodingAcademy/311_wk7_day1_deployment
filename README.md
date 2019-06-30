# App Engine Deployment

## Setup

Initialize and run the app: `npm install` && `npm start`.

The app is using `nodemon`. Any changes made (and saved) will cause the server to restart.

Navigate to the `sql/connections.js` file and alter the following fields to reflect your database setup:

```
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'admin'
```

These will be the same credentials we used to set up a connection in MySQL Workbench.

Finally, in MySQL Workbench, run the `initialize.sql` script (on the "admin" database) that is included in this project.

## Overview

This app is the completed version of the assignment from last class.

The basic setup, routes/controllers, SQL statements and authentication has been done for us. Our job is simply to deploy the application. 

_Keep in mind that your port (4001) may be different when running the application_

## Get familiar with the system

Look in the routes/controllers files and get a feel for what the system is doing. Run the `npm run start:dev` command so that we can test our application and use Postman to become familiar with the different routes that are available. We will do this same run-through once the application is deployed to Google Cloud. 

## Deployment Steps

There are a few actions we need to take with our Google Cloud accounts before we can deploy the app. A lot of it will be one-time setup. After that's complete we will be ready to deploy our application.

### Create App Engine instance
_This is a one-time setup step_

* Open your Google Cloud console
* Open the menu on the top left and choose "App Engine"
* Choose "Create Application", then "Create App"
* Under the language option select "Node.js"
* Click "Next"
* Allow App Engine to be created. This could take a few minutes

Alternatively, look at the following documentation under "Before you begin". Steps 1 & 2
https://cloud.google.com/appengine/docs/standard/go/building-app/creating-your-application

### Download the Cloud SDK
_This is a one-time setup step_

* After the app is created, there should be an option to download the Cloud SDK
* Install it
* Type `gcloud --version` to verify installation
* `gcloud init`
* Choose "Create new configuration"
* Choose "Log in with a new account"
* This should open a browser and allow you to login with your Google Cloud credentials
* Once logged in, pick your project (ex. `new-project-245019`).. should be option 1

### Enable the Cloud SQL Admin API
_This is a one-time setup step_
_Only applicable if we are using a Google Cloud database, which we are_

* In the top bar of the Google Cloud console, search for "cloud sql admin api"
* Choose "Enable Cloud SQL Admin API"
* Click "enable"
* Don't worry about creating credentials

### Choose a Project for Deployment
_This is a RE-OCCURING step. You will do this each time you want to deploy a project_
_THESE ARE THE MAIN DEPLOYMENT STEPS_

* In your terminal, navigate to a repo that you want to deploy (we will use this repo)
* Make sure that an `app.yaml` file exists that has at least one line, the runtime (ex. `runtime: nodejs10`). This file has already been created for us in this repo. Please go look at it.
* Add an `environment_variables` section to your `app.yaml` file
* Find the _instance name_ of your Cloud SQL
  * Navigate to the "Cloud SQL" page in Google Cloud
  * Find "instance connection name" under the "connect to this instance" title
* Add a property for this variable and give it the name "CLOUD INSTANCE": `CLOUD_INSTANCE: <YOUR CLOUD INSTANCE NAME>`
* Run the command: `gcloud app deploy`
* Once deployed, App Engine will use the standard `npm start` command to run your application. Go look at it in the `package.json` file and make sure you know what it's doing
* After a couple of minutes, your app should appear in the online console

* Navigate to your App Engine in Google Cloud. Find the URL where the app lives (top right corner)
* Take this URL and put it in Postman and use it to test your routes and make sure the app works the same as it did when we were testing locally.

## A NOTE ON THE SQL CONFIGURATION

Checkout the `sql/connection.js` file. It looks slightly different than the one from your last assignment. That's because App Engine and Cloud SQL (both of the Google Cloud services we've used) know how to talk to each other automatically. However, in order for the system to understand that we need to add an additional property to the connection pool setup, _socketPath_. Notice that we've also included a `.env` with the variable we need for the second part of the socketPath. That is our Cloud SQL instance. We can find this on the dashboard/homepage of Cloud SQL.

Essentially, what this connection allows us to do is run the app locally with one configuration and also prepare the app for production use when it's deployed on App Engine. 

## Summary

If all went according to plan we now have now deployed our API to a publicly accessible service and tested it to make sure it's working as expected.

Upload the public URL for the HW assignment. 