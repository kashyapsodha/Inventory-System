function goBack() {
    if(sessionStorage.getItem("type") == 'admin') {
        window.location = "admin.html";
    } else {
        window.location = "staff.html";
    }
}

function submit() {
    alert("Coffee added successfully");
}
