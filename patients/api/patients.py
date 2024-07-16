import json
from flask import Blueprint, jsonify, request, redirect 
from patients.api.models import Patient, Visita 
from patients import  db, create_app
from sqlalchemy import exc



patients_blueprint = Blueprint('patients', __name__)

@patients_blueprint.route('/patients', methods=['POST'])
def add_patient():
   data = request.get_json()
   response_object = {'status': 'fail',
                      'message': 'Invalid payload'}
   if not data:
      return jsonify(response_object),400
   name = data.get('name')
   birth_date = data.get('birth_date')
   address = data.get('address')
   phone = data.get('phone')   
   email = data.get('email')
   medical_history = data.get('medical_history')
   try:
      patient = Patient.query.filter_by(email=email).first()
      if not patient:
         db.session.add(Patient(name=name,birth_date=birth_date,
                                address=address,phone=phone,email=email,medical_history=medical_history))
         db.session.commit()
         response_object['status'] = 'success'
         response_object['message']= f'{email} was add!'
         return jsonify(response_object), 201

      else:
         response_object['message'] = 'email already exists.'
         return jsonify(response_object),400
      
   except exc.IntegrityError as e:
      db.session.rollback()
      return jsonify(response_object),400
  
       

@patients_blueprint.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
   try:
      patient = Patient.query.filter_by(id=id).first()
      visit = Visita.query.filter_by(id=id).first()
      response_object = {
         'data': {
            'name': patient.name,
            'id': patient.id,
            'age':patient.age,
            'birth_date': patient.birth_date,
            'phone':patient.phone,
            'email': patient.email,
            'address':patient.address,
            'medical_history': patient.medical_history,               
         }
      }   
      return jsonify(response_object), 200
   except ValueError:
      return jsonify(response_object), 404

@patients_blueprint.route('/patients', methods=['GET'])
def get_patients():        
   res = {}
   for patient in Patient.query.all():
      for visit in Visita.query.all():
         if patient.id == visit.patient_id:                 
            res[patient.id] = {
               'name': patient.name,
               'age': patient.age,
               'phone': patient.phone,
               'email': patient.email,
               'last_visit_summary': f"Visit on {visit.visit_date} : {patient.medical_history}"
            }           
            
   return jsonify(res),200  

@patients_blueprint.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
      try:
         patient = Patient.query.filter_by(id=id).first()
         if patient:
               data = request.get_json()
               patient.email = data['email']
               patient.address = data['address']
               patient.phone = data['phone']
               db.session.commit()
               return jsonify({ 'message': 'patient updated'}),200
         return jsonify({'message': 'patient not found'}),400
      except ValueError as e:
         return jsonify({'message': 'error updating patient'})

        





