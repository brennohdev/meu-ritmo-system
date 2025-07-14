# meu_ritmo/logic/task_builder.py
from typing import Dict, Any
from meu_ritmo.domain.enums.category_enum import CategoriaEnum
from meu_ritmo.domain.enums.priority_enum import PrioridadeEnum
from meu_ritmo.logic.validators.task_validator import Validacao_Tarefas

# Mapa que conecta Categoria a um impacto de energia padrão
MAPA_ENERGIA_CATEGORIAS = {
    CategoriaEnum.TRABALHO: -30,
    CategoriaEnum.FACULDADE: -25,
    CategoriaEnum.AFAZERES_DOMESTICOS: -15,
    CategoriaEnum.ACADEMIA: +15,
    CategoriaEnum.LAZER: +20,
}


def obter_dados_nova_tarefa() -> Dict[str, Any]:
    """
    Função para obter os dados de uma nova tarefa do usuário e retornar um dicionário com os dados validados.
    """
    while True:
        descricao = input("Descrição da tarefa: ")
        is_valid, error_msg = Validacao_Tarefas.validar_descricao(descricao)
        if is_valid:
            break
        print(f"Erro: {error_msg}. Tente novamente.")

    while True:
        opcoes_prioridade = ", ".join([p.name.capitalize() for p in PrioridadeEnum])
        prioridade_str = input(f"Prioridade ({opcoes_prioridade}): ").lower().strip()

        prioridade_selecionada = None
        for p in PrioridadeEnum:
            if p.name.lower() == prioridade_str:
                prioridade_selecionada = p
                break

        if prioridade_selecionada:
            is_valid, error_msg = Validacao_Tarefas.validar_prioridade(
                prioridade_selecionada
            )
            if is_valid:
                break

        print("Erro: Prioridade inválida. Tente novamente.")

    while True:
        opcoes_categoria = ", ".join([c.value for c in CategoriaEnum])
        categoria_str = input(f"Categoria ({opcoes_categoria}): ").strip()

        categoria_selecionada = None
        for c in CategoriaEnum:
            if c.value.lower() == categoria_str.lower():
                categoria_selecionada = c
                break

        if categoria_selecionada:
            is_valid, error_msg = Validacao_Tarefas.validar_categoria(
                categoria_selecionada
            )
            if is_valid:
                break

        print("Erro: Categoria inválida. Tente novamente.")

    impacto_energia = MAPA_ENERGIA_CATEGORIAS[categoria_selecionada]

    dados_tarefa = {
        "descricao": descricao,
        "prioridade": prioridade_selecionada,
        "impacto_energia": impacto_energia,
        "categoria": categoria_selecionada,
    }

    return dados_tarefa
