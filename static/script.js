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

// Change Password
document.getElementById("changePasswordForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const oldPassword = document.getElementById("oldPassword").value;
    const newPassword = document.getElementById("newPassword").value;
    const token = localStorage.getItem("token");

    const response = await fetch(`${API_URL}/auth/change_password`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ old_password: oldPassword, new_password: newPassword })
    });
    const data = await response.json();
    alert(data.message);
    if (response.ok) window.location.href = "/bemvindo";
});

// Forgot Password
document.getElementById("forgotPasswordForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const response = await fetch(`${API_URL}/auth/forgot_password`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email })
    });
    const data = await response.json();
    alert(data.reset_token ? `Token: ${data.reset_token}` : data.message);
    if (response.ok) window.location.href = "/redefinir_senha";
});

// Reset Password
document.getElementById("resetPasswordForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const resetToken = document.getElementById("resetToken").value;
    const newPassword = document.getElementById("newPassword").value;
    const response = await fetch(`${API_URL}/auth/reset_password`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ reset_token: resetToken, new_password: newPassword })
    });
    const data = await response.json();
    alert(data.message);
    if (response.ok) window.location.href = "/";
});

// Exibir nome do usuário na página bem-vindo
if (window.location.pathname === '/bemvindo') {
    const token = localStorage.getItem('token');
    if (!token) window.location.href = '/';

    fetch(`${API_URL}/api/dados_protegidos`, {
        headers: { 'Authorization': `Bearer ${token}` }
    })
    .then(response => {
        if (!response.ok) throw new Error('Não autorizado');
        return response.json();
    })
    .then(data => {
        document.getElementById('username').textContent = data.username;
    })
    .catch(() => {
        localStorage.removeItem('token');
        window.location.href = '/';
    });
}

// Logout
document.getElementById("logout")?.addEventListener("click", () => {
    localStorage.removeItem("token");
    window.location.href = "/";
});