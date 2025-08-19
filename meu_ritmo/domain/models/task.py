import datetime

from meu_ritmo.domain.enums.category_enum import CategoriaEnum
from meu_ritmo.domain.enums.priority_enum import PrioridadeEnum


class Tarefa:
    """Representa uma única tarefa na agenda."""

    def __init__(
        self,
        descricao: str,
        prioridade: PrioridadeEnum,
        impacto_energia: int,
        categoria: CategoriaEnum,
    ):
        self._descricao = descricao
        self.prioridade = prioridade
        self.impacto_energia = impacto_energia
        self.concluida = False
        self.data_criacao = datetime.date.today()
        self.categoria = categoria

    @property
    def descricao(self) -> str:
        """Property para acessar a descrição de forma segura."""
        return self._descricao

    def __repr__(self) -> str:
        status_icone = "✓" if self.concluida else "○"
        sinal_energia = "+" if self.impacto_energia >= 0 else ""
        prioridade_str = self.prioridade.name.capitalize()
        return f"[{status_icone}] {self.descricao} | Categoria: {self.categoria.value} | Prioridade: {prioridade_str} | Energia: {sinal_energia}{self.impacto_energia}"

    def marcar_como_concluida(self):
        self.concluida = True
        print(f"Tarefa '{self.descricao}' marcada como concluída")
