import * as base from "./base.js";

document.getElementById("login_form").addEventListener("submit", function(event) { //by chatgpt
    event.preventDefault(); // Prevent default form submission

    let form = event.target;
    let formData = new FormData(form);
    
    fetch(form.action, {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "error") {
            alert(data.message);  // Show alert only on invalid login
        } else {
            form.submit();  // Allow normal form submission on success
        }
    })
});

document.addEventListener("DOMContentLoaded", function () {
    base.stars();

    base.loginGlitching("loginFrame_bg",2,80);
})