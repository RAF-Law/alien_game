import * as base from "./base.js";

document.addEventListener("DOMContentLoaded", function () {
    base.stars();

    base.loginGlitching("registerFrame_bg",2,80);
})

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

document.getElementById("user_form").addEventListener("submit", function(event) {
    event.preventDefault();

    let form = event.target;
    let formData = new FormData(form);
    
    fetch(form.action, {
        method: "POST",
        body: formData
    })
    .then(response => {
        const contentType = response.headers.get("content-type");
        if (contentType && contentType.includes("application/json")) {
            return response.json();
        } else {
            return response;
        }
    })
    .then(data => {
        if (data.status === "error") {
            let errorMessages = "";
            
            let errors = JSON.parse(data.errors.user_form_errors);
            let profileErrors = JSON.parse(data.errors.profile_form_errors);

            Object.keys(errors).forEach(field => {
                errors[field].forEach(error => {
                    errorMessages += `${field}: ${error.message}\n`;
                });
            });

            Object.keys(profileErrors).forEach(field => {
                profileErrors[field].forEach(error => {
                    errorMessages += `${field}: ${error.message}\n`;
                });
            });

            alert(errorMessages); 
        } else { //if no error then update the page. This is so life-costing..
            document.getElementById("unreg").style.display = "none";
            document.body.insertAdjacentHTML("beforeend", `
                <div class="registration_complete_text">
                    <p>Congratulations... </p>
                    <p>Your registration has been successful</p>
                    <p>Now are you ready to engage in the world...</p>
                    <p>invaded by us aliens...?</p>
                </div>
            `);
        }
    })
});