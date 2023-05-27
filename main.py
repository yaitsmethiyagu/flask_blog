from flask import Flask, render_template
import requests


app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

@app.route('/nchch')
def home():
    all_posts = requests.get(url=blog_url)
    all_posts = all_posts.json()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
