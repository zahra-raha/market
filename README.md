# Market Place

**Market Place** is a safe and unique place, where sellers can easily advertise thier second handed items. Our mission is to help people find thier needed items and contact to the seller through prepared from. Market Place launched in February 2023.

![Responsive Mockup](https://github.com/zahra-raha/market/blob/main/static/img/Capture1.PNG)


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
1. Regular user
  - Home page is the first page user will see. &check;
  - Website menu contain links to Register page and Login page. &check;
  - Regular user can view the home page and advertisement detail page. &check;
  - Regular user can filter advertisements based on category. &check;
  - Regular user can contact to a seller and send a message. &check;
2. Seller user
  - Website menu contain links to Register page and Login page. &check;
  - Both register and login works as it should. &check;
  - first page a seller will see after login is dashboard. &check;
  - Seller has all access a regular user has. &check;
  - Dashboard contain all the advertisemen of the user (approved or not, sold or not). &check;
  - Seller can use Add Advertisement button to create a new advertisement. &check;
  - Seller can create new advertisement without any error. &check;
  - An alert will be shown to the seller when he creates a new advertisement about approval. &check;
  - Seller can update the status of his advertisement . &check;
  - Seller can update details of his advertisement. &check;
  - Seller can delete his advertisement.  &check;
  - Seller can view prospective customers of his advertisements. &check;
3. Super Admin
  - Super admin can manage all categories, customer ,messages and advertisement posts.  &check;
  - Super admin can approve advertisements.  &check;
## Unfixed Bugs
- I see an error in browsers console as:
    ```
    Uncaught TypeError: Cannot read properties of null 
    ```
# Deployment
## Set up ElephantSQL as Database for this application ##

  - Go to the ElephantSQL website (https://www.elephantsql.com/) and create an account.

  - After creating an account, you will be able to create a new PostgreSQL database. Choose the plan that best fits your needs and click "Create new instance".

  - Give your database a name and select a region.

  - Once the database is created, you will see the database details page. Here, you can find the connection details for your database, including the hostname, port, database name, and username.

  - To connect to the database using the connection details provided.
## Set Up Cloudinary to host images and template files ##

  - Sign up for a Cloudinary account at https://cloudinary.com/users/register/free.

  - In the dashboard, you will see your "Cloud Name", "API Key", and "API Secret". These are saved as environment valiables in ***Heruko*** and .env local file.

  - Install the Cloudinary Python library by running the following command:

        pip install cloudinary

  - Add cloudinary in INSTALLED_APPS list in settings.py
  - Add the following code to your Django settings file to configure the Cloudinary library with your account credentials:

    ```
      STATIC_URL = '/static/'
      STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
      STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
      STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

      CLOUDINARY_STORAGE = {
          'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
          'API_KEY': os.environ.get('API_KEY'),
          'API_SECRET': os.environ.get('API_SECRET'),
      }
      
      MEDIA_URL = '/media/'
      DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ```
  - Run the following command to apply the changes to your Django project:
    ```
        python manage.py migrate
    ```

## Deployment to Heroku ##
  - On Heroku create an account and log in.
  - Goto ci-students team
  - Click ***new*** and ***create new app***.
  - Choose a name for your app, select region and click on ***Create App***
  - Create an account and set up a PostgreSGL database in [Elephantsql](https://www.elephantsql.com/docs/index.html)
  - Under the ***Settings*** click ***Reveal Config Vars*** and all environment variables:
    - Set IP to 0.0.0.0 
    - Set PORT to 8000
    - Set DATABASE_URL
    - Set CLOUDINARY_URL 
    - Set HEROKU_HOSTNAME 
    - Set API_KEY 
    - Set API_SECRET
    - Set CLOUD_NAME
    - Set HEROKU_POSTGRESQL_ROSE_URL
    - Set SECRET_KEY 
  - In the local IDE:
    - Pip install dependencies.
    - Create ***requirements.txt*** ($ pip3 freeze --local > requirements.txt)
    - Create a ***Procfile*** (```$ echo web: gunicorn <app_name>.wsgi > Procfile```)
    - Create an evn.py file and add all your environment variables.
    - Create a .gitignore file and add your env.py files
    - Push all the changes
  
  - In Heroku ***Deploy*** Tab, the ***deployment method*** select Github,connect you gethub account if its not already connected
  - Select repository
  - Scroll down to Manual deploy and deploy branch.
  - Once the build is complete, go back to Heroku and click on ***Open App***
 
# Credits
- I Think Therefore I Blog Tutorial in [Code Institute](https://codeinstitute.net/global/)
- [Gp Multipurpose HTML and Bootstrap Template](https://bootstrapmade.com/gp-free-multipurpose-html-bootstrap-template/)
- [Stackoverflow website](https://stackoverflow.com/)