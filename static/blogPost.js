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
document.getElementById('dropDownMob').style.display = "none"
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
projMob.onclick = function() {
    var list = document.getElementById("dropDownMob")
    if (flipOut) {
        list.classList.remove("slideOutLeft")
        list.classList.add("slideInLeft")



    }
    if (list.style.display == "none" || flipOut) {
        list.style.display = "flex"
        flipOut = false;

    } else {

        list.classList.remove("slideInLeft")
        list.classList.add("slideOutLeft")
        flipOut = true;
    }



}
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