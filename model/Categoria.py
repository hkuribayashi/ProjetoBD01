class Categoria:

    def __init__(self, id_categoria, nome):
        self._id_categoria = id_categoria
        self._nome = nome

    @property
    def id_categoria(self):
        return self._id_categoria

    @property
    def nome(self):
        return self._nome
