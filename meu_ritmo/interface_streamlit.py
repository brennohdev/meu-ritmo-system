# meu_ritmo/interface_streamlit.py

import sys
import os
import pandas as pd
# Adiciona o diretório raiz do projeto (MEU-RITMO-SYSTEM) ao path do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import datetime

# As importações são ABSOLUTAS, pois agora o Python sabe onde encontrar "meu_ritmo"
from meu_ritmo.domain.enums.category_enum import CategoriaEnum
from meu_ritmo.domain.enums.priority_enum import PrioridadeEnum
from meu_ritmo.domain.models.task import Tarefa
from meu_ritmo.domain.models.active_day import DiaAtivo
from meu_ritmo.domain.models.types_special_task import TarefaRecorrente, TarefaUrgente
from meu_ritmo.logic.cases.get_data_new_task import MAPA_ENERGIA_CATEGORIAS

# --- MAPEAMENTO DE ÍCONES PARA UMA UI MAIS RICA ---
CATEGORIA_ICONS = {
    CategoriaEnum.TRABALHO: "💻",
    CategoriaEnum.FACULDADE: "🎓",
    CategoriaEnum.AFAZERES_DOMESTICOS: "🧹",
    CategoriaEnum.ACADEMIA: "🏋️‍♀️",
    CategoriaEnum.LAZER: "🎮",
}

PRIORIDADE_ICONS = {
    PrioridadeEnum.ALTA: "🔴",
    PrioridadeEnum.MEDIA: "🟡",
    PrioridadeEnum.BAIXA: "🟢",
}

# --- LÓGICA DO GRAFO (BFS) ---
def atualizar_status_tarefas(tarefas: list[Tarefa]):
    """
    Simula uma travessia no GRAFO de tarefas para definir
    quais estão bloqueadas por dependências.
    """
    for tarefa in tarefas:
        tarefa.bloqueada = tarefa.esta_bloqueada()

# --- Configuração Inicial da Página ---
st.set_page_config(
    page_title="Meu Ritmo",
    page_icon="📅",
    layout="wide"
)

# --- Gerenciamento de Estado ---
if 'dia_ativo' not in st.session_state:
    st.session_state.dia_ativo = DiaAtivo(datetime.date.today())

# --- Barra Lateral (Sidebar) ---
with st.sidebar:
    st.header("✨ Adicionar Nova Tarefa")
    
    with st.form("nova_tarefa_form", clear_on_submit=True):
        descricao = st.text_input("Descrição da tarefa")
        
        prioridade = st.selectbox(
            "Prioridade", 
            options=list(PrioridadeEnum), 
            format_func=lambda p: f"{PRIORIDADE_ICONS[p]} {p.name.capitalize()}"
        )
        
        categoria = st.selectbox(
            "Categoria",
            options=list(CategoriaEnum),
            format_func=lambda c: f"{CATEGORIA_ICONS[c]} {c.value}"
        )
        
        tipo_especial = st.selectbox(
            "Tipo de Tarefa", 
            ["Normal", "Recorrente", "Urgente"]
        )
        
        # FEATURE GRAFOS: Campo para selecionar pré-requisitos
        tarefas_pendentes = [t for t in st.session_state.dia_ativo.tarefas if not t.concluida]
        prereqs_selecionados = st.multiselect(
            "Esta tarefa depende de (pré-requisitos):",
            options=tarefas_pendentes,
            format_func=lambda t: t.descricao
        )

        submitted = st.form_submit_button("＋ Adicionar Tarefa", use_container_width=True, type="primary")
        
        if submitted:
            if not descricao.strip():
                st.warning("A descrição não pode estar em branco.")
            else:
                # Lógica para criar tarefa com dependências
                nova_tarefa = Tarefa(
                    descricao=descricao,
                    prioridade=prioridade,
                    categoria=categoria,
                    impacto_energia=MAPA_ENERGIA_CATEGORIAS[categoria],
                )
                nova_tarefa.prerequisitos = prereqs_selecionados
                st.session_state.dia_ativo.adicionar_tarefa(nova_tarefa)
                st.success(f"Tarefa '{descricao}' adicionada!")
                # A linha st.balloons() foi removida daqui.

# --- Painel Principal ---
st.title("Meu Ritmo 📅")
st.markdown("Seu gerenciador de tarefas e energia diária.")

# --- Exibição do Resumo do Dia ---
with st.container(border=True):
    data_hoje = st.session_state.dia_ativo.data.strftime('%d de %B de %Y')
    st.subheader(f"Resumo para {data_hoje}")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### Status da Camila: **{st.session_state.dia_ativo.nivel_de_cansaco}**")
        energia_atual = st.session_state.dia_ativo.energia_atual
        energia_inicial = st.session_state.dia_ativo.ENERGIA_INICIAL
        energia_percentual = energia_atual / energia_inicial if energia_inicial > 0 else 0
        st.progress(max(0, energia_percentual))
    
    with col2:
        st.metric(
            label="Energia Restante",
            value=f"{energia_atual} / {energia_inicial}"
        )

