from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Tarefa
from schemas import *
from flask_cors import CORS

info = Info(title="Gerenciador de Tarefas", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
tarefa_tag = Tag(name="Tarefa", description="Adição, visualização e remoção de tarefas à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get('/tarefas', tags=[tarefa_tag],
         responses={"200": ListagemTarefasSchema, "404": ErrorSchema})
def get_tarefas():
    """Faz a busca por todos as tarefas cadastradas

    Retorna a listagem de tarefas.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    tarefas = session.query(Tarefa).all()

    if not tarefas:
        # se não há tarefas cadastradas
        return {"tarefas": []}, 200
    else:
        # retorna a representação de tarefa
        print(tarefas)
        return apresenta_tarefas(tarefas), 200

@app.get('/tarefa', tags=[tarefa_tag],
         responses={"200": TarefaViewSchema, "404": ErrorSchema})
def get_tarefa(query: TarefaBuscaSchema):
    """Faz a busca por uma Tarefa a partir do id da tarefa

    Retorna uma representação da tarefa buscada.
    """
    tarefa_titulo = query.titulo
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    tarefa = session.query(Tarefa).filter(Tarefa.titulo == tarefa_titulo).first()

    if not tarefa:
        # se a tarefa não foi encontrada
        error_msg = "Tarefa não encontrada na base :/"
        return {"mesage": error_msg}, 404
    else:
        # retorna a representação de tarefa
        return apresenta_tarefa(tarefa), 200

@app.post('/tarefa', tags=[tarefa_tag],
          responses={"200": TarefaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_tarefa(form: TarefaSchema):
    """Adiciona uma nova Tarefa à base de dados

    Retorna uma representação das tarefas.
    """
    tarefa = Tarefa(
        titulo=form.titulo,
        descricao=form.descricao,
        concluido=form.concluido)
    try:
        # criando conexão com a base
        session = Session()
        # adicionando tarefa
        session.add(tarefa)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return apresenta_tarefa(tarefa), 200
    
    except IntegrityError as e:
        # como a duplicidade do título é a provável razão do IntegrityError
        error_msg = "Tarefa de mesmo título já salvo na base :/"
        return {"mesage": error_msg}, 409
    
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400

@app.delete('/tarefa', tags=[tarefa_tag],
            responses={"200": TarefaDelSchema, "404": ErrorSchema})
def del_tarefa(query: TarefaBuscaSchema):
    """Deleta uma Tarefa a partir do título informado

    Retorna uma mensagem de confirmação da remoção.
    """
    tarefa_titulo = unquote(unquote(query.titulo))
    print(tarefa_titulo)
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Tarefa).filter(Tarefa.titulo == tarefa_titulo).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"mesage": "Tarefa removida", "id": tarefa_titulo}
    else:
        # se a tarefa não foi encontrada
        error_msg = "Tarefa não encontrada na base :/"
        return {"mesage": error_msg}, 404

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
