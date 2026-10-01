/* Modelagem_Logico: */

CREATE TABLE Eventos (
    id_evento integer PRIMARY KEY,
    nome_evento text,
    local text,
    vagas integer,
    data_evento text
);

CREATE TABLE Participante (
    e_mail text PRIMARY KEY,
    nome text,
    aluno boolean,
    Semestre_ano text
);

CREATE TABLE faz_inscricao (
    id_iscricao integer,
    data_inscricao text,
    fk_Participante_e_mail text,
    fk_Eventos_id_evento integer
);
 
ALTER TABLE faz_inscricao ADD CONSTRAINT FK_faz_inscricao_1
    FOREIGN KEY (fk_Participante_e_mail)
    REFERENCES Participante (e_mail);
 
ALTER TABLE faz_inscricao ADD CONSTRAINT FK_faz_inscricao_2
    FOREIGN KEY (fk_Eventos_id_evento)
    REFERENCES Eventos (id_evento);