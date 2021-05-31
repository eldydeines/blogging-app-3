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
    profile_image = db.Column(db.String(200), nullable=True, default="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/480px-No_image_available.svg.png")


    def __repr__(self):
        """show info about user in cmd prompt"""
        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} profile_image={u.profile_image}>"

