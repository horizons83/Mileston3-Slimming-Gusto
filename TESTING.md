# Testing
---

# Code Validators

---

## CSS code was passed through Auto Prefixer to add vendor prefixes
* Prefixed by https://autoprefixer.github.io
* PostCSS: v7.0.29,
* Autoprefixer: v9.7.6
* Browsers: last 4 version
---
## CSS code was passed through the W3C CSS Validator 

No errors found and 8 warnings all relating to vendor prefixes.

---
## HTML code was passed through the W3C Markup Validator. 

Errors found and resolved:

* In base.html a parse error was shown in footer copyright because of semicolon. removed semicolon and retested, no error now shown.
* In categories.html a stray closing /div was found in the h3 element. This was removed and retested no error now shown.

---
## Javascript code was passed through jshint. 

1 undefined variable was found: $ ( this relates to jquery syntax. )

---
## Python code was passed through PEP8 online. 

app.py passed through and returned no errors.

---

# Lighthouse from Chrome Dev Tools

|                         | DESKTOP     |               |               |     | MOBILE      |               |               |     |
|-------------------------|-------------|---------------|---------------|-----|-------------|---------------|---------------|-----|
|                         | Performance | Accessibility | Best Practice | SEO | Performance | Accessibility | Best Practice | SEO |
| Home Page:              | 96          | 93            | 80            | 100 | 67          | 93            | 80            | 92  |
| Register Page:          | 100         | 92            | 93            | 100 | 93          | 96            | 93            | 91  |
| Sign In Page:           | 100         | 92            | 93            | 100 | 94          | 96            | 93            | 100 |
| Categories Page:        | 100         | 88            | 93            | 100 | 93          | 94            | 93            | 100 |
| Recipe Page:            | 100         | 86            | 93            | 100 | 98          | 91            | 93            | 100 |
| My Recipes Page:        | 100         | 88            | 93            | 100 | 93          | 88            | 93            | 100 |
| Add Recipe Page:        | 99          | 83            | 93            | 89  | 91          | 83            | 93            | 91  |
| Edit Recipe Page:       | 100         | 81            | 93            | 89  | 91          | 81            | 93            | 91  |
| Manage Categories Page: | 100         | 88            | 93            | 100 | 91          | 88            | 93            | 100 |
| Edit Category Page:     | 100         | 92            | 93            | 100 | 93          | 92            | 93            | 100 |
| Add Category Page:      | 100         | 92            | 93            | 100 | 93          | 92            | 93            | 100 |

---

# Responsiveness Testing

The responsiveness of the website was tested using Chrome Dev Tools and setting it to display on various mobile/tablet devices that are included. Responsiveness is optimised for screen sizes from 320px up and in portrait orientation for smaller devices.

---

# Device Testing

All aspects of the website mentioned above were manually tested on the following 
devices a mixture of my own and family: iPad Air 2, iPad Pro 11, iPhone SE, iPhone 11, iPhone 12 Pro Max, Samsung Tab S6 Pro, Oppo X2 Neo and a 17.3inch Windows Laptop .

---

# Browser Testing

All aspects of the website mentioned above were manually tested on the following 
browsers: Chrome, Safari, Mozilla Firefox.

---

# Testing User Experience

## Testing User Requirements

1. **As a User I want to be able to easily understand the main purpose of the website.**
   * Home page is welcoming and clearly states the intentions of the site.
   * Invites users to browse and sign up to share recipes.
2. **As a User I want to be able to easily navigate the website.**
   * Clear navigation instructs users how to use the site.
   * Font icons help to direct the user.
   * Mobile devices have slide out menu with navigation links.
3. **As a User I want to easily search and find recipes to follow.**
   * Home page search bar allows users to search recipes by name or part of name.
   * Home page also has image cards of recipe categories which are clickable and will take the user to a list of all recipes for that category.
   * Search page shows results and lists recipes for search criteria or advises no recipes found.
   * Recipe page displays image of recipe along with recipe info, description, ingredients list and method list for user to follow.
4. **As a User I want to be able to register to the site to gain access to the full features of the website.**
   * A registration page is provided where users can sign up using a username and password.
   * The app will alert the user if username is already taken.
   * Sign up form fields use placeholder text to advise user of requirements for username and password.