st.markdown("---")

# --- Lista de Tarefas ---
st.header("Tarefas do Dia")

if not st.session_state.dia_ativo.tarefas:
    st.info("Nenhuma tarefa para hoje. Que tal adicionar uma pela barra lateral? ✨")
else:
    tarefas_ordenadas = sorted(
        st.session_state.dia_ativo.tarefas, 
        key=lambda t: t.prioridade.value
    )
    
    # FEATURE GRAFOS: Atualiza o status antes de exibir
    atualizar_status_tarefas(tarefas_ordenadas)
    
    for i, tarefa in enumerate(tarefas_ordenadas):
        with st.container(border=True):
            is_disabled = tarefa.bloqueada
            status_icone = "🔒" if is_disabled else ("✅" if tarefa.concluida else "⭕️")
            
            cols = st.columns([0.1, 0.5, 0.25, 0.15])
            
            with cols[0]:
                st.markdown(f"### {status_icone}")
            
            with cols[1]:
                if tarefa.concluida:
                    st.markdown(f"~~**{tarefa.descricao}**~~")
                else:
                    st.markdown(f"**{tarefa.descricao}**")
                
                tipo_str = "Normal"
                if isinstance(tarefa, TarefaRecorrente):
                    tipo_str = "Recorrente 🔁"
                elif isinstance(tarefa, TarefaUrgente):
                    tipo_str = "Urgente ⏰"
                st.caption(f"{CATEGORIA_ICONS[tarefa.categoria]} {tarefa.categoria.value} | {tipo_str}")

            with cols[2]:
                st.markdown(f"**Prioridade:** {PRIORIDADE_ICONS[tarefa.prioridade]} {tarefa.prioridade.name.capitalize()}")
                
                cor_energia = "green" if tarefa.impacto_energia >= 0 else "red"
                st.markdown(f"**Energia:** <span style='color:{cor_energia};'>{tarefa.impacto_energia}</span>", unsafe_allow_html=True)

            with cols[3]:
                if not tarefa.concluida:
                    if st.button("Concluir", key=f"concluir_{i}", use_container_width=True, type="primary", disabled=is_disabled):
                        tarefa.marcar_como_concluida()
                        st.toast("Tarefa concluída! Bom trabalho! 🎉")
                        st.rerun()
                
                if st.button("Excluir", key=f"excluir_{i}", use_container_width=True):
                    st.session_state.dia_ativo.energia_atual -= tarefa.calcular_impacto_total() # Usa recursão para remover energia
                    st.session_state.dia_ativo.tarefas.remove(tarefa)
                    st.toast(f"Tarefa '{tarefa.descricao}' removida.", icon="🗑️")
                    st.rerun()
            
            # --- FEATURES RECURSÃO E SUB-TAREFAS ---
            if tarefa.sub_tarefas:
                st.markdown("---")
                for sub in tarefa.sub_tarefas:
                    status_sub = "✅" if sub.concluida else "⭕️"
                    st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp; {status_sub} &nbsp; _{sub.descricao}_ (`{sub.impacto_energia:+}`)")
            
            impacto_total = tarefa.calcular_impacto_total()
            if impacto_total != tarefa.impacto_energia:
                 st.info(f"Impacto total (com sub-tarefas): {impacto_total}", icon="💡")
            
            if not tarefa.concluida:
                with st.expander("Adicionar sub-tarefa"):
                    with st.form(f"sub_tarefa_form_{i}", clear_on_submit=True):
                        sub_descricao = st.text_input("Descrição da sub-tarefa", key=f"sub_desc_{i}")
                        sub_impacto = st.number_input("Impacto de energia", step=5, value=0, key=f"sub_imp_{i}")
                        
                        if st.form_submit_button("＋", use_container_width=True):
                            if sub_descricao:
                                nova_sub = Tarefa(
                                    descricao=sub_descricao, impacto_energia=int(sub_impacto),
                                    prioridade=tarefa.prioridade, categoria=tarefa.categoria
                                )
                                tarefa.sub_tarefas.append(nova_sub)
                                st.rerun()

# --- FEATURE TABELA HASH ---
st.markdown("---")
st.header("📊 Estatísticas do Dia")

with st.expander("Ver resumo por categoria"):
    if not st.session_state.dia_ativo.tarefas:
        st.write("Nenhuma tarefa para analisar.")
    else:
        # 1. Inicializa e preenche a Tabela Hash (dicionário)
        contagem_categorias = {}
        for tarefa in st.session_state.dia_ativo.tarefas:
            categoria = tarefa.categoria.value
            contagem_categorias[categoria] = contagem_categorias.get(categoria, 0) + 1
        
        # 2. Exibe os dados da Tabela Hash em um gráfico
        df_categorias = pd.DataFrame(
            list(contagem_categorias.items()),
            columns=['Categoria', 'Quantidade']
        )
        st.bar_chart(df_categorias, x='Categoria', y='Quantidade', color="#ff6347")