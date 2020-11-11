from createDb import *
from sqlalchemy import or_,desc
import math
from flask import jsonify,make_response,request,redirect,session,Response
from flask_caching import Cache
import os
import datetime
from werkzeug.utils import secure_filename
from flask_mail import Mail
from flask_login import LoginManager
from jinja2 import Undefined
from time import gmtime, strftime
from random import randint
from flask_optimize import FlaskOptimize
import jinja2

JINJA2_ENVIRONMENT_OPTIONS = { 'undefined' : Undefined }
app.config['UPLOAD_FOLDER']={'upload':params["upload_location"],
                             'cover_image':params["upload_location_coverImg"] }
app.config['OPTIMIZE_ALL_RESPONSE']=True
flask_optimize=FlaskOptimize()
cache=Cache()
cache = Cache(config={'CACHE_TYPE': 'filesystem',
                      'CACHE_DIR':'/home/abrar/Desktop/Abrar/myBlog/engineering-blog-repository-master/static'
                     
                      })
cache.init_app(app)
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
@flask_optimize.optimize()
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
@flask_optimize.optimize()
@cache.memoize(timeout=1800)
def arduino_projects(page):
     post=Arduinoproject_posts.query.order_by(desc(Arduinoproject_posts.id)).paginate(per_page=6,page=page,error_out=True)
     thumbnails={"images":[],"current":page}
     for i in post.items:
         thumbnails["images"].append(i.thumbnail)
      
     return render_template('all_projects.html',project=post,title="DIY arduino projects for arduino learners",type="arduino-projects",thumbnails=json.dumps(thumbnails))
@app.route('/basic-projects-page/<int:page>')
@flask_optimize.optimize()
def basic_projects(page):
     post=Basicproject_posts.query.order_by(desc(Basicproject_posts.id)).paginate(per_page=6,page=page,error_out=True)
     thumbnails={"images":[],"current":page}
     for i in post.items:
         thumbnails["images"].append(i.thumbnail)
      
     return render_template('all_projects.html',project=post,title="DIY arduino projects for arduino learners",type="basic-projects",thumbnails=json.dumps(thumbnails))
@app.route('/iot-projects-page/<int:page>')
@flask_optimize.optimize()
def iot_projects(page):
     post=Iotproject_posts.query.order_by(desc(Iotproject_posts.id)).paginate(per_page=6,page=page,error_out=True)
     thumbnails={"images":[],"current":page}
     for i in post.items:
         thumbnails["images"].append(i.thumbnail)
      
     return render_template('all_projects.html',project=post,title="DIY arduino projects for arduino learners",type="iot-projects",thumbnails=json.dumps(thumbnails))
@app.route('/tech-posts-page/<int:page>')
@flask_optimize.optimize()
def other_projects(page):
     post=Other_posts.query.order_by(desc(Other_posts.id)).paginate(per_page=6,page=page,error_out=True)
     thumbnails={"images":[],"current":page}
     for i in post.items:
         thumbnails["images"].append(i.thumbnail)
      
     return render_template('all_projects.html',project=post,title="DIY arduino projects for arduino learners",type="tech-posts",thumbnails=json.dumps(thumbnails))


