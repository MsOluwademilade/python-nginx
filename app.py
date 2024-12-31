from flask import Flask

app = Flask(__name__)

MESSAGE = "The Lord is making my feet like hinds' feet"

@app.route('/')
def home():
    html_page = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    magin: 0
                    background-color: #f0f0f0;
                }}
                .message {{
                    font-size: 24px;
                    text-align: center;
                    padding: 20px;
                    background-color: white;
                    border-radius: 10px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
            </style>
        </head>
        <body>
            <div class="message">
                <p>{MESSAGE}</p>
            </div>
        </body>
    </html>
    """
    return html_page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
