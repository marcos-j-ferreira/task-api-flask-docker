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
        with open('tarefa.json', 'r') as file:
            lista = json.load(file)
            return jsonify(tarefas=lista)
    except Exception as e:
        return jsonify(erro="Erro ao buscar a lista de tarefas")
    

@app.route('/tarefa/listar/<int:id>', methods=['GET'])
def listar_por_id(id):
    try:
        with open('tarefa.json', 'r') as file:
            db = json.load(file)

            for tarefa in db:
                if tarefa['id'] == id:
                    return jsonify(tarefa=tarefa)

            return jsonify(erro="ID não encontrado")
    except Exception as e:
        return jsonify(erro="Erro ao buscar a tarefa por ID")

@app.route('/tarefa/adicionar', methods=['POST'])
def adicionar():
    try:
        dados = request.get_json()
        with open('tarefa.json', 'r') as file:
            tarefas = json.load(file)
            novo_id = tarefas[-1]['id'] + 1 if tarefas else 1

        nova_tarefa = {
            "id": novo_id,
            "tarefa": dados.get('tarefa'),
            "concluida": False
        }

        tarefas.append(nova_tarefa)

        with open('tarefa.json', 'w') as arquivo:
            json.dump(tarefas, arquivo, indent=4)

        return jsonify(sucesso="Tarefa adicionada com sucesso")
    except Exception as e:
        return jsonify(erro="Erro no servidor")
    
@app.route('/tarefa/deletar/<int:id>', methods=['GET'])
def deletar(id):
    try:
        with open('tarefa.json', 'r') as file:
            db = json.load(file)

        db_filtrado = [tarefa for tarefa in db if tarefa['id'] != id]

        with open('tarefa.json', 'w') as arquivo:
            json.dump(db_filtrado, arquivo, indent=4)

        return jsonify(sucesso="Tarefa deletada com sucesso")
    except Exception as e:
        return jsonify(erro="Erro ao deletar a tarefa")

@app.route('/tarefa/estado/<int:id>')
def marcar_concluida(id):
    try:
        with open('tarefa.json', 'r') as file:
            db = json.load(file)

        for tarefa in db:
            if tarefa['id'] == id:
                tarefa['concluida'] = True

        with open('tarefa.json', 'w') as arquivo:
            json.dump(db, arquivo, indent=4)

        return jsonify(sucesso="Tarefa marcada como concluída com sucesso")
    except Exception as e:
        return jsonify(erro="Erro ao marcar a tarefa como concluída")


