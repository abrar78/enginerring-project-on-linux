from createDb import *
from sqlalchemy import or_
import math
from flask import jsonify,make_response,request,redirect,session
import os
import datetime
from werkzeug.utils import secure_filename
from flask_mail import Mail
from flask_login import LoginManager
from jinja2 import Undefined
JINJA2_ENVIRONMENT_OPTIONS = { 'undefined' : Undefined }
app.config['UPLOAD_FOLDER']={'upload':params["upload_location"],
                             'cover_image':params["upload_location_coverImg"] }

global thumbnail
thumbnail="0"
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
def index():

     arduino=Arduinoproject_posts.query.paginate(per_page=4,page=1,error_out=True)
     basic=Basicproject_posts.query.paginate(per_page=4,page=1,error_out=True)
     iot=Iotproject_posts.query.paginate(per_page=4,page=1,error_out=True)
     other=Other_posts.query.paginate(per_page=4,page=1,error_out=True)
     return render_template('index.html',arduino_project=arduino,basic_project=basic,iot_project=iot,other_project=other)

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
             content['id'][str(i)]="/Read_more_Ard/"+str(arduino_db.id)
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
             content['id'][str(i)]="/Read_more_Ard/"+str(arduino_db.id)


    if req['code']=='Basic':

        if req['jump_page']==True:
         content={'heading':{}, 'thumbnail':{},'description':{},'id':{}}
         current_page=int(req['page_no'])
         basic=Basicproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
         for basic_db,i in zip(basic.items,range(1,5)):
             content['heading'][str(i)]=basic_db.heading
             content['thumbnail'][str(i)]=basic_db.thumbnail
             content['description'][str(i)]=basic_db.description
             content['id'][str(i)]="/Read_more_Basic/"+str(basic_db.id)
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
             content['id'][str(i)]='/Read_more_Basic/'+str(basic_db.id)

    if req['code']=='Iot':
         if req['jump_page']==True:
             content={'heading':{}, 'thumbnail':{},'description':{},'id':{}}
             current_page=int(req['page_no'])
             iot=Iotproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
             for iot_db,i in zip(iot.items,range(1,5)):
                content['heading'][str(i)]=iot_db.heading
                content['thumbnail'][str(i)]=iot_db.thumbnail
                content['description'][str(i)]=iot_db.description
                content['id'][str(i)]='/Read_more_Iot/'+str(iot_db.id)
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
                content['id'][str(i)]='/Read_more_Iot/'+str(iot_db.id)


    if req['code']=='Other':
         if req['jump_page']==True:
             content={'heading':{}, 'thumbnail':{},'description':{},'id':{}}
             current_page=int(req['page_no'])
             other=Other_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
             for other_db,i in zip(other.items,range(1,5)):
                content['heading'][str(i)]=other_db.heading
                content['thumbnail'][str(i)]=other_db.thumbnail
                content['description'][str(i)]=other_db.description
                content['id'][str(i)]='/Read_more_Other/'+str(other_db.id)
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
                content['id'][str(i)]='/Read_more_Other/'+str(other_db.id)

    response=make_response(jsonify(content),200)
    return response
    # return response


@app.route('/Read_more_Ard/<int:num>')
def arduinoRead(num):
    arduino_post=Arduinoproject_posts.query.filter_by(id=num).first()
    search_value=arduino_post.keyword
    search="%{0}%".format(search_value)
    print(search)
    related=Arduinoproject_posts.query.filter(or_(Arduinoproject_posts.description.like(search), Arduinoproject_posts.heading.like(search))).all()
    return render_template('readMoreArduino.html', arduino_post_db=arduino_post,related_post=related[0:4])
@app.route('/Read_more_Basic/<int:num>')
def basicRead(num):
    basic_post=Basicproject_posts.query.filter_by(id=num).first()
    search_value=basic_post.keyword
    search="%{0}%".format(search_value)
    related=Basicproject_posts.query.filter(or_(Basicproject_posts.description.like(search), Basicproject_posts.heading.like(search))).all()
    return render_template('readMoreBasic.html', basic_post_db=basic_post,related_post=related[0:4])
@app.route('/Read_more_Iot/<int:num>')
def iotRead(num):
    iot_post=Iotproject_posts.query.filter_by(id=num).first()
    search_value=iot_post.keyword
    search="%{0}%".format(search_value)
    related=Iotproject_posts.query.filter(or_(Iotproject_posts.description.like(search), Iotproject_posts.heading.like(search))).all()
    return render_template('readMoreIot.html', iot_post_db=iot_post,related_post=related[0:4])
@app.route('/Read_more_Other/<int:num>')
def otherRead(num):
    other_post=Other_posts.query.filter_by(id=num).first()
    search_value=other_post.keyword
    search="%{0}%".format(search_value)
    related=Other_posts.query.filter(or_(Other_posts.description.like(search), Other_posts.heading.like(search))).all()

    return render_template('readMoreOther.html', other_post_db=other_post,related_post=related[0:4])

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
@app.route('/dashboard_upload',methods=['GET','POST'])
@login_required
def dashboard_upload():
       f=request.files['file'];
       file_name=f.filename
       file_name=file_name.replace(" ","_")
       thumbnail=file_name
       print(thumbnail)
       f.save(os.path.join(app.config['UPLOAD_FOLDER']['cover_image'],secure_filename(f.filename)))
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
        db.session.delete(delete)
        db.session.commit()
        return redirect('/all_post/1') 
    if type=='Basic':
        delete=Basicproject_posts.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect('/dashboard_basic/1') 
        
    if type=='Iot':
        delete=Iotproject_posts.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect('/dashboard_iot/1') 
    if type=='Other':
        delete=Other_posts.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect('/dashboard_other/1') 
    
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
 return render_template("dashboard.html") 

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
        
      
    return render_template('dashboard_search.html')
@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(seconds=200)
    session.modified = True
if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.run(host='127.0.0.1', port=8000, debug=True)