@app.route('/arduino-tutorial/<string:url>')
@flask_optimize.optimize()
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
@flask_optimize.optimize()
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
@flask_optimize.optimize()
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
@flask_optimize.optimize()
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
    # print(req)
    # message=""
    # if req['with_only_text']==True:
    #        message="only text advertisement is requested by "+req['first_name']+"About the advertisement is:\r\n"+req['something_about_add']
    #        mail.send_message(
    #                         'new message from blog for advertisement'+'  name:'+req['first_name']+req['last_name'],
    #                         sender=req['email'],
    #                         recipients = [params['recipient']],
    #                         body=message
    #                         )
    # if req['image']==True:
    #             if req['have_image']==True:
    #                message="advertisement with image is requested by "+req['first_name']+'client already has an image and uploaded on server'+"\r\nAbout the advertisement is:\r\n"+req['somethingh_about_add']
    #             if req['dont_have']==True:
    #                 if req['make_image']==True:
    #                      message="advertisement with image is requested by "+req['first_name']+'client dont have an image and he dont want to make one for him by us'+"\r\nAbout the advertisement is:\r\n"+req['somethingh_about_add']
    #                 else:
    #                      message="advertisement with image is requested by "+req['first_name']+'client dont have an image and he  want to make one for him by us'+"\r\nAbout the advertisement is:\r\n"+req['somethingh_about_add']

    # if req['other']==True:
    #             message="other type of advertisemet is requested by "+req['first_name']+'\r\nSpecification of type is \r\n'+req['specification_forOther']+"\r\nAbout the advertisement is:\r\n"+req['somethingh_about_add']


    # mail.send_message(
    #                         'new message from blog for advertisement'+'  name:'+req['first_name']+req['last_name'],
    #                         sender=req['email'],
    #                         recipients = [params['recipient']],
    #                         body=message
    #                         )
    content={"response":"Thankyou"}
    response=make_response(jsonify(content))
    return response

@app.route('/message',methods = ['GET', 'POST'])
def message():
    req=request.get_json();
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
    message="Hello Abrar New subscribers on your blog please add it to your list \r\n"+"email is :"+req['e_mail']
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
@login_required
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
       var=Variables.query.filter_by(id=1).first()
       var.thumbnail=file_name
       db.session.commit()
       f.save(os.path.join(app.config['UPLOAD_FOLDER']['cover_image'],secure_filename(f.filename)))
    if type=='cover':
       f=request.files['file'];
       file_name=f.filename
       file_name=file_name.replace(" ","_")
       var=Variables.query.filter_by(id=1).first()
       var.cover_image=file_name
       db.session.commit()
       f.save(os.path.join(app.config['UPLOAD_FOLDER']['cover_image'],secure_filename(f.filename)))
    if type=='para':
       f=request.files['file'];
       file_name=f.filename
       f.save(os.path.join(app.config['UPLOAD_FOLDER']['cover_image'],secure_filename(f.filename)))
    return "SUCCESS"

