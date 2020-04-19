console.log("message JS is attached");
var mail=document.getElementById('message-mail')
var message=document.getElementById("message-text")
var nameMessage=document.getElementById('message-name')
var alertMessage=document.getElementById("submitted")
var messageBtnSpinner=document.getElementById('msg_btn_spinner')
var messageRegExp = /[a-zA-Z0-9\s!.,?\-+=\$()\{\}\[\]]{20,500}$/gy;
var NameRegExp = new RegExp("[a-zA-Z]{3,20}", "g");
var emailRegExp = new RegExp(
    "(^[A-Z0-9._%+-]+)(@[A-Z0-9.-]+)(.[A-Z]{2,})",
    "gi"
  );
var resultName=false;
var resultEMail=false;
var resultMessage=false;


function validateName(id,button){
    NameRegExp.lastIndex = 0;

    resultName = NameRegExp.test(document.getElementById(`${id}`).value);
  
    if (resultName == true) {
      document.getElementById(`${id}`).classList.add("successInput");
      document.getElementById(`${id}`).classList.remove("wrongInput");
      
    }
    if (resultName == false) {
        document.getElementById(`${id}`).classList.add("wrongInput");
        document.getElementById(`${id}`).classList.remove("successInput");
        

    }

}
function validateEmail(id,button){
    emailRegExp.lastIndex = 0;

    resultEMail = emailRegExp.test(document.getElementById(`${id}`).value);
  
    if (resultEMail == true) {
      document.getElementById(`${id}`).classList.add("successInput");
      document.getElementById(`${id}`).classList.remove("wrongInput");
     

    }
    if (resultEMail == false) {
      document.getElementById(`${id}`).classList.add("wrongInput");
      document.getElementById(`${id}`).classList.remove("successInput");
     

    }
}
function validateMessage(id,button){
    messageRegExp.lastIndex = 0;
    console.log(resultMessage);

    resultMessage = messageRegExp.test(document.getElementById(`${id}`).value);
   
     if (resultMessage == true) {
       document.getElementById(`${id}`).classList.add("successInput");
       document.getElementById(`${id}`).classList.remove("wrongInput");
      
 
     }
     if (resultMessage == false) {
       document.getElementById(`${id}`).classList.add("wrongInput");
       document.getElementById(`${id}`).classList.remove("successInput");
       
     }
     console.log(resultMessage);
}
function sendMessage(){
    var senderName=nameMessage.value;
    console.log("in function");
    var mailValue=mail.value;
    var messageTxt=message.value;
    console.log(mailValue,messageTxt,senderName);
    var url=`${window.origin}/message`
    
    var entry={
        e_mail:mailValue,
        message:messageTxt,
        sender_name:senderName
        
    }
    var params={
        method:'POST',
        body:JSON.stringify(entry),
        cache:'no-cache',
        headers:new Headers({
            "content-type":"application/json"
        })
    }
    console.log(resultName,resultEMail,resultMessage)
    if(resultName==true && resultMessage==true && resultEMail==true){
        messageBtnSpinner.style.display="block"
        fetch(url,params).then(response=>{
            if(response.status==200){
                console.log("succesfully_posted")
                alertMessage.style.display="block";
                messageBtnSpinner.style.display="none"
            }
            else{
                console.log("eroor 404, data not posted")
                alert("ERROR: PLEASE TRY AGAIN, maybe Email already exist")
                messageBtnSpinner.style.display="none"
            }
        response.json().then(data=>{
            
            console.log(data)
            //   var heading1=document.getElementById(`${code}head1`)
            
            
            //  container.style.display=""   
        })
    })
}
else{
 alert("please fill the form correctly ,username must-be 3 to 20 character long and only alphabets are allowed and Email should be valid and  20 to 500 characters are allowed in message field ThankYou!!")
}
}