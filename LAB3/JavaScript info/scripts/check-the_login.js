let userLogin = prompt("Enter your login");

if (userLogin === "Admin") {
    adminPassword = prompt("Enter password");

    if( adminPassword === "TheMaster") alert("Welcome!")
    else if(adminPassword === "" || adminPassword == null){
        alert ("Canceled")
    }
    else{
        alert("Wrong password")
    }
}
else if (userLogin === "" || userLogin == null){
    alert("Canceled");
}
else{
    alert("I dont know you");
}