console.log("Text editor .js is succesfully attached")
var content;


tinymce.init({
    selector: "textarea.tinymce",
    theme: "modern",
    skin: "lightgray",
    height: "70vh",
    width: "70vw",
    plugins: "codesample code lists advlist autolink  charmap code emoticons hr image insertdatetime link media paste preview searchreplace table textpattern toc visualblocks visualchars wordcount ",
    codesample_languages: [
        { text: 'HTML/XML', value: 'markup' },
        { text: 'JavaScript', value: 'javascript' },
        { text: 'CSS', value: 'css' },
        { text: 'PHP', value: 'php' },
        { text: 'Python', value: 'python' },
        { text: 'Java', value: 'java' },
        { text: 'C', value: 'c' },
        { text: 'C#', value: 'csharp' },
        { text: 'C++', value: 'cpp' },
        { text: 'arduino', value: 'arduino' }
    ],
    toolbar: "codesample code |code preview | undo redo | formatselect | fontselect | fontsizeselect | bold italic underline strikethrough backcolor | subscript superscript | numlist bullist | alignleft aligncenter alignright alignjustify | outdent indent | paste searchreplace | toc link image media charmap insertdatetime emoticons hr | table tabledelete | tableprops tablerowprops tablecellprops | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol | removeformat",
    insertdatetime_element: true,
    media_scripts: [{
        filter: 'platform.twitter.com'
    }, {
        filter: 's.imgur.com'
    }, {
        filter: 'instagram.com'
    }, {
        filter: 'https://platform.twitter.com/widgets.js'
    }, ],
    browser_spellcheck: true,
    contextmenu: false,

})
var url = ""

function submit(version, type = 0, id = 0) {
    content = tinymce.get('texteditor').getContent();
    if (version == "new") {
        url = `${window.origin}/dashboard/submit-article`;
    } else {
        url = `${window.origin}/save_edited/${id}/${type}`;

    }
    var entry = {
        article: content
    };

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
            alert("Successfully posted")
            response.json().then(data => {

                window.location.href = `${window.origin}${data}`;
            });

        } else {
            console.log("eroor 404, data not posted");
        }
    });
}