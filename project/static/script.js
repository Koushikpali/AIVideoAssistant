async function processVideo() {
  const source = document.getElementById("source").value.trim();
  const language = document.getElementById("language").value;
  const btn = document.getElementById("process-btn");
  const loadingText = document.getElementById("loading-text");
  const errorText = document.getElementById("error-text");
  const resultsSection = document.getElementById("results-section");
  const chatSection = document.getElementById("chat-section");

  // Reset
  errorText.classList.add("hidden");
  errorText.textContent = "";
  resultsSection.classList.add("hidden");
  chatSection.classList.add("hidden");

  if (!source) {
    errorText.textContent = "Please enter a YouTube URL or file path.";
    errorText.classList.remove("hidden");
    return;
  }

  btn.disabled = true;
  loadingText.classList.remove("hidden");

  try {
    const response = await fetch("/api/process", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ source, language }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Failed to process video.");
    }

    document.getElementById("result-title").textContent = data.title || "—";
    document.getElementById("result-summary").textContent = data.summary || "—";
    document.getElementById("result-actions").textContent = data.action_items || "—";
    document.getElementById("result-decisions").textContent = data.key_decisions || "—";
    document.getElementById("result-questions").textContent = data.open_questions || "—";

    resultsSection.classList.remove("hidden");
    chatSection.classList.remove("hidden");

    // Clear old chat history on new process
    document.getElementById("chat-history").innerHTML = "";
  } catch (err) {
    errorText.textContent = err.message || "An unexpected error occurred.";
    errorText.classList.remove("hidden");
  } finally {
    btn.disabled = false;
    loadingText.classList.add("hidden");
  }
}

function handleChatKey(event) {
  if (event.key === "Enter") {
    sendMessage();
  }
}

async function sendMessage() {
  const input = document.getElementById("chat-input");
  const sendBtn = document.getElementById("send-btn");
  const chatHistory = document.getElementById("chat-history");
  const question = input.value.trim();

  if (!question) return;

  // Append user message
  appendMessage(chatHistory, "user", "You", question);
  input.value = "";
  input.disabled = true;
  sendBtn.disabled = true;

  // Placeholder for assistant
  const assistantMsg = appendMessage(chatHistory, "assistant", "Assistant", "Thinking...");

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });

    const data = await response.json();

    if (!response.ok) {
      assistantMsg.querySelector(".chat-msg-text").textContent =
        data.error || "Failed to get a response.";
    } else {
      assistantMsg.querySelector(".chat-msg-text").textContent = data.answer || "—";
    }
  } catch (err) {
    assistantMsg.querySelector(".chat-msg-text").textContent =
      "Network error. Please try again.";
  } finally {
    input.disabled = false;
    sendBtn.disabled = false;
    input.focus();
    chatHistory.scrollTop = chatHistory.scrollHeight;
  }
}

function appendMessage(container, role, label, text) {
  const msg = document.createElement("div");
  msg.className = "chat-msg " + role;

  const labelEl = document.createElement("div");
  labelEl.className = "chat-msg-label";
  labelEl.textContent = label;

  const textEl = document.createElement("div");
  textEl.className = "chat-msg-text";
  textEl.textContent = text;

  msg.appendChild(labelEl);
  msg.appendChild(textEl);
  container.appendChild(msg);
  container.scrollTop = container.scrollHeight;

  return msg;
}
