// Define your API endpoints
var registerApiUrl = 'http://127.0.0.1:5000/register';

function register() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Form data
    var formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    fetch(registerApiUrl, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Show success message or redirect if needed
            document.getElementById("registerStatus").innerHTML = "Registration successful!";
        } else {
            // Show error message for failed registration
            document.getElementById("registerStatus").innerHTML = data.message;
        }
    });
}
