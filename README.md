# Oficina de Integração 2
### Trabalho de Oficina de Integração 2 da Universidade Tecnológica Federal do Paraná.
<ol>
Este projeto visa avaliar o aprendizado e colocar em prática as matérias do curso de engenharia de software da UTFPR. Se trata de um sistema desenvolvido em Python, HTML, CSS Bootstrap e com Framework Django.

O principal objetivo do sistema é poder auxiliar o usuário no gerenciamento de canetas, podendo utilizar as funcionalidades de cadastrar, listar, editar, excluir e gerar relatórios sobre as canetas. Conforme a grande quantidade de canetas manipuladas durante o dia-a-dia deste usuário, o sistema proposto ajudará a obter informações mais precisas e objetivas no resultado. 
</ol>

### Definição da estratégia de automação de testes do sistema.
<ol>
O sistema será testado e validado por meio de testes unitários automatizados, com a utilização da biblioteca unittest do python para o backend, e o fremework selenium webdriver para o frontend.
</ol>
  
## Definição da arquitetura em alto nível do sistema 
<ol>
  
```
https://drive.google.com/file/d/1hVJJJK1faDuTMJKC-eSu0d6bga4IcYxV/view?usp=sharing
```
</ol>
  
## Instalar o projeto
<ol>
  
### Clone o projeto
```
git clone https://github.com/rokukawa/Oficina-de-Integracao-2.git
```
</ol>

  
## Instalar as dependências do projeto
<ol>
  
```
pip install -r requirements.txt
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
</ol>
  
  
## Iniciar o servidor local
<ol>
  
### Criar a máquina virtual
```
python -m venv ./venv
```
  
### Ativar a máquina virtual
```
.\venv\Scripts\activate  
```

### Iniciar a máquina virtual
```
python manage.py runserver
```
</ol>
