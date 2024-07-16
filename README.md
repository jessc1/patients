### Api de Cadastro de pacientes

## Funcionalidades da api:
* Listagem de pacientes : get/patients
* Criar pacientes: post/pacients
* editar pacientes: put/pacients

## Para execução da api
* instalação do flask e das bibliotecas do banco de dados

```
pip  install -r requirements.txt
```

* alterar a string do banco dados na config.py com usuário e banco de dados local
* rodar o recreate-db para recriar o banco de dados
```
python manage.py recreate-db
```

### Para popular o banco de dados
```
python manage.py seed-db
```
### Para rodar api 
```
python manage.py run
```

### Para rodar testes
```
python manage.py test
```
### Tecnologias :
* Python
* Flask
* SQLAlchemy
* PostgreSQL
  

