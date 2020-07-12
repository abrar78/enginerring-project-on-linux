"use strict";
console.log('dashboard.js connected succesfully')
var type = "";
var intend = ""
window.totalType = ""
var heading = document.getElementById("heading");
var descsription = document.getElementById("description");

var entry;

var quickQuestions = [];
var quickAnswers = [];
var backupQuest = [];
var backupAnswer = [];
var contaQuickAnswers = document.getElementById("conta_quick_answers");
window.countQuickAnswers = 1;

window.countCode = 1
var backupCode = []
var backupCodeLanguage = []
var backupCodeHeading = []

window.countIndex = 1;
var contaIndex = document.getElementById("conta_index");
var index_arr = [];
var backupIndex = [];

var para_subheadings = [];
var backupPara = [];
var backupParaSubheading = [];
var backupParaImgDescription = [];
var paras_arr = [];
var para_thumbnail_arr = [];
var para_thumbnail_desc_arr = [];
window.countPara = 1;
var contaPara = document.getElementById("contaPara");

var conclusion = document.getElementById("conclusion");

var faq_q_arr = [];
var backupFaqQ = [];
var backupFaqAns = [];
var faq_ans_arr = [];
var countFaq = 1;
window.contaFaq = document.getElementById("contaFaq");

var typeArdBtn = document.getElementById("type_ard");
var typeBasicBtn = document.getElementById("type_basic");
var typeIotBtn = document.getElementById("type_iot");
var typeOtherBtn = document.getElementById("type_other");
var intendInfo = document.getElementById("intend_info");
var intendTuto = document.getElementById("intend_tuto");
var coverImage = document.getElementById("cover_image_uploader");
var thumbnail = document.getElementById("thumbnail_uploader");
var file;
var formData;

var code_arr = []
var codeLanguage_arr = []
var codeHeading_arr = []

var html = "";
var returnHtml = "";

var heading1 = ""
var heading2 = ""
var col1_arr = []
var col2_arr = []
window.tableRow = 0
var tableHtml = ""


// document.getElementById(`li${data2.current}`).classList.add("active")

function conferm(type, id) {
    window.location.assign(`${window.origin}/Delete/${type}/${id}`);
}

function addTable() {
    document.getElementById('tableDiv').style.display = ""
}

function enterTableRows() {
    tableHtml = ""
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
if (document.getElementById('typeS')) {

    document.getElementById('typeS').disabled = true
}
var check = 0



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
        document.getElementById('typeS').disabled = false
    }

}

function intendChecked() {
    if (intendInfo.checked) {
        intend = "Info";

    }
    if (intendTuto.checked) {
        intend = "Tuto";


    }
    check++
    if (check >= 2) {
        document.getElementById('typeS').disabled = false
    }
}

