"use strict";
console.log('dashboard.js connected succesfully')
var type = "";
var intend = ""
var heading = document.getElementById("heading");
var descsription = document.getElementById("description");

var entry;

var quickQuestions = [];
var quickAnswers = [];
var backupQuest = [];
var backupAnswer = [];
var contaQuickAnswers = document.getElementById("conta_quick_answers");
window.countQuickAnswers = 1;

var countIndex = 1;
var contaIndex = document.getElementById("conta_index");
var index_arr = [];
var backupIndex = [];

var para_subheadings = [];
var backupPara = [];
var backupParaSubheading = [];
var paras_arr = [];
var para_thumbnail_arr = [];
var countPara = 1;
var contaPara = document.getElementById("contaPara");

var conclusion = document.getElementById("conclusion");

var faq_q_arr = [];
var backupFaqQ = [];
var backupFaqAns = [];
var faq_ans_arr = [];
var countFaq = 1;

var contaFaq = document.getElementById("contaFaq");

var typeArdBtn = document.getElementById("type_ard");
var typeBasicBtn = document.getElementById("type_basic");
var typeIotBtn = document.getElementById("type_iot");
var typeOtherBtn = document.getElementById("type_other");
var intendInfo = document.getElementById("intend_info");
var intendTuto = document.getElementById("intend_tuto");
var coverImage = document.getElementById("cover_image_uploader");
var file;
var formData;

var html = "";
var returnHtml = "";

var heading1 = ""
var heading2 = ""
var col1_arr = []
var col2_arr = []
var tableRow = ''
var tableHtml = ""
console.log("dashboard js connected succesfully");

// document.getElementById(`li${data2.current}`).classList.add("active")

function conferm(type, id) {
    window.location.assign(`${window.origin}/Delete/${type}/${id}`);
}

function addTable() {
    document.getElementById('tableDiv').style.display = ""
}

function enterTableRows() {
    tableRow = document.getElementById('rowNo').value
    document.getElementById('tableMain').style.display = ""
    document.getElementById('tableS').style.display = ""
    for (let index = 1; index <= tableRow; index++) {
        tableHtml += `       <tr>
        <th scope="row">${index}</th>
        <td><input id="row${index}_1" class="form-control" type="text" name="" value=""></td>
        <td><input id="row${index}_2" class="form-control" type="text" name="" value=""></td>

    </tr>`

    }
    document.getElementById('tableContent').innerHTML = tableHtml
}
if (document.getElementById('coverS')) {

    document.getElementById('coverS').disabled = true
}
var check = 0

function testG() {
    console.log("In dashboard.js", countQuickAnswers)

}

function typeChecked() {
    if (typeArdBtn.checked) {
        type = "Ard";
    }
    if (typeBasicBtn.checked) {
        type = "Basic";
    }
    if (typeIotBtn.checked) {
        type = "Iot";
    }
    if (typeOtherBtn.checked) {
        type = "Other";
    }
    check++
    if (check >= 2) {
        document.getElementById('coverS').disabled = false
    }

}

function intendChecked() {
    if (intendInfo.checked) {
        intend = "Info";
        console.log(type);
    }
    if (intendTuto.checked) {
        intend = "Tuto";
        console.log(type);

    }
    check++
    if (check >= 2) {
        document.getElementById('coverS').disabled = false
    }
}

function uploadImg(type, num) {
    if (type == "cover") {
        formData = new FormData();
        file = coverImage.files[0];
        console.log(file);
        formData.append("file", coverImage.files[0]);

        fetch(`${window.origin}/dashboard_upload/${type}`, {
            method: "POST",
            body: formData,
        }).then((response) => {
            if (response.status == 200) {
                console.log("DOne uploading");
                let name = coverImage.files[0].name;
                name = name.replace(/ /g, "_");
                document.getElementById("test").src = "/static/images/" + name;
                console.log(name);
            } else {
                console.log("error 404");
            }
        });
    }
    if (type == "para") {
        console.log(num);
        const paraImage = document.getElementById(`paraImgUploader${num}`);
        formData = new FormData();
        file = paraImage.files[0];
        console.log(file);
        formData.append("file", paraImage.files[0]);

        fetch(`${window.origin}/dashboard_upload/${type}`, {
            method: "POST",
            body: formData,
        }).then((response) => {
            if (response.status == 200) {
                console.log("DOne uploading");
                let name = paraImage.files[0].name;
                name = name.replace(/ /g, "_");
                document.getElementById(`paraImg${num}`).src = "/static/images/" + name;
                console.log(name);
            } else {
                console.log("error 404");
            }
        });
    }
}


