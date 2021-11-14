class Produto:

    def __init__(self, id_produto, nome, valor, id_categoria):
        self._id_produto = id_produto
        self._nome = nome
        self._valor = valor
        self._id_categoria = id_categoria

    @property
    def id_produto(self):
        return self._id_produto

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor

    @property
    def id_categoria(self):
        return self._id_categoria
