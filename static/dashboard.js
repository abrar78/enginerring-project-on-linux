'use strict'
console.log("dashboard js connected succesfully")

function conferm(type, id) {


    window.location.assign(`${window.origin}/Delete/${type}/${id}`);


}
var type = "";

var typeArdBtn = document.getElementById('type_ard')
var typeBasicBtn = document.getElementById('type_basic')
var typeIotBtn = document.getElementById('type_iot')
var typeOtherBtn = document.getElementById('type_other')

function typeChecked() {
    if (typeArdBtn.checked) {

        type = 'Ard'
    }
    if (typeBasicBtn.checked) {

        type = 'Basic'
    }
    if (typeIotBtn.checked) {

        type = 'Iot'
    }
    if (typeOtherBtn.checked) {

        type = 'Other'
    }
}

var intendInfo = document.getElementById('intend_info')
var intendTuto = document.getElementById('intend_tuto')

function intendChecked() {
    if (intendInfo.checked) {

        type = type + 'Info'
        console.log(type)
    }
    if (intendTuto.checked) {

        type = type + 'Tuto'
        console.log(type)

    }
}
var coverImage = document.getElementById('cover_image_uploader')
var file;
var formData;

function previewCoverImg(name) {
    document.getElementById('test').src = "/home/abrar/Desktop/Abrar/myBlog/engineering-blog-repository-master/static/images/" + name
}

function uploadCoverImg() {


    formData = new FormData();
    file = coverImage.files[0]
    console.log(file)
    formData.append("file", coverImage.files[0])

    fetch(`${window.origin}/dashboard_upload`, { method: "POST", body: formData }).then((response) => {
        if (response.status == 200) {
            console.log("DOne uploading")
            let name = coverImage.files[0].name
            name = name.replace(/ /g, "_")
            document.getElementById('test').src = "/static/images/" + name
            console.log(name)



        } else {

            console.log("error 404")

        }
    });
}
var heading = document.getElementById('heading')
var descsription = document.getElementById('description')

var quickQuestion1 = document.getElementById('quick_question1')
var quickAnswer1 = document.getElementById('quick_answer1')
var addQ_aBtn = document.getElementById('add_q_a_btn')

var index_1 = document.getElementById('index_1')

var para_subheading1 = document.getElementById('para_subheading1')
var para1 = document.getElementById('para1')