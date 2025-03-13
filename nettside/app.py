from flask import Flask, render_template, request, redirect, url_for, flash
from db.database import create_table, add_user, get_users, delete_user_by_id, add_post, get_posts

app = Flask(__name__)
app.config["SECRET_KEY"] = "local_secret_key"

# Ensure the database table exists
create_table()

@app.route("/")
def home():
    """Show all users in the database."""
    return render_template("index.html")

@app.route("/database_content", methods=["GET", "POST"])
def database_content():
    """Show all users in the database."""
    users = get_users()
    return render_template("database_content.html", users=users)

@app.route("/add_user", methods=["GET", "POST"])
def add_user_route():
    """Handle adding a user via a form."""
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]

        if not username or not email:
            flash("Both fields are required!", "danger")
        else:
            try:
                add_user(username, email)
                flash("User added successfully!", "success")
                return redirect(url_for("home"))
            except:
                flash("Username or Email already exists!", "warning")

    return render_template("add_user.html")

@app.route("/delete_user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    """Delete a user by ID."""
    delete_user_by_id(user_id)  # Calls the function from `database.py`
    flash("User deleted successfully!", "success")
    return redirect(url_for("home"))

@app.route("/add_post", methods=["GET", "POST"])
def add_post_route():
    """Handle adding a post via a form."""
    users = get_users()  # Fetch users for dropdown
    if request.method == "POST":
        user_id = request.form["user_id"]
        content = request.form["content"]

        if not user_id or not content:
            flash("All fields are required!", "danger")
        else:
            add_post(user_id, content)
            flash("Post added successfully!", "success")
            return redirect(url_for("home"))

    return render_template("add_post.html", users=users)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
