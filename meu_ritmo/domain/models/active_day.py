# meu_ritmo/domain/models/active_day.py

import datetime
from typing import List
from meu_ritmo.domain.models.task import Tarefa


class DiaAtivo:
    """
    Gerencia todas as tarefas e o nível de energia para um único dia.

    Características:
        data (date): A data que este objeto representa.
        tarefas (List[Tarefa]): Uma lista de objetos Tarefa para este dia.
        energia_atual (int): O nível de energia restante para o dia.
    """

    ENERGIA_INICIAL: int = 100

    def __init__(self, data: datetime.date):
        self.data = data
        self.tarefas: List[Tarefa] = []
        self.energia_atual = self.ENERGIA_INICIAL
    
    @property
    def nivel_de_cansaco(self) -> str:
        """Calcula o status da Camila com base na energia atual, com emojis."""
        if self.energia_atual > 70:
            return "Disposta 😄"
        elif 40 < self.energia_atual <= 70:
            return "Normal 🙂"
        elif 20 < self.energia_atual <= 40:
            return "Cansada 🥱"
        else:
            return "Exausta 🥵"

    def adicionar_tarefa(self, tarefa: Tarefa):
        """
        Adiciona um objeto Tarefa já criado à lista do dia e atualiza a energia.
        A lógica de criação da tarefa foi movida para a interface, tornando este
        método mais limpo, direto e corrigindo o erro anterior.
        """
        self.tarefas.append(tarefa)
        # Atualiza a energia com base no impacto total da tarefa,
        # incluindo suas sub-tarefas (usando o método recursivo de Tarefa).
        self.energia_atual += tarefa.calcular_impacto_total()

    def mostrar_resumo(self):
        """
        Exibe um resumo do dia no console. Útil para depuração ou para a
        versão original da aplicação sem interface gráfica.
        """
        linha_separadora = "=" * 80
        print("\n" + linha_separadora)
        print(f"Resumo para o dia: {self.data.strftime('%d de %B de %Y')}")
        print("-" * 80)
        print(f"Status da Camila: {self.nivel_de_cansaco}")
        print(f" Energia restante: {self.energia_atual} / {self.ENERGIA_INICIAL}")
        print("\n Tarefas do Dia:")

        if not self.tarefas:
            print("   Nenhuma tarefa. Aproveite para relaxar! :D")
        else:
            # Assumindo que a classe Tarefa também foi atualizada com um método __repr__
            for tarefa in sorted(self.tarefas, key=lambda t: t.prioridade.value):
                print(f"   {tarefa}")
        print(linha_separadora)