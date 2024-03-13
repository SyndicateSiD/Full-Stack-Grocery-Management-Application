// Define your API endpoints
var loginApiUrl = 'http://127.0.0.1:5000/login';

function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Form data
    var formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    fetch(loginApiUrl, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Redirect to welcome.html after successful login
            window.location.href = 'welcome.html';
        } else {
            // Show error message for failed login
            document.getElementById("loginStatus").innerHTML = data.message;
        }
    });
}
