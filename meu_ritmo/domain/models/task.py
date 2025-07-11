import datetime

from meu_ritmo.domain.enums.category_enum import CategoriaEnum
from meu_ritmo.domain.enums.priority_enum import PrioridadeEnum

class Tarefa:
    """
    Representa uma única tarefa na agenda.

    Características:
        descricao (str): O que precisa ser feito.
        prioridade (int): Nivel de urgencia (1-3).
        impacto_energia (int): Quanto de energia a tarefa consome ou gera.
        concluida (bool): Se a tarefa foi concluída.
        data_criacao (date): Data de criação da tarefa.
        categoria (str): Categoria da tarefa (ex: trabalho, pessoal).
    """

    def __init__(
        self,
        descricao: str,
        prioridade: PrioridadeEnum,
        impacto_energia: int,
        categoria: CategoriaEnum,
    ):
        if not descricao:
            raise ValueError("A descrição da tarefa não pode estar vazia.")

        self.descricao = descricao
        self.prioridade = prioridade
        self.impacto_energia = impacto_energia
        self.concluida = False
        self.data_criacao = datetime.date.today()
        self.categoria = categoria

    def __repr__(self) -> str:
        status_icone = "v" if self.concluida else "o"
        sinal_energia = "+" if self.impacto_energia > 0 else ""
        return f"[{status_icone}] {self.descricao} | Prioridade: {self.prioridade} | Energia: {sinal_energia}{self.impacto_energia}"

    def marcar_como_concluida(self):
        self.concluida = True
        print(f"Tarefa '{self.descricao}' marcada como concluída")
