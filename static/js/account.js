import * as base from "./base.js";

document.getElementById('file-upload').addEventListener('change', function(event) {
    // show the pfp even if it's not uploaded yet, approach by chatgpt
    if (event.target.files && event.target.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('pfp').src = e.target.result;
        };
        reader.readAsDataURL(event.target.files[0]);
    }
});
