console.log("this is the paginate js file : attached succesfully");
var Ard1=document.getElementById('Ard1')
var Basic1=document.getElementById('Basic1')
var Iot1=document.getElementById('Iot1')
var Other1=document.getElementById('Other1')

Basic1.classList.add('active')
Ard1.classList.add('active')
Iot1.classList.add('active')
Other1.classList.add('active')

var lastVisitPageArd=1;
var lastVisitPageBasic=1;
var lastVisitPageOther=1;
var lastVisitPageIot=1;

 // ^^ last page attend by the user in arduino sectionby default th lastt page is the one as initiallty no page is attend by the user

var countArd=1;
var countBasic=1;
var countIot=1;
var countOther=1;




function changePage(id){
    lastVisitPageArd=countArd
    lastVisitPageBasic=countBasic
    lastVisitPageIot=countIot
    lastVisitPageOther=countOther

    var pageNo=id.slice(id.length-1)
    var code=id.slice(0,id.length-1)
    console.log("pageNo and code is in vhangePage function",pageNo,code)
    
   
    var next=document.getElementById(`next${code}`)
    var prev=document.getElementById(`prev${code}`)

    prev.classList.remove('disabled')
    next.classList.remove('disabled')
    
    var lastPage=parseInt(next.name);
    
    
    if(code=='Ard'){
        countArd=pageNo
        document.getElementById(`${code}${lastVisitPageArd}`).classList.remove('active')
        document.getElementById(`${code}${pageNo}`).classList.add('active')
        lastVisitPageArd=parseInt(pageNo);
    }
    if (code=='Basic') {
        countBasic=parseInt(pageNo)
        document.getElementById(`${code}${lastVisitPageBasic}`).classList.remove('active')
        document.getElementById(`${code}${pageNo}`).classList.add('active')
        lastVisitPageBasic=parseInt(pageNo)
    }
    if (code=='Iot') {
        countIot=parseInt(pageNo)
        document.getElementById(`${code}${lastVisitPageIot}`).classList.remove('active')
        document.getElementById(`${code}${pageNo}`).classList.add('active')
        lastVisitPageOther=parseInt(pageNo)
    }
    if (code=='Other') {
        countOther=parseInt(pageNo)
        document.getElementById(`${code}${lastVisitPageOther}`).classList.remove('active')
        document.getElementById(`${code}${pageNo}`).classList.add('active')
        lastVisitPageOther=parseInt(pageNo)
    }
    var container=document.getElementById(`${code}`)
    container.classList.remove('fadeIn')
    // console.log(heading1);
    var heading1=document.getElementById(`${code}head1`)
    var heading2=document.getElementById(`${code}head2`)
    var heading3=document.getElementById(`${code}head3`)
    var heading4=document.getElementById(`${code}head4`)

    var readTime1=document.getElementById(`${code}read1`)
    var readTime2=document.getElementById(`${code}read2`)
    var readTime3=document.getElementById(`${code}read3`)
    var readTime4=document.getElementById(`${code}read4`)

    var description1=document.getElementById(`${code}desc1`)
    var description2=document.getElementById(`${code}desc2`)
    var description3=document.getElementById(`${code}desc3`)
    var description4=document.getElementById(`${code}desc4`)

    var id1=document.getElementById(`${code}id1`)
    var id2=document.getElementById(`${code}id2`)
    var id3=document.getElementById(`${code}id3`)
    var id4=document.getElementById(`${code}id4`)


if (pageNo==1) {
      prev.classList.remove("active")
      prev.classList.add("disabled")
      next.classList.remove('disabled')
      next.classList.add('active')
} 

if (pageNo>1 && pageNo<lastPage) {
    prev.classList.remove("disabled")
    prev.classList.add("active")
    next.classList.remove('disabled')
    next.classList.add('active')

}

if(pageNo==lastPage) {

    next.classList.add("disabled")
    next.classList.remove("active")
    prev.classList.remove('disabled')
    prev.classList.add('active')
    
}

   

    console.log(pageNo)
    var entry={
     page_no:pageNo,
     code:code,
     next:false,
     prev:false,
     jump_page:true,
     
  }
  var params={
      method:'POST',
      body:JSON.stringify(entry),
      cache:'no-cache',
      headers:new Headers({
          "content-type":"application/json"
      })
  }
  var url=`${window.origin}/paginate`


  
      fetch(url,params).then(response=>{
          if(response.status==200){
              console.log("succesfully_posted")
          }
          else{
              console.log("eroor 404, data not posted")
          }
          response.json().then(data=>{
              console.log(data['heading'][1])
            //   console.log(heading1)
            // var heading1=document.getElementById(`${code}head1`)
            heading1.innerHTML=data['heading'][1];
            heading2.innerHTML=data['heading'][2];
            heading3.innerHTML=data['heading'][3];
            heading4.innerHTML=data['heading'][4];

            readTime1.innerHTML=data['heading'][1];
            readTime2.innerHTML=data['heading'][2];
            readTime3.innerHTML=data['heading'][3];
            readTime4.innerHTML=data['heading'][4];
            
            description1.innerHTML=data['description'][1];
            description2.innerHTML=data['description'][2];
            description3.innerHTML=data['description'][3];
            description4.innerHTML=data['description'][4];
            //    container.style.display="none"
            id1.href=data['id'][1];
            id2.href=data['id'][2];
            id3.href=data['id'][3];
            id4.href=data['id'][4];
            container.classList.add('fadeIn')
            
        //    container.style.display=""   
          })
      })
}

