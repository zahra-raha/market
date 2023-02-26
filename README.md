# Market Place

**Market Place** is a safe and unique place, where sellers can easily advertise thier second handed items. Our mission is to help people find thier needed items and contact to the seller through prepared from. Market Place launched in February 2023.

![Responsive Mockup](https://github.com/zahra-raha/market/static/img/Capture1.PNG)


# Super Admin credentials
1. Admin:
  - Username : zahra
  - Password : zahra098
2. Seller User:
  - Username: mahmood
  - Password: zahra098

Deployed link : https://zahra-market-place.herokuapp.com/
# User Experience

# User Stories

- As a ***user*** I can ***view paginated list of addvertisement*** so that ***easily find the item I want to buy***
- As a ***user*** I can ***view list of my posts*** so that ***I can select one to view its details***
- As a ***user*** I can ***Fill a form on an advertisement*** so that ***I can share my phone number with the seller***
- As a ***user*** I can ***click on an advertisement*** so that ***I can read the details***
- As a ***Seller*** I can ***register an account*** so that ***I can post advertisements***
- As a ***seller*** I can ***click a button*** so that ***I can mark the advertisement as sold***
- As a ***site admin*** I can ***approve or disapprove the advertisements*** so that ***I can prevent fake advertisements***
- As a ***seller*** I can ***open a form*** so that ***I can submit and create a new post***
- As a ***Seller*** I can ***view the info of users who tried to buy my stuff*** so that ***I can contact them***
- As a ***Seller*** I can ***click a link*** so that ***view list of my addvertisements***
- As a ***Seller*** I can ***click a button*** so that ***delete my advertisement***
- As a ***Seller*** I can ***toggle a button*** so that ***update an advertisement as sold or not sold***
- As a ***user*** I can ***filter the advertisements*** so that ***find specific item faster***

### Simple User Goals

- To check out and find a good item to buy

### Seller Goals

- To advertise his items to sell and find prospective customers

### Developer Goals

- To help people in yard sales
- To create a fully functional website using best technologies 

### User Story

```
As a user, I want to be able to record the trips I am taking in a given Vehicle
```

Criteria

- Site must have a database that is fully functional

Implementation

- Install postgres database



# Features

### Main Features

-	Responsiveness and User friendly – The site is fully responsive to all screen sizes and has a beautiful and easy to use design. This was achieved by using Gb HTML Bootstrap template designed by https://bootstrapmade.com

-	Flash messages – Flash messages designed to inform users about event results such as: creating an advertisement or logging in to the website.

### Home Page
-	Two major sections are on the home page. A slogan and a list of categories are included in the first section, and each category links to a page where items are filtered according to that category.

- Second section is a paginated list of advertisements that can be filtered at same page using the links above it.

- All advertisements listed in second section has a status of not-sale and approved by the admin of the site.

### View advertisements filtered by category
- All users can access this page by clicking on category item listed in home page.
- This page contains all advertisement of specitic category type.

### View Advertisement Details

-	All users can access this page; in this page every user has it's own access level: 
- **Normal user** can view the information detail about the item, item image and a button to contact with seller.
- The item is owned by the **Seller**. Sellers have access to the item's description and image, as well as power over the advertisement (update the status with a single click, change the item's details, and delete the advertisement) and is one click away from the prospect list.

### Create Advertisement Page
- Users can access this page after logging in. By using this page sellers can register thier advertisements.

### Dashboard Page
- Every logged in user has a dashboard where his advertisements are listed without consideration of its approved or not and can be filterd based on status.

### Contact Seller
- Users can use the button provided in advertisement detail page to contact with seller.
- This page contins a form the through which users can send thier phone numbers and messages to seller.

### Update Advertisement Page
- This page can be accessed by the owner of advertisement and if for updating the details of advertisement.

### Prospective Customer Page
- This page is designed to be accessed by the item owner and contain the prospective customers information.

### Authentication Pages
- This pages are provided by the help of **allauth** library and will handle user rigistration, ligin and log out.

## Future Features
### User accounts 
- User accounts need more improvement such as view and edit personal informationa and forgot password process.

### Data Managment
- Now the site is handlling predefined details about advertisement and it need more improvement to be able to get every kind of advertisements.

# Languages

