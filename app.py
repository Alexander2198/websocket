from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Evento de WebSocket
@socketio.on('message')
def handle_message(message):
    print(f"Mensaje recibido: {message}")
    send(f"Mensaje por defecto del servidor: {message}", broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
