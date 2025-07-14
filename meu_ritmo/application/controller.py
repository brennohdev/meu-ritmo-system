import datetime
import time

from meu_ritmo.domain.models.active_day import DiaAtivo
from meu_ritmo.domain.models.task import Tarefa
from meu_ritmo.logic.cases.get_data_new_task import obter_dados_nova_tarefa
from meu_ritmo.logic.cases.task_updater import concluir_tarefa_interativo


class MeuRitmoApp:
    """
    A classe principal que controla o fluxo da aplicação.
    """

    def __init__(self):
        self.dia_atual = DiaAtivo(datetime.date.today())
        self._limpar_tela()
        print("Olá, Camila! Bem-vinda ao seu assistente de rotina, Meu Ritmo.")
        time.sleep(4)

    def _limpar_tela(self):
        print("\n" * 100)

    def _exibir_menu(self):
        print("\n Meu Ritmo")
        print("1. Adicionar uma nova tarefa")
        print("2. Mostrar resumo do dia")
        print("3. Concluir uma tarefa")
        print("4. Sair do programa")
        print("=" * 37)

    def _processar_adicionar_tarefa(self):
        self._limpar_tela()

        dados_da_tarefa = obter_dados_nova_tarefa()

        if dados_da_tarefa:
            nova_tarefa = Tarefa(**dados_da_tarefa)

            self.dia_atual.adicionar_tarefa(nova_tarefa)
            print("\n Tarefa adicionada com sucesso!")
            time.sleep(2)

    def _processar_ver_resumo(self):
        self._limpar_tela()
        self.dia_atual.mostrar_resumo()
        input("\n Pressione Enter para voltar ao menu...")

    def _processar_concluir_tarefa(self):
        self._limpar_tela()
        print("--- Concluir Tarefa ---")

        tarefa_concluida = concluir_tarefa_interativo(self.dia_atual.tarefas)

        if tarefa_concluida:
            print(
                f"\n Parabéns! Tarefa '{tarefa_concluida.descricao}' marcada como concluída."
            )
            time.sleep(2)

    def run(self):
        while True:
            self._limpar_tela()
            self._exibir_menu()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self._processar_adicionar_tarefa()
            elif escolha == "2":
                self._processar_ver_resumo()
            elif escolha == "3":
                self._processar_concluir_tarefa()
            elif escolha == "4":
                self._limpar_tela()
                print("\nAté a próxima! Cuide-se.")
                break
            else:
                print("\nOpção inválida, por favor, tente novamente.")
                time.sleep(2)
