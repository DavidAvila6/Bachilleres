/**
 * Variables
 */
const chatRoom = document.getElementById('room_uuid').textContent.replaceAll('"', '')

let chatSocket = null


/**
 * Elements
 */

const chatLogElements = document.getElementById('chat_log')
const chatInputElements = document.getElementById('chat_message_input')
const chatSubmitElements = document.getElementById('chat_message_submit')


/**
 * Functions
 */

function scrollToBottom() {
    chatLogElements.scrollTop = chatLogElements.scrollHeight
}


function sendMessage() {
    chatSocket.send(JSON.stringify({
        'type': 'message',
        'message': chatInputElements.value,
        'name': document.getElementById('user_name').textContent.replaceAll('"', ''),
        'agent': document.getElementById('user_id').textContent.replaceAll('"', ''),
    }))

    chatInputElements.value = ''
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


/**
 * Web socket
 */

chatSocket = new WebSocket(`ws://${window.location.host}/ws/${chatRoom}/`)

chatSocket.onmessage = function(e) {
    console.log('on message')

    onChatMessage(JSON.parse(e.data))
}

chatSocket.onopen = function(e) {
    console.log('on open')

    scrollToBottom()
}

chatSocket.onclose = function(e) {
    console.log('chat socket closed unexpectadly',e)
}


/**
 * Event listeners
 */

chatSubmitElements.onclick = function(e) {
    e.preventDefault()

    sendMessage()

    return false
}





