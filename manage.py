import unittest
from flask.cli import FlaskGroup
from patients import create_app, db
from patients.api.models import Patient, Visita


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def seed_db():
    db.session.add(Patient(name='alice',birth_date='10/10/2000',address='rua dois',phone='(11)91010-2020',email= 'alice@email.com',medical_history='Patient with Bronquite'))
    db.session.add(Patient(name='bob',birth_date='02/02/2000',address='rua três',phone='(21)94040-5000',email='bob@email.com', medical_history=' Patient with Covid'))
    db.session.add(Visita(patient_id=1, visit_date='05/05/2024', summary='a mild cough '))
    db.session.add(Visita(patient_id=2, visit_date='04/04/2024', summary='wheezing'))
    db.session.commit()
    
@cli.command()
def test():
    tests = unittest.TestLoader().discover('patients/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1
    



if __name__ == '__main__':
    cli()
