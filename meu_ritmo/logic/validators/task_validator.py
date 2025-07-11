from datetime import date

from meu_ritmo.domain.enums.category_enum import CategoriaEnum

from meu_ritmo.domain.enums.priority_enum import PrioridadeEnum


class Validacao_Tarefas:
    # Classe contendo metodos para validar parametros de classe

    def validar_descricao(descricao: str) -> tuple[bool, str]:
        if not isinstance(descricao, str):
            return (False, "Descrição deve ser do tipo string")

        if not descricao.strip():
            return (False, "Descrição deve ter no minimo 1 caracter")

        return (True, "")

    def validar_prioridade(prioridade: PrioridadeEnum) -> tuple[bool, str]:
        if not isinstance(prioridade, PrioridadeEnum):
            return (False, "Prioridade deve ser (Alta/Média/Baixa)")

        return (True, "")

    def validar_impacto_energia(impacto_energia: int) -> tuple[bool, str]:
        if not isinstance(impacto_energia, int):
            return (False, "Impacto de energia deve ser um número inteiro")

        return (True, "")

    def validar_categoria(categoria: CategoriaEnum) -> tuple[bool, str]:
        if not isinstance(categoria, CategoriaEnum):
            return (False, f"Categoria inválida apenas valores {list(CategoriaEnum)}")

        return (True, "")

    def validar_data_de_criacao(data_de_criacao: date) -> tuple[bool, str]:
        if not isinstance(data_de_criacao, date):
            return (False, "Data tem que ser do tipo válido")

        return (True, "")

    def validar_concluido(concluida: bool) -> tuple[bool, str]:
        if not isinstance(concluida, bool):
            return (False, "Concluida tem que ser [True/False]")

        return (True, "")

    def validar_tarefa_completa(
        classe,
        descricao: str,
        prioridade: int,
        impacto_energia: int,
        categoria: CategoriaEnum,
    ) -> tuple[bool, list[str]]:
        errors: list[str] = []

        valid_desc, msg_desc = classe.validar_descricao(descricao)

        if not valid_desc:
            errors.append(msg_desc)

        valid_prior, msg_prior = classe.validar_prioridade(prioridade)

        if not valid_prior:
            errors.append(msg_prior)

        valid_impa, msg_impa = classe.validar_impacto_energia(impacto_energia)

        if not valid_impa:
            errors.append(msg_impa)

        valid_categoria, msg_categoria = classe.validar_categoria(categoria)

        if not valid_categoria:
            errors.append(msg_categoria)

        return (len(errors) == 0, errors)
