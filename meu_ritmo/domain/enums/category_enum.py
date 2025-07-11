from enum import Enum

class CategoriaEnum(Enum):
    """
    Define um conjunto fixo de categorias para as tarefas.
    garantindo consistência e evitando erros de digitação.
    """
    TRABALHO = "Trabalho"
    FACULDADE = "Faculdade"
    AFAZERES_DOMESTICOS = "Afazeres Domésticos"
    ACADEMIA = "Academia"
    LAZER = "Lazer"