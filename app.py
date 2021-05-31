"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/')
@app.route('/users')
def list_users():
    """shows homepage"""
    all_users = User.query.all()
    return render_template('users.html', users = all_users)


@app.route('/users/new')
def render_user_form():
    return render_template('new.html')

@app.route('/users/new', methods=["POST"])
def create_user():
    first_name = request.form['first']
    last_name = request.form['last']
    profile_image = request.form['image']

    new_user = User(first_name=first_name, last_name=last_name, profile_image=profile_image)
    print(new_user)
    db.session.add(new_user)
    db.session.commit()

    #remember to use redirect with post methods
    return redirect('/users')


@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details of user"""
    found_user = User.query.get_or_404(user_id)
    return render_template('details.html', user=found_user)


@app.route('/users/<int:user_id>/edit')
def show_edit_user(user_id):
    """Edit User"""
    edit_user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=edit_user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def update_user(user_id):
    """Edit User"""
    edit_user = User.query.get(user_id)
    edit_user.first_name = request.form['first']
    edit_user.last_name = request.form['last']
    edit_user.profile_image = request.form['image']

    db.session.add(edit_user)
    db.session.commit()
    
    return redirect('/users')

@app.route('/users/<int:user_id>/delete')
def show_deleted_user(user_id):
    """Edit User"""
    delete_user = User.query.get_or_404(user_id)
    return render_template('delete.html', user=delete_user)


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    
    print(User.query.get(user_id))
    User.query.filter_by(id = user_id).delete()
    db.session.commit()
    
    return redirect('/')