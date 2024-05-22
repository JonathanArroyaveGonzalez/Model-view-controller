from flask import Flask, render_template

app = Flask(__name__)

# Modelo
class MessageModel:
    def __init__(self, message):
        self.message = message

# Vista
@app.route('/')
def index():
    message = MessageModel("¡Para continuar navege hacia /presentacion!")
    return render_template('index.html', message=message.message)

@app.route('/presentacion')
def present():
    return render_template('index.html', presentacion=True)

if __name__ == '__main__':
    app.run(debug=True)
