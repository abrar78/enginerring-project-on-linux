console.log("this is the paginate js file : attached succesfully");
var Ard1 = document.getElementById('Ard1')
var Basic1 = document.getElementById('Basic1')
var Iot1 = document.getElementById('Iot1')
var Other1 = document.getElementById('Other1')
var mobileCountArd_ = 1
var mobileCountBasic_ = 1
var mobileCountOther_ = 1

var lastVisitPageArd = 1;
var lastVisitPageBasic = 1;
var lastVisitPageOther = 1;
var lastVisitPageIot = 1;
var mobileCountIot_ = 1
var countArd = 1;
var countBasic = 1;
var countIot = 1;
var countOther = 1;
Basic1.classList.add('active')
Ard1.classList.add('active')
Iot1.classList.add('active')
Other1.classList.add('active')

// ^^ last page attend by the user in arduino sectionby default th lastt page is the one as initiallty no page is attend by the user





function changePage(id) {
    lastVisitPageArd = countArd
    lastVisitPageBasic = countBasic
    lastVisitPageIot = countIot
    lastVisitPageOther = countOther

    var pageNo = id.slice(id.length - 1)
    var code = id.slice(0, id.length - 1)
    console.log("pageNo and code is in changePage function", pageNo, code)
    var thumbnail1 = document.getElementById(`${code}thumb1`)
    var thumbnail2 = document.getElementById(`${code}thumb2`)
    var thumbnail3 = document.getElementById(`${code}thumb3`)
    var thumbnail4 = document.getElementById(`${code}thumb4`)


    var next = document.getElementById(`next${code}`)
    var prev = document.getElementById(`prev${code}`)

    prev.classList.remove('disabled')
    next.classList.remove('disabled')

    var lastPage = parseInt(next.name);


    if (code == 'Ard') {
        countArd = pageNo
        console.log(`${code}${lastVisitPageArd}`)
        document.getElementById(`${code}${lastVisitPageArd}`).classList.remove('active')
        document.getElementById(`${code}${pageNo}`).classList.add('active')
        lastVisitPageArd = parseInt(pageNo);
    }
    if (code == 'Basic') {
        countBasic = parseInt(pageNo)
        document.getElementById(`${code}${lastVisitPageBasic}`).classList.remove('active')
        document.getElementById(`${code}${pageNo}`).classList.add('active')
        lastVisitPageBasic = parseInt(pageNo)
    }
    if (code == 'Iot') {
        countIot = parseInt(pageNo)
        document.getElementById(`${code}${lastVisitPageIot}`).classList.remove('active')
        document.getElementById(`${code}${pageNo}`).classList.add('active')
        lastVisitPageOther = parseInt(pageNo)
    }
    if (code == 'Other') {
        countOther = parseInt(pageNo)
        document.getElementById(`${code}${lastVisitPageOther}`).classList.remove('active')
        document.getElementById(`${code}${pageNo}`).classList.add('active')
        lastVisitPageOther = parseInt(pageNo)
    }
    var container = document.getElementById(`${code}`)
    container.classList.remove('bounceIn')
    // console.log(heading1);
    var heading1 = document.getElementById(`${code}head1`)
    var heading2 = document.getElementById(`${code}head2`)
    var heading3 = document.getElementById(`${code}head3`)
    var heading4 = document.getElementById(`${code}head4`)






    var description1 = document.getElementById(`${code}desc1`)
    var description2 = document.getElementById(`${code}desc2`)
    var description3 = document.getElementById(`${code}desc3`)
    var description4 = document.getElementById(`${code}desc4`)

    var id1 = document.getElementById(`${code}id1`)
    var id2 = document.getElementById(`${code}id2`)
    var id3 = document.getElementById(`${code}id3`)
    var id4 = document.getElementById(`${code}id4`)


    if (pageNo == 1) {
        prev.classList.remove("active")
        prev.classList.add("disabled")
        next.classList.remove('disabled')
        next.classList.add('active')
    }

    if (pageNo > 1 && pageNo < lastPage) {
        prev.classList.remove("disabled")
        prev.classList.add("active")
        next.classList.remove('disabled')
        next.classList.add('active')

    }

    if (pageNo == lastPage) {

        next.classList.add("disabled")
        next.classList.remove("active")
        prev.classList.remove('disabled')
        prev.classList.add('active')

    }



    console.log(pageNo)
    var entry = {
        page_no: pageNo,
        code: code,
        next: false,
        prev: false,
        jump_page: true,

    }
    var params = {
        method: 'POST',
        body: JSON.stringify(entry),
        cache: 'no-cache',
        headers: new Headers({
            "content-type": "application/json"
        })
    }
    var url = `${window.origin}/paginate`



    fetch(url, params).then(response => {
        if (response.status == 200) {
            console.log("succesfully_posted")
        }
        else {
            console.log("eroor 404, data not posted")
        }
        response.json().then(data => {
            console.log(data)
            //   console.log(heading1)
            // var heading1=document.getElementById(`${code}head1`)
            if (data['heading'][1] == undefined) {
                document.getElementById(`${code}card1`).style.display = 'none'
            }
            else {
                document.getElementById(`${code}card1`).style.display = ""
            }
            if (data['heading'][2] == undefined) {
                document.getElementById(`${code}card2`).style.display = 'none'

            }
            else {
                document.getElementById(`${code}card2`).style.display = ''

            }
            if (data['heading'][3] == undefined) {
                document.getElementById(`${code}card3`).style.display = 'none'

            }
            else {
                document.getElementById(`${code}card3`).style.display = ''

            }
            if (data['heading'][4] == undefined) {
                document.getElementById(`${code}card4`).style.display = 'none'

            }
            else {
                document.getElementById(`${code}card4`).style.display = ''

            }
            heading1.innerHTML = data['heading'][1];
            heading2.innerHTML = data['heading'][2];
            heading3.innerHTML = data['heading'][3];
            heading4.innerHTML = data['heading'][4];


            thumbnail1.src = "/static/images/" + data["thumbnail"][1]
            thumbnail2.src = "/static/images/" + data["thumbnail"][2]
            thumbnail3.src = "/static/images/" + data["thumbnail"][3]
            thumbnail4.src = "/static/images/" + data["thumbnail"][4]




            description1.innerHTML = data['description'][1];
            description2.innerHTML = data['description'][2];
            description3.innerHTML = data['description'][3];
            description4.innerHTML = data['description'][4];
            //    container.style.display="none"
            id1.href = data['id'][1];
            id2.href = data['id'][2];
            id3.href = data['id'][3];
            id4.href = data['id'][4];
            container.classList.add('bounceIn')

            //    container.style.display=""   
        })
    })
}