@app.route('/dashboard_create_post/<string:type>',methods=['GET','POST'])
@login_required
def dashboard_create_post(type):
    
    if type=="url":
      var=Variables.query.filter_by(id=1).first()
      req=request.get_json()
      var.url=req['url']
      db.session.commit()
      
    if type=="coverImgDescription":
      var=Variables.query.filter_by(id=1).first()
      req=request.get_json()
      var.cover_image_description=req['coverImgDescription']
      db.session.commit()
        
    if type=="keywordsMeta":
      var=Variables.query.filter_by(id=1).first()
      req=request.get_json()
      var.meta_keywords=req['meta_keywords']
      db.session.commit()
    if type=="title":
      var=Variables.query.filter_by(id=1).first()
      req=request.get_json()
      var.title=req['title']
      db.session.commit()
  
    if type=="keyword":
      var=Variables.query.filter_by(id=1).first()
      req=request.get_json()
      var.keyword=req['keyword']
      db.session.commit()
      
    if type=="heading":
      var=Variables.query.filter_by(id=1).first()
      req=request.get_json()
      var.heading=req['heading']
      db.session.commit()

    if type=="type":
      var=Variables.query.filter_by(id=1).first()
      req=request.get_json()
      var.type_=req['type_']
      db.session.commit()
    
    if type=="description":
      var=Variables.query.filter_by(id=1).first()
      req=request.get_json()
      var.description=req['description']
      db.session.commit()
   
    if type=="quickAnswers":
      var=Variables.query.filter_by(id=1).first()
      req=request.get_json()
      var.quick_answers=str(req['quick_answers'])
      var.quick_questions=str(req['quick_questions'])
      db.session.commit()
    
    if type=="index":
      var=Variables.query.filter_by(id=1).first()
      req=request.get_json()
      var.index=str(req['index'])
      db.session.commit()
      
    if type=="faq":
      var=Variables.query.filter_by(id=1).first()
      req=request.get_json()
      print(req['faq_q'])
      print(req['faq_ans'])
      var.faq_q=str(req['faq_q'])
      var.faq_ans=str(req['faq_ans'])
      db.session.commit()      
    
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
    if type=='Ard':
        delete=Arduinoproject_posts.query.filter_by(id=id).first()
        deleteIndex=Index_arduino.query.filter_by(arduinopost_id=id).all()
        deleteFaq=Faq_arduino.query.filter_by(arduinopost_id=id).all()
        deleteQuickanswers=Quick_answers_arduino.query.filter_by(arduinopost_id=id).all()
        returnPath="/all_post/1"
    if type=='Basic':
        delete=Basicproject_posts.query.filter_by(id=id).first()
        deleteIndex=Index_basic.query.filter_by(basicpost_id=id).all()
        deleteFaq=Faq_basic.query.filter_by(basicpost_id=id).all()
        deleteQuickanswers=Quick_answers_basic.query.filter_by(basicpost_id=id).all()
        returnPath="/dashboard_basic/1"
    if type=='Iot':
        delete=Iotproject_posts.query.filter_by(id=id).first()
        deleteIndex=Index_iot.query.filter_by(iotpost_id=id).all()
        deleteFaq=Faq_iot.query.filter_by(iotpost_id=id).all()
        deleteQuickanswers=Quick_answers_iot.query.filter_by(iotpost_id=id).all()
        returnPath="/dashboard_iot/1"
    if type=='Other':
        delete=Other_posts.query.filter_by(id=id).first()
        deleteIndex=Index_other.query.filter_by(otherpost_id=id).all()
        deleteFaq=Faq_other.query.filter_by(otherpost_id=id).all()
        deleteQuickanswers=Quick_answers_other.query.filter_by(otherpost_id=id).all()
        returnPath="/dashboard_other/1"
    
    if type=='draft':
        delete=Draft.query.filter_by(id=id).first()
        deleteIndex=Index_draft.query.filter_by(draft_id=id).all()
        deleteFaq=Faq_draft.query.filter_by(draft_id=id).all()
        deleteQuickanswers=Quick_answers_draft.query.filter_by(draft_id=id).all()
        returnPath="/dashboard/draft"
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
    var=Variables.query.filter_by(id=1).first()
    var.url=""
    var.title=""
    var.cover_image=""
    var.cover_image_description=""
    var.meta_keywords=""
    var.type_=""
    var.thumbnail=""
    var.keyword=""
    var.heading=""
    var.description=""
    var.quick_questions="[]"
    var.quick_answers="[]"
    var.index="[]"
    var.faq_q="[]"
    var.faq_ans="[]"
    var.article=""
    db.session.commit()
    
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
    if about:
        txt=about.profile
    else:
        txt=""
        
    return render_template('about.html',about=txt) 
@app.route('/dashboard/about/apply',methods=['GET','POST'])
@login_required
def about_apply():
    form=request.form
    txt=form['about']
    if About_me.query.filter_by(id=1).first():
        apply=About_me.query.filter_by(id=1).first()
        apply.profile=txt
        db.session.commit()
    else :
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
@login_required
def test():
    var=Variables.query.filter_by(id=1).first()
    print('type=',var.type_)
    print("heading=",var.heading)
    print("thumbnail=",var.thumbnail)
    print("cover_image=",var.cover_image)
    print("keyword=",var.keyword)
    print("description=",var.description)
    print("index=",eval(var.index))
    print("quickQuestions=",eval(var.quick_questions))
    print("quickAnsweers=",eval(var.quick_answers))
    print("faq_q=",eval(var.faq_q))
    print("faq_ans=",eval(var.faq_ans))
    print("url=",var.url)
    print("title=",var.title)
    print("cover_image=",var.cover_image)
    print("cover_image_description=",var.cover_image_description)
    print("meta_keywords=",var.meta_keywords)

    return render_template('test.html',
                           description=var.description,
                           index=var.index,
                           meta_keywords=var.meta_keywords,
                           faq_q=var.faq_q,
                           faq_ans=var.faq_ans,
                           quickQuestions=var.quick_questions,
                           quickAnsweers=var.quick_answers,
                           url=var.url,
                           title=var.title,
                           cover_image=var.cover_image,
                           cover_image_description=var.cover_image_description,
                           type=var.type_,
                           heading=var.heading,
                           thumbnail=var.thumbnail,
                   
                           keyword=var.keyword
                           
                           
                           
                           )

    
