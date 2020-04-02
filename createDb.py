from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Abrar.786@localhost/all_post';
db=SQLAlchemy(app);

class Arduinoproject_posts(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False);
    date=db.Column(db.String(50), nullable=False);
    reading_time=db.Column(db.String(50), nullable=False);
    heading=db.Column(db.String(100), nullable=False);
    
    content=db.relationship('Content',backref='post_name');
    img=db.relationship('Images',backref='post_name');
    comment=db.relationship('Comments',backref='post_name');
    
    
class Content(db.Model):
   
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    part1=db.Column(db.String(500),nullable=True)
    part2=db.Column(db.String(500),nullable=True)
    part3=db.Column(db.String(500),nullable=True)
    part4=db.Column(db.String(500),nullable=True)
    part5=db.Column(db.String(500),nullable=True)
    part6=db.Column(db.String(500),nullable=True)
    part7=db.Column(db.String(500),nullable=True)
    part8=db.Column(db.String(500),nullable=True)
    part9=db.Column(db.String(500),nullable=True)
    part10=db.Column(db.String(500),nullable=True)
    arduinopost_id=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))
        
    
class Images(db.Model):
       
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    img1=db.Column(db.String(500),nullable=True)
    img2=db.Column(db.String(500),nullable=True)
    img3=db.Column(db.String(500),nullable=True)
    img4=db.Column(db.String(500),nullable=True)
    img5=db.Column(db.String(500),nullable=True)
    img6=db.Column(db.String(500),nullable=True)
    img7=db.Column(db.String(500),nullable=True)
    img8=db.Column(db.String(500),nullable=True)
    img9=db.Column(db.String(500),nullable=True)
    img10=db.Column(db.String(500),nullable=True)
    arduinopost_naemid=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))
        
class Comments(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(100),nullable=False)
    comment=db.Column(db.String(200),nullable=False)
    
    arduinopost_nameid=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))
    
    replies=db.relationship('Comment_replies',backref='comment_name');
    
    
class Comment_replies(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(200),nullable=False)
    reply=db.Column(db.String(200),nullable=False)
    
    Comment_nameid=db.Column(db.Integer,db.ForeignKey('comments.id'))
           
           
    
    

