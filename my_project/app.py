import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="sagar",
    password="1234",
    database="banglore_pgs"
)
print("Database connection established.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form["name"]
    age = request.form["age"]
    college = request.form["college"]
    
    return f"""
<center>

    <h1 style="color: red;font-family: georgia;">Your Profile</h1>
</center>
    <h2 style="font-size: 35px;">Name: {name}</h2>
    <h2 style="font-size: 35px;">Age: {age}</h2>
    <h2 style="font-size: 35px;">College: {college}</h2>
    
    <p style="font-size: 50px;">Thank you for submitting your profile!</p>


"""

if __name__ == "__main__":
    app.run(debug=True)
