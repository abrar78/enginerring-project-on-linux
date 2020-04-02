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
var chooseFile = document.getElementById("File");
var pleaseSpecifyDiv = document.getElementById("pleaseSpecifyInputDiv");
var specifyInput = document.getElementById("Specify");
// *all radio inputs
var onlyText = document.getElementById("onlyText");
var withImage = document.getElementById("withImage");
var other = document.getElementById("other");

var noImage = document.getElementById("noImage");
var noImageOpt1 = document.getElementById("optForImages");
var noImageOpt2 = document.getElementById("opt2ForImages");
var optLabel = document.getElementById("optLabel");
var dontHave = document.getElementById("dontHave");
var haveImage = document.getElementById("have");
var haveImageInp = document.getElementById("haveImageInp");
var dontHaveLabel = document.getElementById("dontHaveLab");
var yesMakeInp = document.getElementById("yes");
var dontMakeInp = document.getElementById("no");
var submit = document.getElementById("submit");
// ? checking for the type of advertisement
withImage.addEventListener("click", () => {
  dontHave.checked = false;
  if (withImage.checked == true) {
    console.log("with image is sielsected");
    chooseFile.style.display = "";
    pleaseSpecifyDiv.style.display = "none";
    noImage.style.display = "";
    dontHave.style.display = "";
    dontHaveLabel.style.display = "";
    noImageOpt1.style.display = "none";
    noImageOpt2.style.display = "nome";
    optLabel.style.display = "none";
    haveImage.style.display = "none";
  }
});