function addNew(type) {
    console.log(type);
    document.getElementById(`${type}Delete`).style.display = "";
    if (type == "quickAnswers") {
        countQuickAnswers++


        console.log(countQuickAnswers);
        contaQuickAnswers.innerHTML += `
        <div id="quickAnswers${countQuickAnswers}">
        
        <label class="text-secondary" for="description"><b>Question</b></label>
        <textarea
        id="quick_question${countQuickAnswers}"
        class="form-control"
        style="width: 50%; margin: 0 auto; border-width: 5px;"
        onblur="backup('quick_question','${countQuickAnswers}')"
        
      rows="1"
      ></textarea>
      <label class="text-secondary mt-3" for="description"><b>Answer</b></label>
      <textarea
      id="quick_answer${countQuickAnswers}"
      class="form-control"
      style="width: 50%; margin: 0 auto; border-width: 5px;"
      onblur="backup('quick_answer','${countQuickAnswers}')"

      rows="2"
      ></textarea>
      
      </div>
      `;
        for (const key in backupQuest) {
            if (backupQuest.hasOwnProperty(key)) {
                const element = backupQuest[key];
                console.log(parseInt(key), element);
                if (element != "") {

                    document.getElementById(
                        `quick_question${parseInt(key)}`
                    ).value = element;
                }
            }
        }
        for (const key in backupAnswer) {
            if (backupAnswer.hasOwnProperty(key)) {
                const element = backupAnswer[key];
                console.log(parseInt(key), element);
                if (element != "") {
                    document.getElementById(
                        `quick_answer${parseInt(key)}`
                    ).value = element;

                }
            }
        }
    }
    if (type == "index") {
        // backupIndex.push(document.getElementById(`index${countIndex}`).value)
        // console.log(backupIndex, document.getElementById(`index${countIndex}`))

        countIndex++;
        contaIndex.innerHTML += `
       

   
        <div class="input-group mb-2 mr-sm-2" style="width: 50%;  margin-left: 26%;" id="indexDiv${countIndex}">
        <div class="input-group-prepend">
          <div class="input-group-text">${countIndex}</div>
        </div>
        <input
          type="text"
          id="index${countIndex}"
          class="form-control"
          onblur="backup('index','${countIndex}')"
          id="inlineFormInputGroupUsername2"
          placeholder="Heading"
        />
      </div>
        `;
        for (const key in backupIndex) {
            if (backupIndex.hasOwnProperty(key)) {
                const element = backupIndex[key];
                console.log(parseInt(key) + 1, element);
                document.getElementById(`index${parseInt(key)}`).value = element;
            }
        }
    }
    if (type == "para") {

        countPara++;

        contaPara.innerHTML += `
    <div id="paraDiv${countPara}">
    <label class="text-secondary mt-2" for="para_heading1"><b>Subheading</b></label>
    <textarea class="form-control" onblur="backup('para_heading','${countPara}')" style="width: 50%; margin:0 auto;border-width:5px;"
     id="para_heading${countPara}" rows="1"></textarea>
    <label class="text-secondary mt-3 " for="para1"><b>Para</b></label>
    <textarea class="form-control" onblur="backup('para','${countPara}')" style="width: 50%; margin:0 auto;border-width:5px;" id="para${countPara}" rows="4"></textarea>
  <!-- *---upload image -->
  <img class="mt-3" id="paraImg${countPara}"   width="40%" alt="upload image">
  <h5 class="text-secondary mt-1">Preview</h5>
    <div class="input-group my-3" style="width: 50%; margin: 0 auto;">
    <input type="file" class="form-control-file" id="paraImgUploader${countPara}">

    <button class="mt-1 btn btn-secondary btn-sm"  onclick="uploadImg('para','${countPara}')">upload</button>
</div>
</div>
   
        `;
        for (const key in backupPara) {
            if (backupPara.hasOwnProperty(key)) {
                const element = backupPara[key];
                console.log(parseInt(key), element);
                if (element != "") {

                    document.getElementById(`para${parseInt(key)}`).value = element;
                }
            }
        }
        for (const key in backupParaSubheading) {
            if (backupParaSubheading.hasOwnProperty(key)) {
                const element = backupParaSubheading[key];
                console.log(parseInt(key), element);
                if (element != "") {

                    document.getElementById(
                        `para_heading${parseInt(key)}`
                    ).value = element;
                }
            }
        }
    }
    if (type == "faq") {


        countFaq++;
        contaFaq.innerHTML += `
       
        <div id="faq${countFaq}">
        <label class="text-secondary mt-2" for="description"><b>Question</b></label>
        <textarea
        id="faq_q${countFaq}"
          class="form-control"
          style="width: 50%; margin: 0 auto; border-width: 5px;"
          onblur="backup('faq_q','${countFaq}')" 
          rows="1"
        ></textarea>
        <label class="text-secondary mt-3" for="description"><b>Answer</b></label>
        <textarea
        id="faq_ans${countFaq}"
          class="form-control"
          style="width: 50%; margin: 0 auto; border-width: 5px;"
          onblur="backup('faq_ans','${countFaq}')" 
          rows="2"
        ></textarea>
        </div>
   
        `;
        for (const key in backupFaqAns) {
            if (backupFaqAns.hasOwnProperty(key)) {
                const element = backupFaqAns[key];
                console.log(parseInt(key), element);
                if (element != "") {
                    document.getElementById(`faq_ans${parseInt(key)}`).value = element;
                }
            }
        }
        for (const key in backupFaqQ) {
            if (backupFaqQ.hasOwnProperty(key)) {
                const element = backupFaqQ[key];
                console.log(parseInt(key), element);
                if (element != "") {

                    document.getElementById(`faq_q${parseInt(key)}`).value = element;
                }
            }
        }
        console.log("Answer=", backupFaqAns)
        console.log("Question=", backupFaqQ)
    }
}

