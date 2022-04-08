from typing import List
class Restaurante():
    def __init__(self,id :int,nome:str,endereco:str,foto:str,hora_funcionamento:str,comentarios:List):
        self._id = id
        self._nome = nome
        self._endereco = endereco
        self._foto = foto
        self._hora_funcionament0 = hora_funcionamento
        self._comentarios = comentarios

    def get_id(self):
        return self._id
    def get_nome(self):
        return self._nome
    def get_endereco(self):
        return self._endereco
    def get_foto(self):
        return self._foto
    def get_hora_funcionamento(self):
        return self._hora_funcionament0
    def get_comentarios(self):
        return self._comentarios

class Especialista():
    def __init__(self,nome:str,comentario:str):
        self._nome = nome
        self._comentario = comentario

    def get_nome(self):
        return self._nome
    def get_comentario(self):
        return self._comentario