function login() {
  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;

  //username = Dexter
  //password = D3xt3r_R0x

  if (username === "Dexter" && password === "D3xt3r_R0x") {
    alert("Welcome Admin!")
  } else {
    alert("Invalid login! Try again and we will find you...");
  }
}