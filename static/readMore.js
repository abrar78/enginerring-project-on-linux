console.log("this JS custom for read more jS");

function hower(i) {

    document.getElementById(i).style.color = 'white'
}

function howerLeave(i) {
    console.log("j")
    document.getElementById(i).style.color = '#F2C36B'
}

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