function deletePrev(type) {
    console.log(type);

    if (type == "quickAnswers" || type == "QuickQuestion") {
        console.log(countQuickAnswers);
        document.getElementById(`${type}${countQuickAnswers}`).remove();
        backupQuest[countQuickAnswers] = ""
        backupAnswer[countQuickAnswers] = ""
        countQuickAnswers--;


        if (countQuickAnswers == 1) {
            document.getElementById("quickAnswersDelete").style.display = "none";
        }
    }

    if (type == "index") {
        document.getElementById(`${type}Div${countIndex}`).remove();
        backupIndex[countIndex] = "";
        countIndex--;

        if (countIndex == 1) {
            document.getElementById("indexDelete").style.display = "none";
        }
    }
    if (type == "para") {
        document.getElementById(`${type}Div${countPara}`).remove();
        backupPara[countPara] = "";
        backupParaSubheading[countPara] = "";
        countPara--;

        if (countPara == 1) {
            document.getElementById("paraDelete").style.display = "none";
        }
    }
    if (type == "faq") {
        document.getElementById(`${type}${countFaq}`).remove();
        backupFaqQ[countFaq] = '';
        backupFaqAns[countFaq] = '';
        console.log('After deleteing')
        console.log('faq_Q', backupFaqQ)
        console.log('faq_ans', backupFaqAns)
        countFaq--;

        if (countFaq == 1) {
            document.getElementById("faqDelete").style.display = "none";
        }
    }
}

