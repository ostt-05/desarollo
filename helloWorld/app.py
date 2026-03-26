from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<html><head><title>Hello world</title></head><body><h1>JoseAntonioSotoCervantes</h1><p>Ir a <a href="/about">About</a></p></body></html>'

@app.route('/about')
def about():
    return '<html><head><title>About Page</title></head><body><h1>About Us</h1><p>This is the About Page.</p></body></html>'

if __name__ == '__main__':
    app.run(debug=True)