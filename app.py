from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    # Get the computer's hostname and IP address
    computer_name = socket.gethostname()
    
    try:
        host_ip = subprocess.check_output(['hostname', '-I']).decode('utf-8').split()[0]
    except:
        host_ip = "Could not get host IP"
    
    # Create a simple HTML page
    html_page = f"""
    <html>
        <body>
            <h1>Welcome to my website!</h1>
            <h2>Server Information:</h2>
            <p>Computer Name: {computer_nme}</p>
            <p>IP Address: {compuer_atip}</p>
        </body>
    </html>
    """
    return html_page

# Start the website
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
