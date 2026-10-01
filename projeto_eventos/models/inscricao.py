class Inscricao:
    def __init__(self, id_inscricao=None, data_inscricao=None, fk_participante_email=None, fk_evento_id=None):
        self.id_inscricao = id_inscricao
        self.data_inscricao = data_inscricao
        self.fk_participante_email = fk_participante_email
        self.fk_evento_id = fk_evento_id
