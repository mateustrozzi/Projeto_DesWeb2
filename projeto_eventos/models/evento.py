class Evento:
    def __init__(self, nome, data, local, vagas=0, id=None):
        self.id = id
        self.nome = nome
        self.data = data
        self.local = local
        self.vagas = vagas
