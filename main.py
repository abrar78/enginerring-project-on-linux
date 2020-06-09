from createDb import *
from sqlalchemy import or_,desc
import math
from flask import jsonify,make_response,request,redirect,session,Response
import os
import datetime
from werkzeug.utils import secure_filename
from flask_mail import Mail
from flask_login import LoginManager
from jinja2 import Undefined
from time import gmtime, strftime
import jinja2

JINJA2_ENVIRONMENT_OPTIONS = { 'undefined' : Undefined }
app.config['UPLOAD_FOLDER']={'upload':params["upload_location"],
                             'cover_image':params["upload_location_coverImg"] }
global url
global title
global cover_image
global cover_image_description
global meta_keywords
global para_ImgDescription
global code_language
global code
global code_heading
code_heading=[]
cover_image=""
url=""
code=[]
code_language=[]
title=""
cover_image_description=""
meta_keywords=""
para_ImgDescription=[]

global type_
type_=''
global heading1
heading1=""
global heading2
heading2=""
global table_col1
table_col1=None
global table_col2
table_col2=None
global thumbnail
thumbnail=""
global para_thumbnail
para_thumbnail=[]
global keyword
keyword=""
global heading
heading=""
global description
description=""
global quick_questions
quick_questions=[]
global quick_asnwers
quick_answers=[]
global index
index=[]
global para
para=[]
global para_subheading
para_subheading=[]

global conclusion
conclusion=""
global faq_q
faq_q=[]
global faq_ans
faq_ans=[]

app.app_context().push()
app.config.update(

    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params["gmail-user"],
    MAIL_PASSWORD =  params["gmail-password"]

    )
results=[]
mail=Mail(app);
@app.route('/')
def index_file():

     arduino=Arduinoproject_posts.query.paginate(per_page=4,page=1,error_out=True)
     basic=Basicproject_posts.query.paginate(per_page=4,page=1,error_out=True)
     iot=Iotproject_posts.query.paginate(per_page=4,page=1,error_out=True)
     other=Other_posts.query.paginate(per_page=4,page=1,error_out=True)
     arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.date)).first()
     basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).first()
     iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).first()
     other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id)).first()
     latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]
   
         
     return render_template('index.html',
                            arduino_project=arduino,
                            basic_project=basic,
                            iot_project=iot,
                            other_project=other,
                            latest_posts=latest_posts)

@app.route('/paginate', methods = ['GET', 'POST'])
def paginate():
    req=request.get_json();
    print(req)

    if req['code']=='Ard':

        if req['jump_page']==True:
         content={'heading':{}, 'thumbnail':{},'description':{},'id':{}}
         current_page=int(req['page_no'])
         arduino=Arduinoproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
         for arduino_db,i in zip(arduino.items,range(1,5)):
             content['heading'][str(i)]=arduino_db.heading
             content['thumbnail'][str(i)]=arduino_db.thumbnail
             content['description'][str(i)]=arduino_db.description
             content['id'][str(i)]=arduino_db.id
         print(req['page_no'])
         response=make_response(jsonify(content),200)
         return response

        if req['next']==True or req['prev']==True:
          content={'heading':{}, 'thumbnail':{},'description':{},'id':{}}
          print(req)
          arduino=Arduinoproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
          for arduino_db,i in zip(arduino.items,range(1,5)):
             content['heading'][str(i)]=arduino_db.heading
             content['thumbnail'][str(i)]=arduino_db.thumbnail
             content['description'][str(i)]=arduino_db.description
             content['id'][str(i)]=arduino_db.id


    if req['code']=='Basic':

        if req['jump_page']==True:
         content={'heading':{}, 'thumbnail':{},'description':{},'id':{}}
         current_page=int(req['page_no'])
         basic=Basicproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
         for basic_db,i in zip(basic.items,range(1,5)):
             content['heading'][str(i)]=basic_db.heading
             content['thumbnail'][str(i)]=basic_db.thumbnail
             content['description'][str(i)]=basic_db.description
             content['id'][str(i)]=basic_db.id
         print(req['page_no'])
         response=make_response(jsonify(content),200)
         return response

        if req['next']==True or req['prev']==True:
          content={'heading':{}, 'thumbnail':{},'description':{},'id':{}}
          basic=Basicproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
          for basic_db,i in zip(basic.items,range(1,5)):
             content['heading'][str(i)]=basic_db.heading
             content['thumbnail'][str(i)]=basic_db.thumbnail
             content['description'][str(i)]=basic_db.description
             content['id'][str(i)]=basic_db.id

    if req['code']=='Iot':
         if req['jump_page']==True:
             content={'heading':{}, 'thumbnail':{},'description':{},'id':{}}
             current_page=int(req['page_no'])
             iot=Iotproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
             for iot_db,i in zip(iot.items,range(1,5)):
                content['heading'][str(i)]=iot_db.heading
                content['thumbnail'][str(i)]=iot_db.thumbnail
                content['description'][str(i)]=iot_db.description
                content['id'][str(i)]=iot_db.id
             print(req['page_no'])
             response=make_response(jsonify(content),200)
             return response

         if req['next']==True or req['prev']==True:
            content={'heading':{}, 'thumbnail':{},'description':{},'id':{}}
            iot=Iotproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
            for iot_db,i in zip(iot.items,range(1,5)):
                content['heading'][str(i)]=iot_db.heading
                content['thumbnail'][str(i)]=iot_db.thumbnail
                content['description'][str(i)]=iot_db.description
                content['id'][str(i)]=iot_db.id


    if req['code']=='Other':
         if req['jump_page']==True:
             content={'heading':{}, 'thumbnail':{},'description':{},'id':{}}
             current_page=int(req['page_no'])
             other=Other_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
             for other_db,i in zip(other.items,range(1,5)):
                content['heading'][str(i)]=other_db.heading
                content['thumbnail'][str(i)]=other_db.thumbnail
                content['description'][str(i)]=other_db.description
                content['id'][str(i)]=other_db.id
             print(req['page_no'])
             response=make_response(jsonify(content),200)
             return response

         if req['next']==True or req['prev']==True:
            content={'heading':{}, 'thumbnail':{},'description':{},'id':{}}
            other=Other_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
            for other_db,i in zip(other.items,range(1,5)):
                content['heading'][str(i)]=other_db.heading
                content['thumbnail'][str(i)]=other_db.thumbnail
                content['description'][str(i)]=other_db.description
                content['id'][str(i)]=other_db.id

    response=make_response(jsonify(content),200)
    return response
    # return response


@app.route('/arduino-projects/<string:url>')
def arduinoRead(url):
    arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.date)).all()
    basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).first()
    iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).first()
    other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id)).first()
    
    arduino_post=Arduinoproject_posts.query.filter_by(url='/arduino-projects/'+url).first()
    print("------------------------------",type(arduino_latest))
    if arduino_post in arduino_latest:
        arduino_latest.remove(arduino_post)
    try:    
        arduino_latest=arduino_latest[0]
    except IndexError:
        arduino_latest=None; 
    
    latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]    
          
    print("0000000000000000000000000",arduino_post)
  
    search_value=arduino_post.keyword
    search="%{0}%".format(search_value)
    print(search)
    related=Arduinoproject_posts.query.filter(or_(Arduinoproject_posts.description.like(search), Arduinoproject_posts.heading.like(search))).all()
    
    print(type(related))
    if arduino_post in related:
        related.remove(arduino_post)

    return render_template('readMoreOther.html', post_db=arduino_post,related_post=related[0:4],latest_posts=latest_posts,url_type="Arduino")
