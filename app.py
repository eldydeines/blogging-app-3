"""Blogly application."""
"""Eldy Deines"""
"""App incorporates SQL Alchemy"""


"""Import necessary libraries and models"""

"""Configure flask object and set database"""
from flask import Flask, request, render_template, redirect, flash
from models import db, connect_db, User, Post, Tag, PostTag
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

""" --------------------------------------------------------------------------------"""
"""This section will connect, drop existing tables,and add new tables based on model"""
"""Section will add sample data into tables ----------------------------------------"""
""" --------------------------------------------------------------------------------"""

connect_db(app)
db.drop_all()
db.create_all()

jane = User(first_name='Calamity', last_name='Jane',
            profile_image="https://horseyhooves.com/wp-content/uploads/2020/09/Calamity-Jane-portrait.jpg")
james = User(first_name='Jesse', last_name='James', profile_image="data:image/jpeg;base64,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")
pearl = User(first_name='Pearl', last_name='Heart')
pickett = User(first_name='Bill', last_name='Pickett',
               profile_image="https://upload.wikimedia.org/wikipedia/commons/5/5f/Bill_Picket_North_Fort_Worth_Historical_Society.jpg")

db.session.add_all([jane, james, pearl, pickett])
db.session.commit()

post1 = Post(title="Cowgirls Rule", user_id=1, content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. A scelerisque purus semper eget duis at. Vulputate ut pharetra sit amet aliquam. Nunc sed blandit libero volutpat sed cras ornare. Neque viverra justo nec ultrices dui sapien eget mi.')
post2 = Post(title="Robbery in the Saloon", user_id=4, content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. A scelerisque purus semper eget duis at. Vulputate ut pharetra sit amet aliquam. Nunc sed blandit libero volutpat sed cras ornare. Neque viverra justo nec ultrices dui sapien eget mi.')
post3 = Post(title="New Sheriff in Town", user_id=2, content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. A scelerisque purus semper eget duis at. Vulputate ut pharetra sit amet aliquam. Nunc sed blandit libero volutpat sed cras ornare. Neque viverra justo nec ultrices dui sapien eget mi.')
post4 = Post(title="Old West", user_id=3, content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. A scelerisque purus semper eget duis at. Vulputate ut pharetra sit amet aliquam. Nunc sed blandit libero volutpat sed cras ornare. Neque viverra justo nec ultrices dui sapien eget mi.')
post5 = Post(title="Riding over the Rockies", user_id=3, content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. A scelerisque purus semper eget duis at. Vulputate ut pharetra sit amet aliquam. Nunc sed blandit libero volutpat sed cras ornare. Neque viverra justo nec ultrices dui sapien eget mi.')
post6 = Post(title="Reward for Calamity Jane", user_id=1, content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. A scelerisque purus semper eget duis at. Vulputate ut pharetra sit amet aliquam. Nunc sed blandit libero volutpat sed cras ornare. Neque viverra justo nec ultrices dui sapien eget mi.')

db.session.add_all([post1, post2, post3, post4, post5, post6])
db.session.commit()

cowboy = Tag(name="cowboy")
cowgirl = Tag(name="cowgirl")
oldWest = Tag(name="OldWest")

db.session.add_all([cowboy, cowgirl, oldWest])
db.session.commit()

firstA = PostTag(post_id=1, tag_id=2)
secondB = PostTag(post_id=1, tag_id=3)
thirdC = PostTag(post_id=3, tag_id=1)

db.session.add_all([firstA, secondB, thirdC])
db.session.commit()


""" -----------------------------------------------------------------------"""
""" ------------------------   ROUTES -------- ----------------------------"""
""" -----------------------------------------------------------------------"""


@app.route('/')
def homepage():
    """homepage for oldwest blog site"""
    recent_posts = Post.query.order_by(Post.id.desc()).limit(5)
    return render_template('index.html', posts=recent_posts)


""" -----------------------------------------------------------------------"""
""" ------------------------   ROUTES FOR USER ----------------------------"""
""" -----------------------------------------------------------------------"""


@app.route('/users')
def list_users():
    """List users in order by last_name"""
    all_users = User.query.order_by(User.last_name).all()
    return render_template('users.html', users=all_users)


@app.route('/users/new')
def render_user_form():
    """renders a create user form"""
    return render_template('new.html')


@app.route('/users/new', methods=["POST"])
def create_user():
    """get input to create a user and post to database"""
    first_name = request.form['first'].capitalize()
    last_name = request.form['last'].capitalize()
    profile_image = request.form['image']
    new_user = User(first_name=first_name, last_name=last_name,
                    profile_image=profile_image)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')


@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details of user"""
    found_user = User.query.get_or_404(user_id)
    found_all_posts = Post.query.filter_by(user_id=user_id)
    count = found_all_posts.count()
    return render_template('details.html', user=found_user, posts=found_all_posts, count=count)


@app.route('/users/<int:user_id>/edit')
def show_edit_user(user_id):
    """Get user that needs to be updated"""
    edit_user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=edit_user)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def update_user(user_id):
    """Edit User and post """
    edit_user = User.query.get(user_id)
    first = request.form['first']
    if first:
        edit_user.first_name = first
    last = request.form['last']
    if last:
        edit_user.last_name = last
    image = request.form['image']
    if image:
        edit_user.profile_image = image
    db.session.add(edit_user)
    db.session.commit()
    return redirect('/users')


@app.route('/users/<int:user_id>/delete')
def show_deleted_user(user_id):
    """Confirm User to be deleted"""
    delete_user = User.query.get_or_404(user_id)
    return render_template('delete.html', user=delete_user)


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """Delete user from database and all their posts"""
    del_user = User.query.get(user_id)
    db.session.delete(del_user)
    db.session.commit()
    return redirect('/')


@app.route('/users/<int:user_id>/posts/new')
def show_post_form(user_id):
    """Show template to add post with available tags"""
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template('add-post.html', user=user, tags=tags)


@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def add_new_post(user_id):
    """adds new post to database"""
    title = request.form['title']
    content = request.form['content']
    # No information on best approach for getting checkbox info --resorted to solution
    tag_ids = [int(num) for num in request.form.getlist("tags")]
    new_tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
    new_post = Post(title=title, content=content,
                    user_id=user_id, tagged=new_tags)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/users/{user_id}')


""" -----------------------------------------------------------------------"""
""" ------------------------   ROUTES FOR POSTS ---------------------------"""
""" -----------------------------------------------------------------------"""


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """Show details of user"""
    selected_post = Post.query.get(post_id)
    writer = User.query.get(selected_post.user_id).get_fullname()
    tags = selected_post.tagged
    return render_template('post.html', this_post=selected_post, full_name=writer, tags=tags)


@app.route('/posts/<int:post_id>/edit')
def show_edit_post(post_id):
    """Get user that needs to be updated"""
    edit_post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()
    return render_template('edit-post.html', post=edit_post, tags=tags)


@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def update_post(post_id):
    """Edit post and post """
    edit_post = Post.query.get(post_id)
    title = request.form['title']
    if title:
        edit_post.title = title
    content = request.form['content']
    if content:
        edit_post.content = content
    tag_ids = [int(num) for num in request.form.getlist("tags")]
    update_tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
    edit_post.tagged = update_tags
    db.session.add(edit_post)
    db.session.commit()
    return redirect(f'/users')


@app.route('/posts/<int:post_id>/delete')
def show_deleted_post(post_id):
    """Confirm User to be deleted"""
    delete_post = Post.query.get_or_404(post_id)
    return render_template('delete-post.html', post=delete_post)


@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def delete_post(post_id):
    """Delete user from database"""
    PostTag.query.filter_by(post_id=post_id).delete()
    Post.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect('/')


""" -----------------------------------------------------------------------"""
""" ------------------------   ROUTES FOR TAGS  ---------------------------"""
""" -----------------------------------------------------------------------"""


@app.route('/tags')
def list_tags():
    """ List tags in order by name """
    all_tags = Tag.query.order_by(Tag.name).all()
    return render_template('all-tags.html', tags=all_tags)


@app.route('/tags/create-tag')
def render_tag_form():
    """renders a create tag form"""
    return render_template('create-tag.html')


@app.route('/tags/create-tag', methods=["POST"])
def create_tag():
    """get input to create new tag and post to database"""
    name = request.form['tag'].lower()
    new_tag = Tag(name=name)
    db.session.add(new_tag)
    db.session.commit()
    return redirect('/tags')


@app.route('/tags/<int:id>')
def show_tag(id):
    """Show details of tag"""
    selected_tag = Tag.query.get(id)
    posts = selected_tag.posts
    return render_template('show-tag.html', tag=selected_tag, posts=posts)


@app.route('/tags/<int:id>/edit')
def show_edit_tag(id):
    """Get user that needs to be updated"""
    edit_tag = Tag.query.get_or_404(id)
    return render_template('edit-tag.html', tag=edit_tag)


@app.route('/tags/<int:id>/edit', methods=["POST"])
def update_tag(id):
    """Edit User and post """
    edit_tag = Tag.query.get(id)
    name = request.form['tag'].lower()
    if name:
        edit_tag.name = name
    db.session.add(edit_tag)
    db.session.commit()
    return redirect('/tags')


@app.route('/tags/<int:id>/delete')
def show_deleted_tag(id):
    """Confirm User to be deleted"""
    delete_tag = Tag.query.get_or_404(id)
    return render_template('delete-tag.html', tag=delete_tag)


@app.route('/tags/<int:id>/delete', methods=["POST"])
def delete_tag(id):
    """Delete user from database"""
    PostTag.query.filter_by(tag_id=id).delete()
    Tag.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/')
