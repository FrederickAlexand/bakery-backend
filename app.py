from flask import Flask, jsonify, request, abort
from models import db, Roti
from config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/roti', methods=['POST'])
def create_roti():
    data = request.json
    if not data or not 'nama_roti' in data or not 'jenis_roti' in data or not 'harga_roti' in data or not 'stok_roti' in data:
        abort(400)

    roti = Roti(
        nama_roti=data['nama_roti'],
        jenis_roti=data['jenis_roti'],
        harga_roti=data['harga_roti'],
        stok_roti=data['stok_roti']
    )
    db.session.add(roti)
    db.session.commit()

    return jsonify({'message': 'Roti added successfully!', 'id': roti.id}), 201


@app.route('/roti', methods=['GET'])
def get_roti():
    roti_list = Roti.query.all()
    return jsonify([{
        'id': roti.id,
        'nama_roti': roti.nama_roti,
        'jenis_roti': roti.jenis_roti,
        'harga_roti': roti.harga_roti,
        'stok_roti': roti.stok_roti
    } for roti in roti_list])


@app.route('/roti/<int:id>', methods=['GET'])
def get_single_roti(id):
    roti = Roti.query.get_or_404(id)
    return jsonify({
        'id': roti.id,
        'nama_roti': roti.nama_roti,
        'jenis_roti': roti.jenis_roti,
        'harga_roti': roti.harga_roti,
        'stok_roti': roti.stok_roti
    })


@app.route('/roti/<int:id>', methods=['PUT'])
def update_roti(id):
    roti = Roti.query.get_or_404(id)
    data = request.json

    if 'nama_roti' in data:
        roti.nama_roti = data['nama_roti']
    if 'jenis_roti' in data:
        roti.jenis_roti = data['jenis_roti']
    if 'harga_roti' in data:
        roti.harga_roti = data['harga_roti']
    if 'stok_roti' in data:
        roti.stok_roti = data['stok_roti']

    db.session.commit()
    return jsonify({'message': 'Roti updated successfully!'})

@app.route('/roti/<int:id>', methods=['DELETE'])
def delete_roti(id):
    roti = Roti.query.get_or_404(id)
    db.session.delete(roti)
    db.session.commit()
    return jsonify({'message': 'Roti deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
