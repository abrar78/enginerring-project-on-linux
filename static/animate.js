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