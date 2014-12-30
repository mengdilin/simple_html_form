from pymongo import Connection

Connection = Connection('mongo.stuycs.org')

def connect():
    db=Connection.admin
    res=db.authenticate('ml7','ml7')
    db=Connection['z-pd7']
    stories=db.stories
    return stories

#add a story into stories collection by inserting a new dictionary called story
#if the story already exists, the method returns false, else it returns true
def add_story(title):
    stories=connect()
    if(stories.find({'title':title}).count()!=0):
        return False
    story={'title':title,'comments':[]}
    stories.insert(story)

#delete a story from stories
def delete_story(title):
    stories=connect()
    story=stories.find_one({'title':title})
    stories.remove(story)

#add a comment to the story having a specific title
def add_comment(title,comment):
    stories=connect()
    if(stories.find({"title":title}).count()!=0):
        story=stories.find_one({"title":title})
        story['comments'].append(comment) 
        stories.update({"title":title},story)

#return all story titles in a list
def get_stories():
    stories=connect()
    titles=[]
    for story in stories.find():
        if "title" in story.keys():
            titles.append(story["title"])
    return titles

#return all comments in a list
def get_comments(title):
    stories=connect()
    for story in stories.find({"title":title}):
        return story["comments"]

def delete_stories():
    stories=connect()
    stories.drop()


