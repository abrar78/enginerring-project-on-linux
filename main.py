from createDb import *
from flask import jsonify,make_response,request
import jinja2




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
         content={'heading':{}, 'readingTime':{},'description':{}}
         current_page=int(req['page_no'])
         arduino=Arduinoproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
         for arduino_db,i in zip(arduino.items,range(1,5)):
             content['heading'][str(i)]=arduino_db.heading
             content['readingTime'][str(i)]=arduino_db.reading_time
             content['description'][str(i)]=arduino_db.description
         print(req['page_no'])    
         response=make_response(jsonify(content),200)
         return response
     
        if req['next']==True or req['prev']==True:
          content={'heading':{}, 'readingTime':{},'description':{}}  
          arduino=Arduinoproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
          for arduino_db,i in zip(arduino.items,range(1,5)):
             content['heading'][str(i)]=arduino_db.heading
             content['readingTime'][str(i)]=arduino_db.reading_time
             content['description'][str(i)]=arduino_db.description
             
    if req['code']=='Basic':
          
        if req['jump_page']==True:
         content={'heading':{}, 'readingTime':{},'description':{}}
         current_page=int(req['page_no'])
         basic=Basicproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
         for basic_db,i in zip(basic.items,range(1,5)):
             content['heading'][str(i)]=basic_db.heading
             content['readingTime'][str(i)]=basic_db.reading_time
             content['description'][str(i)]=basic_db.description
         print(req['page_no'])    
         response=make_response(jsonify(content),200)
         return response
     
        if req['next']==True or req['prev']==True:
          content={'heading':{}, 'readingTime':{},'description':{}}  
          arduino=Arduinoproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
          for arduino_db,i in zip(arduino.items,range(1,5)):
             content['heading'][str(i)]=arduino_db.heading
             content['readingTime'][str(i)]=arduino_db.reading_time
             content['description'][str(i)]=arduino_db.description
             
    if req['code']=='Iot':
         if req['jump_page']==True:
             content={'heading':{}, 'readingTime':{},'description':{}}
             current_page=int(req['page_no'])
             iot=Iotproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
             for iot_db,i in zip(iot.items,range(1,5)):
                content['heading'][str(i)]=iot_db.heading
                content['readingTime'][str(i)]=iot_db.reading_time
                content['description'][str(i)]=iot_db.description
             print(req['page_no'])    
             response=make_response(jsonify(content),200)
             return response
     
         if req['next']==True or req['prev']==True:
            content={'heading':{}, 'readingTime':{},'description':{}}  
            iot=Iotproject_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
            for iot_db,i in zip(iot.items,range(1,5)):
                content['heading'][str(i)]=iot_db.heading
                content['readingTime'][str(i)]=iot_db.reading_time
                content['description'][str(i)]=iot_db.description
                
    if req['code']=='Other':
         if req['jump_page']==True:
             content={'heading':{}, 'readingTime':{},'description':{}}
             current_page=int(req['page_no'])
             other=Other_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
             for other_db,i in zip(other.items,range(1,5)):
                content['heading'][str(i)]=other_db.heading
                content['readingTime'][str(i)]=other_db.reading_time
                content['description'][str(i)]=other_db.description
             print(req['page_no'])    
             response=make_response(jsonify(content),200)
             return response
     
         if req['next']==True or req['prev']==True:
            content={'heading':{}, 'readingTime':{},'description':{}}  
            other=Other_posts.query.paginate(per_page=4,page=int(req['page_no']),error_out=True)
            for other_db,i in zip(other.items,range(1,5)):
                content['heading'][str(i)]=other_db.heading
                content['readingTime'][str(i)]=other_db.reading_time
                content['description'][str(i)]=other_db.description
    response=make_response(jsonify(content),200)
    return response 
    # return response

@app.route('/templates/advertiseWithUs.html')
def advertisse():
    return render_template('advertiseWithUs.html')

@app.route('/dashboard')
def dashboard():
    
    return render_template('dashboard.html')
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 