console.log("succesfully attached")
var onlyText=document.getElementById("onlyText");
var withImage=document.getElementById("withImage")
var other=document.getElementById("other")
onlyText.addEventListener("click",()=>{

    if(onlyText.checked==true)
    {
        console.log("only texrt is sielsected")
    }

})
withImage.addEventListener("click",()=>{

    if(withImage.checked==true)
    {
        console.log("only texrt is sielsected")
    }

})
other.addEventListener("click",()=>{

    if(other.checked==true){
        console.log("only texrt is sielsected")
    }

})