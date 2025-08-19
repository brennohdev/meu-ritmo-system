import time
from typing import List
from meu_ritmo.domain.models.task import Tarefa

def deletar_tarefa_interativa(tarefas_do_dia: List[Tarefa]) -> None:
    """
    Exibe todas as tarefas e permite ao usuário escolher uma para deletar.
    Demonstra o Princípio da Responsabilidade Única (SRP).
    """
    if not tarefas_do_dia:
        print("\nNão há tarefas para deletar.")
        time.sleep(2)
        return
    
    print("\nQual tarefa você deseja deletar?")
    for i, tarefa in enumerate(tarefas_do_dia):
        print(f" {i+1}. {tarefa.descricao}")
        
    while True:
        try:
            escolha_str = input("\nDigite o número da tarefa (ou 'c' para cancelar): ")
            if escolha_str.lower() == "c":
                return

            escolha_num = int(escolha_str)
            if 1 <= escolha_num <= len(tarefas_do_dia):
                tarefa_removida = tarefas_do_dia.pop(escolha_num - 1)
                print(f"\n Tarefa '{tarefa_removida.descricao}' deletada com sucesso.")
                time.sleep(2)
                break
            else:
                print("Erro: Número inválido. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número ou 'c'.")