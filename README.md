FacilyFastAPI

# FastAPI com deploy na AWS
Esta é uma api com um banco de dado mysql, utilizado fastAPI um framework python com um foco em desenhpenho e ser intuitivo.

## Acessar api basta entrar na url
http://ec2-18-116-59-123.us-east-2.compute.amazonaws.com:8000/docs

 * ou para documentação
 
  http://ec2-18-116-59-123.us-east-2.compute.amazonaws.com:8000/redoc

## Estrutura de arquivo do projeto
```
.
└── FacilyFastAPI
    ├── .github   #github CI/CD
    ├──	test      #pytest
    ├── __init__.py 
    ├── crud.py   #interações com banco  
    ├── database.py #conexão com o banco
    ├── main.py    #iniciar servidor
    ├── router.py  #endpoints
    ├── models.py  #criar e define as tabelas
    └── schemas.py  #pydantic com schemas 
```


## Iniciar servidor 

### AWS EC2
<details markdown="1">

* Entrar no client ssh :
```
http://ec2-18-116-59-123.us-east-2.compute.amazonaws.com/
port 22
usuario ubunto
```

* Entrar no projeto e iniciar virtualenv 
```
$ cd FacilyFastAPI
$ source venv/bin/activate
$ python main.py


uvicorn main:app 

INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
</details>


### local
<details markdown="2">

* Entrar no projeto e locallizar `database.py` e mudar SQLALCHEMY_DATABASE_URL :

```
SQLALCHEMY_DATABASE_URL  =  "mysql + pymysql: // <usuario>: <senha> @ localhost: 3306 / contatos"
```
Com seu usuario e senha, em seguida criar uma tabela pelo mysql com o nome de contatos
```
CREATE DATABASE contatos;
```

* Ainda na pasta do projeto criar uma virtuar virtualenv
```
$ virtualenv venv
$ source bin/activate
```

* Instalar as dependenciar 
```
pip  install -r requisitos.txt
```

* Entrar no projeto e locallizar `main.py`:

```
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
</details>


## Banco de dados 

```
id: int
numerodetelefone: int
nome: str
sobrenome: str
email: str
```

## Endpoints
`POST` - http://ec2-18-116-59-123.us-east-2.compute.amazonaws.com:8000/docs#/default/create_contato_contato__post
* Criar um contato 

`GET` - http://ec2-18-116-59-123.us-east-2.compute.amazonaws.com:8000/docs#/default/list_contato_contatos__get
* Busca uma lista de contato

`GET` - http://ec2-18-116-59-123.us-east-2.compute.amazonaws.com:8000/docs#/default/read_contato_contatos__contato_id__get
* Busca um contato por id

`DELETE` - http://ec2-18-116-59-123.us-east-2.compute.amazonaws.com:8000/docs#/default/delete_users_contatos__contato_id__delete
* Deletar um contato por id 

`PUT` - http://ec2-18-116-59-123.us-east-2.compute.amazonaws.com:8000/docs#/contatos/update_contato_contatos__contato_id__put
* Atualizar dados de um contato por id

