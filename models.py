from flask_sqlalchemy import SQLAlchemy

"""Initialize variable for database"""
db = SQLAlchemy()

def connect_db(app):
    """need to associate our app with db and connect"""
    db.app = app
    db.init_app(app)


"""Models for Blogly."""

class User(db.Model):
    """USER MODEL"""
    
    __tablename__ = "users"

    # table columns setup
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    profile_image = db.Column(db.Text, nullable=True, default="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/480px-No_image_available.svg.png")

    #creates relationship and cascade for post deletion if user is deleted
    posts = db.relationship('Post', cascade='all, delete')

    def __repr__(self):
        """show info about user in cmd prompt"""
        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} profile_image={u.profile_image}>"

    def get_fullname(self):
        """generates full_name string"""
        return self.first_name.capitalize() + " " + self.last_name.capitalize()

class Post(db.Model):
    """BLOG POSTS MODEL"""

    __tablename__ = "posts"

    # table columns setup
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.String(30), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    #establishs relationship with User Table
    user = db.relationship('User')

    def __repr__(self):
        """show info about post in cmd prompt"""
        p = self
        return f"<Post id={p.id} title={p.title} added_by={p.user_id}>"