function nextPage(type, code) {
    console.log(code)
    var pageNo = 0
    var container = document.getElementById(`${code}`)
    container.classList.remove('bounceIn')
    var next = document.getElementById(`next${code}`)
    var lastPage = parseInt(next.name);
    console.log('NextPage clciked', type)
    var heading1 = document.getElementById(`${code}head1`)
    var heading2 = document.getElementById(`${code}head2`)
    var heading3 = document.getElementById(`${code}head3`)
    var heading4 = document.getElementById(`${code}head4`)

    var thumbnail1 = document.getElementById(`${code}thumb1`)
    var thumbnail2 = document.getElementById(`${code}thumb2`)
    var thumbnail3 = document.getElementById(`${code}thumb3`)
    var thumbnail4 = document.getElementById(`${code}thumb4`)





    var description1 = document.getElementById(`${code}desc1`)
    var description2 = document.getElementById(`${code}desc2`)
    var description3 = document.getElementById(`${code}desc3`)
    var description4 = document.getElementById(`${code}desc4`)

    var id1 = document.getElementById(`${code}id1`)
    var id2 = document.getElementById(`${code}id2`)
    var id3 = document.getElementById(`${code}id3`)
    var id4 = document.getElementById(`${code}id4`)


    if (code == 'Ard' && countArd < lastPage) {
        lastVisitPageArd = countArd
        console.log('In If block')
        document.getElementById(`${code}${lastVisitPageArd}`).classList.remove('active')
        countArd++
        pageNo = countArd
        console.log(pageNo);
    }


    if (code == 'Basic' && countBasic < lastPage) {
        lastVisitPageBasic = countBasic
        console.log('In If block')
        document.getElementById(`${code}${lastVisitPageBasic}`).classList.remove('active')
        countBasic++
        pageNo = countBasic
        console.log(pageNo);
    }
    if (code == 'Iot' && countIot < lastPage) {
        lastVisitPageIot = countIot
        console.log('In If block')
        document.getElementById(`${code}${lastVisitPageIot}`).classList.remove('active')
        countIot++
        pageNo = countIot
        console.log(pageNo);
    }
    if (code == 'Other' && countOther < lastPage) {
        lastVisitPageOther = countOther
        console.log('In If block')
        document.getElementById(`${code}${lastVisitPageOther}`).classList.remove('active')
        countOther++
        pageNo = countOther
        console.log(pageNo);
    }
    // *  TRACKER
    document.getElementById(`${code}${pageNo}`).classList.add('active')



    // * CHECKING FOR THE END
    var prev = document.getElementById(`prev${code}`)

    prev.classList.remove('disabled')
    next.classList.remove('disabled')



    if (pageNo == 1) {
        prev.classList.remove("active")
        prev.classList.add("disabled")
        next.classList.remove('disabled')
        next.classList.add('active')
    }


    if (pageNo > 1 && pageNo < lastPage) {
        prev.classList.remove("disabled")
        prev.classList.add("active")
        next.classList.remove('disabled')
        next.classList.add('active')
    }

    if (pageNo == lastPage) {
        next.classList.add("disabled")
        next.classList.remove("active")
        prev.classList.remove('disabled')
        prev.classList.add('active')

    }

    var url = `${window.origin}/paginate`
    var entry = {
        page_no: pageNo,
        code: code,
        next: true,
        prev: false,
        jump_page: false,

    }
    var params = {
        method: 'POST',
        body: JSON.stringify(entry),
        cache: 'no-cache',
        headers: new Headers({
            "content-type": "application/json"
        })
    }

    fetch(url, params).then(response => {
        if (response.status == 200) {
            console.log("succesfully_posted")
        }
        else {
            console.log("eroor 404, data not posted")
        }
        response.json().then(data => {

            console.log(data)
            //   var heading1=document.getElementById(`${code}head1`)
            if (data['heading'][1] == undefined) {
                document.getElementById(`${code}card1`).style.display = 'none'
            }
            else {
                document.getElementById(`${code}card1`).style.display = ""
            }
            if (data['heading'][2] == undefined) {
                document.getElementById(`${code}card2`).style.display = 'none'

            }
            else {
                document.getElementById(`${code}card2`).style.display = ''

            }
            if (data['heading'][3] == undefined) {
                document.getElementById(`${code}card3`).style.display = 'none'

            }
            else {
                document.getElementById(`${code}card3`).style.display = ''

            }
            if (data['heading'][4] == undefined) {
                document.getElementById(`${code}card4`).style.display = 'none'

            }
            else {
                document.getElementById(`${code}card4`).style.display = ''

            }
            heading1.innerHTML = data['heading'][1];
            heading2.innerHTML = data['heading'][2];
            heading3.innerHTML = data['heading'][3];
            heading4.innerHTML = data['heading'][4];

            thumbnail1.src = "/static/images/" + data["thumbnail"][1]
            thumbnail2.src = "/static/images/" + data["thumbnail"][2]
            thumbnail3.src = "/static/images/" + data["thumbnail"][3]
            thumbnail4.src = "/static/images/" + data["thumbnail"][4]




            description1.innerHTML = data['description'][1];
            description2.innerHTML = data['description'][2];
            description3.innerHTML = data['description'][3];
            description4.innerHTML = data['description'][4];
            //      container.style.display="none"
            id1.href = data['id'][1];
            id2.href = data['id'][2];
            id3.href = data['id'][3];
            id4.href = data['id'][4];
            container.classList.add('bounceIn')

            //  container.style.display=""   
        })
    })

}


