# Meu Ritmo

## *Um assistente de rotina consciente para ajudar a equilibrar produtividade e bem-estar.*

## Sobre o Projeto

"Meu Ritmo" é um projeto acadêmico desenvolvido para a disciplina de Programação Orientada a Objetos. A aplicação nasceu
da necessidade de criar uma ferramenta de organização que vai além de uma simples lista de tarefas. Para a nossa
persona, Camila, uma estudante sobrecarregada. O maior desafio não é a falta de tarefas, mas a gestão de sua própria
energia mental e física.

Este projeto implementa um sistema de "Bateria de Energia", onde cada tarefa possui um impacto (positivo ou negativo),
permitindo ao usuário visualizar e gerenciar sua disposição ao longo do dia, evitando o esgotamento.

## Funcionalidades

O projeto está sendo desenvolvido em etapas. Abaixo estão as funcionalidades implementadas e em andamento.

### Etapa 1 (Implementando)

* Criação de Tarefas: Adição de tarefas com descrição e prioridade.
* Sistema de Bateria de Energia: O dia começa com 100 pontos de energia que são consumidos ou recuperados com base nas
  tarefas.
* Categorias Inteligentes: O impacto energético é definido automaticamente ao escolher uma categoria pré-definida (ex:
  Trabalho, Lazer, Academia), simplificando a experiência do usuário.
* Arquitetura em Camadas: O código é organizado em Modelos, Lógica e Controle, seguindo as melhores práticas de design
  de software.
* Interface de Terminal: Interação com o usuário via linha de comando.

## Tecnologias Utilizadas

* Linguagem: Python 3.x
* Princípios: Programação Orientada a Objetos (POO)
* Ferramentas: Git, GitHub
* Bibliotecas: Apenas bibliotecas padrão do Python (Etapa 1).

## Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto em sua máquina local.

1. Clone o repositório:
   ```bash
   git clone [https://github.com/](https://github.com/)[SEU_USUARIO_GITHUB]/meu_ritmo_projeto.git
   ```

2. Navegue até a pasta do projeto:
   ```bash
   cd meu_ritmo_projeto
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   # Criar o ambiente
   python -m venv venv

   # Ativar no Windows
   .\venv\Scripts\activate

   # Ativar no macOS/Linux
   source venv/bin/activate
   ```

4. Instale as dependências (se houver):
   ```bash
   pip install -r requirements.txt
   ```
   (Atualmente, o arquivo pode estar vazio, mas este é o comando padrão.)

5. Execute a aplicação:
   ```bash
   python meu_ritmo/main.py
   ```

## Estrutura do Projeto

O projeto segue uma arquitetura em camadas para garantir a separação de responsabilidades e a escalabilidade:

```
meu_ritmo_projeto/                  <-- Pasta raiz, onde o repositório Git é inicializado.
│
├── .gitignore                      <-- Para ignorar arquivos desnecessários.
├── README.md                       <-- A documentação principal do projeto.
├── requirements.txt                <-- As dependências do projeto (mesmo que vazio agora).
├── apresentacao_etapa1.ipynb       <-- O ambiente virtual criado para o projeto.
│
└── meu_ritmo/                      <-- O "pacote" do código-fonte principal.
    │
    ├── __init__.py                  # Marca 'meu_ritmo' como o pacote principal.
    ├── main.py                      # O Lançador: simples, limpo, apenas inicia o app.
    │
    ├── application/                 # Pacote para o controle da aplicação.
    │   ├── __init__.py
    │   └── controller.py            # Contém a classe MeuRitmoApp, o cérebro da interação.
    │
    ├── logic/                       # Pacote para as regras de negócio.
    │   ├── __init__.py
    │   └── validation.py            # Contém as funções puras para validar entradas.
    │
    └── domain/
        ├── models/                  # Pacote para os modelos de dados.
            ├── __init__.py
            ├── task.py              # Contém a classe Tarefa.
            └── active_day.py        # Contém a classe DiaAtivo.
        └── enums/                   # Pacote para os ENUMS.
            ├── __init__.py
            └── category_enum.py     # Contém a classe Categoria, que define as categorias de tarefas.
                 
```

---

## Equipe

Este projeto é o resultado da colaboração e do esforço conjunto de:

* **[Brenno Henrique]** - ([@brennohdev](https://github.com/brennohdev))
* **[Samuel Colaço]** - ([@SamuelColaco](https://github.com/SamuelColaco))
* **[Gustavo Henrique]** - ([@yScroww](https://github.com/yScroww))

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

