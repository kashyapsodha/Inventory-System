function login() {
    var email = document.getElementById("inputEmail").value;
    var password = document.getElementById("inputPassword").value;

    console.log(email);
    console.log(password);

    if(email == "admin" && password == "qwerty123") {
        window.location = 'admin.html';
        console.log("Hi");
    } else if(email == "staff" && password == "qwerty123") {
        window.location = "staff.html";
    } else {
        alert("Invalid Credentials");
    }
}

