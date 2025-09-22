# meu_ritmo/domain/models/task.py

import datetime
from typing import List
from meu_ritmo.domain.enums.category_enum import CategoriaEnum
from meu_ritmo.domain.enums.priority_enum import PrioridadeEnum


class Tarefa:
    """Representa uma única tarefa na agenda, agora com sub-tarefas e dependências."""
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
        
        # --- NOVOS ATRIBUTOS PARA AS FEATURES ---
        self.sub_tarefas: List['Tarefa'] = []      # Para a feature de Recursão
        self.prerequisitos: List['Tarefa'] = []   # Para a feature de Grafo/Dependências
        self.bloqueada = False                    # Atributo auxiliar para a UI

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

    # --- NOVOS MÉTODOS PARA AS FEATURES ---

    def calcular_impacto_total(self) -> int:
        """
        Calcula o impacto de energia desta tarefa mais todas as suas
        sub-tarefas de forma RECURSIVA.
        """
        total = self.impacto_energia
        for sub_tarefa in self.sub_tarefas:
            total += sub_tarefa.calcular_impacto_total() # Chamada recursiva
        return total

    def esta_bloqueada(self) -> bool:
        """
        Verifica se algum dos pré-requisitos (dependências do GRAFO) 
        ainda não foi concluído.
        """
        for prereq in self.prerequisitos:
            if not prereq.concluida:
                return True # Está bloqueada
        return False # Não está bloqueada