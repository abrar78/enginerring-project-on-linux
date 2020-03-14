console.log("succesfully attached");

function hower(i) {
  document.getElementById(i).style.color = "white";
}

function howerLeave(i) {
  document.getElementById(i).style.color = "#F2C36B";
}
// !Form valisdatiion  code for input form for adverisisng

// *all texrt input areas taken below
var firstName = document.getElementById("firstName");
var lastName = document.getElementById("lastName");
var eMail = document.getElementById("exampleInputEmail1");
var txtArea = document.getElementById("exampleFormControlTextarea1");
var tellSomething = document.getElementById("tellSomething");
var chooseFile = document.getElementById("File")
var pleaseSpecifyDiv = document.getElementById("pleaseSpecifyInputDiv")
// *all radio inputs
var onlyText = document.getElementById("onlyText");
var withImage = document.getElementById("withImage");
var other = document.getElementById("other");


var noImage = document.getElementById("noImage");
var noImageOpt1 = document.getElementById("optForImages")
var noImageOpt2 = document.getElementById("opt2ForImages")
var optLabel = document.getElementById("optLabel")
var dontHave=document.getElementById("dontHave")
var haveImage=document.getElementById("have")
var haveImageInp=document.getElementById("haveImageInp")
// todo make one for you?
var yesMakeInp = document.getElementById("yes");
var dontMakeInp = document.getElementById("no");

// ? checking for the type of advertisement
withImage.addEventListener("click", () => {
 
  if (withImage.checked == true) {
    console.log("with image is sielsected");
    chooseFile.style.display = "";
    pleaseSpecifyDiv.style.display = "none";
    noImage.style.display = "";
    noImageOpt1.style.display = "none";
    noImageOpt2.style.display = "nome";
    optLabel.style.display = "none";
    haveImage.style.display = "none";

  }
});

dontHave.addEventListener("click", () => {
  console.log("clcicked666")

 
  if (dontHave.checked == true) {
    chooseFile.style.display = "none";
    noImageOpt1.style.display = "";
    noImageOpt2.style.display = "";
    optLabel.style.display = "";
    haveImage.style.display = "";
  } else {
    noImageOpt1.style.display = "none";
    noImageOpt2.style.display = "none";
    optLabel.style.display = "none";
    chooseFile.style.display = "";
  }
})
haveImageInp.addEventListener("click", ()=>{
  if (haveImageInp.checked==true) {
    chooseFile.style.display = "";
    haveImage.style.display = "none";
    noImageOpt1.style.display = "none";
    noImageOpt2.style.display = "none";
    optLabel.style.display = "none";  
  }
})
other.addEventListener("click", () => {
  if (other.checked == true) {
    console.log("other is sielsected");
    chooseFile.style.display = "none";
    pleaseSpecifyDiv.style.display = "";
    haveImage.style.display = "none";
    noImageOpt1.style.display = "none";
    noImageOpt2.style.display = "none";
    optLabel.style.display = "none";  
  }
});
onlyText.addEventListener("click", () => {
  if (onlyText.checked == true) {
    console.log("only texrt is sielsected");
    chooseFile.style.display = "none";
    pleaseSpecifyDiv.style.display = "none";
    noImage.style.display = "none";
    noImageOpt1.style.display = "none";
    noImageOpt2.style.display = "none";
    optLabel.style.display = "none";
  }
});
if (onlyText.checked == true) {
  console.log("only txt");
  chooseFile.style.display = "none";
  pleaseSpecifyDiv.style.display = "none";
  noImage.style.display = "none";
  noImageOpt1.style.display = "none";
  noImageOpt2.style.display = "none";
  optLabel.style.display = "none";
}
if (withImage.checked == true) {
  console.log("withImage");
}
if (other.checked == true) {
  console.log("other");
}