@app.route('/basic-projects/<string:url>')
def basicRead(url):
    arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.date)).first()
    basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).all()
    iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).first()
    other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id)).first()
    basic_post=Basicproject_posts.query.filter_by(url="/basic-projects/"+url).first()
    search_value=basic_post.keyword
    search="%{0}%".format(search_value)
    related=Basicproject_posts.query.filter(or_(Basicproject_posts.description.like(search), Basicproject_posts.heading.like(search))).all()
    if basic_post in basic_latest:
        basic_latest.remove(basic_post)
    try:    
        basic_latest=basic_latest[0]
    except IndexError:
        basic_latest=None; 
    latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]    
    if basic_post in related:
        related.remove(basic_post)
    return render_template('readMoreOther.html', post_db=basic_post,related_post=related[0:4],latest_posts=latest_posts)
@app.route('/iot-projects/<string:url>')
def iotRead(url):
    arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.date)).first()
    basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).first()
    iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).all()
    other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id)).first()
    iot_post=Iotproject_posts.query.filter_by(url="/iot-projects/"+url).first()
    search_value=iot_post.keyword
    search="%{0}%".format(search_value)
    related=Iotproject_posts.query.filter(or_(Iotproject_posts.description.like(search), Iotproject_posts.heading.like(search))).all()
    if iot_post in iot_latest:
        iot_latest.remove(iot_post)
    try:    
        iot_latest=iot_latest[0]
    except IndexError:
        basic_latest=None; 
    latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]    
    if iot_post in related:
        related.remove(iot_post)

    return render_template('readMoreOther.html', post_db=iot_post,related_post=related[0:4],latest_posts=latest_posts)
@app.route('/tech-posts/<string:url>')
def otherRead(url):
    arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.date)).first()
    basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).first()
    iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).first()
    other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id))
    latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]    
    other_post=Other_posts.query.filter_by(url="/tech-post/"+url).first()
    search_value=other_post.keyword
    search="%{0}%".format(search_value)
    related=Other_posts.query.filter(or_(Other_posts.description.like(search), Other_posts.heading.like(search))).all()
    if other_post in other_latest:
        other_latest.remove(other_post)
    try:    
        other_latest=other_latest[0]
    except IndexError:
        other_latest=None; 
    latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]    
    if other_post in related:
        related.remove(other_post)
    return render_template('readMoreOther.html', post_db=other_post,related_post=related[0:4],latest_posts=latest_posts)
@app.route('/Read_more_draft/<int:num>')
@login_required
def draftRead(num):

    latest_posts=[]    
    draft_post=Draft.query.filter_by(id=num).first()
    draft_type=draft_post.type
    draft_type=draft_type[0:-4]
    search_value=draft_post.keyword
    search="%{0}%".format(search_value)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    if arduino_latest or basic_latest or iot_latest or other_latest:
      print("Yes latest posts")
      
    print(draft_type)
    if draft_type=="Ard":
            print("im Ard")
            related=Arduinoproject_posts.query.filter(or_(Other_posts.description.like(search), Other_posts.heading.like(search))).all()
            arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.date)).all()
            basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).first()
            iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).first()
            other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id)).first()
            if draft_post in arduino_latest:
                arduino_latest.remove(draft_post)
            try:    
                arduino_latest=arduino_latest[0]
            except IndexError:
                arduino_latest=None; 
            latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]    


    if draft_type=="Iot":
            related=Iotproject_posts.query.filter(or_(Other_posts.description.like(search), Other_posts.heading.like(search))).all()
            arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.date)).all()
            basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).first()
            iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).all()
            other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id)).first()
            if draft_post in iot_latest:
                iot_latest.remove(draft_post)
            try:    
                iot_latest=iot_latest[0]
            except IndexError:
                iot_latest=None; 
            latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]   

    if draft_type=="Basic":
            related=Basicproject_posts.query.filter(or_(Other_posts.description.like(search), Other_posts.heading.like(search))).all()
            arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.date)).all()
            basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).all()
            iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).all()
            other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id)).first()
            if draft_post in basic_latest:
                basic_latest.remove(draft_post)
            try:    
                basic_latest=basic_latest[0]
            except IndexError:
                basic_latest=None; 
            latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]   

    if draft_type=="Other":
            related=Other_posts.query.filter(or_(Other_posts.description.like(search), Other_posts.heading.like(search))).all()
            arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.date)).all()
            basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).first()
            iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).all()
            other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id)).all()
            if draft_post in other_latest:
                other_latest.remove(draft_post)
            try:    
                other_latest=other_latest[0]
            except IndexError:
                other_latest=None; 
            latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]   

    return render_template('readMoreOther.html',post_db=draft_post,related_post=related[0:4],latest_posts=latest_posts,test="red")

@app.route('/templates/advertiseWithUs.html')
def advertise():
    return render_template('advertiseWithUs.html')


@app.route('/form',methods = ['GET', 'POST'])
def form_submit():
    req=request.get_json();
    print(req)
    message=""
    if req['with_only_text']==True:
           message="only text advertisement is requested by "+req['first_name']+"About the advertisement is:\r\n"+req['something_about_add']
           mail.send_message(
                            'new message from blog for advertisement'+'  name:'+req['first_name']+req['last_name'],
                            sender=req['email'],
                            recipients = [params['recipient']],
                            body=message
                            )
    if req['image']==True:
                if req['have_image']==True:
                   message="advertisement with image is requested by "+req['first_name']+'client already has an image and uploaded on server'+"\r\nAbout the advertisement is:\r\n"+req['somethingh_about_add']
                if req['dont_have']==True:
                    if req['make_image']==True:
                         message="advertisement with image is requested by "+req['first_name']+'client dont have an image and he dont want to make one for him by us'+"\r\nAbout the advertisement is:\r\n"+req['somethingh_about_add']
                    else:
                         message="advertisement with image is requested by "+req['first_name']+'client dont have an image and he  want to make one for him by us'+"\r\nAbout the advertisement is:\r\n"+req['somethingh_about_add']

    if req['other']==True:
                message="other type of advertisemet is requested by "+req['first_name']+'\r\nSpecification of type is \r\n'+req['specification_forOther']+"\r\nAbout the advertisement is:\r\n"+req['somethingh_about_add']


    mail.send_message(
                            'new message from blog for advertisement'+'  name:'+req['first_name']+req['last_name'],
                            sender=req['email'],
                            recipients = [params['recipient']],
                            body=message
                            )
    content={"response":"Thankyou"}
    response=make_response(jsonify(content))
    return response

@app.route('/message',methods = ['GET', 'POST'])
def message():
    req=request.get_json();
    print(req)
    mail.send_message('new message from blog'+'  name:'+req['sender_name'],
                      sender=req['e_mail'],
                      recipients = [params['recipient']],
                      body=req['message'])
    message=Messages(send_by=req['sender_name'],email=req['e_mail'],messsage=req['message'])
    db.session.add(message)
    db.session.commit()
    content={"response":"Thankyou"}
    response=make_response(jsonify(content))
    return response
@app.route('/subscribe',methods = ['GET', 'POST'])
def subscriber():
    req=request.get_json();
    subscriber=Subscribers(user_name=req['name'],email=req['e_mail']);
    message="Hello Abrar New subscribers on your blog please add it to your list \r\n"+"name and email is "+req['name']+" "+req['e_mail']
    mail.send_message('new message from blog for new subscribing request',
                      sender=req['e_mail'],
                      recipients = [params['recipient']],
                      body=message)
    db.session.add(subscriber)
    db.session.commit()
    content={"response":"Thankou For subscribing"}
    response=make_response(jsonify(content))
    return response

