from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def rotas_disponiveis():
    obj = {
        '/tarefa': "Uma resposta simples",
        '/tarefa/listar': "Lista todas as tarefas adicionadas",
        '/tarefa/listar/id': "Lista uma tarefa pelo ID",
        '/tarefa/adicionar': "Adiciona uma nova tarefa",
        '/tarefa/deletar': "Deleta uma tarefa",
        '/tarefa/estado/': "Marca uma tarefa como concluída"
    }
    return jsonify(rotas=obj)

@app.route('/tarefa')
def hello():
    return jsonify(message="Uma API simples com Flask na WSL")

@app.route('/tarefa/listar')
def listar():
    try:
        with open('db.json', 'r') as file:
            lista = json.load(file)
            return jsonify(tarefas=lista)
    except Exception as e:
        return jsonify(erro="Erro ao buscar a lista de tarefas")
    
