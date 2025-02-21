const API_URL = "http://127.0.0.1:5001";

document.getElementById("loginForm")?.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    const response = await fetch(`${API_URL}/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    const data = await response.json();
    if (response.ok) {
        localStorage.setItem("token", data.access_token);
        window.location.href = "/bemvindo";
    } else {
        alert(data.message || "Erro ao fazer login.");
    }
});
document.getElementById("registerForm")?.addEventListener("submit", async (event) => {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const email = document.getElementById("registerEmail").value;
    const password = document.getElementById("registerPassword").value;

    try {
        const response = await fetch(`${API_URL}/auth/register`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, email, password })
        });

        const data = await response.json();
        if (response.ok) {
            alert("Cadastro realizado com sucesso!");
            window.location.href = "/";
        } else {
            alert(data.message || "Erro ao cadastrar.");
        }
    } catch (error) {
        alert("Erro ao conectar ao servidor.");
    }
});

