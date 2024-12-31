from flask import Flask
import socket
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    
    computer_name = socket.gethostname()
    
    try:
        host_ip = subprocess.check_output(['hostname', '-I']).decode('utf-8').split()[0]
    except:
        host_ip = "Could not get host IP"
    
    html_page = f"""
    <html>
        <body>
            <h1>Welcome to my website!</h1>
            <h2>Server Information:</h2>
           <p>Computer Name: {computer_name}</p>
            <p>IP Address: {host_ip}</p>
        </body>
    </html>
    """
    return html_page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