function prevPage(type, code) {
    var pageNo = 0
    var container = document.getElementById(`${code}`)
    container.classList.remove('bounceIn')
    var next = document.getElementById(`next${code}`)
    var lastPage = parseInt(next.name);
    console.log('prevPage clciked', type)
    var heading1 = document.getElementById(`${code}head1`)
    var heading2 = document.getElementById(`${code}head2`)
    var heading3 = document.getElementById(`${code}head3`)
    var heading4 = document.getElementById(`${code}head4`)
    var thumbnail1 = document.getElementById(`${code}thumb1`)
    var thumbnail2 = document.getElementById(`${code}thumb2`)
    var thumbnail3 = document.getElementById(`${code}thumb3`)
    var thumbnail4 = document.getElementById(`${code}thumb4`)






    var description1 = document.getElementById(`${code}desc1`)
    var description2 = document.getElementById(`${code}desc2`)
    var description3 = document.getElementById(`${code}desc3`)
    var description4 = document.getElementById(`${code}desc4`)

    var id1 = document.getElementById(`${code}id1`)
    var id2 = document.getElementById(`${code}id2`)
    var id3 = document.getElementById(`${code}id3`)
    var id4 = document.getElementById(`${code}id4`)


    if (code == 'Ard' && countArd > 0) {
        lastVisitPageArd = countArd
        document.getElementById(`${code}${lastVisitPageArd}`).classList.remove('active')
        console.log('In If block')
        countArd--
        pageNo = countArd
        console.log(pageNo);
    }
    if (code == 'Basic' && countBasic > 0) {
        lastVisitPageBasic = countBasic
        document.getElementById(`${code}${lastVisitPageBasic}`).classList.remove('active')
        console.log('In If block')
        countBasic--
        pageNo = countBasic
        console.log(pageNo);
    }
    if (code == 'Iot' && countIot > 0) {
        lastVisitPageIot = countIot
        document.getElementById(`${code}${lastVisitPageIot}`).classList.remove('active')
        console.log('In If block')
        countIot--
        pageNo = countIot
        console.log(pageNo);
    }
    if (code == 'Other' && countOther > 0) {
        lastVisitPageOther = countOther
        document.getElementById(`${code}${lastVisitPageOther}`).classList.remove('active')
        console.log('In If block')
        countOther--
        pageNo = countOther
        console.log(pageNo);
    }

    // *  TRACKER
    document.getElementById(`${code}${pageNo}`).classList.add('active')



    // * CHECKING FOR THE END
    var prev = document.getElementById(`prev${code}`)

    prev.classList.remove('disabled')
    next.classList.remove('disabled')



    if (pageNo == 1) {
        prev.classList.remove("active")
        prev.classList.add("disabled")
        next.classList.remove('disabled')
        next.classList.add('active')
    }


    if (pageNo > 1 && pageNo < lastPage) {
        prev.classList.remove("disabled")
        prev.classList.add("active")
        next.classList.remove('disabled')
        next.classList.add('active')
    }

    if (pageNo == lastPage) {
        next.classList.add("disabled")
        next.classList.remove("active")
        prev.classList.remove('disabled')
        prev.classList.add('active')

    }

    var url = `${window.origin}/paginate`
    var entry = {
        page_no: pageNo,
        code: code,
        next: false,
        prev: true,
        jump_page: false,

    }
    var params = {
        method: 'POST',
        body: JSON.stringify(entry),
        cache: 'no-cache',
        headers: new Headers({
            "content-type": "application/json"
        })
    }

    fetch(url, params).then(response => {
        if (response.status == 200) {
            console.log("succesfully_posted")
        }
        else {
            console.log("eroor 404, data not posted")
        }
        response.json().then(data => {

            console.log(data)
            //   var heading1=document.getElementById(`${code}head1`)
            if (data['heading'][1] == undefined) {
                document.getElementById(`${code}card1`).style.display = 'none'
            }
            else {
                document.getElementById(`${code}card1`).style.display = ""
            }
            if (data['heading'][2] == undefined) {
                document.getElementById(`${code}card2`).style.display = 'none'

            }
            else {
                document.getElementById(`${code}card2`).style.display = ''

            }
            if (data['heading'][3] == undefined) {
                document.getElementById(`${code}card3`).style.display = 'none'

            }
            else {
                document.getElementById(`${code}card3`).style.display = ''

            }
            if (data['heading'][4] == undefined) {
                document.getElementById(`${code}card4`).style.display = 'none'

            }
            else {
                document.getElementById(`${code}card4`).style.display = ''

            }
            heading1.innerHTML = data['heading'][1];
            heading2.innerHTML = data['heading'][2];
            heading3.innerHTML = data['heading'][3];
            heading4.innerHTML = data['heading'][4];




            thumbnail1.src = "/static/images/" + data["thumbnail"][1]
            thumbnail2.src = "/static/images/" + data["thumbnail"][2]
            thumbnail3.src = "/static/images/" + data["thumbnail"][3]
            thumbnail4.src = "/static/images/" + data["thumbnail"][4]


            description1.innerHTML = data['description'][1];
            description2.innerHTML = data['description'][2];
            description3.innerHTML = data['description'][3];
            description4.innerHTML = data['description'][4];
            //      container.style.display="none"
            id1.href = data['id'][1];
            id2.href = data['id'][2];
            id3.href = data['id'][3];
            id4.href = data['id'][4];
            container.classList.add('bounceIn')

            //  container.style.display=""   
        })
    })

}
var seeMoreBtnArduino = document.getElementById("seeMoreBtnArd")
var seeMoreBtnBasic = document.getElementById("seeMoreBtnBasic")
var seeMoreBtnIot = document.getElementById("seeMoreBtnIot")
var seeMoreBtnOther = document.getElementById("seeMoreBtnOther")