@app.route('/search/<int:page>',methods=['GET','POST'])
def search(page):
    per_page=10
    next=2;
    prev=0;
    current=page;
    if request.method=="POST":

        form=request.form
        search_value=form['search_string']
        search="%{0}%".format(search_value)
        print(search)
        result1=Arduinoproject_posts.query.filter(or_(Arduinoproject_posts.description.like(search), Arduinoproject_posts.heading.like(search))).all()
        result2=Iotproject_posts.query.filter(or_(Iotproject_posts.description.like(search), Iotproject_posts.heading.like(search))).all()
        result3=Basicproject_posts.query.filter(or_(Basicproject_posts.description.like(search), Basicproject_posts.heading.like(search))).all()
        result4=Other_posts.query.filter(or_(Other_posts.description.like(search), Other_posts.heading.like(search))).all()
        global results
        results=result1+result2+result3+result4
    pages=math.ceil(len(results)/per_page)

    if current==1:
        prev=0
        next=current+1

    if current>1:
        prev=current-1;
        next=current+1;

    if current==pages:
        next=0;
        prev=current-1;

    result=results[per_page*page-per_page : per_page*page]
    print(type(results))
    data={"next":next,"prev":prev,"current":current}
    return render_template('search.html',result=result,totalPages=pages,next=next,prev=prev,data=json.dumps(data))

@app.route('/upload',methods=['GET','POST'])
def upload():
       f=request.files['file'];
       f.save(os.path.join(app.config['UPLOAD_FOLDER']['upload'],secure_filename(f.filename)))
       return "SUCCESS"
   
@app.route('/dashboard_upload/<string:type>',methods=['GET','POST'])
@login_required
def dashboard_upload(type):
    if type=='thumbnail':
       f=request.files['file'];
       file_name=f.filename
       file_name=file_name.replace(" ","_")
       global thumbnail
       
       thumbnail=file_name
       print(thumbnail)
       f.save(os.path.join(app.config['UPLOAD_FOLDER']['cover_image'],secure_filename(f.filename)))
    if type=='cover':
       f=request.files['file'];
       file_name=f.filename
       file_name=file_name.replace(" ","_")
       global cover_image
       
       cover_image=file_name
       print(cover_image)
       f.save(os.path.join(app.config['UPLOAD_FOLDER']['cover_image'],secure_filename(f.filename)))
    if type=='para':
       f=request.files['file'];
       file_name=f.filename
    #    file_name=file_name.replace(" ","_")
    #    global para_thumbnail
    #    para_thumbnail.append(file_name)
    #    print(para_thumbnail)
       f.save(os.path.join(app.config['UPLOAD_FOLDER']['cover_image'],secure_filename(f.filename)))
    return "SUCCESS"

@app.route('/dashboard_create_post/<string:type>',methods=['GET','POST'])
@login_required
def dashboard_create_post(type):
    global type_
    # type='description
    # '
    if type=="url":
      req=request.get_json()
      global url
      url=req['url']
      print(url)
      
    if type=="coverImgDescription":
      req=request.get_json()
      global cover_image_description
      cover_image_description=req['coverImgDescription']
      print(cover_image_description)
        
    if type=="code":
      req=request.get_json()
      global code
      global code_language
      global code_heading
      code=req['source_code']
      code_language=req['language']
      code_heading=req['code_heading']
      print(code)
      print(code_language)
      print(code_heading)
    if type=="keywordsMeta":
      req=request.get_json()
      global meta_keywords
      meta_keywords=req['meta_keywords']
    if type=="title":
      req=request.get_json()
      global title
      title=req['title']
  
    if type=="keyword":
      req=request.get_json()
      print("------------------------------------------------------------------")
      print(req) 
      global keyword
      keyword=req['keyword']
      
    if type=="heading":
      req=request.get_json()
      global heading
      global type_
      heading=req['heading']
      type_=req['type_']

    if type=="type":
      req=request.get_json()
      type_=req['type_']
    
    if type=="description":
      req=request.get_json()
      global description
      description=req['description']
   
    if type=="quickAnswers":
      req=request.get_json()
      global quick_answers
      global quick_questions
      quick_answers=req['quick_answers']
      quick_questions=req['quick_questions']
    
    if type=="index":
      req=request.get_json()
      global index
      index=req['index']
    if type=="para":
      req=request.get_json()
      global para
      global para_subheading
      global para_thumbnail
      global para_ImgDescription
      para=req['para']
      para_ImgDescription=req['thumbnail_desc']
      para_subheading=req['subheading']
      para_thumbnail=req['thumbnail']
      print(para_ImgDescription)
    if type=="conclusion":
      req=request.get_json()
      global conclusion
      conclusion=req['conclusion']
      
    if type=="faq":
      req=request.get_json()
      global faq_q
      global faq_ans
      faq_q=req['faq_q']
      faq_ans=req['faq_ans']
    if type=="table":
      req=request.get_json()
      global heading1
      global heading2
      global table_col1
      global table_col2
      table_col1=req['col1']
      table_col2=req['col2']
      heading1=req['heading1']
      heading2=req['heading2']
      
    
    return "SUCCESS"
@app.route('/all_post/<int:page_no>')
@login_required
def all_post(page_no):
    per_page=12
    next=2;
    prev=0;
    current=page_no;
    arduino=Arduinoproject_posts.query.paginate(per_page=12,page=int(page_no),error_out=True)
    return render_template('all_post.html',arduino_project=arduino,data=json.dumps({'current':current}))

@app.route('/dashboard_basic/<int:page_no>')
@login_required
def dashboard_basic(page_no):
    per_page=12
    next=2;
    prev=0;
    current=page_no;
    basic=Basicproject_posts.query.paginate(per_page=12,page=int(page_no),error_out=True)
    return render_template('dashboard_basic_edit.html',basic_project=basic,data=json.dumps({'current':current}))

@app.route('/dashboard_iot/<int:page_no>')
@login_required
def dashboard_iot(page_no):
    per_page=12
    next=2;
    prev=0;
    current=page_no;
    iot=Iotproject_posts.query.paginate(per_page=12,page=int(page_no),error_out=True)
    return render_template('dashboard_iot_edit.html',iot_project=iot,data=json.dumps({'current':current}))

@app.route('/dashboard_other/<int:page_no>')
@login_required
def dashboard_other(page_no):
    per_page=12
    next=2;
    prev=0;
    current=page_no;
    other=Other_posts.query.paginate(per_page=12,page=int(page_no),error_out=True)
    return render_template('dashboard_other_edit.html',other_project=other,data=json.dumps({'current':current}))