function nextPage(type,code){
    console.log(code)
    var pageNo=0
    var container=document.getElementById(`${code}`)
    container.classList.remove('fadeIn')
    var next=document.getElementById(`next${code}`)
    var lastPage=parseInt(next.name);
    console.log('NextPage clciked',type)
    var heading1=document.getElementById(`${code}head1`)
    var heading2=document.getElementById(`${code}head2`)
    var heading3=document.getElementById(`${code}head3`)
    var heading4=document.getElementById(`${code}head4`)

    var readTime1=document.getElementById(`${code}read1`)
    var readTime2=document.getElementById(`${code}read2`)
    var readTime3=document.getElementById(`${code}read3`)
    var readTime4=document.getElementById(`${code}read4`)

    var description1=document.getElementById(`${code}desc1`)
    var description2=document.getElementById(`${code}desc2`)
    var description3=document.getElementById(`${code}desc3`)
    var description4=document.getElementById(`${code}desc4`)
    
    var id1=document.getElementById(`${code}id1`)
    var id2=document.getElementById(`${code}id2`)
    var id3=document.getElementById(`${code}id3`)
    var id4=document.getElementById(`${code}id4`)


    if (code=='Ard' && countArd<lastPage) {
        lastVisitPageArd=countArd
        console.log('In If block')
        document.getElementById(`${code}${lastVisitPageArd}`).classList.remove('active')
        countArd++
        pageNo=countArd
        console.log(pageNo);
    }
    
    
    if (code=='Basic' && countBasic<lastPage) {
        lastVisitPageBasic=countBasic
        console.log('In If block')
        document.getElementById(`${code}${lastVisitPageBasic}`).classList.remove('active')
        countBasic++
        pageNo=countBasic
        console.log(pageNo);
    }
    if (code=='Iot' && countIot<lastPage) {
        lastVisitPageIot=countIot
        console.log('In If block')
        document.getElementById(`${code}${lastVisitPageIot}`).classList.remove('active')
        countIot++
        pageNo=countIot
        console.log(pageNo);
    }
    if (code=='Other' && countOther<lastPage) {
        lastVisitPageOther=countOther
        console.log('In If block')
        document.getElementById(`${code}${lastVisitPageOther}`).classList.remove('active')
        countOther++
        pageNo=countOther
        console.log(pageNo);
    }
// *  TRACKER
document.getElementById(`${code}${pageNo}`).classList.add('active')

   

 // * CHECKING FOR THE END
    var prev=document.getElementById(`prev${code}`)

     prev.classList.remove('disabled')
     next.classList.remove('disabled')
 
     

     if (pageNo==1) {
        prev.classList.remove("active")
        prev.classList.add("disabled")
        next.classList.remove('disabled')
        next.classList.add('active')
               }
               
               
     if (pageNo>1 && pageNo<lastPage) {
                prev.classList.remove("disabled")
                prev.classList.add("active")
                next.classList.remove('disabled')
                next.classList.add('active')
              }
  
    if(pageNo==lastPage) {
      next.classList.add("disabled")
      next.classList.remove("active")
      prev.classList.remove('disabled')
      prev.classList.add('active')
      
                  }
    
    var url=`${window.origin}/paginate`
    var entry={
        page_no:pageNo,
        code:code,
        next:true,
        prev:false,
        jump_page:false,
        
     }
     var params={
        method:'POST',
        body:JSON.stringify(entry),
        cache:'no-cache',
        headers:new Headers({
            "content-type":"application/json"
        })
    }

    fetch(url,params).then(response=>{
        if(response.status==200){
            console.log("succesfully_posted")
        }
        else{
            console.log("eroor 404, data not posted")
        }
        response.json().then(data=>{
           
            console.log(data)
        //   var heading1=document.getElementById(`${code}head1`)
          heading1.innerHTML=data['heading'][1];
          heading2.innerHTML=data['heading'][2];
          heading3.innerHTML=data['heading'][3];
          heading4.innerHTML=data['heading'][4];

          readTime1.innerHTML=data['heading'][1];
          readTime2.innerHTML=data['heading'][2];
          readTime3.innerHTML=data['heading'][3];
          readTime4.innerHTML=data['heading'][4];
          
          description1.innerHTML=data['description'][1];
          description2.innerHTML=data['description'][2];
          description3.innerHTML=data['description'][3];
          description4.innerHTML=data['description'][4];
        //      container.style.display="none"
        id1.href=data['id'][1];
        id2.href=data['id'][2];
        id3.href=data['id'][3];
        id4.href=data['id'][4];
          container.classList.add('fadeIn')
          
        //  container.style.display=""   
        })
    })

}


