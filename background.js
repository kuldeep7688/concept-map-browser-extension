var websocket;

websocket = new WebSocket(host);
console.log("======== websocket ===========", websocket);

websocket.onopen = function () {
    websocket.send("I exist!");
};

websocket.onmessage = function (event) {
    var received_msg = JSON.parse(event.data);
    var notificationOptions = {
        type: "basic",
        title: received_msg.title,
        message: received_msg.message,
        iconUrl: "extension-icon.png"
    }
    chrome.notifications.create("", notificationOptions);
};

websocket.onclose = function () { alert("==== web socket closed ======"); };
