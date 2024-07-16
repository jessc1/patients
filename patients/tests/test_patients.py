import json
import unittest
from datetime import date
from patients import db
from patients.api.models import Patient, Visita
from patients.tests.base import BaseTestCase

class TestPatients(BaseTestCase):
   
    def test_add_patient(self):
        with self.client:
            response = self.client.post(
                '/patients',
                data=json.dumps({
                    'name': 'John Doe',
                    'birth_date': '01/01/1981',
                    'address': 'rua um',
                    'phone': '(11) 91020-3040',                    
                    'email' :'johndoe@email.com',
                    'medical_history': 'Gastrite'
                }),
                content_type = 'application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            

    
    def test_add_patient_duplicate_email(self):
        with self.client:
            self.client.post(
                '/patients',
                data=json.dumps({
                    'name': 'John Doe',
                    'birth_date': '01/01/1981',
                    'address': 'rua um',
                    'phone': '(11) 91020-3040',                    
                    'email' :'johndoe@email.com',
                    'medical_history': 'Gastrite'
                }),
                content_type='application/json',
                
            )
            response = self.client.post(
                '/patients',
                data=json.dumps({
                    'name': 'John Doe',
                    'birth_date': '01/01/1981',
                    'address': 'rua um',
                    'phone': '(11) 91020-3040',                    
                    'email' :'johndoe@email.com',
                    'medical_history': 'Gastrite'
                }),
                content_type='application/json',
                
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('email already exists.', data['message'])
            self.assertIn('fail', data['status'])
    
                    
    def test_get_patient(self):
        patient = Patient(name='John Doe', birth_date='01/01/1981',
              address='rua um', phone='(11)91020-3040', email='johndoe@email.com', medical_history='Gastrite')
        visit = Visita(patient_id=1, visit_date='05/05/2024', summary='a mild cough')
        db.session.add(patient)
        db.session.add(visit)
        db.session.commit()
        with self.client:
            response = self.client.get(f'/patients/{patient.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code,200)
            self.assertIn('John Doe', data['data']['name'])        
            self.assertIn('johndoe@email.com', data['data']['email'])
            self.assertIn('Gastrite', data['data']['medical_history'])            
           
