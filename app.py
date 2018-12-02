#importing libraries and dependencies

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# creating Flask app

app = Flask(__name__)

# connecting to PyMongo

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_anaylsis_db"
mongo = PyMongo(app)


# creating route 

@app.route("/")
def index():
    
        mars_data = mongo.db.mars_data.find_one()
        
        return render_template("index.html", mars_data = mars_data)
 

# creating scrape function

@app.route("/scrape")
def scrape():
    mars_data = mongo.db.mars_data
    mars_data_scrape = scrape_mars.scrape()

    mars_data.update({}, mars_data_scrape, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
