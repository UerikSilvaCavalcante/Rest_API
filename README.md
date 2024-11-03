# REST API
- Utilizando Django e Django-ninja

## Função
Esta uma REST API desenvolvida em **python** e **django**, utlizando a biblioteca **django-ninja**, para facilitar na organização e ciração da **CRUD** desta **APi**

## Objetivo
Esta API tem um objtivo simples, pelo fato ser feita apenas para aprendizagem.
Ela é um gerenciador de livros, nela se faz o armazenamento dos livros e tambem e possivel avaliar os mesmos, dando um nota e adicionando um comentario

## Tecnologias
- Python
- Django
- Djnago-Ninja
- SQLite3

## Como usar
- (Opcional) crie um ambiente virtual python
- ative ele
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
- instale o Django
    ```
        pip install django
    ```

- instale o Django-Ninja
    ```
        pip install django-ninja
    ```

- Execute o makemigration do manage.py para atulizar a migrations
    ``` 
        python manage.py makemigration
    ```
- Execute o migrate do manage.py para rodar as migrations no banco
    ``` 
        python manage.py migrate
    ```

- Execute o runserver para rodar a API
    ``` 
        python manage.py runserver
    ```