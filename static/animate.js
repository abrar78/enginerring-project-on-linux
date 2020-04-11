console.log("this ios custom for read more jS");
var w;
var h;
function myFunction() {
    var w = window.outerWidth;
    var h = window.outerHeight;
    var txt = "Window size: width=" + w + ", height=" + h;
    console.log(txt);
  }
function hower(i) {

    document.getElementById(i).style.color = 'white'
}

function howerLeave(i) {
    console.log("j")
    document.getElementById(i).style.color = '#F2C36B'
}
var nav = document.getElementById("navBar")
console.log(nav)
var bottom=document.getElementById("bottom")
window.onscroll = function () {
    
    if (window.pageYOffset> 500) {
        console.log(window.pageXOffset);
        nav.style.background = "rgb(0, 0, 0,.8)"
    } else {
        nav.style.background = "rgb(1, 41, 65,0)"
    }
   
    }


// Type writing effet 
const text = ["Sign Up  for latest updates", "Blog for Engineers", "Blog for Electronic-Hobyist"]
let count = 0;
let index = 0;
let currentText = "";
let letter = "";
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


// pagination using function $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
// var totalPage = 3;
// var nextLatest = 1;
// var nextArd = 1;
// var nextBasic = 1;
// var nextIOT = 1;
// var nextOther = 1;

// function nextPage(tempId, next) {
//     let code = tempId.slice(4, tempId.length)
//     console.log(code, window[next])
//     let trackLatestPost = document.getElementsByClassName(code)
//     trackLatestPost[window[next]].classList.remove("active");
//     let prevBtn = document.getElementById("prev" + code);
//     prevBtn.classList.remove("disabled");
//     prevBtn.classList.add("active");
//     let currentDiv = document.getElementById(String(window[next] + code))
//     currentDiv.style.display = "none"
//     window[next]++;
//     let nextDiv = document.getElementById(String(window[next]) + code)
//     nextDiv.style.display = "";
//     trackLatestPost[window[next]].classList.add("active");
//     // adding Animations
//     nextDiv.classList.add("fadeInLeft")
//     nextDiv.classList.add("fadeInRight")
//     // taking care of last page
//     let nextBtn = document.getElementById(tempId);

//     if (window[next] == totalPage) {
//         nextBtn.classList.add("disabled")
//     }

// }


// function prevPage(tempId, next) {
//     let code = tempId.slice(4, tempId.length)
//     console.log(code, window[next])
//     let trackLatestPost = document.getElementsByClassName(code)
//     trackLatestPost[window[next]].classList.remove("active");
//     let nextBtn = document.getElementById("next" + code);
//     if (window[next] == totalPage) {
//         nextBtn.classList.remove("disabled")
//         nextBtn.classList.add("active");
//     }
//     let currentDiv = document.getElementById(String(window[next] + code))
//     currentDiv.style.display = "none"
//     window[next]--;
//     let prevDiv = document.getElementById(String(window[next]) + code)
//     prevDiv.style.display = "";
//     trackLatestPost[window[next]].classList.add("active");
//     // adding Animations
//     prevDiv.classList.remove("fadeInRight")
//     prevDiv.classList.add("fadeInLeft")
//     // taking care of  first page
//     let prevBtn = document.getElementById(tempId);

//     if (window[next] == 1) {
//         prevBtn.classList.add("disabled")
//     }
// }

// function customPage(tempId){
//    let code=tempId.slice(1,tempId.length-1)
//    let num=parseInt(tempId.slice(0,1));
//     console.log("code and num is:",code, num)
//     let currentDivNum=window['next'+code]
//     console.log("currentDiv Id is" +String(window['next'+code]) + code)
//     let currentDiv=document.getElementById(String(window['next'+code]) + code);
//     currentDiv.style.display="none";
//      var animation="";
//      var removeAnim="";
//      let currentButtonId=currentDiv.id+"_"
//      let currentButton=document.getElementById(currentButtonId);
//      currentButton.classList.remove("active")
//      let clickedButton=document.getElementById(tempId)
//      clickedButton.classList.add("active");

//     if (num>currentDivNum) {
//          animation="fadeInRight"
//          removeAnim="fadeInLeft"
//     }
//     else{
//         animation="fadeInLeft"
//         removeAnim="fadeInRight"
//     }

    // checking for end and first of page
//     let nextBtn=document.getElementById("next"+code)
//     let prevBtn=document.getElementById("prev"+code)
//     if (num==totalPage) {
//         console.log("at last ____ if")
//         prevBtn.classList.remove("disabled")
//         nextBtn.classList.add("disabled")
//     } if(num==1) {
//         console.log("at last ___ else")
//         prevBtn.classList.add("disabled")
//         nextBtn.classList.remove("disabled")
//         nextBtn.classList.add("active")
//     }
//     if(num>1&& num<totalPage){
//         prevBtn.classList.remove("disabled")
//         nextBtn.classList.remove("disabled")
//         prevBtn.classList.add("active")
//         nextBtn.classList.add("active")
//     }

    
//     window["next"+code]=num;
    
//     let requireDiv=document.getElementById(String(window['next'+code] )+ code);
//     console.log("require Div ID is" +requireDiv.id)
//     requireDiv.style.display="";
//     requireDiv.classList.remove(removeAnim);
//     requireDiv.classList.add(animation);

// }

// *responsive Java Script
var search=document.getElementById("search")
var mobileSearchBar=document.getElementById("mobileSearchBar");
var mobileNav=document.getElementById("mobileNav")
var closeSearch=document.getElementById("closeSearch");
var lock=true;
search.onclick= function(){
    console.log("seacrh clicked");
    mobileSearchBar.style.display="flex";
    mobileNav.style.display="none";
    lock=false;

}

var burger=document.getElementById("burger")
var slider=document.getElementById("slider")
var closeSlider=document.getElementById("closeSlider")
var lockSlider=true
burger.onclick=function(){
    slider.style.display="flex";
    slider.classList.add("slideInLeft")
    slider.classList.remove("slideOutLeft")
    // slider.classList.remove="slideOutLeft"
    lockSlider=false;
}
closeSearch.onclick=function(){
    console.log("clicked parallex function");
    if(lock==false) {
        
        mobileSearchBar.style.display="none";
        mobileNav.style.display="flex";
        lock=true;
    }
  if (lockSlider==false) {
      slider.style.display="none";
      lockSlider=true;
  }    
}
closeSlider.onclick=function(){
    console.log("clicked close");
    slider.classList.remove("slideInLeft")
    slider.classList.add("slideOutLeft")
    
}