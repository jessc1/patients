from datetime import datetime
from patients import db
from sqlalchemy import inspect
from sqlalchemy_serializer import SerializerMixin


class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date= db.Column(db.Date)      
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15))
    email = db.Column(db.String(100))
    medical_history=db.Column(db.Text)
    visit = db.relationship(
        'Visita', backref=db.backref('patients', lazy=True))
    serialize_rules = ('-visits',)

    def __init__(self, name, birth_date, address, phone, email, medical_history):
        self.name = name
        self.birth_date = birth_date
        self.address = address
        self.phone = phone
        self.email = email
        self.medical_history = medical_history
        

    @property
    def age(self):
        today = datetime.now().date()
        age = int(today.year
                  -(self.birth_date.year)
                  -((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )
        return age

 

    def __repr__(self):
        return "<%r>" % self.name

class Visita(db.Model, SerializerMixin):
    __tablename__ = 'visita'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    visit_date = db.Column(db.Date)
    summary = db.Column(db.Text)
    

    def __repr__(self):
        return "<%r>" % self.id

    

    


    
