import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    categories = list(mongo.db.categories.find())
    return render_template("index.html", categories=categories)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user onto 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("my_recipes", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "my_recipes", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # If username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/search_page")
def search_page():
    return render_template("search_page.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("search_page.html", recipes=recipes, query=query)


@app.route("/my_recipes/<username>")
def my_recipes(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # Once session['user] cookie is truthy return their profile page
    if session["user"]:
        recipes = mongo.db.recipes.find(
            {"added_by": session["user"]}).sort("_id", -1)
        return render_template(
            "my_recipes.html", username=username,
            recipes=recipes, title="Profile")

    return redirect(url_for("login"))


@app.route("/categories/<category>/<recipe_url>/<recipe_id>")
def recipe(category, recipe_url, recipe_id):
    # Display recipe information
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    method = recipe["method"]
    ingredients = recipe["ingredients"]
    return render_template(
        "recipes.html", recipe=recipe, method=method,
        ingredients=ingredients)


@app.route("/logout")
def logout():
    # remove user session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # Enable user to add recipe to database
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name").lower(),
            "recipe_title": request.form.get("recipe_title"),
            "recipe_description": request.form.get("recipe_description"),
            "serves": int(request.form.get("serves")),
            "prep_time": int(request.form.get("prep_time")),
            "cook_time": int(request.form.get("cook_time")),
            "kcal": request.form.get("kcal"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "image_url": request.form.get("image_url"),
            "added_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added Successfully")
        return redirect(url_for("add_recipe"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # Enable user to edit recipe they have added to database.
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_title": request.form.get("recipe_title"),
            "recipe_description": request.form.get("recipe_description"),
            "serves": int(request.form.get("serves")),
            "prep_time": int(request.form.get("prep_time")),
            "cook_time": int(request.form.get("cook_time")),
            "kcal": request.form.get("kcal"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "image_url": request.form.get("image_url"),
            "added_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe successfully updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", categories=categories,
                           recipe=recipe)


@app.route("/categories/<category_name>")
def category(category_name):
    # List categories on index.html
    name = category_name
    category = mongo.db.categories.find_one({"category_name": category_name})
    recipes = list(mongo.db.recipes.find({"category_name": category_name}))
    return render_template(
        "categories.html", recipes=recipes, name=name, category=category)


@app.route("/manage")
def manage():
    # Allow admin user to manage categories and recipes
    # Direct user to login if not in session
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_title", 1))
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))
    # If user in session is Admin then show category list and recipe list
    if session["user"] == "admin":
        categories = list(mongo.db.categories.find().sort("category_name", 1))
        recipes = list(mongo.db.recipes.find().sort("recipe_title", 1))
    return render_template(
        "manage.html", categories=categories, recipes=recipes)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # Allow admin to add categories
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))
    if session["user"] == "admin":
        if request.method == "POST":
            category = {
             "category_name": request.form.get("category_name"),
             "image": request.form.get("image")
            }
            mongo.db.categories.insert_one(category)
            flash("New Category Added")
            return redirect(url_for("manage"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    # Allow admin to edit categories
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "image": request.form.get("image")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("manage"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    # Allow user to delete recipe
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("index"))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    # Allow Admin user to delete category
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))
    if session["user"] == "admin":
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("Category successfully deleted")
    return redirect(url_for("manage"))


@app.errorhandler(404)
def not_found_error(error):
    # 404 error page to handle any errors
    return render_template('404.html', error=error, title="404 Error"), 404


@app.errorhandler(500)
def internal_server_error(error):
    # 500 error handling page
    return render_template('500.html', error=error, title="500 Error"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