function uploadImg(type, num) {
    if (type == "cover") {
        formData = new FormData();
        file = coverImage.files[0];
        formData.append("file", coverImage.files[0]);

        fetch(`${window.origin}/dashboard_upload/${type}`, {
            method: "POST",
            body: formData,
        }).then((response) => {
            if (response.status == 200) {
                let name = coverImage.files[0].name;
                name = name.replace(/ /g, "_");
                document.getElementById("cover").src = "/static/images/" + name;
            } else {
                console.log("error 404");
            }
        });
    }
    if (type == "thumbnail") {
        formData = new FormData();
        file = thumbnail.files[0];
        formData.append("file", thumbnail.files[0]);

        fetch(`${window.origin}/dashboard_upload/${type}`, {
            method: "POST",
            body: formData,
        }).then((response) => {
            if (response.status == 200) {
                let name = thumbnail.files[0].name;
                name = name.replace(/ /g, "_");
                document.getElementById("thumbnail").src = "/static/images/" + name;

            } else {
                console.log("error 404");
            }
        });
    }
    if (type == "para") {
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
        <div id="quickAnswersDiv${countQuickAnswers}">
        
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

    if (type == "faq") {


        countFaq++;
        contaFaq.innerHTML += `
       
        <div id="faqDiv${countFaq}">
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
    if (type == "code") {


        countCode++;
        contaCode.innerHTML += `
       
        <div class="my-3" id="codeDiv${countCode}">
        
        <textarea class="form-control" style="width: 50%; margin: 0 auto; border-width: 5px;" id="codeHeading${countCode}" placeholder="Heading" onblur="backup('codeHeading','${countCode}')" rows="1"></textarea>

        <textarea class="form-control" style="width: 50%; margin: 0 auto; border-width: 5px;" id="code${countCode}" placeholder="Source-code" onblur="backup('code','${countCode}')" rows="9"></textarea>
        <textarea placeholder="Language of code" class="form-control" style="width: 50%; margin: 0 auto; border-width: 5px;" onblur="backup('language','${countCode}')" id="language${countCode}" rows="1"></textarea>

    </div>
   
        `;
        for (const key in backupCode) {
            if (backupCode.hasOwnProperty(key)) {
                const element = backupCode[key];
                console.log(parseInt(key), element);
                if (element != "") {
                    document.getElementById(`code${parseInt(key)}`).value = element;
                }
            }
        }
        for (const key in backupCodeLanguage) {
            if (backupCodeLanguage.hasOwnProperty(key)) {
                const element = backupCodeLanguage[key];
                console.log(parseInt(key), element);
                if (element != "") {

                    document.getElementById(`language${parseInt(key)}`).value = element;
                }
            }
        }
        for (const key in backupCodeHeading) {
            if (backupCodeHeading.hasOwnProperty(key)) {
                const element = backupCodeHeading[key];
                console.log(parseInt(key), element);
                if (element != "") {

                    document.getElementById(`codeHeading${parseInt(key)}`).value = element;
                }
            }
        }

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
    if (type == "code") {
        document.getElementById(`${type}Div${countCode}`).remove();
        backupCode[countCode] = "";
        backupCodeLanguage[countCode] = "";
        backupCodeHeading[countCode] = "";
        countCode--;


        if (countCode == 1) {
            document.getElementById("codeDelete").style.display = "none";
        }
    }
    if (type == "para") {
        document.getElementById(`${type}Div${countPara}`).remove();
        backupPara[countPara] = "";
        backupParaSubheading[countPara] = "";
        backupParaImgDescription[countPara] = "";
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
    if (type_ == "coverImgDescription") {
        entry = {
            coverImgDescription: document.getElementById('coverImgDescription').value
        }
    }
    if (type_ == "url") {
        entry = {
            url: document.getElementById('url').value
        }
    }
    if (type_ == "title") {
        entry = {
            title: document.getElementById('title').value
        }
    }
    if (type_ == "keywordsMeta") {
        entry = {
            meta_keywords: document.getElementById('keywordsMeta').value
        }
    }

    if (type_ == "keyword") {
        console.log("in keywords")
        entry = {
            keyword: document.getElementById('keyword').value
        }
    }
    if (type_ == "heading") {
        totalType = type + intend
        console.log(totalType)
        entry = {
            heading: heading.value,
            type_: totalType
        };
    }
    if (type_ == "type") {
        totalType = type + intend
        console.log(totalType)
        entry = {
            heading: heading.value,
            type_: totalType
        };
    }
    if (type_ == "description") {
        entry = {
            description: descsription.value,
        };
    }
    if (type_ == "quickAnswers") {
        quickQuestions = []
        quickAnswers = []
        console.log(countQuickAnswers)
        for (let index = 1; index <= countQuickAnswers; index++) {
            console.log(index);
            // console.log(document.getElementById('quick_question1'))
            if (document.getElementById(`quick_question${index}`)) {
                let quest = document.getElementById(`quick_question${index}`).value;
                quickQuestions.push(quest);
            }
            if (document.getElementById(`quick_answer${index}`)) {
                let answers = document.getElementById(`quick_answer${index}`).value;
                quickAnswers.push(answers);
            }
        }
        entry = {
            quick_questions: quickQuestions,
            quick_answers: quickAnswers,
        };
    }
    if (type_ == "index") {
        index_arr = []
        for (let index = 1; index <= countIndex; index++) {
            if (document.getElementById(`index${index}`)) {
                let index_val = document.getElementById(`index${index}`).value;
                index_arr.push(index_val);
            }
        }
        entry = {
            index: index_arr,
        };
    }


    if (type_ == "faq") {
        faq_q_arr = []
        faq_ans_arr = []
        console.log(countFaq)
        for (let index = 1; index <= countFaq; index++) {
            if (document.getElementById(`faq_q${index}`)) {

                let faq_q_val = document.getElementById(`faq_q${index}`).value;
                faq_q_arr.push(faq_q_val);
            }
            if (document.getElementById(`faq_ans${index}`)) {

                let faq_ans_val = document.getElementById(`faq_ans${index}`).value;
                faq_ans_arr.push(faq_ans_val);
            }
        }
        entry = {
            faq_q: faq_q_arr,
            faq_ans: faq_ans_arr,
        };
    }
    if (type_ == "code") {
        console.log("IN CODE")
        code_arr = []
        codeLanguage_arr = []
        codeHeading_arr = []
        for (let index = 1; index <= countCode; index++) {
            console.log("IN FOR")
            let code_val = document.getElementById(`code${index}`).value;
            code_arr.push(code_val);
            let language_val = document.getElementById(`language${index}`).value;
            codeLanguage_arr.push(language_val);
            let codeHeading_val = document.getElementById(`codeHeading${index}`).value;
            codeHeading_arr.push(codeHeading_val);
        }
        entry = {
            source_code: code_arr,
            language: codeLanguage_arr,
            code_heading: codeHeading_arr
        }
    }
    if (type_ == "table") {
        heading1 = document.getElementById('heading1').value
        heading2 = document.getElementById('heading2').value
        col1_arr = []
        col2_arr = []
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
            if (document.getElementById(`${type_}S`)) {
                document.getElementById(`${type_}S`).classList.remove('btn-secondary')
                document.getElementById(`${type_}S`).classList.add('btn-outline-success')
            }
        } else {
            console.log("eroor 404, data not posted");
        }
    });
}

// function newTable() {
//     document.getElementById('tableDiv').remove()
// }

function backup(type, num) {
    let val = document.getElementById(`${type}${num}`).value

    if (type == "index") {
        backupIndex[num] = val
    }
    if (type == "code") {
        backupCode[num] = val
    }
    if (type == "language") {
        backupCodeLanguage[num] = val
    }
    if (type == "codeHeading") {
        backupCodeHeading[num] = val
    }
    if (type == "para") {
        backupPara[num] = val
    }
    if (type == "para_heading") {
        backupParaSubheading[num] = val
    }
    if (type == "para_imgDescription") {
        backupParaImgDescription[num] = val
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

function deleteThis(type_, num, id, post_type) {
    console.log(`${type_}Div${num}`)
    document.getElementById(`${type_}Div${num}`).remove()
    entry = {
        id: id,
        type: type_,
        post_type: post_type
    }
    var params = {
        method: "POST",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json",
        }),
    };
    var url = `${window.origin}/delete_item`;
    fetch(url, params).then((response) => {
        if (response.status == 200) {
            console.log("succesfully_posted");
            if (type_ == 'table') {
                location.reload()
            }

        } else {
            console.log("eroor 404, data not posted");
        }
    });

}