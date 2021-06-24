# Encurtador de Links Python - Django

Como usar ou testar?

1 - Deve-se, primeiramente, criar um ambiente python e usar o arquivos requirements na raiz do projeto para instalar as dependências:

pip install -r requirements.txt

2 - Após a instalação das dependencias, deve-se criar a base de dados que irá guardar as urls:

python manager.py makemigrations
python manager.py migrate

3 - Deixei um arquivo para popular a base de dados, caso não queiram criar várias urls e ainda um usuário. Para carregar os dados, use:
python manager.py loaddata db.json

E pronto!

O sistema já está pronto para o uso. Para rodar a aplicação django utilize: 
python manager.py runserver


# API
Para enviar à API uma url a ser encurtada use a seguinte URL:

http://localhost:8000/api/

Tipo: POST

Parâmetros:
 
	url_full: Obrigatório,esta é a URL a ser encurtada 
	url_hash: Opcional, esta é o nome desejável da URL encurtada
	expired_at: Opcional, o formato de data aceitável é: "yyyy-mm-dd hh:mm", o padrão são 7 dias. 

O formato solicitado é JSON e não é necessário ter autênticação.

# FrontEnd
Para visualizar a lista de URLs encurtadas:

Abra o seu navegador e digite na url: http://localhost:8000

Neste momento, irá ser solicitado usuário e senha. Caso não tenha carregado o arquivo que deixei para popular o banco, você terá que criar um superusuário usando o comando:

python manager.py createsuperuser 

Caso tenha carregado o arquivo para a base de dados, utilize o usuário: admin e a senha: 123456


Feito o login, é possível visualizar as URLs encurtadas utilizando a API.

*Para acessar uma URL encurtada basta colocar o nome da URL encurtada após localhost:8000.
Exemplo:

localhost:8000/nome_url 
