from orm import Database, Table, Column, ForeignKey

db = Database("./test.db")

class Author(Table):
    name = Column(str)
    lucky_number = Column(int)

class Post(Table):
    title = Column(str)
    published = Column(bool)
    author = ForeignKey(Author)

class Book(Table):
    title =  Column(str)
    Published = Column(int)
    Author = ForeignKey(Author)
    noofchapter = Column(int)


db.create(Author)
db.create(Post)



greg = Author(name="Greg Back",lucky_number=13)

print("data table for Author and Post is created")
db.save(greg)

authors = db.all(Author)

bob = db.get(Author, 47)

post = Post(title="Building an ORM",published=True,author=greg)

db.save(post)


print(Post.get(55).author.name)