@app.route('/Delete/<string:type>/<int:id>' , methods=['GET','POST'])
@login_required
def delete(id,type):
    print(id,type)
    if type=='Ard':
        delete=Arduinoproject_posts.query.filter_by(id=id).first()
        deleteContent=Content_arduino.query.filter_by(arduinopost_id=id).all()
        deleteIndex=Index_arduino.query.filter_by(arduinopost_id=id).all()
        deleteTable=Comparison_table_arduino.query.filter_by(arduinopost_id=id).all()
        deleteFaq=Faq_arduino.query.filter_by(arduinopost_id=id).all()
        deleteQuickanswers=Quick_answers_arduino.query.filter_by(arduinopost_id=id).all()
        deleteCode=Code_arduino.query.filter_by(arduinopost_id=id).all()
        returnPath="/all_post/1"
    if type=='Basic':
        delete=Basicproject_posts.query.filter_by(id=id).first()
        deleteContent=Content_basic.query.filter_by(basicpost_id=id).all()
        deleteIndex=Index_basic.query.filter_by(basicpost_id=id).all()
        deleteTable=Comparison_table_basic.query.filter_by(basicpost_id=id).all()
        deleteFaq=Faq_basic.query.filter_by(basicpost_id=id).all()
        deleteQuickanswers=Quick_answers_basic.query.filter_by(basicpost_id=id).all()
        deleteCode=Code_basic.query.filter_by(basicpost_id=id).all()
        returnPath="/dashboard_basic/1"
        
    if type=='Iot':
        delete=Iotproject_posts.query.filter_by(id=id).first()
        deleteContent=Content_iot.query.filter_by(iotpost_id=id).all()
        deleteIndex=Index_iot.query.filter_by(iotpost_id=id).all()
        deleteTable=Comparison_table_iot.query.filter_by(iotpost_id=id).all()
        deleteFaq=Faq_iot.query.filter_by(iotpost_id=id).all()
        deleteQuickanswers=Quick_answers_iot.query.filter_by(iotpost_id=id).all()
        deleteCode=Code_iot.query.filter_by(iotpost_id=id).all()
        returnPath="/dashboard_iot/1"
    if type=='Other':
        delete=Other_posts.query.filter_by(id=id).first()
        deleteContent=Content_other.query.filter_by(otherpost_id=id).all()
        deleteIndex=Index_other.query.filter_by(otherpost_id=id).all()
        deleteTable=Comparison_table_other.query.filter_by(otherpost_id=id).all()
        deleteFaq=Faq_other.query.filter_by(otherpost_id=id).all()
        deleteQuickanswers=Quick_answers_other.query.filter_by(otherpost_id=id).all()
        deleteCode=Code_other.query.filter_by(otherpost_id=id).all()
        returnPath="/dashboard_other/1"
    
    if type=='draft':
        delete=Draft.query.filter_by(id=id).first()
        deleteContent=Content_draft.query.filter_by(draft_id=id).all()
        deleteIndex=Index_draft.query.filter_by(draft_id=id).all()
        deleteTable=Comparison_table_draft.query.filter_by(draft_id=id).all()
        deleteFaq=Faq_draft.query.filter_by(draft_id=id).all()
        deleteQuickanswers=Quick_answers_draft.query.filter_by(draft_id=id).all()
        deleteCode=Code_draft.query.filter_by(draft_id=id).all()
        returnPath="/dashboard/draft"
    if deleteContent:
            for d in deleteContent:
                db.session.delete(d)
                db.session.commit()
    if deleteIndex:
            for d in deleteTable:
             db.session.delete(d)
             db.session.commit()
            
    if deleteTable:
         for d in deleteTable:
            db.session.delete(d)
            db.session.commit()
            
    if deleteFaq:
            for d in deleteFaq:
                db.session.delete(d)
                db.session.commit()
       
    if deleteQuickanswers:
            for d in deleteQuickanswers:
                db.session.delete(d)
                db.session.commit()
    if deleteCode:
            for d in deleteCode:
                db.session.delete(d)
                db.session.commit()
        
    db.session.delete(delete)
    db.session.commit()
    return redirect(returnPath) 
    
@app.route('/create_post')
@login_required
def create_post():
    return render_template('create_post.html')
@app.route('/logout')
def logout():
    logout_user()
    return "LOGOUT SUCCESFULL"

@app.route('/dashboard@@@',methods = ['GET', 'POST'])
@login_required
def dashboard():
 savedPost=Draft.query.filter().count()
 subscribers=Subscribers.query.filter().all()
 subscribersNo=Subscribers.query.filter().count()

  
 return render_template("dashboard.html",postNo=savedPost,subscribersNo=subscribersNo) 
@app.route('/dashboard/emails/<int:page_no>',methods=['GET','POST'])
def emails(page_no):
    subscribersNo=Subscribers.query.filter().count()
    subscribers=Subscribers.query.filter().paginate(per_page=100,page=page_no,error_out=True)
   
 
    return render_template('email.html',subscribers=subscribers,subscribersNo=subscribersNo)
@app.route('/dashboard/email/search', methods=['GET','POST'])
def emailSearch():
    if request.method=='POST':
            form=request.form
            search_value=form['email_search_string']
            search="%{0}%".format(search_value)
            print(search)
            result=Subscribers.query.filter(Subscribers.email.like(search)).all()
            return render_template("email_search.html",result_email=result)
@app.route('/dashboard/email/delete/<int:id>')
def femailDelete(id):
    delete=Subscribers.query.filter_by(id=id).first()
    db.session.delete(delete)
    db.session.commit()
    return redirect('/dashboard/emails')
@app.route('/search/<string:type>/<int:page>',methods=['POST','GET'])
@login_required
def search_dashboard(type,page):
    if type=='Ard':
         if request.method=="POST":

            form=request.form
            search_value=form['search_string']
            search="%{0}%".format(search_value)
            print(search)
            result=Arduinoproject_posts.query.filter(Arduinoproject_posts.heading.like(search)).paginate(per_page=12,page=page,error_out=True)
            return render_template("dashboard_search.html",result_ard=result)
    if type=='Other':
         if request.method=="POST":

            form=request.form
            search_value=form['search_string']
            search="%{0}%".format(search_value)
            print(search)
            result=Other_posts.query.filter(Other_posts.heading.like(search)).paginate(per_page=12,page=page,error_out=True)
            return render_template("dashboard_search.html",result_ard=result)
    if type=='Basic':
         if request.method=="POST":

            form=request.form
            search_value=form['search_string']
            search="%{0}%".format(search_value)
            print(search)
            result=Basicproject_posts.query.filter(Basicproject_posts.heading.like(search)).paginate(per_page=12,page=page,error_out=True)
            return render_template("dashboard_search.html",result_ard=result)
    if type=='Iot':
         if request.method=="POST":

            form=request.form
            search_value=form['search_string']
            search="%{0}%".format(search_value)
            print(search)
            result=Iotproject_posts.query.filter(Iotproject_posts.heading.like(search)).paginate(per_page=12,page=page,error_out=True)
            return render_template("dashboard_search.html",result_ard=result)
        
      
    return render_template('dashboard_search.html')
@app.route('/test')
def test():
    
    print('type=',type_)
    print("heading=",heading)
    print("thumbnail=",thumbnail)
    print("cover_image=",cover_image)
    print("keyword=",keyword)
    
    print("description=",description)
    print("index=",index)
    print("quickQuestions=",quick_questions)
    print("quickAnsweers=",quick_answers)
    print("para=",para)
    print("para_subheading=",para_subheading)
    print("para_thumbnail=",para_thumbnail)
    print("conclusion=",conclusion)
    print("faq_q=",faq_q)
    print("faq_ans=",faq_ans)
    print("col1=",table_col1)
    print("col2=",table_col2)

    
    print("url=",url)
    print("code=",code)
    print("code_language=",code_language)
    print("title=",title)
    print("cover_image=",cover_image)
    print("cover_image_description=",cover_image_description)
    print("meta_keywords=",meta_keywords)
    print("para_ImgDescription=",para_ImgDescription)
    return "CHECK THE  CONSOLE"

    
