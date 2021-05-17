![responsive image](https://github.com/horizons83/Milestone3-Slimming-Gusto/blob/master/readme-documents/am-i-responsive.png)
This is a screenshot from [Am I Responsive](http://ami.responsivedesign.is/)

### Slimming Gusto, Tasty Guilt Free Recipes.

Slimming Gusto is a recipe app that provides a place for people to share healthy delicious food recipes for people to follow and create.

The website is aimed at people who maybe trying to loose weight following diet plans from weight loss companies or users who just want 
good healthy meals.

This site was conceived from my own personal journey with loosing weight and to show that you can still have great tasting meals even when
following a strict diet plan. There are many misconceptions about diet plans from tiny portions to horrible cardboard food. This is 
totally not the case and this app is here to prove that you can still eat good sized meals with zero guilt or regret!

## Table of Contents
1. [User Experience](#User-Experience-UX)
2. [Scope](#Scope)
    - [Functional Specifications](#Functional-Specifications)
	- [Content Requirements](#Content-Requirements)
	
3. [Design](#Design)
    - [Wireframes](#Wireframes)
	- [Fonts](#Fonts)
	- [Colour Scheme](#Colour-Scheme)
	
4. [Features](#Features)
    - [Features Currently Implemented](#Features-Currently-Implemented)
	- [Future Features](#Future-Features)
	
5. [Technologies Used](#Technologies-Used)
    - [Languages](#Languages)
	- [Frameworks Libraries and Programs](#Frameworks-Libraries-and-Programs)
	
6. [Defensive Design](#Defensive-Design)
   
7. [Testing](#Testing)

8. [Database](#Database)
    - [Database Collections](#Database-Collections)

9. [Deployment](#Deployment)
    - [Heroku Deployment](#Heroku-Deployment)
	- [Creating A Local Clone](#Creating-A-Local-Clone)
	
10. [Site Content](#Content)

11. [Acknowledgements](#Acknowledgements)

12. [Disclaimer](#Disclaimer)
 

## User Experience UX

### User Requirements

- As a **User** I want to be able to easily understand the main purpose of the website.
- As a **User** I want to be able to easily navigate the website.
- As a **User** I want to easily search and find recipes to follow.
- As a **User** I want to be able to register to the site to gain access to the full features of the website.
- As a **User** I want to see to be able to add my slimming recipes to the site to share with others.
- As a **User** I want to be able to access, edit and update all recipes I have added to the site.
- As a **User** I want to be able to delete a recipe I have added to the site.
- As a **User** I want to be able to contact site admin to report a bug or submit a query.

### Owners Requirements

- As an **Owner** I want the home page to immediately tell the User what the site is for.
- As an **Owner** I want the User to be able to easily navigate the site via navigation links.
- As an **Owner** I want users to be able to register to the site to access all features.
- As an **Owner** I want users to be able to add recipes to the site to build database and share with others.
- As an **Owner** I want users to be able to be able to see,edit and delete any recipes they have added.
- As an **Owner** I want to be able to be able to see, edit and delete any recipes added and manage recipe categories.

[Contents](#Table-of-Contents)

---

# Scope
This will be a Minimal Viable Product containing the most essential core content required.

## Functional Specifications 

* Home
* Recipe categories
* Search functionality
* Full Recipe
* Registration
* Log In
* User Profile functionality:
    - Add Recipe
    - Edit Recipe
    - Delete Recipe
* Log out functionality
* Admin functionality:
    - Manage Recipes - Edit & delete all recipes
    - Manage Categories - Add, edit & delete categories

## Content Requirements

* Logo
* Navigation
* Home page
* Image slider on home page with welcome text overlay
* Full recipe page
* Register page with registration form & link to Log In page
* Log In page with login form & link to Registration page
* User profile page
* Edit/Delete buttons for users recipes
* Add recipe page with form for adding recipe details
* Edit recipe page with form for editing recipe details
* Admin manage recipes page - edit/delete any recipe
* Admin manage categories page - add/edit/delete categories
* Footer with Social media links

[Contents](#Table-of-Contents)

---
## Design

I did the design for this website using Balsamiq to create the wireframes. I have created wireframes for all pages on desktop, tablet and mobile.

### Wireframes

|                                                      Slimming Gusto                                            	|
|:--------------------------------------------------------------------------------------------------------------:
| [Home Page](https://github.com/horizons83/Milestone3-Slimming-Gusto/blob/master/readme-documents/wireframes/wireframe-index.pdf) 	|  
|  [Register Page](https://github.com/horizons83/Milestone3-Slimming-Gusto/blob/master/readme-documents/wireframes/wireframe-register.pdf)  	|  
|  [Log In Page](https://github.com/horizons83/Milestone3-Slimming-Gusto/blob/master/readme-documents/wireframes/wireframe-login.pdf)  	|
|  [Profile Page](https://github.com/horizons83/Milestone3-Slimming-Gusto/blob/master/readme-documents/wireframes/wireframe-profile.pdf)  	|
|  [Recipe Page](https://github.com/horizons83/Milestone3-Slimming-Gusto/blob/master/readme-documents/wireframes/wireframe-recipe.pdf)  	|
|  [Add Recipe Page](https://github.com/horizons83/Milestone3-Slimming-Gusto/blob/master/readme-documents/wireframes/wireframe-add-recipe.pdf)  	| 
|  [Admin Management Page](https://github.com/horizons83/Milestone3-Slimming-Gusto/blob/master/readme-documents/wireframes/wireframe-admin.pdf)  	|
|  [Edit Category Page](https://github.com/horizons83/Milestone3-Slimming-Gusto/blob/master/readme-documents/wireframes/wireframe-edit-category.pdf)  	|
|  [Edit Recipe Page](https://github.com/horizons83/Milestone3-Slimming-Gusto/blob/master/readme-documents/wireframes/wireframe-edit-recipe.pdf)  	|

### Fonts

For typography I have used Pacifico for the main app title and also some page headings. I then used Roboto for main text sections some
the main text bodies are clear for the user to read.

### Colour Scheme

I wanted to keep the colour scheme soft so used a mixture of soft greens and off whites.
I have created a palette using [Coolors](https://coolors.co/) and it is displayed below.
![colour palette](Milestone3-Slimming-Gusto/blob/master/readme-documents/ms3-coolors.png)

[Contents](#Table-of-Contents)

---

## Features

### Features Currently Implemented

- The website is responsive.
- Navigation in header which collapses for mobile use.
- Recipes include recipe image and a brief recipe description.
- Home page includes image slider with text overlay.
- Category images on home page which are clickable and take the user to all recipes for each category.
- Log in page.
- Log out functionality.
- Registration page.
- Forms for adding and editing recipes.
- Footer with social links.
- Admin functionality to edit categories and recipes including delete function.

### Future Features

- Build user profile page to include avatar/image and allow user to edit/delete profile or change password.
- Add comment/ratings to recipes so other registered users can rate/comment on other recipes they may try.
- Currently recipe images are stored in a Google Cloud bucket with image url stored in database, I would like to connect
app to image service so users can upload their own recipe image and this can be stored and link passed to database.

[Contents](#Table-of-Contents)

---

## Technologies Used

### Languages

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Hyper Text Markup Language, used for creating the website.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) - Cascading Style Sheet, used for styling the website.
- [Javascript](https://www.javascript.com/) – Used for providing functionality for add/edit forms and delete buttons.
- [Python](https://www.python.org/) - Language used to programme the app.

### Frameworks Libraries and Programs

* [MongoDB](https://www.mongodb.com/1)  
   * Document based database used for this project.  
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) 
   * Framework used for the project.
* [Pymongo](https://pypi.org/project/pymongo/) 
   * Pymongo was used to interact with the database.
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) 
   * Templating engine used to render data in the HTML templates.
* [Wergzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) 
   * Provides security features - generate password hash to salt the password and check password.
* [Materialize](https://materializecss.com/about.html) 
   * responsive framework.
* [Google Fonts](https://fonts.google.com/) 
   * Fonts used in design are from Google Fonts.
* [Font Awesome](https://fontawesome.com/) 
   * Used for icons and social logos.
* [Balsamiq](https://balsamiq.com/)
   * Used to create wireframes for the project.
* [Gitpod IDE](https://gitpod.io/)
   * Development environment where project was built.
* [Github](https://github.com/)
   * Used to store project repository.
* [Git](https://git-scm.com/)
   * Used for version control.
* [Heroku](https://www.heroku.com/home)
   * Platform where live site is deployed.
* [PEP 8](http://pep8online.com/)
   * Used to validate Python code.
* [W3C HTML Validator](https://validator.w3.org/)
   * Used to validate HTML code.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
   * Used to validate CSS.
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
   * Used throughout the development of the website to quickly see changes, find problems and debug. Also used to view website in different device views.
* [Lighthouse](https://developers.google.com/web/tools/lighthouse)
   * Used to test website performance.

[Contents](#Table-of-Contents)

---

## Defensive Design

* Users cannot brute force their way onto pages that they don’t have access to eg a not logged in user cannot access the add_recipe page by adding /add_recipe to the url, a flash message will be displayed asking them to log in.
* Only logged in users can access the add recipe page.
* Logged in users can only edit/delete their own recipes.
* Only admin user can access the admin pages.
* 404 error page has being included.

---

## Testing

Testing documentation can be found [here]()

---
   
## Database

### Database Collections

#### Users:

 - _id: Object_id
 - username: string
 - password: string
 
 #### Categories:
 
 - _id: Object_id
 - category_name: string
 - image: string
 
 #### Recipes:
 
 - _id: Object_id
 - category_name: string
 - recipe_title: string
 - recipe_description: string
 - serves: integer
 - prep_time: integer
 - cook_time: integer
 - kcal: string
 - ingredients: array
 - method: array
 - image_url: string
 - added_by: string

[Contents](#Table-of-Contents)

---

# Deployment

This website was created in the Gitpod development environment. After creating a new repository in GitHub using the Code Institute template, the green Gitpod button was used to initialise the repository in Gitpod. Throughout the process the git commands `git add` and `git commit` were used to store the work in the local Gitpod environment, `git push` would then be used to push the commits to the GitHub repository. From here the website could then deployed via Heroku.

## Heroku Deployment

Before creating the application in Heroku, 

1. Create a requirements.txt file in your work environment by running the following command in the command line interface:

	`pip3 freeze —local > requirements.txt`

This will save all the dependencies currently used by the app to the requirements.txt file.

2. Create a Procfile, which tells Heroku which file runs the app and how to run it. To do this run the following command in the CLI:

	`echo web: python app.py > Procfile`

3. `Git add`, `git commit` and `git push` these files to GitHub so they are available to Heroku which will use them to build the app.

### In Heroku

1. Login and click New -> Create New App
	- Add a name
	- Select region
	- Click Create App

2. Select Connect to GitHub, when the Github profile is displayed add the name of your repo and click search, once it finds & displays the correct repo click connect.

3. Set up the config vars required to run the app. In the Settings Tab click Revel Config Vars
- Create the following variables and assign their values:
            IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME
- Click Hide Config Vars

4. In the Deploy Tab
	- Click Enable Automatic Deploys
	- Select the branch the repo is using
	- Click Deploy Branch
 => Your app was successfully deployed will be displayed with the option to view the app.

## Creating A Local Clone

You can clone the repository to create a local copy on your computer.

From the Git Hub repository:
- Click `Code` at the top of the file list
- Click the clipboard icon to copy the url provided

Open terminal:
- Change the current working directory to where you want the cloned directory to be
- Type `git clone` and paste the copied url after it
- Press enter and the clone will be created

[Contents](#Table-of-Contents)

---

## Content

All recipes and recipe images are from the [Pinch Of Nom](https://pinchofnom.com/) website

Index page image slider images are from [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/):
- [Brooke Lark](https://unsplash.com/photos/jUPOXXRNdcA) on [Unsplash](https://pinchofnom.com/)
- [Adonyi Gábor](https://www.pexels.com/photo/assorted-vegetables-on-brown-wooden-table-1414651/) on [Pexels](https://www.pexels.com/)
- [Rodnae Productions](https://www.pexels.com/photo/crop-faceless-person-adding-cut-tomatoes-in-bowl-with-guacamole-5737581/) on [Pexels](https://www.pexels.com/)
- [Ponyo Sakana](https://www.pexels.com/pt-br/foto/salada-de-legumes-na-tigela-de-ceramica-3662136/) on [Pexels](https://www.pexels.com/)

index page category images are from [Unsplash](https://unsplash.com/):
- Breakfast - [Ben Kolde](https://unsplash.com/photos/FFqNATH27EM) on [Unsplash](https://unsplash.com/)
- Mains - [Louis Hansel](https://unsplash.com/photos/Si5lP0g-sR8) on [Unsplash](https://unsplash.com/)
- Dessert - [MadMax Chef](https://unsplash.com/photos/Pzjez86SsvQ) on [Unsplash](https://unsplash.com/)

---

## Acknowledgements

My mentor Gerry McBride for great support.

All at Code Institute and Tutor support.

The Slack Community for their knowledge.

##  Disclaimer

This project is for educational purposes only.

[Contents](#Table-of-Contents)