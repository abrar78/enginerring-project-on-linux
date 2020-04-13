from createDb import *
from flask import jsonify,make_response,request
from flask_mail import Mail


app.config.update(
   
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params["gmail-user"],
    MAIL_PASSWORD =  params["gmail-password"]
    );
mail=Mail(app);
@app.route('/')
def index():
     arduino=Arduinoproject_posts.query.paginate(per_page=4,page=1,error_out=True)
     basic=Basicproject_posts.query.paginate(per_page=4,page=1,error_out=True)
     iot=Iotproject_posts.query.paginate(per_page=4,page=1,error_out=True)
     other=Other_posts.query.paginate(per_page=4,page=1,error_out=True)
     return render_template('index.html',arduino_project=arduino,basic_project=basic,iot_project=iot,other_project=other)

@app.route('/load_more_posts')
def load_more_posts():
    req=request.get_json();
    print(req);
    if req['code']=='Ard':
         content={'heading':{}, 'readingTime':{},'description':{}}
         arduino=Arduinoproject_posts.query.paginate(per_page=4+req['pageArd'], page=1,error_out=True)
         for db,i in zip(arduino.items,range(1,5)):
             content['heading'][str(i)]=db.heading
             content['readingTime'][str(i)]=db.reading_time
             content['description'][str(i)]=db.description
             
         response=make_response(jsonify(content),200)
         return response

@app.route('/paginate', methods = ['GET', 'POST'])
def paginate():
    req=request.get_json();
    print(req)
   
    if req['code']=='Ard':
          
        if req['jump_page']==True:
         content={'heading':{}, 'readingTime':{},'description':{},'id':{}}
         current_page=int(req['page_no'])
         arduino=Arduinoproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
         for arduino_db,i in zip(arduino.items,range(1,5)):
             content['heading'][str(i)]=arduino_db.heading
             content['readingTime'][str(i)]=arduino_db.reading_time
             content['description'][str(i)]=arduino_db.description
             content['id'][str(i)]="/Read_more_arduino_post/"+str(arduino_db.id)
         print(req['page_no'])    
         response=make_response(jsonify(content),200)
         return response
     
        if req['next']==True or req['prev']==True:
          content={'heading':{}, 'readingTime':{},'description':{},'id':{}}  
          arduino=Arduinoproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
          for arduino_db,i in zip(arduino.items,range(1,5)):
             content['heading'][str(i)]=arduino_db.heading
             content['readingTime'][str(i)]=arduino_db.reading_time
             content['description'][str(i)]=arduino_db.description
             content['id'][str(i)]="/Read_more_arduino_post/"+str(arduino_db.id)
             
             
    if req['code']=='Basic':
          
        if req['jump_page']==True:
         content={'heading':{}, 'readingTime':{},'description':{},'id':{}}
         current_page=int(req['page_no'])
         basic=Basicproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
         for basic_db,i in zip(basic.items,range(1,5)):
             content['heading'][str(i)]=basic_db.heading
             content['readingTime'][str(i)]=basic_db.reading_time
             content['description'][str(i)]=basic_db.description
             content['id'][str(i)]="/Read_more_basic/"+str(basic_db.id)
         print(req['page_no'])    
         response=make_response(jsonify(content),200)
         return response
     
        if req['next']==True or req['prev']==True:
          content={'heading':{}, 'readingTime':{},'description':{},'id':{}}  
          basic=Basicproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
          for basic_db,i in zip(basic.items,range(1,5)):
             content['heading'][str(i)]=basic_db.heading
             content['readingTime'][str(i)]=basic_db.reading_time
             content['description'][str(i)]=basic_db.description
             content['id'][str(i)]='/Read_more_basic/'+str(basic_db.id)
             
    if req['code']=='Iot':
         if req['jump_page']==True:
             content={'heading':{}, 'readingTime':{},'description':{},'id':{}}
             current_page=int(req['page_no'])
             iot=Iotproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
             for iot_db,i in zip(iot.items,range(1,5)):
                content['heading'][str(i)]=iot_db.heading
                content['readingTime'][str(i)]=iot_db.reading_time
                content['description'][str(i)]=iot_db.description
                content['id'][str(i)]='/Read_more_iot/'+str(iot_db.id)
             print(req['page_no'])    
             response=make_response(jsonify(content),200)
             return response
     
         if req['next']==True or req['prev']==True:
            content={'heading':{}, 'readingTime':{},'description':{},'id':{}}  
            iot=Iotproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
            for iot_db,i in zip(iot.items,range(1,5)):
                content['heading'][str(i)]=iot_db.heading
                content['readingTime'][str(i)]=iot_db.reading_time
                content['description'][str(i)]=iot_db.description
                content['id'][str(i)]='/Read_more_iot/'+str(iot_db.id)
                
                
    if req['code']=='Other':
         if req['jump_page']==True:
             content={'heading':{}, 'readingTime':{},'description':{},'id':{}}
             current_page=int(req['page_no'])
             other=Other_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
             for other_db,i in zip(other.items,range(1,5)):
                content['heading'][str(i)]=other_db.heading
                content['readingTime'][str(i)]=other_db.reading_time
                content['description'][str(i)]=other_db.description
                content['id'][str(i)]='/Read_more_other/'+str(other_db.id)
             print(req['page_no'])    
             response=make_response(jsonify(content),200)
             return response
     
         if req['next']==True or req['prev']==True:
            content={'heading':{}, 'readingTime':{},'description':{},'id':{}}  
            other=Other_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
            for other_db,i in zip(other.items,range(1,5)):
                content['heading'][str(i)]=other_db.heading
                content['readingTime'][str(i)]=other_db.reading_time
                content['description'][str(i)]=other_db.description
                content['id'][str(i)]='/Read_more_other/'+str(other_db.id)
                
    response=make_response(jsonify(content),200)
    return response 
    # return response
    
    