@app.route('/save_draft',methods=['GET','POST'])
@login_required
def save_as_draft():
    current_date=strftime("%Y-%m-%d ", gmtime())
    global url
    global code
    global code_language
    global code_heading
    global title
    global cover_image_description
    global meta_keywords
    global para_ImgDescription
    global heading
    global type_
    global quick_questions
    global quick_answers
    global heading1
    global heading2
    global faq_q
    global faq_ans
    global conclusion
    global description
    global keyword
    global para
    global para_subheading
    global para_thumbnail
    global thumbnail
    global cover_image
    global index
    
    
    draft=Draft(date=current_date,
                thumbnail=thumbnail,
                cover_img=cover_image,
                url=url,
                meta_keywords=meta_keywords,
                meta_title=title,
                img_description=cover_image_description,
                keyword=keyword,type=type_,
                heading=heading,
                description=description,
                Tableheading1=heading1,
                Tableheading2=heading2,
                conclusion=conclusion)
    db.session.add(draft)
    db.session.commit()
    print("quick_amswrs=",quick_answers)
    print("quick_questions=",quick_questions)
    if quick_questions:
      for Q,A in zip(quick_questions, quick_answers) :
        draftQA=Quick_answers_draft(ques=Q,ans=A,post_name=draft)
        db.session.add(draftQA)
        db.session.commit()
        
    if faq_q or faq_ans:
      for Q,A in zip(faq_q, faq_ans) :
        draftQA=Faq_draft(faq_q=Q,faq_ans=A,post_name=draft)
        db.session.add(draftQA)
        db.session.commit()
    if code:
      for heading,code,language in zip(code_heading,code, code_language) :
        draftCode=Code_draft(heading=heading,code=code,language=code_language,post_name=draft)
        db.session.add(draftCode)
        db.session.commit()
    for ind in index:
        indexDraft=Index_draft(topic=ind,post_name=draft)
        db.session.add(indexDraft)
        db.session.commit()
    for content,heading,img in zip(para,para_subheading,para_thumbnail):
        content=Content_draft(heading=heading,img=img,para=content,post_name=draft)
        db.session.add(content)
        db.session.commit()
  
    if heading1 or heading2 or table_col1 or table_col2:
      for col1,col2 in zip(table_col1,table_col2):
            table=Comparison_table_draft(head1_point=col1,head2_point=col2,post_name=draft)
            db.session.add(table)
            db.session.commit()
  
    
        
    
    return redirect('/dashboard/draft')
@app.route('/dashboard/draft' ,methods=['GET','POST'])
def draft():
    draft=Draft.query.filter().paginate(per_page=12,page=1,error_out=True)
    print(draft)
    return render_template('draft.html' ,draft=draft)
@app.route('/Edit/<string:type>/<int:id>')
def EditPost(type,id):
    if type=="Ard":
        post=Arduinoproject_posts.query.filter_by(id=id).first()
        
    if type=="Basic":
        post=Basicproject_posts.query.filter_by(id=id).first()
    if type=="Iot":
        post=Iotproject_posts.query.filter_by(id=id).first()
        
    if type=="Other":
        post=Other_posts.query.filter_by(id=id).first()
        
    if type=="draft":
        post=Draft.query.filter_by(id=id).first()
        
    global para_ImgDescription
    para_ImgDescription=[]
    global code_language
    code_language=[]
    global code
    code=[]
    global code_heading
    code_heading=[]
    global type_
    type_=post.type
    global heading1
    heading1=post.Tableheading1
    global heading2
    heading2=post.Tableheading2
    
    global table_col1
    global table_col2
    table_col1=[]
    table_col2=[]
    for db in post.comparison_table:
        table_col1.append(db.head1_point)
        table_col2.append(db.head2_point)
    #! todo----------------------------------------
    #! todo----------------------------------------
    
    global thumbnail
    thumbnail=post.thumbnail
    global keyword
    keyword=post.keyword
    global meta_keywords
    meta_keywords=post.meta_keywords
    global cover_image
    cover_image=post.cover_img
    global url
    url=post.url
    global title
    title=post.meta_title
    global cover_image_description
    cover_image_description=post.img_description
    global heading
    heading=post.heading
    global description
    description=post.description
    
    global quick_questions
    global quick_asnwers
    quick_questions=[]
    quick_answers=[]
    for db in post.quick_answers:
        quick_answers.append(db.ans)
        quick_questions.append(db.ques)
    #! todo --------------------------------------------
    #! todo --------------------------------------------
    
    global index
    index=[]
    for db in post.index:
        index.append(db.topic)
        
   
    # ! todo --------------------------------------------
 
        
        
    global para_thumbnail
    global para
    global para_subheading
    para_thumbnail=[]
    para=[]
    para_subheading=[]
    for db in post.content_parts:
        para_subheading.append(db.heading)
        para_ImgDescription.append(db.img_description)
        para_thumbnail.append(db.img)
        para.append(db.para)
    for db in post.code:
        code.append(db.code)
        code_language.append(db.language)
        code_heading.append(db.heading)
      
    # ! todo -------------------------------------------
    # ! todo -----------------------------------------
    # ! todo --------------------------------------------
    
    global conclusion
    conclusion=post.conclusion
    
    global faq_q
    global faq_ans
    faq_q=[]
    faq_ans=[]
    for db in post.faq:
        faq_q.append(db.faq_q)
        faq_ans.append(db.faq_ans)
    #! todo --------------------------------------------
    #! todo --------------------------------------------
    conclusion=post.conclusion
   
    post_type=type_[0:-4]
    intend=type_[len(post_type):]
    
   
    print("para:",para)
    print("para_subheading:",para_subheading)
    print("para_thumbnail:",para_thumbnail)
    print("para_imgDescription:",para_ImgDescription)
    return render_template('edit_post.html',
                           coverImg=cover_image,
                           metaKeywords=meta_keywords,
                           coverImgDescription=cover_image_description,
                           title=title,
                           url=url,
                           paraImgDescription=para_ImgDescription,
                           code=code,
                           codeLanguage=code_language,
                           codeHeading=code_heading,
                           quickAnswersDb=post.quick_answers,
                           indexDb=post.index,
                           codeDb=post.code,
                           paraDb=post.content_parts,
                           faqDb=post.faq,
                           tableDb=post.comparison_table,
                           totalType=json.dumps(type_),
                           countCode=json.dumps(len(code_heading)),
                           countQuickQuestions=json.dumps(len(quick_questions)),
                           countQuickAnswers=json.dumps(len(quick_answers)),
                           countFaq_q=json.dumps(len(faq_q)),
                           countFaq_ans=json.dumps(len(faq_ans)),
                           countIndex=json.dumps(len(index)),
                           countPara=json.dumps(len(para)),
                           countContentHeading=json.dumps(len(para_subheading)),
                           countContentThumbnail=json.dumps(len(para_thumbnail)),
                           type=type,
                           post_type=post_type,
                           keyword=keyword,
                           intend=intend,
                           heading=heading,
                           thumbnail=thumbnail,
                           description=description,
                           index=index,
                           quickQuestions=quick_questions,
                           quickAnswers=quick_answers,
                           para=para,
                           para_subheading=para_subheading,
                           para_thumbnail=para_thumbnail,
                           conclusion=conclusion,
                           faq_q=faq_q,
                           faq_ans=faq_ans,
                           col1=table_col1,
                           col2=table_col2,
                           countCol1=json.dumps(len(table_col1)),
                           countCol2=json.dumps(len(table_col2)),
                           tableHeading1=post.Tableheading1,
                           tableHeading2=post.Tableheading2,
                           id=id
                           )
