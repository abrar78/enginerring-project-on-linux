console.log("message JS is attached");
var mail=document.getElementById('message-mail')
var message=document.getElementById("message-text")
var nameMessage=document.getElementById('message-name')
console.log(nameMessage)
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

    fetch(url,params).then(response=>{
        if(response.status==200){
            console.log("succesfully_posted")
            alertMessage.style.display="block";
        }
        else{
            console.log("eroor 404, data not posted")
            alert("NOT SENT: PLEASE TRY AGAIn")
        }
        response.json().then(data=>{
           
            console.log(data)
        //   var heading1=document.getElementById(`${code}head1`)
          
          
        //  container.style.display=""   
        })
})
}