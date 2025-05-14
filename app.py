from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Deployment Status</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #00b09b, #96c93d);
                color: white;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
            }
            .message-box {
                background: rgba(0, 0, 0, 0.3);
                padding: 50px;
                border-radius: 12px;
                text-align: center;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 0.5em;
            }
            p {
                font-size: 1.3rem;
            }
        </style>
    </head>
    <body>
        <div class="message-box">
            <h1>🚀 Success!</h1>
            <p>CICD Pipeline with GitHub + AWS Codepipeline + ECS Fargate!! Changes</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)