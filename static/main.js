console.log("this is main jS");
var mobileSearchBar = document.getElementById("mobileSearchBar");
var mobileNav = document.getElementById("mobileNav")
var searchBarOpen = false
var w;
var h;

function myFunction() {
    w = window.outerWidth;
    h = window.outerHeight;
    var txt = "Window size: width=" + w + ", height=" + h;
    if (w > 1000) {
        location.reload()
    }


    console.log(txt);
}
// if(searchBarOpen==true){
//     mobileNav.style.display="flex"

// }



var nav = document.getElementById("navBar")
console.log(nav)
var bottom = document.getElementById("bottom")



// Type writing effet 
var text = ["subscribe  for latest updates", "Blog for Engineers", "Blog for Electronic-Hobyist"]
var count = 0;
var index = 0;
var currentText = "";
var letter = "";
type();

function type() {
    if (count === text.length) {
        count = 0;
    }
    currentText = text[count];
    letter = currentText.slice(0, ++index);
    document.getElementById("typeWriter").textContent = letter;
    var timerID = setTimeout(type, 50)
    if (letter.length === currentText.length) {
        clearTimeout(timerID)
        setTimeout(backSpace, 2000)
    }

}

function backSpace() {

    letter = currentText.slice(0, currentText.length - 1);

    document.getElementById("typeWriter").textContent = letter;
    currentText = letter;
    var bsID = setTimeout(backSpace, 20)
    if (letter.length == 0) {
        count++;
        index = 0;
        clearTimeout(bsID);
        setTimeout(type, 0)
    }
}



// *responsive Java Script
var search = document.getElementById("search")

var closeSearch = document.getElementById("closeSearch");
var lock = true;
search.onclick = function() {
    console.log("seacrh clicked");
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
var nameD = document.getElementById('sName')
var emailD = document.getElementById('sEmail')
var subscribeBtnSpinner = document.getElementById('subs_btn_spinner')


var alertMessageS = document.getElementById('messageS')



var NameRegExp = new RegExp("[a-zA-Z]{3,20}", "g");
var emailRegExp = new RegExp(
    "(^[A-Z0-9._%+-]+)(@[A-Z0-9.-]+)(.[A-Z]{2,})",
    "gi"
);
var resultName = false;
var resultEMail = false;



function validateName(id, button) {
    NameRegExp.lastIndex = 0;

    resultName = NameRegExp.test(document.getElementById(`${id}`).value);

    let footer = false;
    if (id.slice(0, 6) == "footer") {
        footer = true;
    }


    if (resultName == true && !footer) {
        document.getElementById(`${id}`).classList.add("successInput");
        document.getElementById(`${id}`).classList.remove("wrongInput");

    }
    if (resultName == false && !footer) {
        document.getElementById(`${id}`).classList.add("wrongInput");
        document.getElementById(`${id}`).classList.remove("successInput");


    }

}
// ! ----- RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRREEEEEEEEEEEEEEEEEEEEEEMMMMMMMMMMMMMMMMMMMMMMMMMMOOOOOOOOOOOOOVEEEEE
function Temp(id, button) {
    emailRegExp.lastIndex = 0;

    resultEMail = emailRegExp.test(document.getElementById(`${id}`).value);
    footer = false;
    console.log(id.slice(0, 6))
    if (id.slice(0, 6) == "footer") {
        footer = true

    }
    if (resultEMail == true && !footer) {
        document.getElementById(`${id}`).classList.add("successInput");
        document.getElementById(`${id}`).classList.remove("wrongInput");


    }
    if (resultEMail == false && !footer) {
        document.getElementById(`${id}`).classList.add("wrongInput");
        document.getElementById(`${id}`).classList.remove("successInput");


    }
    if (resultEMail == true && footer) {
        document.getElementById(`${id}`).style.border = "solid 2px green"
        document.getElementById(`${button}`).disabled = false


    }
    if (resultEMail == false && footer) {
        document.getElementById(`${id}`).style.border = "solid 1px red"
        document.getElementById(`${button}`).disabled = true



    }

}



function subscribe(type) {

    email = emailD.value

    var url = `${window.origin}/subscribe`

    var entry = {
        e_mail: email


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
        subscribeBtnSpinner.style.display = "block";
        fetch(url, params).then(response => {

            if (response.status == 200) {
                console.log("succesfully_posted")
                subscribeBtnSpinner.style.display = "none";
                alertMessageS.style.display = "block";
            } else {
                console.log("eroor 404, data not posted")
                subscribeBtnSpinner.style.display = "none";
                alert("NOT SENT: PLEASE TRY AGAIn")
            }
            response.json().then(data => {

                console.log(data)
                    //   var heading1=document.getElementById(`${code}head1`)


                //  container.style.display=""   
            })
        })
    } else {
        alert("please Fill the form properly with valid user nmae(3-20 characters long and no special characters,or numbers allowed) and valid Email")
    }
}