@app.route('/save_edited/<string:type>/<int:id>',methods=['GET','POST'])
@login_required
def save_edited(type,id):
    if type=='Ard':
      post=Arduinoproject_posts.query.filter_by(id=id).first()
      returnPath="/all_post/1"
      
    if type=='Basic':
      post=Basicproject_posts.query.filter_by(id=id).first()
      returnPath="/dashboard_basic/1"
      
    if type=='Iot':
      post=Iotproject_posts.query.filter_by(id=id).first()
      returnPath="/dashboard_iot/1"
      
    if type=='Other':
      post=Other_posts.query.filter_by(id=id).first()
      returnPath="/dashboard_other/1"
      
    if type=='draft':
      post=Draft.query.filter_by(id=id).first()
      returnPath="/dashboard/draft"
      
    global heading
    global type_
    global description
    global keyword
    global quick_answers
    global quick_questions
    global index
    global para
    global para_subheading
    global para_thumbnail
    global conclusion
    global faq_q
    global faq_ans
    global heading1
    global heading2
    global table_col1
    global table_col2
    global thumbnail
    global url
    global title
    global cover_image
    global cover_image_description
    global meta_keywords
    global para_ImgDescription
    global code_language
    global code
    global code_heading
    post.url=url
    post.title=title
    post.cover_img=cover_image
    post.meta_keywords=meta_keywords
    post.img_description=cover_image_description
    
    post.heading=heading
    post.description=description
    post.type=type_
    post.thumbnail=thumbnail
    post.Tableheading1=heading1
    post.Tableheading2=heading2
    post.keyword=keyword
    post.conclusion=conclusion
    db.session.commit()
    
    
    if quick_answers or quick_questions:
        
      for ind in range(0,len(post.quick_answers)):
          try:
              post.quick_answers[ind].ans=quick_answers[ind]
          except IndexError:
              pass
          try:
              post.quick_answers[ind].ques=quick_questions[ind]
              
          except IndexError:
              pass
              
          db.session.commit()  
      if len(post.quick_answers)<len(quick_answers) or len(post.quick_answers)<len(quick_questions):
           for i in range(len(post.quick_answers),len(quick_questions)):
             if type=='Ard':
                addedData=Quick_answers_arduino(ques=quick_questions[i],ans=quick_answers[i],post_name=post)
                 
             if type=='Basic':
                addedData=Quick_answers_basic(ques=quick_questions[i],ans=quick_answers[i],post_name=post)
                 
             if type=='Iot':
                addedData=Quick_answers_iot(ques=quick_questions[i],ans=quick_answers[i],post_name=post)
                 
             if type=='Other':
                addedData=Quick_answers_other(ques=quick_questions[i],ans=quick_answers[i],post_name=post)
                 
             if type=='draft':
                 addedData=Quick_answers_draft(ques=quick_questions[i],ans=quick_answers[i],post_name=post)
                 
             db.session.add(addedData)   
             db.session.commit()   
    
    if faq_ans or faq_q:
        
      for ind in range(0,len(post.faq)):
          try:
              post.faq[ind].faq_ans=faq_ans[ind]
          except IndexError:
              pass
          try:
              post.faq[ind].faq_q=faq_q[ind]
              
          except IndexError:
              pass
              
          db.session.commit()
            
      if len(post.faq)<len(faq_q) or len(post.faq)<len(faq_ans):
           for i in range(len(post.faq),len(faq_q)):
            if type=='Ard':
                addedData=Faq_arduino(faq_q=faq_q[i],faq_ans=faq_ans[i],post_name=post)
                 
            if type=='Basic':
                addedData=Faq_basic(faq_q=faq_q[i],faq_ans=faq_ans[i],post_name=post)
                 
            if type=='Iot':
                addedData=Faq_iot(faq_q=faq_q[i],faq_ans=faq_ans[i],post_name=post)
                 
            if type=='Other':
                addedData=Faq_other(faq_q=faq_q[i],faq_ans=faq_ans[i],post_name=post)
                 
            if type=='draft':
                 addedData=Faq_draft(faq_q=faq_q[i],faq_ans=faq_ans[i],post_name=post)
            db.session.add(addedData)   
            db.session.commit()   
    if code or code_language or code_heading:
      print(code_heading,code,code_language)  
      for ind in range(0,len(post.code)):
          print("in for 1")
          try:
              post.code[ind].code=code[ind]
          except IndexError:
              pass
          try:
              post.code[ind].heading=code_heading[ind]
              
          except IndexError:
              pass
          try:
              post.code[ind].language=code_language[ind]
              
          except IndexError:
              pass
              
          db.session.commit()
            
      if len(post.code)<len(code) or len(post.code)<len(code_heading)  or len(post.code)<len(code_language):
           for i in range(len(post.code),len(code_heading)):
            if type=='Ard':
                addedData=Code_arduino(heading=code_heading[i],code=code[i],language=code_language[i],post_name=post)
                 
            if type=='Basic':
                addedData=Code_basic(heading=code_heading[i],code=code[i],language=code_language[i],post_name=post)
                 
            if type=='Iot':
                addedData=Code_iot(heading=code_heading[i],code=code[i],language=code_language[i],post_name=post)
                 
            if type=='Other':
                addedData=Code_other(heading=code_heading[i],code=code[i],language=code_language[i],post_name=post)
                 
            if type=='draft':
                 addedData=Code_draft(heading=code_heading[i],code=code[i],language=code_language[i],post_name=post)
            db.session.add(addedData)   
            db.session.commit()   

    if para or para_subheading:
        
      for ind in range(0,len(post.content_parts)):
          try:
              post.content_parts[ind].heading=para_subheading[ind]
          except IndexError:
              pass
          try:
              post.content_parts[ind].para=para[ind]
              
          except IndexError:
              pass
          
          try:
              post.content_parts[ind].img=para_thumbnail[ind]
              
          except IndexError:
              pass
          try:
              post.content_parts[ind].img_description=para_ImgDescription[ind]
              
          except IndexError:
              pass
              
          db.session.commit()
            
      if len(post.content_parts)<len(para_subheading) or len(post.content_parts)<len(para):
           print("legth post.content_parts",len(post.content_parts))
           print("legth para_subheading",len(para_subheading))
           for i in range(len(post.content_parts),len(para_subheading)):
             if type=='Ard':
                addedData=Content_arduino(heading=para_subheading[i],img_description=para_ImgDescription[i],img=para_thumbnail[i],para=para[i],post_name=post)
                 
             if type=='Basic':
                addedData=Content_basic(heading=para_subheading[i],img_description=para_ImgDescription[i],img=para_thumbnail[i],para=para[i],post_name=post)
                 
             if type=='Iot':
                addedData=Content_iot(heading=para_subheading[i],img_description=para_ImgDescription[i],img=para_thumbnail[i],para=para[i],post_name=post)
                 
             if type=='Other':
                addedData=Content_other(heading=para_subheading[i],img_description=para_ImgDescription[i],img=para_thumbnail[i],para=para[i],post_name=post)
                 
             if type=='draft':
                 addedData=Content_draft(heading=para_subheading[i],img_description=para_ImgDescription[i],img=para_thumbnail[i],para=para[i],post_name=post)
             db.session.add(addedData)   
             db.session.commit()   
 
    if index:
      for ind in range(0,len(post.index)):
          try:
            post.index[ind].topic=index[ind]
          except IndexError:
              pass
          db.session.commit()   
      if len(post.index)<len(index):
         for i in range(len(post.index),len(index)):
             if type=='Ard':
                addedData=Index_arduino(topic=index[i],post_name=post)
                 
             if type=='Basic':
                addedData=Index_basic(topic=index[i],post_name=post)
                 
             if type=='Iot':
                addedData=Index_iot(topic=index[i],post_name=post)
                 
             if type=='Other':
                addedData=Index_other(topic=index[i],post_name=post)
                 
             if type=='draft':
                 addedData=Index_draft(topic=index[i],post_name=post)
             db.session.add(addedData)   
             db.session.commit()    

    if table_col1 or table_col2:
      for ind in range(0,len(post.comparison_table)):
          try:
             post.comparison_table[ind].head1_point=table_col1[ind]
          except IndexError:
              pass
          
          try:
              post.comparison_table[ind].head2_point=table_col2[ind]
          except:
             pass
          db.session.commit()   
      if len(post.comparison_table)<len(table_col1) or len(post.comparison_table)<len(table_col2):
          for i in range(len(post.comparison_table),len(table_col1)):
             if type=='Ard':
                addedData=Comparison_table_arduino(head1_point=table_col1[i],head2_point=table_col2[i],post_name=post)
                 
             if type=='Basic':
                addedData=Comparison_table_basic(head1_point=table_col1[i],head2_point=table_col2[i],post_name=post)
                 
             if type=='Iot':
                addedData=Comparison_table_iot(head1_point=table_col1[i],head2_point=table_col2[i],post_name=post)
                 
             if type=='Other':
                addedData=Comparison_table_other(head1_point=table_col1[i],head2_point=table_col2[i],post_name=post)
                 
             if type=='draft':
                 addedData=Comparison_table_draft(head1_point=table_col1[i],head2_point=table_col2[i],post_name=post)
             db.session.add(addedData)   
             db.session.commit()     
             
    return redirect(returnPath)
