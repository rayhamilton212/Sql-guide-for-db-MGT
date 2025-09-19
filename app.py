from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_time = request.form['time']
        return render_template('result.html', user_time=user_time)
    return render_template('index.html')

@app.route('/confirm', methods=['POST'])
def confirm():
    confirmation = request.form['confirmation']
    if confirmation == 'yes':
        return render_template('confirmed.html')
    else:
        return render_template('cancelled.html')

if __name__ == '__main__':
    app.run(debug=True)
