from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "8891techa0128"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def p_survey():
    if request.method == "POST":
        user_name = request.form["user_name"]
        location = request.form["select_dojo"]
        language = request.form["select_language"]

        session["user_name"] = user_name
        session["dojo_location"] = location
        session["favorite_language"] = language
        return redirect("/result")
    
@app.route("/result")
def r_survey():
    if not any(key in session for key in ["user_name", "dojo_location", "favorite_language"]):
        return redirect("/")
    user_name = session["user_name"]
    dojo_location = session["dojo_location"]
    favorite_language = session["favorite_language"]
    return render_template("result.html", user_name=user_name, dojo_location = dojo_location, favorite_language = favorite_language)

if __name__ == ("__main__"):
    app.run(debug=True)