console.log("Blog post JAVA script file connected is succesfullty")

function myFunction() {
    w = window.outerWidth;
    h = window.outerHeight;
    var txt = "Window size: width=" + w + ", height=" + h;
    if (w > 1000) {
        location.reload()
    }
}

function hower(i) {

    document.getElementById(i).style.color = 'white'

}

function test() {
    console.log("success")
}

function howerLeave(i) {

    document.getElementById(i).style.color = '#F2C36B'
    let type = i.slice(0, 3)
    if (type == "nav") {
        document.getElementById(i).style.color = 'black'

    }
}

var projDesktop = document.getElementById("projDesktop")
var projMob = document.getElementById("projMob")
document.getElementById('dropDownDesktop').style.display = "none"

var flipOut = false;


projDesktop.onclick = function() {
        var list = document.getElementById("dropDownDesktop")
        if (flipOut) {
            list.classList.remove("flipOutX")
            list.classList.add("flipInX")



        }
        if (list.style.display == "none" || flipOut) {
            list.style.display = "flex"
            flipOut = false;

        } else {

            list.classList.remove("flipInX")
            list.classList.add("flipOutX")
            flipOut = true;
        }



    }
    // projMob.onclick = function() {
    //     var list = document.getElementById("dropDownMob")
    //     if (flipOut) {
    //         list.classList.remove("slideOutLeft")
    //         list.classList.add("slideInLeft")



//     }
//     if (list.style.display == "none" || flipOut) {
//         list.style.display = "flex"
//         flipOut = false;

//     } else {

//         list.classList.remove("slideInLeft")
//         list.classList.add("slideOutLeft")
//         flipOut = true;
//     }



// }
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}
var search = document.getElementById("search")

var closeSearch = document.getElementById("closeSearch");
var lock = true;
search.onclick = function() {
    mobileSearchBar.style.display = "flex";
    mobileNav.style.display = "none";
    lock = false;
    searchBarOpen = true

}


var burger = document.getElementById("burger")
var slider = document.getElementById("slider")
var closeSlider = document.getElementById("closeSlider")
var lockSlider = true
burger.onclick = function() {
    slider.style.display = "flex";
    slider.classList.add("slideInLeft")
    slider.classList.remove("slideOutLeft")
        // slider.classList.remove="slideOutLeft"
    lockSlider = false;
}
closeSearch.onclick = function() {
    console.log("clicked parallex function");
    if (lock == false) {

        mobileSearchBar.style.display = "none";
        mobileNav.style.display = "flex";
        searchBarOpen = false
        lock = true;
    }
    if (lockSlider == false) {
        slider.style.display = "none";
        lockSlider = true;
    }
}
closeSlider.onclick = function() {
    console.log("clicked close");
    slider.classList.remove("slideInLeft")
    slider.classList.add("slideOutLeft")

}

// ! Message .js file


console.log("message JS is attached");
var mail = document.getElementById('footerMessageEmailInput')
var message = document.getElementById("footerMessageInput")
var nameMessage = document.getElementById('message-name')
var alertMessage = document.getElementById("submitted")
var messageBtnSpinner = document.getElementById('message_btn_spinner')
var alertMessageS = document.getElementById('messageS')
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
    resultMessage = messageRegExp.test(document.getElementById(`${id}`).value);

    if (resultMessage == true) {
        document.getElementById(`${id}`).style.border = "solid 2px green"
        txtMessage = true


    }
    if (resultMessage == false) {
        document.getElementById(`${id}`).style.border = "solid 1px red"
        txtMessage = false


    }

    if (emailMessage && txtMessage) {
        document.getElementById(`${button}`).disabled = false

    }
}

function sendMessage() {
    console.log("in function");
    var mailValue = mail.value;
    var messageTxt = message.value;
    var url = `${window.origin}/message`

    var entry = {
        e_mail: mailValue,
        message: messageTxt


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

                messageBtnSpinner.style.display = "none"
                window.location.replace('#popup2');
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
        footer: true


    }
    var params = {
        method: 'POST',
        body: JSON.stringify(entry),
        cache: 'no-cache',
        headers: new Headers({
            "content-type": "application/json"
        })
    }
    if (resultEMail == true) {
        document.getElementById('subscribe_btn_spinner').style.display = "block";
        document.getElementById('subscribe').style.display = "none";
        fetch(url, params).then(response => {

            if (response.status == 200) {
                console.log("succesfully_posted")
                document.getElementById('subscribe_btn_spinner').style.display = "none";
                document.getElementById('subscribe').style.display = "block";
                window.location.replace('#popup1');

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