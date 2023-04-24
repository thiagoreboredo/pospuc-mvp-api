from pydantic import BaseModel
from typing import Optional, List
from model.tarefa import Tarefa

class TarefaSchema(BaseModel):
    """ Define como uma nova tarefa a ser inserida deve ser representada
    """
    titulo: str = "Tarefa Simples"
    descricao: str = "Descrição da Tarefa"
    concluido: bool = False


class TarefaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do tarefa.
    """
    titulo: str = "Teste"


class ListagemTarefasSchema(BaseModel):
    """ Define como uma listagem de tarefas será retornada.
    """
    tarefas:List[TarefaSchema]


def apresenta_tarefas(tarefas: List[Tarefa]):
    """ Retorna uma representação do tarefa seguindo o schema definido em
        TarefaViewSchema.
    """
    result = []
    for tarefa in tarefas:
        result.append({
            "titulo": tarefa.titulo,
            "descricao": tarefa.descricao,
            "concluido": tarefa.concluido,
        })

    return {"tarefas": result}


class TarefaViewSchema(BaseModel):
    """ Define como um tarefa será retornado: tarefa + comentários.
    """
    id: int = 1
    titulo: str = "Tarefa Simples"
    descricao: str = "Descrição da Tarefa"
    concluido: bool = False


class TarefaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    titulo: str

def apresenta_tarefa(tarefa: Tarefa):
    """ Retorna uma representação do tarefa seguindo o schema definido em
        TarefaViewSchema.
    """
    return {
        "id": tarefa.id,
        "titulo": tarefa.titulo,
        "descricao": tarefa.descricao,
        "concluido": tarefa.concluido
    }
