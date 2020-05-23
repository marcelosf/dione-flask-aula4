from flask import Flask, jsonify, request
import json
from json.decoder import JSONDecodeError


app = Flask(__name__)


tarefas = [
    {
        'id': 0,
        'responsavel': 'Abreu',
        'tarefa': 'imprimir relatório',
        'status': 'concluido'
    },

    {
        'id': 1,
        'responsavel': 'Thalia',
        'tarefa': 'Pagar Boletos',
        'status': 'pendente'
    }
]

#Lista todas as tarefas
@app.route('/tarefas/', methods=['GET'])
def lista_tarefas():
    return  jsonify(tarefas)


#Retorna uma tarefa por meio do id
@app.route('/tarefas/<int:id>/', methods=['GET'])
def get_tarefa(id):
    try:
        response = jsonify(tarefas[id])
    except IndexError:
        mensagem = 'A tarefa com id {} não existe'.format(id)
        response = jsonify({'status': 'erro', 'mensagem': mensagem})
    return response


#Atualiza o status de uma tarefa
@app.route('/tarefas/<int:id>/', methods=['PUT'])
def atualiza_tarefa(id):
    try:
        response = jsonify(tarefas[id])
    except IndexError:
        mensagem = 'A tarefa com id {} não existe'.format(id)
        response = jsonify({'status': 'erro', 'mensagem': mensagem})
    except Exception:
        mensagem = 'Erro desconhecido. Contate o administrador da API.'
        response = jsonify({'status': 'erro', 'mensagem': mensagem})
    data = json.loads(request.data)
    tarefas[id]['status'] = data['status']
    return jsonify({'status': 'sucesso', 'mensagem': 'Tarefa atualizada com sucesso.'})


#Exclui uma tarefa
@app.route('/tarefas/<int:id>/', methods=['DELETE'])
def deleta_tarefa(id):
    try:
        response = jsonify(tarefas[id])
    except IndexError:
        mensagem = 'A tarefa com id {} não existe'.format(id)
        response = jsonify({'status': 'erro', 'mensagem': mensagem})
    except Exception:
        mensagem = 'Erro desconhecido. Contate o administrador da API.'
        response = jsonify({'status': 'erro', 'mensagem': mensagem})
    tarefas.pop(id)
    return jsonify({'status':'sucesso', 'mensagem':'Tarefa excluída com sucesso.'})


#Insere uma nova tarefa
@app.route('/tarefas/', methods=['POST'])
def adiciona_tarefa():
    try:
        response = json.loads(request.data)
    except json.decoder.JSONDecodeError:
        mensagem = 'Os dados não foram informados corretamente'
        return jsonify({'status': 'erro', 'mensagem': mensagem})
    posicao = len(tarefas)
    response['id'] = posicao
    tarefas.append(response)
    return jsonify({'status':'sucesso', 'tarefa':response})




if __name__ == '__main__':
    app.run(debug=True) 

    