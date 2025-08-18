import datetime
from typing import List
from meu_ritmo.domain.models.types_special_task import TarefaRecorrente, TarefaUrgente
from meu_ritmo.domain.models.task import Tarefa
from meu_ritmo.domain.models.special_task import TarefaEspecial


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

    def adicionar_tarefa(self, dados_tarefa):
        # Cria o tipo de tarefa apropriado
        if dados_tarefa["tipo_especial"] == "recorrente":
            tarefa = TarefaRecorrente(
                descricao=dados_tarefa["descricao"],
                prioridade=dados_tarefa["prioridade"],
                categoria=dados_tarefa["categoria"],
                impacto_energia=dados_tarefa["impacto_energia"],
            )
        elif dados_tarefa["tipo_especial"] == "urgente":
            tarefa = TarefaUrgente(
                descricao=dados_tarefa["descricao"],
                prioridade=dados_tarefa["prioridade"],
                categoria=dados_tarefa["categoria"],
                impacto_energia=dados_tarefa["impacto_energia"],
            )
        else:
            tarefa = Tarefa(
                descricao=dados_tarefa["descricao"],
                prioridade=dados_tarefa["prioridade"],
                categoria=dados_tarefa["categoria"],
                impacto_energia=dados_tarefa["impacto_energia"],
            )

        self.tarefas.append(tarefa)
        self.energia_atual += tarefa.impacto_energia

    def mostrar_resumo(self):
        linha_separadora = "=" * 60
        print("\n" + linha_separadora)
        print(f"Resumo para o dia: {self.data.strftime('%d de %B de %Y')}")
        print("-" * 60)
        print(f"⚡ Energia restante: {self.energia_atual} / {self.ENERGIA_INICIAL}")
        print("\n Tarefas do Dia:")

        if not self.tarefas:
            print("   Nenhuma tarefa. Aproveite para relaxar! :D")
        else:
            for tarefa in sorted(self.tarefas, key=lambda t: t.prioridade.value):
                # Determina o tipo da tarefa de forma mais robusta
                tipo = "Normal"  # Padrão

                # Verifica o tipo real da instância
                if isinstance(tarefa, TarefaEspecial):
                    if isinstance(tarefa, TarefaRecorrente):
                        tipo = "🔁 Recorrente"
                    elif isinstance(tarefa, TarefaUrgente):
                        tipo = "⏰ Urgente"
                    else:
                        tipo = "✨ Especial"

                sinal_energia = "+" if tarefa.impacto_energia >= 0 else ""
                status_icone = "✓" if tarefa.concluida else "○"

                print(
                    f"   - [{status_icone}] {tarefa.descricao.ljust(20)} | "
                    f"Categoria: {tarefa.categoria.value.ljust(15)} | "
                    f"Prioridade: {tarefa.prioridade.name.capitalize().ljust(6)} | "
                    f"Energia: {sinal_energia}{str(tarefa.impacto_energia).ljust(3)} | "
                    f"Tipo: {tipo}"
                )
        print(linha_separadora)
