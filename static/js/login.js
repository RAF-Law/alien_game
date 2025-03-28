import * as base from "./base.js";
//alert box stuff
document.getElementById("login_form").addEventListener("submit", function(event) { //by chatgpt
    event.preventDefault(); // if you remove this, the form is always submitted and it gives you a json content page back

    let form = event.target;
    let formData = new FormData(form);
    
    fetch(form.action, {
        method: "POST",
        body: formData
    })
    .then(response => {
        // Check if response is JSON before attempting to parse, preventing lagging-login
        const contentType = response.headers.get("content-type");
        if (contentType && contentType.includes("application/json")) {
            return response.json();
        } else {
            // If response is not JSON (successful login), allow normal form submission
            window.location.href = response.url;
            return;
        }
    })
    .then(data => {
        if (data.status === "error") {
            alert(data.message);  // Show alert only on invalid login
        }
    })
});

document.addEventListener("DOMContentLoaded", function () {
    base.stars();

    base.loginGlitching("loginFrame_bg",2,80);
})