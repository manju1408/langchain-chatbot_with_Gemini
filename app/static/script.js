async function sendMessage() {
  const input = document.getElementById("message-input");
  const chatBox = document.getElementById("chat-box");
  const userMessage = input.value.trim();

  if (!userMessage) return;

  // Display user's message
  chatBox.innerHTML += `<div class="text-right"><strong>You:</strong> ${userMessage}</div>`;
  input.value = "";

  // Send message to Flask backend
  try {
    const response = await fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: userMessage })
    });

    const data = await response.json();

    if (data.answer) {
      chatBox.innerHTML += `<div><strong>Gemini:</strong> ${data.answer}</div>`;
    } else {
      chatBox.innerHTML += `<div class="text-red-600"><strong>Error:</strong> ${data.error}</div>`;
    }
  } catch (err) {
    chatBox.innerHTML += `<div class="text-red-600"><strong>Network error:</strong> ${err.message}</div>`;
  }

  chatBox.scrollTop = chatBox.scrollHeight;
}
