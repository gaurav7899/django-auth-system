const form = document.getElementById("reset-password-form")
const submitbtn = document.getElementById("submit-btn")

form.addEventListener("submit",function(event){
    submitbtn.disabled = true;
    submitbtn.innerHTML = 'Sending......'
})