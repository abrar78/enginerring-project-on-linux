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
cover_image=""
url=""

title=""
cover_image_description=""
meta_keywords=""
global type_
type_=''
global thumbnail
thumbnail=""
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
global faq_q
faq_q=[]
global faq_ans
faq_ans=[]
global article
article=""


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

     profile=About_me.query.first()
     
     if profile:
        txt=profile.profile
     else:
         txt=""    
     arduino=Arduinoproject_posts.query.order_by(desc(Arduinoproject_posts.id)).paginate(per_page=7,page=1,error_out=True)
     basic=Basicproject_posts.query.order_by(desc(Basicproject_posts.id)).paginate(per_page=7,page=1,error_out=True)
     iot=Iotproject_posts.query.order_by(desc(Iotproject_posts.id)).paginate(per_page=7,page=1,error_out=True)
     other=Other_posts.query.order_by(desc(Other_posts.id)).paginate(per_page=7,page=1,error_out=True)
     arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.id)).first()
     basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).first()
     iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).first()
     other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id)).first()
     latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]
     
     latest_thumbnails={"imgs":[]}
     arduino_thumbnails={"imgs":[]}
     basic_thumbnails={"imgs":[]}
     iot_thumbnails={"imgs":[]}
     other_thumbnails={"imgs":[]}
     print (latest_posts)
     if latest_posts[0] and latest_posts[1] and latest_posts[2] and latest_posts[3]:
      for i in latest_posts:
         latest_thumbnails["imgs"].append(i.thumbnail)
      for i in arduino.items:
         arduino_thumbnails["imgs"].append(i.thumbnail)
      for i in basic.items:
         basic_thumbnails["imgs"].append(i.thumbnail)
      for i in iot.items:
         iot_thumbnails["imgs"].append(i.thumbnail)
      for i in other.items:
         other_thumbnails["imgs"].append(i.thumbnail)
      
   
         
     return render_template('index.html',
                            arduino_project=arduino,
                            basic_project=basic,
                            iot_project=iot,
                            other_project=other,
                            latest_posts=latest_posts,
                            arduino_thumbnails=json.dumps(arduino_thumbnails),
                            basic_thumbnails=json.dumps(basic_thumbnails),
                            iot_thumbnails=json.dumps(iot_thumbnails),
                            latest_thumbnails=json.dumps(latest_thumbnails),
                            latest_url_type=['arduino-projects','basic-projects','iot-projects','tech-posts'],
                            other_thumbnails=json.dumps(other_thumbnails),
                            txt=txt
                            )
@app.route('/arduino-projects-page/<int:page>')
def arduino_projects(page):
     post=Arduinoproject_posts.query.order_by(desc(Arduinoproject_posts.id)).paginate(per_page=6,page=page,error_out=True)
     thumbnails={"images":[],"current":page}
     for i in post.items:
         thumbnails["images"].append(i.thumbnail)
      
     return render_template('all_projects.html',project=post,title="DIY arduino projects for arduino learners",type="arduino-projects",thumbnails=json.dumps(thumbnails))
@app.route('/basic-projects-page/<int:page>')
def basic_projects(page):
     post=Basicproject_posts.query.order_by(desc(Basicproject_posts.id)).paginate(per_page=6,page=page,error_out=True)
     thumbnails={"images":[],"current":page}
     for i in post.items:
         thumbnails["images"].append(i.thumbnail)
      
     return render_template('all_projects.html',project=post,title="DIY arduino projects for arduino learners",type="basic-projects",thumbnails=json.dumps(thumbnails))
@app.route('/iot-projects-page/<int:page>')
def iot_projects(page):
     post=Iotproject_posts.query.order_by(desc(Iotproject_posts.id)).paginate(per_page=6,page=page,error_out=True)
     thumbnails={"images":[],"current":page}
     for i in post.items:
         thumbnails["images"].append(i.thumbnail)
      
     return render_template('all_projects.html',project=post,title="DIY arduino projects for arduino learners",type="iot-projects",thumbnails=json.dumps(thumbnails))
@app.route('/tech-posts-page/<int:page>')
def other_projects(page):
     post=Other_posts.query.order_by(desc(Other_posts.id)).paginate(per_page=6,page=page,error_out=True)
     thumbnails={"images":[],"current":page}
     for i in post.items:
         thumbnails["images"].append(i.thumbnail)
      
     return render_template('all_projects.html',project=post,title="DIY arduino projects for arduino learners",type="tech-posts",thumbnails=json.dumps(thumbnails))


