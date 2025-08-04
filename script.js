async function sendMessage() {
    let input = document.getElementById("user-input").value;
    let response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input })
    });
    let data = await response.json();
    let box = document.getElementById("chat-box");
    box.innerHTML += "<div>User: " + input + "</div>";
    box.innerHTML += "<div>Grehni: " + data.response + "</div>";
    document.getElementById("user-input").value = "";
    box.scrollTop = box.scrollHeight;
}