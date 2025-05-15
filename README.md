# Consulta de Equipamentos Getrak

Este projeto consiste em uma API e um exportador para consulta de equipamentos através da API da Getrak.

## 🚀 Configuração do Ambiente

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

## 📡 Executando a API
```bash
uvicorn main:app --reload
```
## 2. A API estará disponível em: http://localhost:8000
- Endpoints Disponíveis:
- GET /equipamentos
    - Parâmetros de query:
    - status : "Y" para ativos (padrão) ou "N" para inativos

## 📥 Executando o Exportador
```bash
python exportador.py
```
## O exportador irá:

- Gerar arquivos JSON separados para equipamentos ativos e inativos
- Salvar na pasta configurada com os nomes:
  - equipamentos_ativos.json
  - equipamentos_inativos.json