- [HTML5](https://bootstrapmade.com/gp-free-multipurpose-html-bootstrap-template/)
Used in frontend

- [CSS3 and SCSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
Used in frontend

- [Python3](https://www.python.org/)
Used to handle server side functionalities


- [Javscript](https://www.javascript.com/)
Used in some design functionalities like message disapearing

# Technologies

**Template**
- [Gp Multipurpose HTML and Bootstrap Template](https://bootstrapmade.com/gp-free-multipurpose-html-bootstrap-template/)
build with HTML,CSS, Scss and Bootstrap
**Libraries**
- [Django](https://www.djangoproject.com/)
Python web framework
- [Cloudinary](https://cloudinary.com/) is used to upload images
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) Used for account and user management
- For more libraries please check [requirement.txt](/requirement.txt) file

**Database**
- [PostgreSQL](https://www.postgresql.org)
Relational database used to store all the persistent data

**IDE**
- [Gitpod](https://gitpod.io/)
Gitpod is used as IDE for this web app

**Deployment**
- [Heroku](https://www.heroku.com/)
Heroku is a platform as a service (PaaS) application that provides developers with hosting and data storage in the cloud. There are many tiers of service, though I used the free one. 

- [Cloudinary](https://cloudinary.com/)
Cloudinary is image and vedio API provider.

- [ElephantSQL](https://www.elephantsql.com/)
ElephantSQL is providing PostgreSQL as a service and installs and manages PostgreSQL databases.

# Testing
## Code Validation

## Manual Testing

# Deployment
#### Creation of a Python Virtual Environment ####
Creating a virtual python environment allows you to only install the packages required for your project and helps to stop system wide packages causing errors within your project. 
When using VS Code, if there is a venv folder in your project, it will automatically start the virtual environment when you open the terminal. 

*Note: The process may be different depending upon your own OS - please follow this [Python help guide](https://python.readthedocs.io/en/latest/library/venv.html)
to understand how to create a virtual environment*

#### Install the required packages ####

- After initialising the venv, in your IDE terminal, install the dependencies from the requirements.txt file with the following command:
 
pip install -r requirements.txt

#### Create the database in PostgreSQL #####
- Download the postgres client from their website [postgreSQL](https://www.postgresql.org/download/) and follow the set up guidance in the wizard. 
- If you are using windows, in order to use the PSQL terminal in your IDE, you will need to set up environment variables to point to the terminal application. A Guide to do this can be found here [Terminal](https://blog.sqlbackupandftp.com/setting-windows-path-for-postgres-tools)

 #### Create env.py file ####

- The env.py file should contain the below details:
- when deploying to heroku, these also need to be configured in the config vars section

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "your_secret_key")
os.environ.setdefault("DB_URL", "postgresql:///databasename")

```

- Please ensure you add in your own SECRET_KEY and DB_URL values.
- Ensure that the env file is in your 

#### Run the application ####

- To run the application enter the following command into the terminal window:

```
python3 app.py
```

### Deploying the app to Heroku ###

#### Create the Heroku App ####

- Ensure you have an account created at [Heroku](https://signup.heroku.com/login)
- Log in to your Heroku account dashboard and create a new app.
#### Push your repository to GitHub ####

- Commit and push your local repository to your GitHub linked repository

- create the Procile and requirements file using the following commands:


echo web: python app.py > Procfile
pip3 freeze --local > requirements.txt


- Push your local Git repository to GitHub

#### Connect Heroku to GitHub ####

- In the Heroku App Settings page, open the section Config Vars
- Add all the variables from the env file as individual vars


- In the Heroku App Deploy page: 
  - Select GitHub from the Deployment Method options
  - Select Connect to GitHub
  - Log in to your GitHub account from Heroku to link the App to GitHub
  - Search for and select the repository to be linked in Github
  - Select Connect
  - Select Enable Automatic Deployment from GitHub

- Then create the database in the python shell via heroku: 
    - Select more, then Run console
    - Type in 'Python'
    - Once the python shell opens, type 'from mileagetracker import db'
    - then type db.create_all()

#### Launch the App ####

- Click Open App in Heroku to launch the App in a new browser window.

**Successful deployment**
[Heroku deployment](https://milestone3-mileage-tracker.herokuapp.com/login)
# Credits

- Task Manager Tutorial
- Flask documentation for flask-login implementation [docs](https://flask.palletsprojects.com/en/2.1.x/)