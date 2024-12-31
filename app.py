from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():

    computer_name = socket.gethostname()
    computer_ip = socket.gethostbyname(computer_name)
    

    html_page = f"""
    <html>
        <body>
            <h1>Welcome to my website!</h1>
            <h2>Server Information:</h2>
            <p>Computer Name: {computer_name}</p>
            <p>IP Address: {computer_ip}</p>
        </body>
    </html>
    """
    return html_page


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
