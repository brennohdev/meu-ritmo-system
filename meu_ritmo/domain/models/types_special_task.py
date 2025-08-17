from meu_ritmo.domain.models.special_task import TarefaEspecial
import datetime

class TarefaRecorrente(TarefaEspecial):
    """Tarefa que se repete automaticamente após conclusão"""
    
    def __init__(self, *args, **kwargs):
        kwargs['efeito_especial'] = "Recorrência semanal"
        super().__init__(*args, **kwargs)
    
    def _calcular_data_limite(self) -> datetime.date:
        return datetime.date.today() + datetime.timedelta(days=7)
    
    def aplicar_efeito_especial(self) -> str:
        return f"🔁 Esta tarefa se repetirá em 7 dias (em {self.data_limite})"

class TarefaUrgente(TarefaEspecial):
    """Tarefa com prazo muito curto e bônus de energia"""
    
    def __init__(self, *args, **kwargs):
        kwargs['efeito_especial'] = "Urgência com bônus"
        super().__init__(*args, **kwargs)
    
    def _calcular_data_limite(self) -> datetime.date:
        return datetime.date.today() + datetime.timedelta(days=1)
    
    def aplicar_efeito_especial(self) -> str:
        return "⏰ Tarefa urgente concluída! +15 de energia extra!"
    
    def marcar_como_concluida(self):
        energia = super().marcar_como_concluida()
        return energia + 15  # Bônus por urgência