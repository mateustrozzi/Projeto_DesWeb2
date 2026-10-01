from dao.database import conectar, criar_tabelas
from models.evento import Evento
from models.participante import Participante
from models.inscricao import Inscricao

class EventoDAO:
    @staticmethod
    def criar_tabela():
        criar_tabelas()

    @staticmethod
    def salvar_evento(evento):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO evento (nome_evento, local, vagas, data_evento) VALUES (?, ?, ?, ?)",
            (evento.nome, evento.local, evento.vagas, evento.data)
        )
        evento.id = cursor.lastrowid
        conexao.commit()
        conexao.close()
        return evento

    @staticmethod
    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, nome_evento, data_evento, local, vagas FROM evento"
        )
        linhas = cursor.fetchall()
        conexao.close()

        eventos = []
        for linha in linhas:
            evento = Evento(
                id=linha[0],
                nome=linha[1],
                data=linha[2],
                local=linha[3],
                vagas=linha[4]
            )
            eventos.append(evento)

        return eventos

    @staticmethod
    def buscar_por_id(id_evento):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, nome_evento, data_evento, local, vagas FROM evento WHERE id = ?",
            (id_evento,)
        )
        linha = cursor.fetchone()
        conexao.close()

        if linha:
            return Evento(
                id=linha[0],
                nome=linha[1],
                data=linha[2],
                local=linha[3],
                vagas=linha[4]
            )
        return None

    # Métodos delegados para compatibilidade
    @staticmethod
    def salvar_participante(participante):
        return ParticipanteDAO.salvar(participante)

    @staticmethod
    def salvar_inscricao(inscricao):
        return InscricaoDAO.salvar(inscricao)


class ParticipanteDAO:
    @staticmethod
    def salvar(participante):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO participante (email, nome, aluno, semestre_ano) VALUES (?, ?, ?, ?)",
            (participante.email, participante.nome, participante.aluno, participante.semestre_ano)
        )
        conexao.commit()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT email, nome, aluno, semestre_ano FROM participante")
        linhas = cursor.fetchall()
        conexao.close()

        participantes = []
        for linha in linhas:
            p = Participante(
                email=linha[0],
                nome=linha[1],
                aluno=linha[2],
                semestre_ano=linha[3]
            )
            participantes.append(p)
        return participantes


class InscricaoDAO:
    @staticmethod
    def salvar(inscricao):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO faz_inscricao (data_inscricao, fk_participante_email, fk_evento_id) VALUES (?, ?, ?)",
            (inscricao.data_inscricao, inscricao.fk_participante_email, inscricao.fk_evento_id)
        )
        inscricao.id_inscricao = cursor.lastrowid
        conexao.commit()
        conexao.close()
        return inscricao

    @staticmethod
    def listar():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id_inscricao, data_inscricao, fk_participante_email, fk_evento_id FROM faz_inscricao")
        linhas = cursor.fetchall()
        conexao.close()

        inscricoes = []
        for linha in linhas:
            i = Inscricao(
                id_inscricao=linha[0],
                data_inscricao=linha[1],
                fk_participante_email=linha[2],
                fk_evento_id=linha[3]
            )
            inscricoes.append(i)
        return inscricoes