5. **As a User I want to see to be able to add my slimming recipes to the site to share with others.**
   * My Recipes page has add recipe button and nav includes link to add recipe page.
   * Add recipe page displays card panel with labelled input fields for user to add recipe details.
   * Recipes added by users list in the My Recipes page.
6. **As a User I want to be able to access, edit and update all recipes I have added to the site.**
   * The My Recipes page lists all recipes added by the user by title.
   * User can click title to display the recipe description and buttons where user can select see recipe, edit recipe or delete recipe.
   * The edit button for the recipe takes the user to the edit page where all fields are populated with the current data held for that recipe and they can edit and store
     any changes made.
7. **As a User I want to be able to delete a recipe I have added to the site.**
   * My recipes page includes a delete button for each recipe added.
   * Delete button re-affirms users request to delete recipe by asking if they are sure they want to delete and has yes or no buttons.
   
---

## Testing Owner Requirements

1. **As an Owner I want the home page to immediately tell the User what the site is for.**
   * Home page welcomes users image slider text provides clear statements.
   * Search bar invites users to search for recipes.
   * category cards provide links to recipes in each category.
2. **As an Owner I want the User to be able to easily navigate the site via navigation links.**
   * Nav bar provided for large devices and nav slide menu for devices upto 992px
   * Nav is available on all pages except 404 error page.
   * Font icons on larger devices add extra visual indication.
3. **As an Owner I want users to be able to register to the site to access all features.**
   * Registration page is provided for users to sign up.
   * Placeholder text is used to instruct user on requirements for username and password.
   * link is provided for users already registered to go to log in page.
   * Seperate log in page provided for registered users to sign in.
4. **As an Owner I want users to be able to add recipes to the site to build database and share with others.**
   * My Recipes page has Add Recipe button.
   * Add Recipe link is provided in Nav bar.
   * Add Recipe form is straight forward and contains all inputs and relevent information needed to add recipe to database.
5. **As an Owner I want users to be able to be able to see,edit and delete any recipes they have added.**
   * My Recipes page lists all recipes added by user by title which when clicked reveal recipe description with buttons to see recipe, edit and delete.
   * Recipe page displays recipe image, info, description, ingredients and method.
   * Edit recipe button takes user to edit page with form fields populated with recipe details which can be edited. 
   * Delete recipe button provided which confirms user wants to delete recipe by using yes or no buttons.
6. **As an Owner I want to be able to be able to see, edit and delete any recipes added and manage recipe categories.**
   * Manage page provides admin with list of current categories and list of all recipes.
   * Categories list has add category button allowing admin to add new category.
   * All categories have edit button and delete button.
   * Add category and edit category pages have cancel buttons which will take admin back to management panel.
   * All recipes have edit and delete buttons.
   
---

# Manual Testing

Each page was tested and passed under the criteria set out below.

## All Pages 

### Header:

* Displays on all pages.

    #### Logo:

* The logo is displayed in the header.

* Logo displays on all pages.

* The logo is a clickable link which returns the user to the home page.

	#### Navigation:

* Displays on all pages except 404.html page
* On devices of 992px or lower a menu slider is provided by clicking hamburger icons
* On larger devices navigation items appear in header with icons and text.
* **Navigation items are:**
   * Clickable.
   * Link to associated page.
* **For users not registered/logged in the navigation items displayed are:**
   * Home
   * Register 
   * Log In 
* **For users that are logged in the navigation items diplayed are:**
   * Home
   * My Recipes
   * Add Recipe
   * Log Out
* **For admin users logged in the navigation items displayed are:**
   * Home
   * My Recipes
   * Add Recipes
   * Manage Categories/Recipes
   * Log Out   

### Footer:

* Displays on all pages except 404.html.
* Contains Social icons which link to associated social site.

## Home Page

* Displays for all users

### Image Slider

* displays responsive images on all devices.
* Each image displays text messages.

### Search Bar

* Search bar available on all devices.
* Can be reset.
* Returns search results.

### Category Image Cards

* Displays responsive image on all devices.
* Contains category name.
* Clickable to take user to list of all recipes within category.

