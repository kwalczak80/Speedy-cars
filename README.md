# Speedy Cars

## User Experience (UX)

### Primary Goal

The primary goal of the website from the site owner’s perspective is as follows:

- To attract customers to the business by showing a variety of cars for sale
- To allow a user to navigate the website easily
- To allow a user to make an inquiry about a car
- To allow a user to book a test drive
- To allow a user to easily search a car they are looking for
- Ability to add a new car for sale
- ** To allow a user to read testimonials about the Speedy Cars

The primary goal of the website from a site user’s perspective is as follows:

- To view the car’s stock
- To view details about car along with description and price
- To be able to easily find a car they are looking for
- To book a test drive
- To make an inquiry about the car
- To view opening hours and address
- To read more about the business
- ** To view other customer’s testimonials about Speedy Cars

## User Requirements and Expectations

- Easy to navigate by using the few buttons
- Appealing dashboard with a functional overview
- No broken links
- Appropirate error handling
- Responsive and visually appealing on all devices.
- Ability to make an inquiry about the car
- Ability to book a test drive
- Ability to edit or cancel a test drive

## User Stories

### Users

- As a user, I want to be able to view all available cars in one of the categories:
  - Petrol
  - Diesel
  - Hybrid
  - Electric
- As a user, I want to see professional descriptions of each car available for sale along with relevant pictures
- As a user, I want to be able to navigate the website quickly and easily
- As a user, I want to be able to use the search option to find the car I’m looking for
- As a user, I want to be able to view the price of the cars
- **As a user, I want to be able to read other user’s testimonials
- As a user, I want to be able to make an inquiry about the car
- As a user, I want to be able to book a test drive
- As a user, I want to be able to edit or delete a test drive I have made
- As a user, I want to read more information about the business
- As a user, I want to be able to see featured cars
- As a user, I want to be able to sign in to or create an account
- As a user, I want to be able to log out of an account
- As a user, I want to be able to view the business’s social media channels
- As a user, I want to log in after I created an account and see my test drive bookings
- As a user, I want to be informed if a test drive cannot be completed for any reason
- As a user, I want to be informed if a test drive was booked successfully

### Site owners Goals

- As a site owner, I want to attract car buyers
- As a site owner, I want an appealing website with a range of cars
- As a site owner, I want users to be to view the full range of cars available for sale
- As a site owner, I want users to be able to view the relevant description of each car along with the price
- As a site owner, I want users to able to have an option to search for the car they are looking for
- As a site owner, I want users to be able to make an inquiry about the car
- As a site owner, I want users to be able to book the test drive with the selected car. These need to include data validation so the user can only book future dates and within valid opening times
- As a site owner, I want users to be informed if a test drive cannot be booked
- As a site owner, I want users to be able to edit and cancel a test drive
- As a site owner, I want users to be able to read about the business
- As a site owner, I want users to be able to navigate the site easily and quickly
- As a site owner, I want users to be able to sign in to or create an account
- As a site owner, I want users to be able to log out of their account
- As a site owner, I want to be able to add new cars or remove if sold
- As a site owner, I want users to be able to view the business’ social media
- ** As a logged-in administrator, I want to be able to add testimonials

### Error Flow

- In the event that the desired page cannot be located, the user should be able to return through the website's navigational structure without hitting the back button on their browser

## Wireframes - Desktop

### Home page

![Home page](docs/wireframes/desktop/home_page_desktop.png)

### Search page

![Search page](docs/wireframes/desktop/search_page_desktop.png)

### About page

![About page](docs/wireframes/desktop/about_page_desktop.png)

### Log in page

![Log in page](docs/wireframes/desktop/log_in_page_desktop.png)

### Registration page

![Sign Up page](docs/wireframes/desktop/registration_page_desktop.png)

## Site Map

The information architecture was organized in such a way as to ensure that users can navigate through the site easily.

![Site Map](docs/site_map/speedy_cars_site_map.jpg)

## Features

- Responsive design
- Navigation Menu
- Postgress databases to store information and user login/profile information
- Ability to book a test drive with a specific car (only for logged-in users)
- Dashboard page where logged-in users can edit/cancel existing test drives (CRUD Functionality)
- Customized Admin (business owner) panel
- Admin panel – ability to select cars that will be displayed on the page. No need to delete the car from the database if for some reason the business owner does not want it to be displayed on the website.
- The search page where user can find a car with specific searching criteria
- Search form "remembers" options selected by the user
- Dynamic page titles
- Once clicked thumbinals are nicely presented on the screen (Lightbox) to allow user to view a car in details
- Messages system to provide feedback to the user

## Structure

### Code Structure

The project is organized into various applications, as constructed using the Django Framework.
App details are as follows:

- Home - this app contains information about the Speedy Cars home page with quick links to the about and search pages via the nav bar.
- Booking - this app contains information related to the test drive booking system (for users to view, edit or cancel booked test drives).
- Cars - this app is for the users to view the cars or to view the search results.
- Employees - this app is for the business owner to manage Speedy Cars staff via admin panel.

To complement the apps there are

- Speedy Cars: Speedy Cars level files - settings.py for project level settings and urls.py to route the website urls.
- templates: Containing the base.html, allauth(django authentication). The partial folder contains the navbar and footer HTML.
- templates (app level): some of the apps have their own templates directory for HTML to consider portability and reuse.
- urls (app level): each app has its own url.py file to consider portability and reuse.
- static: Base css and Javascript files.
- manage.py: This file is used to start the site and perform functions during development.
- README.md: Readme documentation.
- Procfile: To run the application on Heroku.
- Requirements.txt: Containing the project dependencies Note: Environment variable values are not exposed in the source code as they are stored locally in env.py that is not checked in(and listed in .gitignore, and on Heroku in app settings).







