from abc import ABC, abstractmethod
from meu_ritmo.domain.models.task import Tarefa
from meu_ritmo.domain.enums.category_enum import CategoriaEnum
from meu_ritmo.domain.enums.priority_enum import PrioridadeEnum
import datetime

class TarefaEspecial(Tarefa, ABC):
    """
    Classe abstrata base para tarefas especiais que extendem o comportamento padrão.
    Implementa o princípio Open/Closed (OCP) do SOLID.
    """
    
    def __init__(
        self,
        descricao: str,
        prioridade: PrioridadeEnum,
        impacto_energia: int,
        categoria: CategoriaEnum,
        efeito_especial: str = None
    ):
        super().__init__(descricao, prioridade, impacto_energia, categoria)
        self.efeito_especial = efeito_especial
        self.data_limite = self._calcular_data_limite()
        self.concluida = False
    
    @abstractmethod
    def _calcular_data_limite(self) -> datetime.date:
        """Calcula a data limite específica para cada tipo de tarefa especial"""
        pass
    
    @abstractmethod
    def aplicar_efeito_especial(self) -> str:
        """Aplica o efeito especial quando a tarefa é concluída"""
        pass
    
    def marcar_como_concluida(self):
        """Sobrescreve com polimorfismo o método original"""
        mensagem_original = super().marcar_como_concluida()
        mensagem_especial = self.aplicar_efeito_especial()
        return f"{mensagem_original}\n{mensagem_especial}"
    
    def __repr__(self) -> str:
        repr_original = super().__repr__()
        return f"{repr_original} | Efeito: {self.efeito_especial} | Data Limite: {self.data_limite}"