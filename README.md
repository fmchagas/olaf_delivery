# Olaf Delivery
Olaf Delivery é uma mini replica do ifood desenvolvido no curso de python com flask do [@rochacbruno](https://github.com/codeshow/curso-flask/tree/master)

## Começando
Para executar o projeto, será necessário instalar os seguintes programas:
* Python 3.8
* pip
* S.O Linux (este projeto foi desenvolvido no WSL2)

## Desenvolvimento
Para iniciar o desenvolvimento, é necessário clonar o projeto do GitHub num diretório:
* crie um ambiente virtual
```shell
python3.8 -m venv delivery/.venv
cd "delivery"
git clone https://github.com/fmchagas/olaf_delivery.git
cd "olaf_delivery"
```
* Ative o ambiente virtual e instale as dependencias
```shell
source .venv/bin/activate
make install
```
* Rode a aplicação
```shell
export FLASK_APP=olaf_delivery/app.py
flask run
```
## Testes
```
make test
```