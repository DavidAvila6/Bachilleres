/**
 *  Variables
 */

let chatName = "";
let chatSocket = null;
let chatWindowUrl = window.location.href;
let chatRoomUuid = Math.random().toString(36).slice(2, 12);

console.log(chatRoomUuid);

/*
    Elements
*/

const chatElements = document.getElementById("chat");
const chatOpenElements = document.getElementById("chat_open");
const chatJoinElements = document.getElementById("chat_join");
const chatIconElements = document.getElementById("chat_icon");
const chatWelcomeElements = document.getElementById("chat_welcome");
const chatRoomElements = document.getElementById("chat_room");
const chatNameElements = document.getElementById("chat_name");
const chatLogElements = document.getElementById("chat_log");
const chatInputElement = document.getElementById("chat_message_input");
const chatSubmitElement = document.getElementById("chat_message_submit");

/**
 *  Funtions
 */

function getCookie(name) {
  var cookieValue = null;

  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();

      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));

        break;
      }
    }
  }

  return cookieValue;
}

function sendMessage() {
  chatSocket.send(
    JSON.stringify({
      type: "message",
      message: chatInputElement.value,
      name: chatName,
    })
  );

  chatInputElement.value = "";
}

function onChatMessage(data) {
  console.log("onChatMessage", data);

  if (data.type == "chat_message") {
    if (data.agent) {
    } else {
      chatLogElements.innerHTML += `
      <div class="d-flex  mt-2" justify-content-end>
        <div class=" flex-shrink-1 mt-2 px-2">
            ${data.initials}
        </div>
        <div class="bg-primary mx-1">
            <p>${data.message}</p>
        </div>
        <div class="d-flex mx-1">
            <span>${data.created_at} ago</span>
        </div>
      </div>
      `;
    }
  }
}

async function joinRooms() {
  console.log("JoinRooms");

  chatName = chatNameElements.value;

  console.log("Join as ", chatName);
  console.log("room uuid", chatRoomUuid);

  const data = new FormData();

  data.append("name", chatName);
  data.append("url", chatWindowUrl);

  await fetch(`/api/create-room/${chatRoomUuid}/`, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: data,
  })
    .then(function (res) {
      return res.json();
    })
    .then(function (data) {
      console.log("data", data);
    });

  chatSocket = new WebSocket(
    `ws://${window.location.host}/ws/${chatRoomUuid}/`
  );

  chatSocket.onmessage = function (e) {
    console.log("onMessage");

    onChatMessage(JSON.parse(e.data));
  };

  chatSocket.onopen = function (e) {
    console.log("onOpen - chat socket was opened");

    // scrollToBottom();
  };

  chatSocket.onclose = function (e) {
    console.log("onClose - chat socket was closed");
  };
}

/**
 *  Event listener
 */

chatOpenElements.onclick = function (e) {
  e.preventDefault();
  chatIconElements.classList.add("d-none");
  chatWelcomeElements.classList.remove("d-none");

  return false;
};

chatJoinElements.onclick = function (e) {
  e.preventDefault();
  chatWelcomeElements.classList.add("d-none");
  chatRoomElements.classList.remove("d-none");
  joinRooms();
  return false;
};

chatSubmitElement.onclick = function (e) {
  e.preventDefault();

  sendMessage();

  return false;
};