@app.route('/arduino-tutorial/<string:url>')
def arduinoRead(url):
    arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.id)).all()
    basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).first()
    iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).first()
    other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id)).first()
    
    arduino_post=Arduinoproject_posts.query.filter_by(url='/arduino-tutorial/'+url).first()
    print("------------------------------",type(arduino_latest))
    if arduino_post in arduino_latest:
        arduino_latest.remove(arduino_post)
    try:    
        arduino_latest=arduino_latest[0]
    except IndexError:
        arduino_latest=None; 
    
    latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]    
    search_value=arduino_post.keyword
    search="%{0}%".format(search_value)
    related=Arduinoproject_posts.query.filter(or_(Arduinoproject_posts.description.like(search), Arduinoproject_posts.heading.like(search))).all()
    if arduino_post in related:
        related.remove(arduino_post)
         
    return render_template('readMoreOther.html', post_db=arduino_post,related_post=related[0:4],latest_posts=latest_posts,url_type="Arduino")
@app.route('/basic-electronics/<string:url>')
def basicRead(url):
    arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.id)).first()
    basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).all()
    iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).first()
    other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id)).first()
    basic_post=Basicproject_posts.query.filter_by(url="/basic-electronics/"+url).first()
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
    arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.id)).first()
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
    arduino_latest=Arduinoproject_posts.query.filter().order_by(desc(Arduinoproject_posts.id)).first()
    basic_latest=Basicproject_posts.query.filter().order_by(desc(Basicproject_posts.id)).first()
    iot_latest=Iotproject_posts.query.filter().order_by(desc(Iotproject_posts.id)).first()
    other_latest=Other_posts.query.filter().order_by(desc(Other_posts.id)).all()
    latest_posts=[arduino_latest,basic_latest,iot_latest,other_latest]    
    other_post=Other_posts.query.filter_by(url="/tech-posts/"+url).first()
    print("===============",other_post)
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
    req=request.get_json()
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
    mail.send_message('new message from blog',
                      sender=req['e_mail'],
                      recipients = [params['recipient']],
                      body=req['message'])
    message=Messages(email=req['e_mail'],messsage=req['message'])
    db.session.add(message)
    db.session.commit()
    content={"response":"Thankyou"}
    response=make_response(jsonify(content))
    return response
@app.route('/subscribe',methods = ['GET', 'POST'])
def subscriber():
    req=request.get_json();
    subscriber=Subscribers(email=req['e_mail']);
    message="Hello Abrar New subscribers on your blog please add it to your list \r\n"+"email is"+req['e_mail']
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
      
      
     
      
      para=req['para']
      para_ImgDescription=req['thumbnail_desc']
      para_subheading=req['subheading']
      para_thumbnail=req['thumbnail']
      print(para_ImgDescription)
    if type=="conclusion":
      req=request.get_json()
  
      conclusion=req['conclusion']
      
    if type=="faq":
      req=request.get_json()
      global faq_q
      global faq_ans
      faq_q=req['faq_q']
      faq_ans=req['faq_ans']
    if type=="table":
      req=request.get_json()
    
      
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
        deleteContent=Para_arduino.query.filter_by(arduino_id=id).first()
        deleteIndex=Index_arduino.query.filter_by(arduinopost_id=id).all()
        deleteFaq=Faq_arduino.query.filter_by(arduinopost_id=id).all()
        deleteQuickanswers=Quick_answers_arduino.query.filter_by(arduinopost_id=id).all()
        returnPath="/all_post/1"
    if type=='Basic':
        delete=Basicproject_posts.query.filter_by(id=id).first()
        deleteContent=Para_basic.query.filter_by(basic_id=id).first()
        deleteIndex=Index_basic.query.filter_by(basicpost_id=id).all()
        deleteFaq=Faq_basic.query.filter_by(basicpost_id=id).all()
        deleteQuickanswers=Quick_answers_basic.query.filter_by(basicpost_id=id).all()
        returnPath="/dashboard_basic/1"
        
    if type=='Iot':
        delete=Iotproject_posts.query.filter_by(id=id).first()
        deleteContent=Para_iot.query.filter_by(iot_id=id).first()
        deleteIndex=Index_iot.query.filter_by(iotpost_id=id).all()
        deleteFaq=Faq_iot.query.filter_by(iotpost_id=id).all()
        deleteQuickanswers=Quick_answers_iot.query.filter_by(iotpost_id=id).all()
        returnPath="/dashboard_iot/1"
    if type=='Other':
        delete=Other_posts.query.filter_by(id=id).first()
        deleteContent=Para_other.query.filter_by(other_id=id).first()
        deleteIndex=Index_other.query.filter_by(otherpost_id=id).all()
        deleteFaq=Faq_other.query.filter_by(otherpost_id=id).all()
        deleteQuickanswers=Quick_answers_other.query.filter_by(otherpost_id=id).all()
        returnPath="/dashboard_other/1"
    
    if type=='draft':
        delete=Draft.query.filter_by(id=id).first()
        deleteContent=Para_draft.query.filter_by(draft_id=id).first()
        deleteIndex=Index_draft.query.filter_by(draft_id=id).all()
        deleteFaq=Faq_draft.query.filter_by(draft_id=id).all()
        deleteQuickanswers=Quick_answers_draft.query.filter_by(draft_id=id).all()
        returnPath="/dashboard/draft"
    if deleteContent:
        db.session.delete(deleteContent)
        db.session.commit()
    if deleteIndex:
            for d in deleteIndex:
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
        
    db.session.delete(delete)
    db.session.commit()
    return redirect(returnPath) 
    
