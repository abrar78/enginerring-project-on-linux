from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/advertiseWithUs.html')
def advertisse():
    return render_template('advertiseWithUs.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 