from flask import Flask, render_template,request,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security,SQLAlchemyUserDatastore,UserMixin, RoleMixin, login_required
from flask_security.utils import hash_password
import json


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__,instance_path='/home/g9529693800aa/enginerring-project-on-linux/special_files')
app.config['SQLALCHEMY_DATABASE_URI']=params['local_uri_all_post']
app.config["SECRET_KEY"]="###@@@***786786"
app.config["SECURITY_PASSWORD_SALT"]="###@@@***abrar"
# app.config['SECURITY_LOGIN_USER_TEMPLATE'] = '/security/login_user.html'
app.app_context().push()
db=SQLAlchemy(app)


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

# !----------------------Admin pannel setup-------------------------------------------------
roles_users=db.Table('roles_users',
                     db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
                     db.Column('role_id',db.Integer,db.ForeignKey('role.id'))
                     )
class User(UserMixin,db.Model):
    
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(255))
    active=db.Column(db.Boolean)
    confirmed_at=db.Column(db.DateTime)
    roles=db.relationship('Role',
                          secondary=roles_users,
                          backref=db.backref('users',lazy='dynamic')
                          )
    
class Role(db.Model,RoleMixin):
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    description=db.Column(db.String(200))
    
user_datastore=SQLAlchemyUserDatastore(db,User,Role)
security=Security(app,user_datastore)

# !--------------------------------------------------------------------------------------------------------------------------

class Arduinoproject_posts(db.Model):
    
    id=db.Column(db.Integer ,primary_key=True, nullable=False);
    date=db.Column(db.String(50), nullable=False);
    thumbnail=db.Column(db.String(100), nullable=False);
    cover_img=db.Column(db.String(100), nullable=False);
    url=db.Column(db.String(100), nullable=False);
    meta_keywords=db.Column(db.String(100), nullable=False);
    meta_title=db.Column(db.String(100), nullable=False);
    img_description=db.Column(db.String(100), nullable=False);
    keyword=db.Column(db.String(100), nullable=False);
    type=db.Column(db.String(100), nullable=True);
    heading=db.Column(db.String(100), nullable=False);
    description=db.Column(db.String(100), nullable=False);

   
        # * one to many relationship tables down
    
    paragraphs=db.relationship('Para_arduino',backref="post_name",uselist=False)
    quick_answers=db.relationship('Quick_answers_arduino', backref='post_name')
    index=db.relationship('Index_arduino',backref='post_name');

    faq=db.relationship('Faq_arduino',backref='post_name');
    comment=db.relationship('Comments_arduino',backref='post_name');  #! currently this comment fuunctuanilitiy is not added
    
class Para_arduino(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    content=db.Column(db.Text)
   
    arduino_id=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))
class Index_arduino(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    topic=db.Column(db.String(100),nullable=True)

    arduinopost_id=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))