@app.route('/create_post')
@login_required
def create_post():
    global article
    article=""
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
@app.route('/dashboard/about')
@login_required
def about():
    about=About_me.query.first()
    print("-------------------------------------------------------------------------------")
    if about:
        print("PROFILE YES")
        txt=about.profile
    else:
        print("PROFILE NO")
        txt=""
        
    return render_template('about.html',about=txt) 
@app.route('/dashboard/about/apply',methods=['GET','POST'])
@login_required
def about_apply():
    form=request.form
    txt=form['about']
    print("-0000000000000000000000 ")
    if About_me.query.filter_by(id=1).first():
        print("YES")
        apply=About_me.query.filter_by(id=1).first()
        apply.profile=txt
        db.session.commit()
    else :
        print("NO")
        apply=About_me(profile=txt)
        db.session.add(apply)
        db.session.commit()
    return redirect("/dashboard/about") 
@app.route('/dashboard/emails/<int:page_no>',methods=['GET','POST'])
@login_required
def emails(page_no):
    subscribersNo=Subscribers.query.filter().count()
    subscribers=Subscribers.query.paginate(per_page=100,page=page_no,error_out=True)
    data={"current":subscribers.page}
   
 
    return render_template('email.html',data=json.dumps(data),subscribers=subscribers,subscribersNo=subscribersNo)
@app.route('/dashboard/email/search', methods=['GET','POST'])
@login_required
def emailSearch():
    if request.method=='POST':
            form=request.form
            search_value=form['email_search_string']
            search="%{0}%".format(search_value)
            print(search)
            result=Subscribers.query.filter(Subscribers.email.like(search)).all()
            return render_template("email_search.html",result_email=result)
@app.route('/dashboard/email/delete/<int:id>', methods=['GET','POST'])
@login_required
def femailDelete(id):
    delete=Subscribers.query.filter_by(id=id).first()
    db.session.delete(delete)
    db.session.commit()
    return redirect('/dashboard/emails/1')
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
    global title
    global cover_image_description
    global meta_keywords
    global heading
    global type_
    global quick_questions
    global quick_answers
    global faq_q
    global faq_ans
    global description
    global keyword
    global thumbnail
    global cover_image
    global index
    global article
    
    
    draft=Draft(date=current_date,
                thumbnail=thumbnail,
                cover_img=cover_image,
                url=url,
                meta_keywords=meta_keywords,
                meta_title=title,
                img_description=cover_image_description,
                keyword=keyword,
                type=type_,
                heading=heading,
                description=description)
 
    db.session.add(draft)
    db.session.commit()

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
    if index:
     for ind in index:
        indexDraft=Index_draft(topic=ind,post_name=draft)
        db.session.add(indexDraft)
        db.session.commit()
    if article:
        article=Para_draft(content=article,post_name=draft)
        db.session.add(article)
        db.session.commit()
        article=""

    return redirect('/dashboard/draft')
@app.route('/dashboard/submit-article',methods=["GET","POST"])
@login_required
def submitArticle():
    req=request.get_json()
    global article
    article=req['article']
    response=make_response(jsonify("/save_draft"),200)
    return response
@app.route('/dashboard/texteditor/<int:id>/<string:type>',methods=["GET","POST"] )
@login_required
def texteditor(id,type):
    global article
    print(article)
    return render_template('texteditor.html',content=article,id=id,type=type)
