from datetime import date

__author__ = "adarsh"

import datetime
import uuid
from database import Database


class Post(object):
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.title = title
        self.content = content
        self.author = author
        self.blog_id = blog_id
        self.created_date = date
        self.id = uuid .uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection= "posts",
                        data = self.json())

    def json(self):
        return {
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "blog_id": self.blog_id,
            "created_date": self.created_date,
            "id": self.id
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection="posts",query={"id":id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_data['id'])

    @staticmethod
    def from_blog(blog_id):
        return [posts for posts in Database.find(collection="posts", query={"blog_id" : blog_id})]