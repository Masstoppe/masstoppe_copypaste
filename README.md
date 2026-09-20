# masstoppe_copypaste
Allows copy-paste between mobile device and PC interchangeably

# How to use (with autostart in Windows)

1. Download ***clip_server.pyw*** and put it as a shortcut in shell:starup:
    1.1 WIN+R type **shell:startup**
    1.2 Create new shortcut -> run with source path to pythonw.exe. To find that go into Powershell and type: (Get-Command pythonw).Source.
    1.3 Go into properties of your new shortcut. In the Target field, enter both the path to pythonw.exe and the path to your script, enclosed in quotation marks with a space in between. In the Start field, specify the folder where the script is located.
    1.4 Click Apply and OK. To verify success: double-click the shortcut to test launch it, and run the following in PowerShell: **Get-NetTCPConnection -LocalPort 8765**.

2. Both devices; Install and connect your mobile device and PC on Tailscale with same account.

3. On phone: Install HTTP Shortcuts from Play Store

4. Create Shortcut 1: "Send to PC" Press + and select Standard HTTP Shortcut. URL: http:// :8765/clip Method: POST Go to the Request Body: Select Custom Text. Tap the variable icon ({}) and select the default variable clipboard. Under Feedback/Actions: Activate a short Toast ("Sent to PC"). Create Shortcut 2: "Download from PC" Create a new shortcut. URL: http:// :8765/clip Method: GET During Response Action: Turn on Copy to clipboard. Under Feedback/Actions: Enable Toast ("Copied from PC"). Verification: Manually tap the "Send to PC" shortcut in the app and paste (Ctrl+V) into your computer's notes to confirm that the text appeared.