@app.route('/dashboard/draft' ,methods=['GET','POST'])
@login_required
def draft():
    draft=Draft.query.order_by(desc(Draft.id)).paginate(per_page=20,page=1,error_out=True)
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
        
    
    para_ImgDescription=[]
    global type_
    type_=post.type

  
  
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



    
    global faq_q
    global faq_ans
    faq_q=[]
    faq_ans=[]
    for db in post.faq:
        faq_q.append(db.faq_q)
        faq_ans.append(db.faq_ans)

   
    post_type=type_[0:-4]
    intend=type_[len(post_type):]
    if post.paragraphs:
        global article
        article=post.paragraphs.content
    print("======================")
    print(article)
    print("******************************")
    json_for_texteditor={"id":id,"type":type}
    return render_template('edit_post.html',
                           text_editor_json=json.dumps(json_for_texteditor),
                           coverImg=cover_image,
                           metaKeywords=meta_keywords,
                           coverImgDescription=cover_image_description,
                           title=title,
                           url=url,
                           quickAnswersDb=post.quick_answers,
                           indexDb=post.index,
                           faqDb=post.faq,
                           totalType=json.dumps(type_),
                           countQuickQuestions=json.dumps(len(quick_questions)),
                           countQuickAnswers=json.dumps(len(quick_answers)),
                           countFaq_q=json.dumps(len(faq_q)),
                           countFaq_ans=json.dumps(len(faq_ans)),
                           countIndex=json.dumps(len(index)),
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
                           faq_q=faq_q,
                           faq_ans=faq_ans,
                           id=id
                           )
@app.route('/save_edited/<string:type>/<int:id>',methods=['GET','POST'])
@login_required
def save_edited(type,id):
    req=request.get_json()
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
    global faq_q
    global faq_ans
    global thumbnail
    global url
    global title
    global cover_image
    global cover_image_description
    global meta_keywords
    global article
    article=req['article']
    post.paragraphs.content=article
    post.url=url
    post.title=title
    post.cover_img=cover_image
    post.meta_keywords=meta_keywords
    post.img_description=cover_image_description
    post.heading=heading
    post.description=description
    post.type=type_
    post.thumbnail=thumbnail
    post.keyword=keyword
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



    response=make_response(jsonify(returnPath),200)      
    return response
@app.route('/delete_item', methods=['POST','GET'])
@login_required
def delete_item():
       global heading
       global type_
       global quick_answers
       global quick_questions
       global faq_q
       global faq_ans
       global description
       global keyword
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
          if req['type']=='faq':
              faq_q=[]
              faq_ans=[]
              delete=Faq_arduino.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
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

          if req['type']=='faq':
              faq_q=[]
              faq_ans=[]
              delete=Faq_basic.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
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
          if req['type']=='faq':
              faq_q=[]
              faq_ans=[]
              delete=Faq_iot.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
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
          if req['type']=='faq':
              faq_q=[]
              faq_ans=[]
              delete=Faq_other.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
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

          if req['type']=='faq':
              faq_q=[]
              faq_ans=[]
              delete=Faq_draft.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
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
                               description=draft.description
                              )

      db.session.add(add)
      db.session.commit()
      para=Para_arduino(content=draft.paragraphs.content,post_name=add)
      db.session.add(para)
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
                             description=draft.description
                           
                           )
      db.session.add(add)
      db.session.commit()
      para=Para_basic(content=draft.paragraphs.content,post_name=add)
      db.session.add(para)
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
                           description=draft.description
                           )
      db.session.add(add)
      db.session.commit()
      para=Para_iot(content=draft.paragraphs.content,post_name=add)
      db.session.add(para)
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
                      description=draft.description)
      db.session.add(add)
      db.session.commit()
      para=Para_other(content=draft.paragraphs.content,post_name=add)
      db.session.add(para)
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
 # todo : ------------------------------------------------------------------------------------
    print(id)
    deleteContent=Para_draft.query.filter_by(draft_id=draft_id).first()
    deleteIndex=Index_draft.query.filter_by(draft_id=draft_id).all()
    deleteFaq=Faq_draft.query.filter_by(draft_id=draft_id).all()
    deleteQuickanswers=Quick_answers_draft.query.filter_by(draft_id=draft_id).all()
     
    print("+++++++++++++",draft_id)
    print(deleteContent)
    if deleteContent:
         db.session.delete(deleteContent)
         db.session.commit()
    if deleteIndex:
            for d in deleteIndex:
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
    deleteSelf=Draft.query.filter_by(id=draft_id).first()
    db.session.delete(deleteSelf)
    db.session.commit()
        
    return redirect('/dashboard/draft')
    #   todo: ----Tomorrow do complete this publis
#  todo make robots.txt file at the end  
@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.join(app.instance_path,''),'robots.txt')
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.instance_path,''),'sitemap.xml')
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(seconds=200)
    session.modified = True
if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.run(host='0.0.0.0')
