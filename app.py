from flask import Flask, make_response, jsonify, request
import pymysql

app = Flask(__name__)

app.json.sort_keys = False #type:ignore


def connect_db(
        db_host='localhost', 
        db_user='root', 
        db_password='12345678', 
        db_name='banco_funcionarios'
    ):
    db = pymysql.connect(host=db_host, user=db_user, passwd=db_password, database=db_name)
    return db   


@app.route('/funcionarios/', methods=['GET'])
def get_carros():
    banco = connect_db()
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM funcionario;")

    resultado_fetchall = cursor.fetchall()
    banco.close()

    lista_func_json = [
        {
            "id":func[0],
            "nome":func[1],
            "telefone":func[2],
        }
        for func in resultado_fetchall
    ]

    dados_ordenados = sorted(
        lista_func_json,
        key= lambda x: x['id'],
        reverse=True
    )

    return make_response(
        jsonify(
            mensagem='Lista de Funcionarios',
            total=len(dados_ordenados),
            dados=dados_ordenados
            )
        )

@app.route('/funcionarios/', methods=['POST'])
def create_carro():
    dados_recebidos = request.get_json()
    nome_user = dados_recebidos['nome']
    telefone_user = dados_recebidos['telefone']

    banco = connect_db()
    cursor = banco.cursor()

    sql = "INSERT INTO funcionario (nome, telefone) values (%s, %s)"
    cursor.execute(sql, (nome_user, telefone_user))
    banco.commit()

    id_criado = cursor.lastrowid

    banco.close()

    return make_response(
        jsonify(
            mensagem='Funcionario cadastrado com sucesso.',
            carro={
                "id": id_criado,
                "nome": nome_user,
                "telefone": telefone_user,
            }
        ),
        201
    )

if __name__=="__main__":
    app.run(debug=True)