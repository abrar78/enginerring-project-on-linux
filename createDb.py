from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=params['local_uri_all_post']
app.config['SQLALCHEMY_BINDS']={'other_details':params['local_uri_other']}
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
    description=db.Column(db.String(100), nullable=False);
    # * one to many relationship tables down
    
    quick_answers=db.relationship('Quick_answers_arduino', backref='post_name')
    
    index=db.relationship('Index_arduino',backref='post_name');
    content_parts=db.relationship('Content_arduino',backref='post_name');
    comparison_table=db.relationship('Comparison_table_arduino',backref='post_name');
    conclusion=db.relationship('Conclusion_arduino',backref='post_name');
    faq=db.relationship('Faq_arduino',backref='post_name');
    
    
    comment=db.relationship('Comments_arduino',backref='post_name');  #! currently this comment fuunctuanilitiy is not added
class Index_arduino(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    topic=db.Column(db.String(100),nullable=True)

    arduinopost_id=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))

class Quick_answers_arduino(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    ques=db.Column(db.String(100),nullable=True)
    ans=db.Column(db.String(300),nullable=True)
   
    arduinopost_id=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))

class Comparison_table_arduino(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    heading1=db.Column(db.String(100),nullable=False)        
    heading2=db.Column(db.String(100),nullable=False)
    head1_point=db.Column(db.String(200),nullable=True)
    head2_point=db.Column(db.String(200),nullable=True)
    arduinopost_id=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))
class Conclusion_arduino(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    text=db.Column(db.String(500),nullable=False)
    arduinopost_id=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))   
    
class Faq_arduino(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False);
    faq_q=db.Column(db.String(100),nullable=True)
    faq_ans=db.Column(db.String(100),nullable=True)
   
    arduinopost_id=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))   
    
            
class Content_arduino(db.Model):
   
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    cover_img=db.Column(db.String(100),nullable=True)
    heading=db.Column(db.String(100),nullable=True)
    img=db.Column(db.String(100),nullable=True)
    para=db.Column(db.String(500),nullable=True)
    
    
    arduinopost_id=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))
        
    
        
class Comments_arduino(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(100),nullable=False)
    comment=db.Column(db.String(200),nullable=False)
    replies=db.relationship('Comment_replies_arduino',backref='comment_name');
    
    arduinopost_nameid=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))
    
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
    description=db.Column(db.String(100), nullable=False);
    
    quick_answers=db.relationship('Quick_answers_basic', backref='post_name')
    
    index=db.relationship('Index_basic',backref='post_name');
    comparison_table=db.relationship('Comparison_table_basic',backref='post_name');
    conclusion=db.relationship('Conclusion_basic',backref='post_name');
    faq=db.relationship('Faq_basic',backref='post_name');
    content_parts=db.relationship('Content_basic',backref='post_name');
    
    comment=db.relationship('Comments_basic',backref='post_name');
 
