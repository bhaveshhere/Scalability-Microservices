const userServiceUrl = "http://localhost:8007";  // URL for user-service
const postServiceUrl = "http://localhost:8001";  // URL for post-service
const followServiceUrl = "http://localhost:8003";  // URL for follow-service
const notificationServiceUrl = "http://localhost:8004";  // URL for notification-service

// Function to fetch user info
function getUserInfo() {
    fetch(`${userServiceUrl}/user-info`) // Adjust the endpoint as per your service
        .then(response => response.json())
        .then(data => {
            document.getElementById("user-info").innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => {
            document.getElementById("user-info").innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
        });
}

// Function to create a post
function createPost() {
    fetch(`${postServiceUrl}/create-post`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title: 'My New Post', content: 'This is a post content' })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("post-info").innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    })
    .catch(error => {
        document.getElementById("post-info").innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    });
}

// Function to follow a user
function followUser() {
    fetch(`${followServiceUrl}/follow`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ userId: 1, followId: 2 })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("follow-info").innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    })
    .catch(error => {
        document.getElementById("follow-info").innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    });
}

// Function to send a notification
function sendNotification() {
    fetch(`${notificationServiceUrl}/send-notification`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ userId: 1, message: 'This is a test notification' })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("notification-info").innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    })
    .catch(error => {
        document.getElementById("notification-info").innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    });
}
