# 📋 masstoppe_copypaste

Seamlessly sync and share your clipboard between your mobile device and Windows PC using a lightweight local Python server and Tailscale.

---

## ⚡ Prerequisites

- **Python 3.x** installed on Windows
- **Python dependency**:
  ```powershell
  pip install pyperclip
  ```
- **[Tailscale](https://tailscale.com/)** installed and signed into the same account on both PC & Phone
- **[HTTP Shortcuts](https://play.google.com/store/apps/details?id=ch.rmy.android.http_shortcuts)** installed on your Android phone

---

## 🚀 Setup Guide

### Step 1: Windows Autostart Configuration

Make the background server run automatically on boot:

1. Press <kbd>Win</kbd> + <kbd>R</kbd>, type `shell:startup`, and press <kbd>Enter</kbd>.
2. Right-click inside the folder $\rightarrow$ **New** $\rightarrow$ **Shortcut**.
3. Find your `pythonw.exe` path by running this in PowerShell:
   ```powershell
   (Get-Command pythonw).Source
   ```
4. Configure the shortcut properties:
   - **Target**: Enter the path to `pythonw.exe` followed by the path to `clip_server.pyw` (both in quotes):
     ```text
     "C:\Path\To\pythonw.exe" "C:\Path\To\clip_server.pyw"
     ```
   - **Start in**: The directory where `clip_server.pyw` is stored:
     ```text
     "C:\Path\To\"
     ```
5. Click **Apply** and **OK**.

> [!TIP]
> **Verify Server Running**: Double-click the shortcut to test it. Then run:
> ```powershell
> Get-NetTCPConnection -LocalPort 8765
> ```
> If the state shows `Listen`, your server is active!

---

### Step 2: Tailscale Network Connection

1. Ensure **Tailscale** is connected on both your PC and Mobile.
2. Note down your PC's **Tailscale IP address** (e.g., `100.x.y.z`).

---

### Step 3: Phone Setup (HTTP Shortcuts App)

Open **HTTP Shortcuts** on your phone and create two shortcuts:

#### 📤 Shortcut 1: "Send to PC" (Upload Phone Clipboard $\rightarrow$ PC)
- **Shortcut Type**: Standard HTTP Shortcut
- **Method**: `POST`
- **URL**: `http://<YOUR_PC_TAILSCALE_IP>:8765/clip`
- **Request Body**:
  - Type: **Custom Text**
  - Tap the `{}` variable icon and select **Clipboard**
- **Feedback / Actions**:
  - Show Toast: `"Sent to PC"`

#### 📥 Shortcut 2: "Download from PC" (Fetch PC Clipboard $\rightarrow$ Phone)
- **Shortcut Type**: Standard HTTP Shortcut
- **Method**: `GET`
- **URL**: `http://<YOUR_PC_TAILSCALE_IP>:8765/clip`
- **Response Actions**:
  - Enable **Copy to clipboard**
- **Feedback / Actions**:
  - Show Toast: `"Copied from PC"`

---

## 🧪 Testing

1. On your phone, copy any text and tap **"Send to PC"**. Press <kbd>Ctrl</kbd> + <kbd>V</kbd> on your PC to verify.
2. On your PC, copy any text. Tap **"Download from PC"** on your phone and paste to verify.