function submitCreatePost(type_) {
    var url = `${window.origin}/dashboard_create_post/${type_}`;
    if (type_ == 'keyword') {
        entry = {
            keyword: document.getElementById('keyword').value
        }
    }
    if (type_ == "heading") {
        let x = type + intend
        console.log(x)
        entry = {
            heading: heading.value,
            type_: x
        };
    }
    if (type_ == "description") {
        entry = {
            description: descsription.value,
        };
    }
    if (type_ == "quickAnswers") {
        for (let index = 1; index <= countQuickAnswers; index++) {
            console.log(index);
            // console.log(document.getElementById('quick_question1'))
            let quest = document.getElementById(`quick_question${index}`).value;
            quickQuestions.push(quest);
            let answers = document.getElementById(`quick_answer${index}`).value;
            quickAnswers.push(answers);
        }
        entry = {
            quick_questions: quickQuestions,
            quick_answers: quickAnswers,
        };
    }
    if (type_ == "index") {
        for (let index = 1; index <= countIndex; index++) {
            let index_val = document.getElementById(`index${index}`).value;
            index_arr.push(index_val);
        }
        entry = {
            index: index_arr,
        };
    }

    if (type_ == "para") {
        for (let index = 1; index <= countPara; index++) {
            let para_val = document.getElementById(`para${index}`).value;
            paras_arr.push(para_val);
            let para_subheading_val = document.getElementById(`para_heading${index}`).value;
            para_subheadings.push(para_subheading_val);
            let para_thumbnail_val = document.getElementById(`paraImg${index}`)
            para_thumbnail_val = para_thumbnail_val.src.split("/").pop()
            console.log(para_thumbnail_val)
                // para_thumbnail_val.replace(/ /g, "_")
            para_thumbnail_arr.push(para_thumbnail_val)
            console.log(para_thumbnail_arr)
        }
        entry = {
            subheading: para_subheadings,
            para: paras_arr,
            thumbnail: para_thumbnail_arr
        };
    }
    if (type_ == "conclusion") {
        entry = {
            conclusion: conclusion.value,
        };
    }
    if (type_ == "faq") {
        for (let index = 1; index <= countFaq; index++) {
            let faq_q_val = document.getElementById(`faq_q${index}`).value;
            faq_q_arr.push(faq_q_val);
            let faq_ans_val = document.getElementById(`faq_ans${index}`).value;
            faq_ans_arr.push(faq_ans_val);
        }
        entry = {
            faq_q: faq_q_arr,
            faq_ans: faq_ans_arr,
        };
    }
    if (type_ == "table") {
        heading1 = document.getElementById('heading1').value
        heading2 = document.getElementById('heading2').value
        for (let index = 1; index <= tableRow; index++) {
            let col1_val = document.getElementById(`row${index}_1`).value;
            col1_arr.push(col1_val);
            let col2_val = document.getElementById(`row${index}_2`).value;
            col2_arr.push(col2_val);
        }
        console.log(col1_arr, col2_arr)
        entry = {
            heading1: heading1,
            heading2: heading2,
            col1: col1_arr,
            col2: col2_arr
        };
    }

    // ? Posting data below>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    var params = {
        method: "POST",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json",
        }),
    };

    fetch(url, params).then((response) => {
        if (response.status == 200) {
            console.log("succesfully_posted");
            document.getElementById(`${type_}S`).classList.remove('btn-secondary')
            document.getElementById(`${type_}S`).classList.add('btn-outline-success')
        } else {
            console.log("eroor 404, data not posted");
        }
    });
}

function backup(type, num) {
    let val = document.getElementById(`${type}${num}`).value
    if (type == "index") {
        backupIndex[num] = val
    }
    if (type == "para") {
        backupPara[num] = val
    }
    if (type == "para_heading") {
        backupParaSubheading[num] = val
    }
    if (type == "quick_question") {
        backupQuest[num] = val

    }
    if (type == "quick_answer") {
        backupAnswer[num] = val

    }
    if (type == "faq_q") {
        backupFaqQ[num] = val
    }
    if (type == "faq_ans") {
        backupFaqAns[num] = val
    }
}