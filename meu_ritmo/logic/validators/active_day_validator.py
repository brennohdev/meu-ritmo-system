from datetime import date

from meu_ritmo.domain.models.task import Tarefa


class DiaAtivo_Validator:

    def validar_data(data: date) -> tuple[bool, str]:
        if not isinstance(data, date):
            return (False, "Data tem que ser do tipo válido")

        return (True, "")

    def validar_tarefa(tarefas: list[Tarefa]) -> tuple[bool, str]:
        if not isinstance(tarefas, list):
            return (False, "Tarefas tem que ser uma lista")

        for tarefa in tarefas:
            if not isinstance(tarefa, Tarefa):
                return (False, "Os itens tem que ser da classe Tarefa")

        return (True, "")
