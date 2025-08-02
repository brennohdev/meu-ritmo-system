import time
from typing import Optional, List

from meu_ritmo.domain.models.task import Tarefa


def concluir_tarefa_interativo(tarefas_do_dia: List[Tarefa]) -> Optional[Tarefa]:
    """
    Filtra as tarefas pendentes, exibe-as para o usuário e processa a escolha.
    Retorna a tarefa que foi concluida ou None se nenhuma ação foi tomada.
    :param tarefas_do_dia: lista de tarefas
    :return: tarefa concluida ou None.
    """
    tarefas_pendentes = [t for t in tarefas_do_dia if not t.concluida]

    if not tarefas_pendentes:
        print("\nVocê não tem tarefas pendentes. Ótimo trabalho!")
        time.sleep(2)
        return None

    print("\nQual tarefa você concluiu?")
    for i, tarefa in enumerate(tarefas_pendentes):
        print(f"   {i + 1}. {tarefa.descricao}")

    while True:
        try:
            escolha_str = input("\nDigite o número da tarefa (ou 'c' para cancelar): ")
            if escolha_str.lower() == "c":
                return None

            escolha_num = int(escolha_str)
            if 1 <= escolha_num <= len(tarefas_pendentes):
                tarefa_a_concluir = tarefas_pendentes[escolha_num - 1]
                tarefa_a_concluir.marcar_como_concluida()

                return tarefa_a_concluir
            else:
                print("Erro: Número inválido. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número ou 'c'.")