class Quick_answers_basic(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    ques=db.Column(db.String(100),nullable=True)
    ans=db.Column(db.String(300),nullable=True)
   
    basicpost_id=db.Column(db.Integer,db.ForeignKey('basicproject_posts.id'))

class Comparison_table_basic(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    heading1=db.Column(db.String(100),nullable=False)        
    heading2=db.Column(db.String(100),nullable=False)
    head1_point=db.Column(db.String(200),nullable=True)
    head2_point=db.Column(db.String(200),nullable=True)
    basicpost_id=db.Column(db.Integer,db.ForeignKey('basicproject_posts.id'))
    
class Conclusion_basic(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    text=db.Column(db.String(500),nullable=False)
    basicpost_id=db.Column(db.Integer,db.ForeignKey('basicproject_posts.id'))   
    
class Faq_basic(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False);
    faq_q=db.Column(db.String(100),nullable=True)
    faq_ans=db.Column(db.String(100),nullable=True)
    basicpost_id=db.Column(db.Integer,db.ForeignKey('basicproject_posts.id'))   
       
    
class Content_basic(db.Model):
   
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    cover_img=db.Column(db.String(100),nullable=True)
    heading=db.Column(db.String(100),nullable=True)
    img=db.Column(db.String(500),nullable=True)
    para=db.Column(db.String(500),nullable=True)
    basicpost_id=db.Column(db.Integer,db.ForeignKey('basicproject_posts.id'))
        
    
        
class Comments_basic(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(100),nullable=False)
    comment=db.Column(db.String(200),nullable=False)
    basicpost_nameid=db.Column(db.Integer,db.ForeignKey('basicproject_posts.id'))
    replies=db.relationship('Comment_replies_basic',backref='comment_name');
    
    
class Comment_replies_basic(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(200),nullable=False)
    reply=db.Column(db.String(200),nullable=False)
    Comment_nameid=db.Column(db.Integer,db.ForeignKey('comments_basic.id'))
    
class Index_basic(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    topic=db.Column(db.String(100),nullable=True)
    basicpost_id=db.Column(db.Integer,db.ForeignKey('basicproject_posts.id'))

# *-----------------------------------------------------------------------------------------------------------
class Iotproject_posts(db.Model):
    
    id=db.Column(db.Integer ,primary_key=True, nullable=False);
    date=db.Column(db.String(50), nullable=False);
    reading_time=db.Column(db.String(50), nullable=False);
    heading=db.Column(db.String(100), nullable=False);
    description=db.Column(db.String(100), nullable=False);
    
    quick_answers=db.relationship('Quick_answers_iot', backref='post_name')
    
    index=db.relationship('Index_iot',backref='post_name');
    content_parts=db.relationship('Content_iot',backref='post_name');
    comparison_table=db.relationship('Comparison_table_iot',backref='post_name');
    conclusion=db.relationship('Conclusion_iot',backref='post_name');
    faq=db.relationship('Faq_iot',backref='post_name');
    content_parts=db.relationship('Content_iot',backref='post_name');
   
    comment=db.relationship('Comments_iot',backref='post_name');
    
 
class Quick_answers_iot(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    ques=db.Column(db.String(100),nullable=True)
    ans=db.Column(db.String(300),nullable=True)
    
    iotpost_id=db.Column(db.Integer,db.ForeignKey('iotproject_posts.id'))

class Comparison_table_iot(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    heading1=db.Column(db.String(100),nullable=False)        
    heading2=db.Column(db.String(100),nullable=False)
    
    head1_poin1=db.Column(db.String(200),nullable=True)
   
    
    head2_poin1=db.Column(db.String(200),nullable=True)
    
    iotpost_id=db.Column(db.Integer,db.ForeignKey('iotproject_posts.id'))
class Conclusion_iot(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    text=db.Column(db.String(500),nullable=False)
    iotpost_id=db.Column(db.Integer,db.ForeignKey('iotproject_posts.id'))   
    
class Faq_iot(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False);
    faq_q=db.Column(db.String(100),nullable=True)
    faq_ans=db.Column(db.String(100),nullable=True)
    
    iotpost_id=db.Column(db.Integer,db.ForeignKey('iotproject_posts.id'))   
       
    
class Content_iot(db.Model):
   
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    cover_img=db.Column(db.String(100),nullable=True)
    heading=db.Column(db.String(100),nullable=True)
    img=db.Column(db.String(500),nullable=True)
    para=db.Column(db.String(500),nullable=True)
   
    iotpost_id=db.Column(db.Integer,db.ForeignKey('iotproject_posts.id'))
        
    
  
class Comments_iot(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(100),nullable=False)
    comment=db.Column(db.String(200),nullable=False)
    
    iotpost_nameid=db.Column(db.Integer,db.ForeignKey('iotproject_posts.id'))
    
    replies=db.relationship('Comment_replies_iot',backref='comment_name');
    
    
class Comment_replies_iot(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(200),nullable=False)
    reply=db.Column(db.String(200),nullable=False)
    Comment_nameid=db.Column(db.Integer,db.ForeignKey('comments_iot.id'))
                             
class Index_iot(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    topic=db.Column(db.String(100),nullable=True)
   
    iotpost_id=db.Column(db.Integer,db.ForeignKey('iotproject_posts.id'))
    
# *-----------------------------------------------------------------------------------------------------------
class Other_posts(db.Model):
    
    id=db.Column(db.Integer ,primary_key=True, nullable=False);
    date=db.Column(db.String(50), nullable=False);
    reading_time=db.Column(db.String(50), nullable=False);
    heading=db.Column(db.String(100), nullable=False);
    description=db.Column(db.String(100), nullable=False);
    quick_answers=db.relationship('Quick_answers_other', backref='post_name')
    
    index=db.relationship('Index_other',backref='post_name');
    content_parts=db.relationship('Content_other',backref='post_name');
    comparison_table=db.relationship('Comparison_table_other',backref='post_name');
    conclusion=db.relationship('Conclusion_other',backref='post_name');
    faq=db.relationship('Faq_other',backref='post_name');
    content_parts=db.relationship('Content_other',backref='post_name');
   
    comment=db.relationship('Comments_other',backref='post_name');
class Quick_answers_other(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    ques=db.Column(db.String(100),nullable=True)
    ans=db.Column(db.String(300),nullable=True)
   
    otherpost_id=db.Column(db.Integer,db.ForeignKey('other_posts.id'))

class Comparison_table_other(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    heading1=db.Column(db.String(100),nullable=False)        
    heading2=db.Column(db.String(100),nullable=False)
    head1_poin1=db.Column(db.String(200),nullable=True)
    head2_poin1=db.Column(db.String(200),nullable=True)
    otherpost_id=db.Column(db.Integer,db.ForeignKey('other_posts.id'))

class Conclusion_other(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    text=db.Column(db.String(500),nullable=False)
    otherpost_id=db.Column(db.Integer,db.ForeignKey('other_posts.id'))   
    
class Faq_other(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False);
    faq_q=db.Column(db.String(100),nullable=True)
    faq_ans=db.Column(db.String(100),nullable=True)
    
    otherpost_id=db.Column(db.Integer,db.ForeignKey('other_posts.id'))   
           
    
class Content_other(db.Model):
   
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    cover_img=db.Column(db.String(100),nullable=True)
    heading=db.Column(db.String(100),nullable=True)
    img=db.Column(db.String(500),nullable=True)
    para=db.Column(db.String(500),nullable=True)
   
   
    otherpost_id=db.Column(db.Integer,db.ForeignKey('other_posts.id'))
        
    
   
class Comments_other(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(100),nullable=False)
    comment=db.Column(db.String(200),nullable=False)
    
    other_nameid=db.Column(db.Integer,db.ForeignKey('other_posts.id'))
    
    replies=db.relationship('Comment_replies_other',backref='comment_name');
    
    
class Comment_replies_other(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    user_name=db.Column(db.String(200),nullable=False)
    reply=db.Column(db.String(200),nullable=False)
    
    Comment_nameid=db.Column(db.Integer,db.ForeignKey('comments_other.id'))
class Index_other(db.Model):
    id=db.Column(db.Integer ,primary_key=True, nullable=False)
    topic=db.Column(db.String(100),nullable=True)
   
    otherpost_id=db.Column(db.Integer,db.ForeignKey('other_posts.id'))
        
           
#!--all_post tables END-----|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


# ! other_details tables start-----------------------------------------------------------------------------------
class Subscribers(db.Model):
    __bind_key__='other_details'
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    user_name=db.Column(db.String(100),primar_key=True,nullable=False)
    email=db.Column(db.String(111),nullable=False,unique=True)
    
    
class Messages(db.Model):
    __bind_key__='other_details'
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    send_by=db.Column(db.String(100),primar_key=True,nullable=False)
    email=db.Column(db.String(111),nullable=False,unique=True)
    messsage=db.Column(db.String(1000),nullable=False)

class About_me(db.Model):
    __bind_key__='other_details'
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    profile=db.Column(db.Integer,nullable=True)

#! end---------------------------------------------------------------------------------------------------------