seeMoreBtnArduino.disabled = false
seeMoreBtnBasic.disabled = false
seeMoreBtnIot.disabled = false
seeMoreBtnOther.disabled = false


function seeMore(code) {
    var totalPages = document.getElementById(`seeMoreBtn${code}`).name
    totalPages = parseInt(totalPages);
    var page_no_ = 0
    if (code == "Ard") {
        mobileCountArd_++
        page_no_ = mobileCountArd_;
        if (mobileCountArd_ == totalPages) {
            seeMoreBtnArduino.disabled = true
        }
    }
    if (code == "Basic") {
        mobileCountBasic_++
        page_no_ = mobileCountBasic_;
        if (mobileCountBasic_ == totalPages) {
            seeMoreBtnBasic.disabled = true
        }
    }
    if (code == "Iot") {
        mobileCountIot_ = mobileCountIot_++
        page_no_ = mobileCountIot_;
        if (mobileCountIot_ == totalPages) {
            seeMoreBtnIot.disabled = true
        }
    }
    if (code == "Other") {
        mobileCountOther_++
        page_no_ = mobileCountOther_;
        if (mobileCountOther_ ==totalPages) {
            seeMoreBtnOther.disabled = true
        }
    }
    console.log("Arduino Basic IOT OThER", mobileCountArd_, mobileCountBasic_, mobileCountIot_, mobileCountOther_)
    console.log("page no is ", page_no_)

    var url = `${window.origin}/paginate`
    var entry = {
        page_no: page_no_,
        code: code,
        next: true,
        jump_page: false


    }
    var params = {
        method: 'POST',
        body: JSON.stringify(entry),
        cache: 'no-cache',
        headers: new Headers({
            "content-type": "application/json"
        })
    }

    fetch(url, params).then(response => {
        if (response.status == 200) {
            console.log("succesfully_posted")
        }
        else {
            console.log("eroor 404, data not posted")
        }
        response.json().then(data => {

            // console.log(data[thumbnail])
            for (let index = 1; index < 5; index++) {

               if(data['heading'][index]){                
                document.getElementById(`mob${code}`).innerHTML += `  <div class="postMobile mt-3">
                <img src="/static/images/${data['thumbnail'][index]}" class="thumbnailMob "alt="">
                <div class="mobViewContent" >
                <h3>${data['heading'][index]}</h3>
                <p> ${data['description'][index]}</p>
                <a href="" class="streached-link">Read Mor..</a>
                </div>
                </div>`}
            }
        })
    })
}