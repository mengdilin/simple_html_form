from flask import Flask
from flask import url_for, redirect, request, render_template, flash
import database

app=Flask(__name__)
app.secret_key='secret'

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET':
         return render_template("home.html",titles=database.get_stories())      
    if request.method=='POST':
        if(request.form["button"]=="Submit"):
            database.add_story(str(request.form['title']))
            return render_template("home.html",titles=database.get_stories())
        elif (request.form["button"]=="Go To Story"):
            title=str(request.form['select'])
            assert title!=""
            return render_template("story.html",title=title,comments=database.get_comments(title))     
        elif (request.form["button"]=="Delete Story"):
            title=str(request.form['select'])
            database.delete_story(title)
            return render_template("home.html",titles=database.get_stories())
       
@app.route("/story",methods=['GET','POST'])
def story():
    if request.method=="POST":
        if request.form["button"]=="comment":
            comment=str(request.form["comments"])
            title=str(request.form["title"])
            database.add_comment(title,comment)
            return render_template("story.html",title=title,comments=database.get_comments(title))
        if request.form["button"]=="go back":
            return redirect(url_for("index"))


if __name__=="__main__":
    app.run(port=5000)
 
