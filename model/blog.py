from database import Database

__author__ = "adarsh"

import datetime
from model.post import Post
import uuid


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title : ")
        content = input("Enter Post content : ")
        date = input("Enter the post date or leave blank for today (in format DDMMYYYY)")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date,"%d%m%Y")
        post = Post(blog_id= self.id,
                    title = title,
                    content= content,
                    author=self.author,
                    date=date)
        post.save_to_mongo()

    def get_post(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection="posts",
                        data=self.json())

    def json(self):
        return {
            "author" : self.author,
            "title"  : self.title,
            "description" : self.description,
            "id" : self.id
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection="posts", query={"id":id})
        return cls(author=blog_data["author"],
                   title=blog_data["title"],
                   description=blog_data["description"],
                   id=blog_data["id"])


