console.log("message JS is attached");
var mail = document.getElementById('message-mail')
var message = document.getElementById("message-text")
var nameMessage = document.getElementById('message-name')
var alertMessage = document.getElementById("submitted")
var messageBtnSpinner = document.getElementById('msg_btn_spinner')
var messageRegExp = /[a-zA-Z0-9\s!.,?\-+=\$()\{\}\[\]]{20,500}$/gy;
var NameRegExp = new RegExp("[a-zA-Z]{3,20}", "g");
var emailRegExp = new RegExp(
    "(^[A-Z0-9._%+-]+)(@[A-Z0-9.-]+)(.[A-Z]{2,})",
    "gi"
);
var resultName = false;
var resultEMail = false;
var resultMessage = false;


function validateName(id, button) {
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
var emailMessage = false
var txtMessage = false

function validateEmail(id, button) {
    emailRegExp.lastIndex = 0;

    resultEMail = emailRegExp.test(document.getElementById(`${id}`).value);



    if (resultEMail == true) {
        document.getElementById(`${id}`).style.border = "solid 2px green"
        if (id == "footerSubscriberInp") {
            document.getElementById(`${button}`).disabled = false

        } else {

            emailMessage = true
        }


    }
    if (resultEMail == false) {
        document.getElementById(`${id}`).style.border = "solid 1px red"
        if (id == "footerSubscriberInp") {
            document.getElementById(`${button}`).disabled = true

        } else {

            emailMessage = false
        }

    }
    if (emailMessage && txtMessage) {
        document.getElementById(`${button}`).disabled = false

    }

}

function validateMessage(id, button) {
    messageRegExp.lastIndex = 0;
    console.log(resultMessage);

    resultMessage = messageRegExp.test(document.getElementById(`${id}`).value);

    if (resultMessage == true) {
        document.getElementById(`${id}`).style.border = "solid 2px green"
        txtMessage = true


    }
    if (resultMessage == false) {
        document.getElementById(`${id}`).style.border = "solid 1px red"
        txtMessage = false


    }
    console.log(resultMessage);
    if (emailMessage && txtMessage) {
        document.getElementById(`${button}`).disabled = false

    }
}

function sendMessage() {
    console.log("in function");
    var mailValue = mail.value;
    var messageTxt = message.value;
    console.log(mailValue, messageTxt);
    var url = `${window.origin}/message`

    var entry = {
        e_mail: mailValue,
        message: messageTxt,


    }
    var params = {
        method: 'POST',
        body: JSON.stringify(entry),
        cache: 'no-cache',
        headers: new Headers({
            "content-type": "application/json"
        })
    }
    console.log(resultEMail, resultMessage)
    if (resultMessage == true && resultEMail == true) {
        messageBtnSpinner.style.display = "block"
        document.getElementById('send').style.display = "none";
        fetch(url, params).then(response => {
            if (response.status == 200) {
                console.log("succesfully_posted")
                alertMessage.style.display = "block";
                messageBtnSpinner.style.display = "none"
                document.getElementById('send').style.display = "";
            } else {
                console.log("eroor 404, data not posted")
                alert("ERROR: PLEASE TRY AGAIN, maybe Email already exist")
                messageBtnSpinner.style.display = "none"
                document.getElementById('send').style.display = "";
            }
            response.json().then(data => {

                console.log(data)
                    //   var heading1=document.getElementById(`${code}head1`)


                //  container.style.display=""   
            })
        })
    } else {
        alert("please fill the form correctly ,username must-be 3 to 20 character long and only alphabets are allowed and Email should be valid and  20 to 500 characters are allowed in message field ThankYou!!")
    }
}

function subscribeFooter(email) {


    var url = `${window.origin}/subscribe`

    var entry = {
        e_mail: email,


    }
    var params = {
        method: 'POST',
        body: JSON.stringify(entry),
        cache: 'no-cache',
        headers: new Headers({
            "content-type": "application/json"
        })
    }
    if (resultName == true && resultEMail == true) {
        document.getElementById('subscribe_btn_spinner').style.display = "block";
        document.getElementById('subscribe').style.display = "none";
        fetch(url, params).then(response => {

            if (response.status == 200) {
                console.log("succesfully_posted")
                document.getElementById('subscribe_btn_spinner').style.display = "none";
                document.getElementById('subscribe').style.display = "block";

                alertMessageS.style.display = "block";
            } else {
                console.log("eroor 404, data not posted")
                document.getElementById('subscribe_btn_spinner').style.display = "none";
                document.getElementById('subscribe').style.display = "block";

                alert("NOT SENT: PLEASE TRY AGAIn")
            }
            response.json().then(data => {

                console.log(data)

            })
        })
    } else {
        alert("INTERNAL-SERVOR-ERROR OCCURED, maybe you are already subscribed, ThankYou!")
    }
}