@app.route('/save_draft',methods=['GET','POST'])
@login_required
def save_as_draft():
    current_date=strftime("%Y-%m-%d ", gmtime())
    var = Variables.query.filter_by(id=1).first()
    
    
    draft=Draft(date=current_date,
                thumbnail=var.thumbnail,
                cover_img=var.cover_image,
                url=var.url,
                meta_keywords=var.meta_keywords,
                meta_title=var.title,
                img_description=var.cover_image_description,
                keyword=var.keyword,
                type=var.type_,
                heading=var.heading,
                description=var.description,
                article=var.article)
 
    db.session.add(draft)
    db.session.commit()

    if var.quick_questions:
      for Q,A in zip(eval(var.quick_questions), eval(var.quick_answers)) :
        draftQA=Quick_answers_draft(ques=Q,ans=A,post_name=draft)
        db.session.add(draftQA)
        db.session.commit()
        
    if var.faq_q or var.faq_ans:
      for Q,A in zip(eval(var.faq_q), eval(var.faq_ans)) :
        draftQA=Faq_draft(faq_q=Q,faq_ans=A,post_name=draft)
        db.session.add(draftQA)
        db.session.commit()
    if var.index:
     for ind in eval(var.index):
        indexDraft=Index_draft(topic=ind,post_name=draft)
        db.session.add(indexDraft)
        db.session.commit()
    return redirect('/dashboard/draft')
@app.route('/dashboard/submit-article',methods=["GET","POST"])
@login_required
def submitArticle():
    var=Variables.query.filter_by(id=1).first()
    req=request.get_json()
    var.article=req['article']
    db.session.commit()
    response=make_response(jsonify("/save_draft"),200)
    return response
@app.route('/dashboard/texteditor/<int:id>/<string:type>',methods=["GET","POST"] )
@login_required
def texteditor(id,type):
    
    if type == "Ard":
        post=Arduinoproject_posts.query.filter_by(id=id).first()
    if type == "Basic":
        post=Basicproject_posts.query.filter_by(id=id).first()
    if type == "Iot":
        post=Iotproject_posts.query.filter_by(id=id).first()
    if type == "Other":
        post=Other_posts.query.filter_by(id=id).first()
    if type == "draft":
        post=Draft.query.filter_by(id=id).first()
    
    if id==0:
        new=True
    else:
        new=False
    if post:
        article=post.article
    else:
        article=""
    print("new=",new)

    return render_template('texteditor.html',content=article,id=id,type=type,new=new)
@app.route('/dashboard/draft' ,methods=['GET','POST'])
@login_required
def draft():
    draft=Draft.query.order_by(desc(Draft.id)).paginate(per_page=20,page=1,error_out=True)
    print(draft)
    return render_template('draft.html' ,draft=draft)
