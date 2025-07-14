from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory member records for demonstration
members = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/packages")
def packages():
    return render_template("packages.html")

@app.route("/edit_member")
def edit_member():
    return render_template("edit_member.html", members=members)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        package = request.form["package"]
        members.append({"name": name, "email": email, "package": package})
        return redirect("/")
    return render_template("register.html")

@app.route("/attendance")
def attendance():
    return render_template("attendance.html")

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        feedback_text = request.form["feedback"]
        print("Feedback received:", feedback_text)
        return redirect("/")
    return render_template("feedback.html")

if __name__ == "__main__":
    app.run(debug=True)
