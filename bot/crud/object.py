from typing import Type

from models.object import Object


class CRUDQuizRespondents:
    def __init__(self, model: Type[Object]):
        self.model = model


crud = CRUDQuizRespondents(Object)
