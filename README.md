# 🔒 Ducx Chat  
**1-to-1 Real-Time Video Chat App | FastAPI + WebRTC + Netlify + Render**

DucxVC is a minimal yet powerful **peer-to-peer video chat application** built using **FastAPI** (for WebSocket signaling) and **WebRTC** (for real-time media streaming).  
It enables two users to securely connect and chat face-to-face — directly from the browser, with no plugins or logins required.

---

## 🚀 Live Demo
🌐 **Frontend (Web App):** [https://ducxvc.netlify.app/](https://ducxvc.netlify.app/)  
⚙️ **Backend (FastAPI Signaling):** [https://ducxvc.onrender.com](https://ducxvc.onrender.com)

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML5, CSS3, JavaScript, WebRTC |
| **Backend** | FastAPI (Python 3.11), WebSockets |
| **Signaling** | WebSocket (custom signaling logic in FastAPI) |
| **Deployment** | Render (backend) + Netlify (frontend) |
| **Protocol** | STUN-based peer connection (`stun:stun.l.google.com:19302`) |

---

## 🧠 How It Works

1. A user clicks **"Create Room"** — the backend generates a unique `room_id`.  
2. Another user enters that `room_id` and clicks **"Join Room"**.  
3. Both users connect via the **FastAPI WebSocket** channel.
4. WebRTC negotiates a **P2P connection** using STUN (and optionally TURN).
5. Once ICE candidates resolve, a **direct video/audio connection** is established between the two clients.

No user data or media passes through the server — it only helps peers discover each other.  

---
