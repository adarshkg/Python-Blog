from model.blog import Blog
from database import Database

Database.initialize()

blog = Blog(author= "adarsh",
            title = "Sample title",
            description="Sample Description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_post())