@app.route('/Edit/<string:type>/<int:id>')
@login_required
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
    
    post_type=post.type[0:-4]
    intend=post.type[len(post_type):]
  
    quick_questions=[]
    quick_answers=[]
    index=[]
    faq_q=[]
    faq_ans=[]
  
    for database in post.quick_answers:
        quick_answers.append(database.ans)
        quick_questions.append(database.ques)
    for database in post.index:
        index.append(database.topic)  
    for database in post.faq:
        faq_q.append(database.faq_q)
        faq_ans.append(database.faq_ans)
    
    var=Variables.query.filter_by(id=1).first()
    var.url=post.url
    var.title=post.meta_title
    var.cover_image=post.cover_img
    var.cover_image_description=post.img_description
    var.meta_keywords=post.meta_keywords
    var.type_=post.type
    var.thumbnail=post.thumbnail
    var.keyword=post.keyword
    var.heading=post.heading
    var.description=post.description
    var.quick_questions=str(quick_questions)
    var.quick_answers=str(quick_answers)
    var.index=str(index)
    var.faq_q=str(faq_q)
    var.faq_ans=str(faq_ans)
    var.article=post.article
    db.session.commit()
    print("-----------------------------")
    print(post.cover_img)    
    print(len(faq_q))
    print(len(faq_ans))
    json_for_texteditor={"id":id,"type":type}
    return render_template('edit_post.html',
                           text_editor_json=json.dumps(json_for_texteditor),
                           coverImg=post.cover_img,
                           metaKeywords=post.meta_keywords,
                           coverImgDescription=post.img_description,
                           title=post.meta_title,
                           url=post.url,
                           quickAnswersDb=post.quick_answers,
                           indexDb=post.index,
                           faqDb=post.faq,
                           totalType=json.dumps(post.type),
                           countQuickQuestions=json.dumps(len(quick_questions)),
                           countQuickAnswers=json.dumps(len(quick_answers)),
                           countFaq_q=json.dumps(len(faq_q)),
                           countFaq_ans=json.dumps(len(faq_ans)),
                           countIndex=json.dumps(len(index)),
                           type=type,
                           post_type=post_type,
                           keyword=post.keyword,
                           intend=intend,
                           heading=post.heading,
                           thumbnail=post.thumbnail,
                           description=post.description,
                           index=index,
                           quickQuestions=quick_questions,
                           quickAnswers=quick_answers,
                           faq_q=faq_q,
                           faq_ans=faq_ans,
                           id=id
                        )
    # todo: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Change the variablses in edit-post.html<<<<<<<<<<<<........
@app.route('/save_edited/<string:type>/<int:id>',methods=['GET','POST'])
@login_required
def save_edited(type,id):
    req=request.get_json()
    print(type,id)
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
      print("IN DRAFT=================")
      print(id,type)  
      post=Draft.query.filter_by(id=id).first()
      returnPath="/dashboard/draft"
      
    var=Variables.query.filter_by(id=1).first()
    var.article=req['article']
    post.article=var.article
    post.url=var.url
    post.title=var.title
    post.cover_img=var.cover_image
    post.meta_keywords=var.meta_keywords
    post.img_description=var.cover_image_description
    post.heading=var.heading
    post.description=var.description
    post.type=var.type_
    post.thumbnail=var.thumbnail
    post.keyword=var.keyword
    db.session.commit()
    
    
    if var.quick_answers or var.quick_questions:
        
      for ind in range(0,len(post.quick_answers)):
          try:
              post.quick_answers[ind].ans=eval(var.quick_answers)[ind]
          except IndexError:
              pass
          try:
              post.quick_answers[ind].ques=eval(var.quick_questions)[ind]
              
          except IndexError:
              pass
              
          db.session.commit()  
      if len(post.quick_answers)<len(eval(var.quick_answers)) or len(post.quick_answers)<len(eval(var.quick_questions)):
           for i in range(len(post.quick_answers),len(eval(var.quick_questions))):
             if type=='Ard':
                addedData=Quick_answers_arduino(ques=eval(var.quick_questions)[i],ans=eval(var.quick_answers)[i],post_name=post)
                 
             if type=='Basic':
                addedData=Quick_answers_basic(ques=eval(var.quick_questions)[i],ans=eval(var.quick_answers)[i],post_name=post)
                 
             if type=='Iot':
                addedData=Quick_answers_iot(ques=eval(var.quick_questions)[i],ans=eval(var.quick_answers)[i],post_name=post)
                 
             if type=='Other':
                addedData=Quick_answers_other(ques=eval(var.quick_questions)[i],ans=eval(var.quick_answers)[i],post_name=post)
                 
             if type=='draft':
                 addedData=Quick_answers_draft(ques=eval(var.quick_questions)[i],ans=eval(var.quick_answers)[i],post_name=post)
                 
             db.session.add(addedData)   
             db.session.commit()   
    
    if var.faq_ans or var.faq_q:
        
      for ind in range(0,len(post.faq)):
          try:
              post.faq[ind].faq_ans=eval(var.faq_ans)[ind]
          except IndexError:
              pass
          try:
              post.faq[ind].faq_q=eval(var.faq_q)[ind]
              
          except IndexError:
              pass
              
          db.session.commit()
            
      if len(post.faq)<len(eval(var.faq_q)) or len(post.faq)<len(eval(var.faq_ans)):
           for i in range(len(post.faq),len(eval(var.faq_q))):
            if type=='Ard':
                addedData=Faq_arduino(faq_q=eval(var.faq_q)[i],faq_ans=eval(var.faq_ans)[i],post_name=post)
                 
            if type=='Basic':
                addedData=Faq_basic(faq_q=eval(var.faq_q)[i],faq_ans=eval(var.faq_ans)[i],post_name=post)
                 
            if type=='Iot':
                addedData=Faq_iot(faq_q=eval(var.faq_q)[i],faq_ans=eval(var.faq_ans)[i],post_name=post)
                 
            if type=='Other':
                addedData=Faq_other(faq_q=eval(var.faq_q)[i],faq_ans=eval(var.faq_ans)[i],post_name=post)
                 
            if type=='draft':
                 addedData=Faq_draft(faq_q=eval(var.faq_q)[i],faq_ans=eval(var.faq_ans)[i],post_name=post)
            db.session.add(addedData)   
            db.session.commit()   
 

   
 
    if var.index:
      for ind in range(0,len(post.index)):
          try:
            post.index[ind].topic=eval(var.index)[ind]
          except IndexError:
              pass
          db.session.commit()   
      if len(post.index)<len(eval(var.index)):
         for i in range(len(post.index),len(eval(var.index))):
             if type=='Ard':
                addedData=Index_arduino(topic=eval(var.index)[i],post_name=post)
                 
             if type=='Basic':
                addedData=Index_basic(topic=eval(var.index)[i],post_name=post)
                 
             if type=='Iot':
                addedData=Index_iot(topic=eval(var.index)[i],post_name=post)
                 
             if type=='Other':
                addedData=Index_other(topic=eval(var.index)[i],post_name=post)
                 
             if type=='draft':
                 addedData=Index_draft(topic=eval(var.index)[i],post_name=post)
             db.session.add(addedData)   
             db.session.commit()    



    response=make_response(jsonify(returnPath),200)      
    return response
