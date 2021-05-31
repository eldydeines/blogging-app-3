"""Blogly application."""
"""Eldy Deines"""
"""App incorporates SQL Alchemy"""


"""Import necessary libraries and models"""
from flask import Flask, request, render_template, redirect, flash
from models import db, connect_db, User


"""Configure flask object and set database"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


"""This will connect, drop existing tables, 
   and add new tables based on model
"""
connect_db(app)
db.drop_all()
db.create_all()


@app.route('/')
@app.route('/users')
def list_users():
    """shows homepage"""
    all_users = User.query.all()
    return render_template('users.html', users = all_users)


@app.route('/users/new')
def render_user_form():
    """renders a create user form"""
    return render_template('new.html')


@app.route('/users/new', methods=["POST"])
def create_user():
    """get input to create a user and post to database"""

    first_name = request.form['first']
    last_name = request.form['last']
    profile_image = request.form['image']

    new_user = User(first_name=first_name, last_name=last_name, profile_image=profile_image)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details of user"""
    found_user = User.query.get_or_404(user_id)
    return render_template('details.html', user=found_user)


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
    """Delete user from database"""
    User.query.filter_by(id = user_id).delete()
    db.session.commit()
    
    return redirect('/')