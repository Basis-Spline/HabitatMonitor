from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sensor_data.db'
app.config['SECRET_KEY'] = 'secret!'
db = SQLAlchemy(app)
socketio = SocketIO(app)

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String(50))
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    soil_moisture = db.Column(db.Float)
    timestamp = db.Column(db.String(50))

db.create_all()

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    node_id = data.get('node_id')
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    soil_moisture = data.get('soil_moisture')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if node_id:
        sensor_data = SensorData(node_id=node_id, temperature=temperature, humidity=humidity, soil_moisture=soil_moisture, timestamp=timestamp)
        db.session.add(sensor_data)
        db.session.commit()
        
        # Emit data to WebSocket clients
        socketio.emit('new_data', {'node_id': node_id, 'temperature': temperature, 'humidity': humidity, 'soil_moisture': soil_moisture, 'timestamp': timestamp})
        
        print(f'Received data from {node_id}: {data}')
    
    return jsonify({"status": "success", "message": "Data received"}), 200

@app.route('/')
def index():
    data = SensorData.query.order_by(SensorData.timestamp.desc()).all()
    return render_template('index.html', sensor_data=data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
