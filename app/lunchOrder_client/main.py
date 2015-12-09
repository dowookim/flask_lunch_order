from flask import Flask, render_template
app = Flask(__name__)

@app.route('/main')
def hello_world():
	user_list = ['asd','asd']
	return render_template('main.html', user_list=user_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)