@app.route('/Read_more_arduino_post/<int:num>')
def arduinoRead(num):
    arduino_post=Arduinoproject_posts.query.filter_by(id=num).first()
    return render_template('readMoreArduino.html', arduino_post_db=arduino_post)
@app.route('/Read_more_basic/<int:num>')
def basicRead(num):
    basic_post=Basicproject_posts.query.filter_by(id=num).first()
    return render_template('readMoreBasic.html', basic_post_db=basic_post)
@app.route('/Read_more_iot/<int:num>')
def iotRead(num):
    iot_post=Iotproject_posts.query.filter_by(id=num).first()
    return render_template('readMoreIot.html', iot_post_db=iot_post)
@app.route('/Read_more_other/<int:num>')
def otherRead(num):
    other_post=Other_posts.query.filter_by(id=num).first()
    return render_template('readMoreOther.html', other_post_db=other_post)

@app.route('/templates/advertiseWithUs.html')
def advertise():
    return render_template('advertiseWithUs.html')


@app.route('/form',methods = ['GET', 'POST'])
def form_submit():
    req=request.get_json();
    print(req)
    content={"response":"Thankyou"}
    response=make_response(jsonify(content))
    return response

@app.route('/message',methods = ['GET', 'POST'])
def message():
    req=request.get_json();
    print(req)
    message=Messages(send_by=req['sender_name'],email=req['e_mail'],message=req['message'])
    db.session.add(message)
    db.session.commit()
    mail.send_message('new message from blog'+'  name:'+req['sender_name'],
                      sender=req['e_mail'],
                      recipients=[params("recipent_mail")],
                      body=req['message'])
    content={"response":"Thankyou"}
    response=make_response(jsonify(content))
    return response
    
@app.route('/dashboard',methods = ['GET', 'POST'])
def dashboard():
    
    return render_template('dashboard.html')
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 