function prevPage(type,code){
    var pageNo=0
    var container=document.getElementById(`${code}`)
    container.classList.remove('fadeIn')
    var next=document.getElementById(`next${code}`)
    var lastPage=parseInt(next.name);
    console.log('prevPage clciked',type)
    var heading1=document.getElementById(`${code}head1`)
    var heading2=document.getElementById(`${code}head2`)
    var heading3=document.getElementById(`${code}head3`)
    var heading4=document.getElementById(`${code}head4`)

    var readTime1=document.getElementById(`${code}read1`)
    var readTime2=document.getElementById(`${code}read2`)
    var readTime3=document.getElementById(`${code}read3`)
    var readTime4=document.getElementById(`${code}read4`)

    var description1=document.getElementById(`${code}desc1`)
    var description2=document.getElementById(`${code}desc2`)
    var description3=document.getElementById(`${code}desc3`)
    var description4=document.getElementById(`${code}desc4`)
    
    var id1=document.getElementById(`${code}id1`)
    var id2=document.getElementById(`${code}id2`)
    var id3=document.getElementById(`${code}id3`)
    var id4=document.getElementById(`${code}id4`)


    if (code=='Ard' && countArd>0) {
        lastVisitPageArd=countArd
        document.getElementById(`${code}${lastVisitPageArd}`).classList.remove('active')
        console.log('In If block')
        countArd--
        pageNo=countArd
        console.log(pageNo);
    }
    if (code=='Basic' && countBasic>0) {
        lastVisitPageBasic=countBasic
        document.getElementById(`${code}${lastVisitPageBasic}`).classList.remove('active')
        console.log('In If block')
        countBasic--
        pageNo=countBasic
        console.log(pageNo);
    }
    if (code=='Iot' && countIot>0) {
        lastVisitPageIot=countIot
        document.getElementById(`${code}${lastVisitPageIot}`).classList.remove('active')
        console.log('In If block')
        countIot--
        pageNo=countIot
        console.log(pageNo);
    }
    if (code=='Other' && countOther>0) {
        lastVisitPageOther=countOther
        document.getElementById(`${code}${lastVisitPageOther}`).classList.remove('active')
        console.log('In If block')
        countOther--
        pageNo=countOther
        console.log(pageNo);
    }

// *  TRACKER
document.getElementById(`${code}${pageNo}`).classList.add('active')

   

 // * CHECKING FOR THE END
    var prev=document.getElementById(`prev${code}`)

     prev.classList.remove('disabled')
     next.classList.remove('disabled')
 
     

     if (pageNo==1) {
        prev.classList.remove("active")
        prev.classList.add("disabled")
        next.classList.remove('disabled')
        next.classList.add('active')
               }
               
               
     if (pageNo>1 && pageNo<lastPage) {
                prev.classList.remove("disabled")
                prev.classList.add("active")
                next.classList.remove('disabled')
                next.classList.add('active')
              }
  
    if(pageNo==lastPage) {
      next.classList.add("disabled")
      next.classList.remove("active")
      prev.classList.remove('disabled')
      prev.classList.add('active')
      
                  }
    
    var url=`${window.origin}/paginate`
    var entry={
        page_no:pageNo,
        code:code,
        next:false,
        prev:true,
        jump_page:false,
        
     }
     var params={
        method:'POST',
        body:JSON.stringify(entry),
        cache:'no-cache',
        headers:new Headers({
            "content-type":"application/json"
        })
    }

    fetch(url,params).then(response=>{
        if(response.status==200){
            console.log("succesfully_posted")
        }
        else{
            console.log("eroor 404, data not posted")
        }
        response.json().then(data=>{
           
            console.log(data)
        //   var heading1=document.getElementById(`${code}head1`)
          heading1.innerHTML=data['heading'][1];
          heading2.innerHTML=data['heading'][2];
          heading3.innerHTML=data['heading'][3];
          heading4.innerHTML=data['heading'][4];

          readTime1.innerHTML=data['heading'][1];
          readTime2.innerHTML=data['heading'][2];
          readTime3.innerHTML=data['heading'][3];
          readTime4.innerHTML=data['heading'][4];
          
          description1.innerHTML=data['description'][1];
          description2.innerHTML=data['description'][2];
          description3.innerHTML=data['description'][3];
          description4.innerHTML=data['description'][4];
        //      container.style.display="none"
        id1.href=data['id'][1];
        id2.href=data['id'][2];
        id3.href=data['id'][3];
        id4.href=data['id'][4];
          container.classList.add('fadeIn')
          
        //  container.style.display=""   
        })
    })

}