@app.route('/delete_item', methods=['POST','GET'])
@login_required
def delete_item():
       req=request.get_json()
       post_type=req['post_type']
    #    print(req['post_type']) 
       if post_type=="Ard":
        
          if req['type']=='index':
              print(req['id'])
              delete=Index_arduino.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='quickAnswers':
              delete=Quick_answers_arduino.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='faq':
              delete=Faq_arduino.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          
       if post_type=="Basic":
           
          if req['type']=='index':
              print(req['id'])
              delete=Index_basic.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='quickAnswers':
              delete=Quick_answers_basic.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()

          if req['type']=='faq':
              delete=Faq_basic.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          
       if post_type=="Iot":
           
          if req['type']=='index':
              delete=Index_iot.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='quickAnswers':
              delete=Quick_answers_iot.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='faq':
              delete=Faq_iot.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          
       if post_type=="Other":
           
          if req['type']=='index':
              delete=Index_other.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='quickAnswers':
              delete=Quick_answers_other.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='faq':
              delete=Faq_other.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
               
       if post_type=="draft":
          print(req['type'])  
          if req['type']=='index':
              delete=Index_draft.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()
          if req['type']=='quickAnswers':
              delete=Quick_answers_draft.query.filter_by(id=req['id']).first()
              db.session.delete(delete)
              db.session.commit()

          if req['type']=='faq':
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
                               description=draft.description,
                               article=draft.article
                              )

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
                             article=draft.article
                           
                           )
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
                           article=draft.article
                           )
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
                      article=draft.article
                      )
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
 # todo : ------------------------------------------------------------------------------------
    print(id)

    deleteIndex=Index_draft.query.filter_by(draft_id=draft_id).all()
    deleteFaq=Faq_draft.query.filter_by(draft_id=draft_id).all()
    deleteQuickanswers=Quick_answers_draft.query.filter_by(draft_id=draft_id).all()
     
    print("+++++++++++++",draft_id)
 
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
@app.route('/test-login')
@login_required
def test_login():
    return "SUCCESFULLY LOGGED IN"
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
  app.run(host='127.0.0.1', debug=True)