@app.route('/delete_item', methods=['POST','GET'])
@login_required
def delete_item():
       global heading
       global type_
       global quick_answers
       global quick_questions
       global heading1
       global heading2
       global faq_q
       global faq_ans
       global conclusion
       global description
       global keyword
       global para
       global para_subheading
       global para_thumbnail
       global thumbnail
       global index
       req=request.get_json()
       post_type=req['post_type']
       print(req['type']) 
       print(req['id']) 
       print(post_type)
    #    print(req['post_type']) 
       if post_type=="Ard":
        
          if req['type']=='index':
              index=[]
              print(req['id'])
              delete=Index_arduino.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='quickAnswers':
              delete=Quick_answers_arduino.query.filter_by(id=req['id']).first()
              quickAnswers=[]
              quickQuestions=[]
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='para':
              print('in para')
              print(req['id'])
              para=[]
              para_subheading=[]
              para_thumbnail=[]
              para_ImgDescription=[]
              delete=Content_arduino.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='faq':
              faq_q=[]
              faq_ans=[]
              delete=Faq_arduino.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='code':
              code=[]
              code_heading=[]
              code_language=[]
              delete=Code_arduino.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='table':
              table_col1=[]
              table_col2=[]
              heading1=""
              heading2=""
              print('-------------------------------------------------------------------')
              delete=Comparison_table_arduino.query.filter_by(draft_id=req['id'])
              for i in delete:
                        db.session.delete(i)
                        db.session.commit()
       if post_type=="Basic":
           
          if req['type']=='index':
              index=[]
              print(req['id'])
              delete=Index_basic.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='quickAnswers':
              quickAnswers=[]
              quickQuestions=[]
              delete=Quick_answers_basic.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='para':
              para=[]
              para_subheading=[]
              para_thumbnail=[]
              para_ImgDescription=[]
              delete=Content_basic.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='faq':
              faq_q=[]
              faq_ans=[]
              delete=Faq_basic.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='code':
              code=[]
              code_heading=[]
              code_language=[]
              delete=Code_basic.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='table':
              table_col1=[]
              table_col2=[]
              heading1=""
              heading2=""
              print('-------------------------------------------------------------------')
              delete=Comparison_table_basic.query.filter_by(draft_id=req['id'])
              for i in delete:
                        db.session.delete(i)
                        db.session.commit()              
       if post_type=="Iot":
           
          if req['type']=='index':
              index=[]
              delete=Index_iot.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='quickAnswers':
              quickAnswers=[]
              quickQuestions=[]
              delete=Quick_answers_iot.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='para':
              para=[]
              para_subheading=[]
              para_thumbnail=[]
              para_ImgDescription=[]
              delete=Content_iot.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='faq':
              faq_q=[]
              faq_ans=[]
              delete=Faq_iot.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='code':
              code=[]
              code_heading=[]
              code_language=[]
              delete=Code_iot.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='table':
              table_col1=[]
              table_col2=[]
              heading1=""
              heading2=""
              print('-------------------------------------------------------------------')
              delete=Comparison_table_iot.query.filter_by(draft_id=req['id'])
              for i in delete:
                        db.session.delete(i)
                        db.session.commit()              
       if post_type=="Other":
           
          if req['type']=='index':
              index=[]
              delete=Index_other.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='quickAnswers':
              quickAnswers=[]
              quickQuestions=[]
              delete=Quick_answer_other.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='para':
              para=[]
              para_subheading=[]
              para_thumbnail=[]
              para_ImgDescription=[]
              delete=Content_other.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='faq':
              faq_q=[]
              faq_ans=[]
              delete=Faq_other.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='code':
              code=[]
              code_heading=[]
              code_language=[]
              delete=Code_other.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='table':
              table_col1=[]
              table_col2=[]
              heading1=""
              heading2=""
              print('-------------------------------------------------------------------')
              delete=Comparison_table_other.query.filter_by(draft_id=req['id'])
              for i in delete:
                        db.session.delete(i)
                        db.session.commit()              
       if post_type=="draft":
          print(req['type'])  
          if req['type']=='index':
              index=[]
              delete=Index_draft.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='quickAnswers':
              quickAnswers=[]
              quickQuestions=[]
              delete=Quick_answers_draft.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='para':
              para=[]
              para_subheading=[]
              para_thumbnail=[]
              para_ImgDescription=[]
              delete=Content_draft.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='faq':
              faq_q=[]
              faq_ans=[]
              delete=Faq_draft.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='code':
              print("=================",req['id'])
              code=[]
              code_heading=[]
              code_language=[]
              delete=Code_draft.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()              
          if req['type']=='table':
              table_col1=[]
              table_col2=[]
              heading1=""
              heading2=""
              print('-------------------------------------------------------------------')
              delete=Comparison_table_draft.query.filter_by(draft_id=req['id'])
              for i in delete:
                        db.session.delete(i)
                        db.session.commit()
       return "__success__"     
