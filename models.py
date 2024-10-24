from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Roti(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_roti = db.Column(db.String(100), nullable=False)
    jenis_roti = db.Column(db.String(10), nullable=False)  
    harga_roti = db.Column(db.Float, nullable=False)
    stok_roti = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Roti {self.nama_roti}>'
