from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Abrar.786@localhost/all_post';
app.config['SQLALCHEMY_BINDS']={'other_details':'mysql://root:Abrar.786@localhost/other_details'}
db=SQLAlchemy(app);

# ! all_post Table starts---------------------------------------------------------------------------------------
# TODO hoe to aces elements using below database structure------>>>

# ?   -----example is taken of Arduinoproject_posts table---- alias of Arduinoproject_posts is App
# ?   App_obj_name.content_parts[index_num].columns -----1 (.part1 or .img1)
# ?   App_obj_name.comment[index_num].column ----3
# ?   App_obj_name.comment[index_num].replies[index_num].column ----3
# ?   PERFECT >>>>        {+++**+++}     {+++**++++}         
# ?                             
# ?                                   00
# ?                          ----___     ___----
#?                                  -----  

class Arduinoproject_posts(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False);
    date=db.Column(db.String(50), nullable=False);
    reading_time=db.Column(db.String(50), nullable=False);
    heading=db.Column(db.String(100), nullable=False);
    
    content_parts=db.relationship('Content',backref='post_name');
   
    comment=db.relationship('Comments',backref='post_name');
    
    
class Content_arduino(db.Model):
   
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
    arduinopost_id=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))
        
    
        
class Comments_arduino(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(100),nullable=False)
    comment=db.Column(db.String(200),nullable=False)
    
    arduinopost_nameid=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))
    
    replies=db.relationship('Comment_replies',backref='comment_name');
    
    
class Comment_replies_arduino(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(200),nullable=False)
    reply=db.Column(db.String(200),nullable=False)
    
    Comment_nameid=db.Column(db.Integer,db.ForeignKey('comments_arduino.id'))
# *-----------------------------------------------------------------------------------------------------------
class Basicproject_posts(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False);
    date=db.Column(db.String(50), nullable=False);
    reading_time=db.Column(db.String(50), nullable=False);
    heading=db.Column(db.String(100), nullable=False);
    
    content_parts=db.relationship('Content',backref='post_name');
    
    comment=db.relationship('Comments',backref='post_name');
    
    
class Content_basic(db.Model):
   
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
    basicpost_id=db.Column(db.Integer,db.ForeignKey('basicproject_posts.id'))
        
    
        
class Comments_basic(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(100),nullable=False)
    comment=db.Column(db.String(200),nullable=False)
    
    basicpost_nameid=db.Column(db.Integer,db.ForeignKey('basicproject_posts.id'))
    
    replies=db.relationship('Comment_replies',backref='comment_name');
    
    
class Comment_replies_basic(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(200),nullable=False)
    reply=db.Column(db.String(200),nullable=False)
    
    Comment_nameid=db.Column(db.Integer,db.ForeignKey('comments_basic.id'))
# *-----------------------------------------------------------------------------------------------------------
class Iotproject_posts(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False);
    date=db.Column(db.String(50), nullable=False);
    reading_time=db.Column(db.String(50), nullable=False);
    heading=db.Column(db.String(100), nullable=False);
    
    content_parts=db.relationship('Content',backref='post_name');
   
    comment=db.relationship('Comments',backref='post_name');
    
    
class Content_iot(db.Model):
   
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
    iotpost_id=db.Column(db.Integer,db.ForeignKey('iotproject_posts.id'))
        
    
  
class Comments_iot(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(100),nullable=False)
    comment=db.Column(db.String(200),nullable=False)
    
    iotpost_nameid=db.Column(db.Integer,db.ForeignKey('iotproject_posts.id'))
    
    replies=db.relationship('Comment_replies',backref='comment_name');
    
    
class Comment_replies_iot(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(200),nullable=False)
    reply=db.Column(db.String(200),nullable=False)
    
    Comment_nameid=db.Column(db.Integer,db.ForeignKey('comments_iot.id'))
# *-----------------------------------------------------------------------------------------------------------
class Other_posts(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False);
    date=db.Column(db.String(50), nullable=False);
    reading_time=db.Column(db.String(50), nullable=False);
    heading=db.Column(db.String(100), nullable=False);
    
    content_parts=db.relationship('Content',backref='post_name');
   
    comment=db.relationship('Comments',backref='post_name');
    
    
class Content_other(db.Model):
   
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
    otherpost_id=db.Column(db.Integer,db.ForeignKey('other_posts.id'))
        
    
   
class Comments_other(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(100),nullable=False)
    comment=db.Column(db.String(200),nullable=False)
    
    other_nameid=db.Column(db.Integer,db.ForeignKey('other_posts.id'))
    
    replies=db.relationship('Comment_replies',backref='comment_name');
    
    
class Comment_replies_other(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(200),nullable=False)
    reply=db.Column(db.String(200),nullable=False)
    
    Comment_nameid=db.Column(db.Integer,db.ForeignKey('comments_other.id'))
    
#!--all_post tables END-----|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


# ! other_details tables start-----------------------------------------------------------------------------------
class Users(db.Model):
    __bind_key__='other_details'
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    user_name=db.Column(db.String(100),primar_key=True,nullable=False)
    email=db.Column(db.String(111),nullable=False,unique=True)
    password=db.Column(db.String(50),nullable=False)
    
class Messages(db.Model):
    __bind_key__='other_details'
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    send_by=db.Column(db.String(100),primar_key=True,nullable=False)
    email=db.Column(db.String(111),nullable=False,unique=True)
    messsage=db.Column(db.String(1000),nullable=False)

#! end---------------------------------------------------------------------------------------------------------