class Quick_answers_arduino(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    ques=db.Column(db.String(100),nullable=True)
    ans=db.Column(db.Text,nullable=True)
   
    arduinopost_id=db.Column(db.Integer,db.ForeignKey('arduinoproject_posts.id'))


class Faq_arduino(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False);
    faq_q=db.Column(db.String(100),nullable=True)
    faq_ans=db.Column(db.Text,nullable=True)
   
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
    thumbnail=db.Column(db.String(100), nullable=False);
    cover_img=db.Column(db.String(100), nullable=False);
    url=db.Column(db.String(100), nullable=False);
    meta_keywords=db.Column(db.String(100), nullable=False);
    meta_title=db.Column(db.String(100), nullable=False);
    img_description=db.Column(db.String(100), nullable=False);
    keyword=db.Column(db.String(100), nullable=False);
    type=db.Column(db.String(100), nullable=True);
    heading=db.Column(db.String(100), nullable=False);
    description=db.Column(db.String(100), nullable=False);
   

    paragraphs=db.relationship('Para_basic',backref="post_name",uselist=False)

    quick_answers=db.relationship('Quick_answers_basic', backref='post_name')
    index=db.relationship('Index_basic',backref='post_name');
    faq=db.relationship('Faq_basic',backref='post_name');
    comment=db.relationship('Comments_basic',backref='post_name');
    
class Para_basic(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    content=db.Column(db.Text)
   
    basic_id=db.Column(db.Integer,db.ForeignKey('basicproject_posts.id'))
 
class Quick_answers_basic(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    ques=db.Column(db.String(100),nullable=True)
    ans=db.Column(db.Text,nullable=True)
   
    basicpost_id=db.Column(db.Integer,db.ForeignKey('basicproject_posts.id'))

class Faq_basic(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False);
    faq_q=db.Column(db.String(100),nullable=True)
    faq_ans=db.Column(db.Text,nullable=True)
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
    thumbnail=db.Column(db.String(100), nullable=False);
    cover_img=db.Column(db.String(100), nullable=False);
    url=db.Column(db.String(100), nullable=False);
    meta_keywords=db.Column(db.String(100), nullable=False);
    meta_title=db.Column(db.String(100), nullable=False);
    img_description=db.Column(db.String(100), nullable=False);
    keyword=db.Column(db.String(100), nullable=False);
    type=db.Column(db.String(100), nullable=True);
    heading=db.Column(db.String(100), nullable=False);
    description=db.Column(db.String(100), nullable=False);
    
    paragraphs=db.relationship('Para_iot',backref="post_name",uselist=False)
    quick_answers=db.relationship('Quick_answers_iot', backref='post_name')
    index=db.relationship('Index_iot',backref='post_name');
    faq=db.relationship('Faq_iot',backref='post_name');

    comment=db.relationship('Comments_iot',backref='post_name');
    
    
class Para_iot(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    content=db.Column(db.Text)
   
    iot_id=db.Column(db.Integer,db.ForeignKey('iotproject_posts.id')) 
class Quick_answers_iot(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    ques=db.Column(db.String(100),nullable=True)
    ans=db.Column(db.Text,nullable=True)
    
    iotpost_id=db.Column(db.Integer,db.ForeignKey('iotproject_posts.id'))


class Faq_iot(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False);
    faq_q=db.Column(db.String(100),nullable=True)
    faq_ans=db.Column(db.Text,nullable=True)
    
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
    thumbnail=db.Column(db.String(100), nullable=False);
    cover_img=db.Column(db.String(100), nullable=False);
    url=db.Column(db.String(100), nullable=False);
    meta_keywords=db.Column(db.String(100), nullable=False);
    meta_title=db.Column(db.String(100), nullable=False);
    img_description=db.Column(db.String(100), nullable=False);
    keyword=db.Column(db.String(100), nullable=False);
    type=db.Column(db.String(100), nullable=True);
    heading=db.Column(db.String(100), nullable=False);
    description=db.Column(db.String(100), nullable=False);
   

    paragraphs=db.relationship('Para_other',backref="post_name",uselist=False)
    quick_answers=db.relationship('Quick_answers_other', backref='post_name')
    index=db.relationship('Index_other',backref='post_name');
    faq=db.relationship('Faq_other',backref='post_name');
    comment=db.relationship('Comments_other',backref='post_name');
    
class Para_other(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    content=db.Column(db.Text)
   
    other_id=db.Column(db.Integer,db.ForeignKey('other_posts.id'))
class Quick_answers_other(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    ques=db.Column(db.String(100),nullable=True)
    ans=db.Column(db.Text,nullable=True)
   
    otherpost_id=db.Column(db.Integer,db.ForeignKey('other_posts.id'))



class Faq_other(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False);
    faq_q=db.Column(db.String(100),nullable=True)
    faq_ans=db.Column(db.Text,nullable=True)
    
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
   
#!----------------Draft database---------------------------------------------!    #  
class Draft(db.Model):
   
    id=db.Column(db.Integer ,primary_key=True, nullable=False);
    date=db.Column(db.String(50), nullable=False);
    thumbnail=db.Column(db.String(100), nullable=False);
    cover_img=db.Column(db.String(100), nullable=False);
    url=db.Column(db.String(100), nullable=False);
    meta_keywords=db.Column(db.String(100), nullable=False);
    meta_title=db.Column(db.String(100), nullable=False);
    img_description=db.Column(db.String(100), nullable=False);
    keyword=db.Column(db.String(100), nullable=False);
    type=db.Column(db.String(100), nullable=True);
    heading=db.Column(db.String(100), nullable=False);
    description=db.Column(db.String(100), nullable=False);
   
    
    paragraphs=db.relationship('Para_draft',backref="post_name",uselist=False)
    quick_answers=db.relationship('Quick_answers_draft', backref='post_name')
    index=db.relationship('Index_draft',backref='post_name');
    faq=db.relationship('Faq_draft',backref='post_name');

    

    
class Para_draft(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    content=db.Column(db.Text)
   
    draft_id=db.Column(db.Integer,db.ForeignKey('draft.id'))
    
class Quick_answers_draft(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    ques=db.Column(db.String(100),nullable=True)
    ans=db.Column(db.Text,nullable=True)
   
    draft_id=db.Column(db.Integer,db.ForeignKey('draft.id'))


class Faq_draft(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False);
    faq_q=db.Column(db.String(100),nullable=True)
    faq_ans=db.Column(db.Text,nullable=True)
    draft_id=db.Column(db.Integer,db.ForeignKey('draft.id'))   

class Index_draft(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    topic=db.Column(db.String(100),nullable=True)
    draft_id=db.Column(db.Integer,db.ForeignKey('draft.id'))

# !-------------------------------------------------------------------------------------------------------------------------

    
#!--all_post tables END-----|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


# ! other_details tables start-----------------------------------------------------------------------------------
class Subscribers(db.Model):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    email=db.Column(db.String(111),nullable=False,unique=True)
    
    
class Messages(db.Model):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    email=db.Column(db.String(111),nullable=False,unique=False)
    messsage=db.Column(db.Text,nullable=False)

class About_me(db.Model):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    profile=db.Column(db.Text,nullable=True)

#! end---------------------------------------------------------------------------------------------------------

def putPassword(password,email):
            user_datastore.create_user(
                email=email,
                password=password
            )
            db.session.commit()
            

 
