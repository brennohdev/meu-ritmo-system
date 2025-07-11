import datetime
from typing import List

from meu_ritmo.domain.models.task import Tarefa


class DiaAtivo:
    """
    Gerencia todas as tarefas e o nível de energia para um único dia.

    Caratecterísticas:
        data (date): A data que este objeto representa.
        tarefas (List[Tarefa]): Uma lista de objetos Tarefa para este dia.
        energia_atual (int): O nível de energia restante para o dia.
    """
    ENERGIA_INICIAL: int = 100

    def __init__(self, data: datetime.date):
        self.data = data
        self.tarefas: List[Tarefa] = []
        self.energia_atual = self.ENERGIA_INICIAL

    def adicionar_tarefa(self, tarefa: Tarefa):
        self.tarefas.append(tarefa)
        self.energia_atual += tarefa.impacto_energia

        if self.energia_atual < 20 and self.energia_atual > 0:
            print(f"Ei, Camila! Sua energia está baixa, olha: {self.energia_atual}. Considere uma pausa!")
        elif self.energia_atual <= 0:
            print(f"Ei, Camila! Infelizmente sua energia acabou, olha: {self.energia_atual}. "
                  f"Evite novas tarefas ou isso pode gerar desgaste.")

    def mostrar_resumo(self):
        print("\n" + "=" * 40)
        print(f"Resumo para o dia: {self.data.strftime('%d de %B de %Y')}")
        print("=" * 40)
        print(f"Energia restante: {self.energia_atual} / {self.ENERGIA_INICIAL}")
        print("\n Tarefas do Dia:")

        if not self.tarefas:
            print(" Nenhuma tarefa. Aproveite para relaxar! :D")
        else:
            for tarefa in sorted(self.tarefas, key=lambda t: t.prioridade, reverse=True):
                print(f"\nTarefa: {tarefa}")
        print("=" * 40)