dontHave.addEventListener("click", () => {
  console.log("clcicked666");

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
});
haveImageInp.addEventListener("click", () => {
  if (haveImageInp.checked == true) {
    chooseFile.style.display = "";
    haveImage.style.display = "none";
    noImageOpt1.style.display = "none";
    noImageOpt2.style.display = "none";
    optLabel.style.display = "none";
  }
});
other.addEventListener("click", () => {
  if (other.checked == true) {
    console.log("other is sielsected");
    chooseFile.style.display = "none";
    pleaseSpecifyDiv.style.display = "";
    haveImage.style.display = "none";
    dontHave.style.display = "none";
    dontHaveLabel.style.display = "none";
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
// !end of form working---------------------------------------------------------------------------------------------------------------------------end of form working

// todo>>>>> regular expression form validation start from here

var firstNameRegExp = new RegExp("[a-zA-Z]{3,20}", "g");
var lastNameRegExp = new RegExp("[a-zA-Z]{3,20}", "g");
var emailRegExp = new RegExp(
  "(^[A-Z0-9._%+-]+)(@[A-Z0-9.-]+)(.[A-Z]{2,})",
  "gi"
);
// new RegExp("[a-zA-Z0-9]{30,}", "g");
var infoOfAdvertRegEx = /[a-zA-Z0-9\s]{50,200}$/gy;
var specificationOfAdvertRegEx = new RegExp("[a-zA-Z0-9s]{30,100}$", "gy");
// !firstName lastName eMail txtArea(specify) tellSomething
var resultFirstName = false;
var resultLastName = false;
var resultEMail = false;
var resultSpecify = false;
var resultTellSomething = false;
var resultImage = false;

firstName.addEventListener("focus", () => {
  resultFirstName = false;
  firstName.value = "";
  firstName.classList.remove("successInput");
  firstName.classList.remove("wrongInput");
});
firstName.addEventListener("blur", e => {
  firstNameRegExp.lastIndex = 0;

  resultFirstName = firstNameRegExp.test(firstName.value);

  if (resultFirstName == true) {
    firstName.classList.add("successInput");
    firstName.classList.remove("wrongInput");
  }
  if (resultFirstName == false) {
    firstName.classList.add("wrongInput");
    firstName.classList.remove("successInput");
  }
});

lastName.addEventListener("focus", () => {
  resultLastName = false;
  lastName.value = "";
  lastName.classList.remove("successInput");
  lastName.classList.remove("wrongInput");
});
lastName.addEventListener("blur", () => {
  resultLastName = lastNameRegExp.test(lastName.value);

  if (resultLastName == true) {
    lastName.classList.add("successInput");
    lastName.classList.remove("wrongInput");
  }
  if (resultLastName == false) {
    lastName.classList.add("wrongInput");
    lastName.classList.remove("successInput");
  }
});

eMail.addEventListener("focus", () => {
  eMail.value = "";

  resultEMail = false;
  eMail.classList.remove("successInput");

  eMail.classList.remove("wrongInput");
});
eMail.addEventListener("blur", e => {
  emailRegExp.lastIndex = 0;

  resultEMail = emailRegExp.test(eMail.value);

  if (resultEMail == true) {
    eMail.classList.add("successInput");
    eMail.classList.remove("wrongInput");
  }
  if (resultEMail == false) {
    eMail.classList.add("wrongInput");
    eMail.classList.remove("successInput");
  }
});
var charCounterTellSomething = 0;
var counterDisplayTellSomething = document.getElementById("chrCountTellSomething")
var key1;
tellSomething.addEventListener("focus", () => {
  tellSomething.onkeydown = function() {
    key1 = event.keyCode || event.charCode;
    if (key1 == 13) {
      return false;
    }
    
  };
  infoOfAdvertRegEx.lastIndex = 0;
  resultSpecify = false;
});
tellSomething.addEventListener("blur", e => {
  resultTellSomething = false;
  resultTellSomething = infoOfAdvertRegEx.test(tellSomething.value);
  
  if (resultTellSomething == true) {
    tellSomething.classList.add("successInput");
    tellSomething.classList.remove("wrongInput");
  }
  if (resultTellSomething == false) {
    tellSomething.classList.add("wrongInput");
    tellSomething.classList.remove("successInput");
  }
});

tellSomething.addEventListener("input", function() {
  tellSomething.onkeydown = function() {
    key1 = event.keyCode || event.charCode;
    if (key1 == 13) {
      return false;
    }
    console.log("key1:", key1);
  };
  if (tellSomething.value == "") {
    charCounterTellSomething = 1;
  }
  if (key1 == 8) {
    charCounterTellSomething--;
    console.log(charCounterTellSomething);
  } else {
    charCounterTellSomething++;
    console.log(charCounterTellSomething);
  }
  counterDisplayTellSomething.innerText = '50 to 200 characters are allowed' +" "+"["+charCounterTellSomething+"]";
});
// !-----------------------------------------------------------------------------------------------------------------

var charCounterSpecify = 0;
var counterDisplaySpecify = document.getElementById("chrCountSpecify");
var key2;
specifyInput.addEventListener("focus", () => {
  specifyInput.onkeydown = function() {
    key2 = event.keyCode || event.charCode;
    if (key2 == 13) {
      return false;
    }
    console.log("key:", key2);
  };
  infoOfAdvertRegEx.lastIndex = 0;
  resultSpecify = false;
});
specifyInput.addEventListener("blur", e => {
  resultSpecify = false;
  resultSpecify = infoOfAdvertRegEx.test(specifyInput.value);

  if (resultSpecify == true) {
    specifyInput.classList.add("successInput");
    specifyInput.classList.remove("wrongInput");
  }
  if (resultSpecify == false) {
    specifyInput.classList.add("wrongInput");
    specifyInput.classList.remove("successInput");
  }
});

specifyInput.addEventListener("input", function() {
  specifyInput.onkeydown = function() {
    key2 = event.keyCode || event.charCode;
    if (key2 == 13) {
      return false;
    }
    console.log("key:", key2);
  };
  if (specifyInput.value == "") {
    charCounterSpecify = 1;
  }
  if (key2 == 8) {
    charCounterSpecify--;
    console.log(charCounterSpecify);
  } else {
    charCounterSpecify++;
    console.log(charCounterSpecify);
  }
  counterDisplaySpecify.innerText = ` 50 to 200 characters are allowed [${charCounterSpecify}]`;
});

var fileInput=document.getElementById("XFile")
var tooLarge=document.getElementById("tooLarge")
fileInput.onchange=function(){

  if (!dontHave.checked) {
    console.log("inMain");
    if(fileInput.files[0].size<=10485760){
      resultImage=true;
      tooLarge.style.display="none";
    }
    if (fileInput.files[0].size>10485760 ) {
      resultImage=false;
      tooLarge.style.display="";
    }
  }}
dontHave.onclick=function(){
if (dontHave.checked) {
resultImage=true;  
tooLarge.style.display="none";
}

}
haveImage.onclick=function(){
  console.log("clicked22222222----------------");
  if (!dontHave.checked) {
    resultImage=false;  
   
    }
}

// var resultFirstName = false;
// var resultLastName = false;
// var resultEMail = false;
// var resultSpecify = false;
// var resultTellSomething = false;
// var resultFile = false;

var submit=document.getElementById("submit") 
// submit.onsubmit=()=>{
//   console.log("insubmt");
//   var result = true;

//   if (resultFirstName==false) {
//     result=false;
//   }
//   if (resultLastName==false) {
//     result=false;
//   }
//   if (resultEMail==false) {
//     result=false;
//   }
//   if (resultTellSomething==false) {
//     result=false;
//   }
//   if(withImage.checked){
//            if(resultImage==false){
//              result=false;
//            }

//   }
//   if(other.checked){
//            if(resultSpecify==false){
//              result=false;
//            }
//   }
//   console.log("firstName",resultFirstName)
//   console.log("lastName",resultLastName)
//   console.log("email",resultEMail)
//   console.log("tellsomething",resultTellSomething)
//   console.log("image",resultImage)
//   console.log("specify",resultSpecify)
//   console.log("total",result)
//   return result;
// }
var alertError=document.getElementById("alertError");
var alertDone=document.getElementById("alertDone");
function validateForm(){
  var result = true;
  console.log("insubmt");

  if (resultFirstName==false || resultLastName==false || resultEMail==false || resultTellSomething==false) {
    result=false;
  }
  
  if(withImage.checked){
           if(resultImage==false){
             result=false;
           }

  }
  if(other.checked){
           if(resultSpecify==false){
             result=false;
           }
  }
  console.log("firstName",resultFirstName)
  console.log("lastName",resultLastName)
  console.log("email",resultEMail)
  console.log("tellsomething",resultTellSomething)
  console.log("image",resultImage)
  console.log("specify",resultSpecify)
  console.log("total",result)
  if (result==false) {
    alertError.style.display="";
    alertDone.style.display="none"
  }
  else{
    alertError.style.display="none";
    alertDone.style.display=""
  }
  return result;

}