@app.route('/publish/<string:type>/<draft_id>', methods=['GET', 'POST'])
@login_required
def publish(type,draft_id):
    current_date=strftime("%Y-%m-%d ", gmtime())
    draft=Draft.query.filter_by(id=draft_id).first()
    if type=="Ard":
      add=Arduinoproject_posts(date=current_date,
                               thumbnail=draft.thumbnail,
                               cover_img=draft.cover_img,
                               url=draft.url,
                               meta_keywords=draft.meta_keywords,
                               meta_title=draft.meta_title,
                               img_description=draft.img_description,
                               
                               keyword=draft.keyword,
                               type=draft.type,
                               heading=draft.heading,
                               description=draft.description,Tableheading1=draft.Tableheading1,Tableheading2=draft.Tableheading2,conclusion=draft.conclusion)

      db.session.add(add)
      db.session.commit()
      for i in draft.index:
          addIndex=Index_arduino(topic=i.topic,post_name=add)
          db.session.add(addIndex)
          db.session.commit()
          
      for i in draft.quick_answers:
          addQuickAnswers=Quick_answers_arduino(ques=i.ques,ans=i.ans,post_name=add)
          db.session.add(addQuickAnswers)
          db.session.commit()
      for i in draft.faq:
          addFaq=Faq_arduino(faq_q=i.faq_q,faq_ans=i.faq_ans,post_name=add)
          db.session.add(addFaq)
          db.session.commit()
      for i in draft.content_parts:
          addPara=Content_arduino(heading=i.heading,img=i.img,para=i.para,post_name=add)
          db.session.add(addPara)
          db.session.commit()
      for i in draft.comparison_table:
          addTable=Comparison_table_arduino(head1_point=i.head1_point,head2_point=i.head2_point,post_name=add)
          db.session.add(addTable)
          db.session.commit()
      for i in draft.code:
          addTable=Code_arduino(heading=i.heading,code=i.code,language=i.language,post_name=add)
          db.session.add(addTable)
          db.session.commit()
    if type=="Basic":
      add=Basicproject_posts(date=current_date,
                             thumbnail=draft.thumbnail,
                             cover_img=draft.cover_img,
                             url=draft.url,
                             meta_keywords=draft.meta_keywords,
                             meta_title=draft.meta_title,
                             img_description=draft.img_description,
                             keyword=draft.keyword,
                             type=draft.type,
                             heading=draft.heading,
                             description=draft.description,
                             Tableheading1=draft.Tableheading1,
                             Tableheading2=draft.Tableheading2,
                             conclusion=draft.conclusion)
      db.session.add(add)
      db.session.commit()
      for i in draft.index:
          addIndex=Index_basic(topic=i.topic,post_name=add)
          db.session.add(addIndex)
          db.session.commit()
      for i in draft.quick_answers:
          addQuickAnswers=Quick_answers_basic(ques=i.ques,ans=i.ans,post_name=add)
          db.session.add(addQuickAnswers)
          db.session.commit()
      for i in draft.faq:
          addFaq=Faq_basic(faq_q=i.faq_q,faq_ans=i.faq_ans,post_name=add)
          db.session.add(addFaq)
          db.session.commit()
      for i in draft.content_parts:
          addPara=Content_basic(heading=i.heading,img=i.img,para=i.para,post_name=add)
          db.session.add(addPara)
          db.session.commit()
      for i in draft.comparison_table:
          addTable=Comparison_table_basic(head1_point=i.head1_point,head2_point=i.head2_point,post_name=add)
          db.session.add(addTable)
          db.session.commit()
      for i in draft.code:
          addTable=Code_basic(heading=i.heading,code=i.code,language=i.language,post_name=add)
          db.session.add(addTable)
          db.session.commit()
    if type=="Iot":
      add=Iotproject_posts(date=current_date,
                           thumbnail=draft.thumbnail,
                           cover_img=draft.cover_img,
                           url=draft.url,
                           meta_keywords=draft.meta_keywords,
                           meta_title=draft.meta_title,
                           img_description=draft.img_description,
                           keyword=draft.keyword,
                           type=draft.type,
                           heading=draft.heading,
                           description=draft.description,
                           Tableheading1=draft.Tableheading1,
                           Tableheading2=draft.Tableheading2,
                           conclusion=draft.conclusion)
      db.session.add(add)
      db.session.commit()
      for i in draft.index:
          addIndex=Index_iot(topic=i.topic,post_name=add)
          db.session.add(addIndex)
          db.session.commit()
      for i in draft.quick_answers:
          addQuickAnswers=Quick_answers_iot(ques=i.ques,ans=i.ans,post_name=add)
          db.session.add(addQuickAnswers)
          db.session.commit()
      for i in draft.faq:
          addFaq=Faq_iot(faq_q=i.faq_q,faq_ans=i.faq_ans,post_name=add)
          db.session.add(addFaq)
          db.session.commit()
      for i in draft.content_parts:
          addPara=Content_iot(heading=i.heading,img=i.img,para=i.para,post_name=add)
          db.session.add(addPara)
          db.session.commit()
      for i in draft.comparison_table:
          addTable=Comparison_table_iot(head1_point=i.head1_point,head2_point=i.head2_point,post_name=add)
          db.session.add(addTable)
          db.session.commit()
      for i in draft.code:
          addTable=Code_iot(heading=i.heading,code=i.code,language=i.language,post_name=add)
          db.session.add(addTable)
          db.session.commit()
    if type=="Other":
      add=Other_posts(date=current_date,
                      thumbnail=draft.thumbnail,
                      cover_img=draft.cover_img,
                      url=draft.url,
                      meta_keywords=draft.meta_keywords,
                      meta_title=draft.meta_title,
                      img_description=draft.img_description,                      
                      keyword=draft.keyword,
                      type=draft.type,
                      heading=draft.heading,
                      description=draft.description,
                      Tableheading1=draft.Tableheading1,
                      Tableheading2=draft.Tableheading2,
                      conclusion=draft.conclusion)
      db.session.add(add)
      db.session.commit()
      for i in draft.index:
          addIndex=Index_other(topic=i.topic,post_name=add)
          db.session.add(addIndex)
          db.session.commit()
      for i in draft.quick_answers:
          addQuickAnswers=Quick_answers_other(ques=i.ques,ans=i.ans,post_name=add)
          db.session.add(addQuickAnswers)
          db.session.commit()
      for i in draft.faq:
          addFaq=Faq_other(faq_q=i.faq_q,faq_ans=i.faq_ans,post_name=add)
          db.session.add(addFaq)
          db.session.commit()
      for i in draft.content_parts:
          addPara=Content_other(heading=i.heading,img=i.img,para=db.para,post_name=add)
          db.session.add(addPara)
          db.session.commit()
      for i in draft.comparison_table:
          addTable=Comparison_table_other(head1_point=i.head1_point,head2_point=i.head2_point,post_name=add)
          db.session.add(addTable)
          db.session.commit()
      for i in draft.code:
          addTable=Code_other(heading=i.heading,code=i.code,language=i.language,post_name=add)
          db.session.add(addTable)
          db.session.commit()
 # todo : ------------------------------------------------------------------------------------
    print(draft_id)
    deleteSelf=Draft.query.filter_by(id=draft_id).first()
    print(deleteSelf)
    db.session.delete(deleteSelf)
    db.session.commit()
    deleteContent=Content_draft.query.filter_by(draft_id=id).all()
    deleteIndex=Index_draft.query.filter_by(draft_id=id).all()
    deleteTable=Comparison_table_draft.query.filter_by(draft_id=id).all()
    deleteFaq=Faq_draft.query.filter_by(draft_id=id).all()
    deleteQuickanswers=Quick_answers_draft.query.filter_by(draft_id=id).all()
     
    if deleteContent:
            for d in deleteContent:
                db.session.delete(d)
                db.session.commit()
    if deleteIndex:
            for d in deleteTable:
             db.session.delete(d)
             db.session.commit()
            
    if deleteTable:
         for d in deleteTable:
            db.session.delete(d)
            db.session.commit()
            
    if deleteFaq:
            for d in deleteFaq:
                db.session.delete(d)
                db.session.commit()
       
    if deleteQuickanswers:
            for d in deleteQuickanswers:
                db.session.delete(d)
                db.session.commit()
        
    return redirect('/dashboard/draft')
    #   todo: ----Tomorrow do complete this publis
#  todo make robots.txt file at the end  
@app.route("/robots.txt")
def robots_txt():
    Disallow = lambda string: 'Disallow: {0}'.format(string)
    return Response("User-agent: *\n{0}\n".format("\n".join([
        Disallow('/dashboard/*'),
        Disallow('/thank-you'),
    ])))
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(seconds=200)
    session.modified = True
if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.run(host='127.0.0.1', port=8000, debug=True)
