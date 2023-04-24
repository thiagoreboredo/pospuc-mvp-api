from sqlalchemy import Column, String, Integer, DateTime, Boolean
from datetime import datetime
from typing import Union

from model import Base

class Tarefa(Base):
    __tablename__ = 'tarefa'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), unique=True, nullable=False)
    descricao = Column(String(200), nullable=False)
    concluido = Column(Boolean, default=False, nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())
    data_finalizacao = Column(DateTime, default=datetime.now())

    def __init__(self, titulo:str, descricao:int, concluido:bool,
                 data_insercao:Union[DateTime, None] = None,
                 data_finalizacao:Union[DateTime, None] = None):
        """
        Cria um Tarefa

        Arguments:
            título: título da tarefa.
            descrição: descrição explicando a tarefa
            concluido: indica se a tarefa já foi concluída
            data_insercao: data de quando a tarefa foi inserido à base
            data_finalizacao: data de quando a tarefa foi finalizada
        """
        self.titulo = titulo
        self.descricao = descricao
        self.concluido = concluido

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao