from flask import Flask, render_template
import requests
import post

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

all_posts = requests.get(url=blog_url)
all_posts = all_posts.json()

all_post_class = [post.Post(id=posts["id"],
                            title=posts["title"],
                            subtitle=posts["subtitle"],
                            body=posts["body"])
                  for posts in all_posts]

@app.route("/")
def home():

    return render_template("index.html", posts=all_post_class)

@app.route("/<id>")
def blog_page(id):

    selected_post = [posts for posts in all_post_class if int(id) == posts.id]
    selected_post = selected_post[0]
    return render_template("post.html", post = selected_post)




if __name__ == "__main__":
    app.run(debug=True)

