from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return 'lunar'
    return render_template('index.html')

@app.route('/whereami')
def whereami(name):
    return 'Ghana!'

@app.route('/thename <lunar>')
def thename(lunar):
    print(lunar)
    return render_template('myname.html', thename)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    

