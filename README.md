# Projeto: Analisador de Texto Simples (Colaborativo)

Bem-vindo ao projeto Analisador de Texto Simples! Este projeto foi criado como uma ferramenta de aprendizado para praticar o fluxo de trabalho colaborativo usando Git e GitHub, incluindo a criação de branches, submissão de Pull Requests (PRs) e, o mais importante, a resolução de conflitos de merge.

## 🎯 Objetivo Educacional

O objetivo principal deste projeto é simular um ambiente onde múltiplos desenvolvedores (vocês, os alunos!) contribuem para uma mesma base de código. Ao longo do exercício, vocês irão:

* Clonar um repositório existente.
* Criar branches para desenvolver novas funcionalidades isoladamente.
* Fazer commits seguindo boas práticas.
* Enviar (push) suas alterações para o repositório remoto.
* Abrir Pull Requests para integrar suas contribuições à branch principal.
* Vivenciar e resolver conflitos de merge que surgem quando diferentes alterações são feitas no mesmo trecho de código.

## 📝 Descrição do Projeto

O `analisador_texto.py` é um script Python simples que realiza algumas análises básicas em um texto de exemplo. Novas funcionalidades de análise são fornecidas em módulos separados, e a tarefa dos contribuidores é integrar essas funcionalidades ao script principal.

## 📁 Estrutura do Projeto

analisador_projeto/
├── analisador_texto.py         # Script principal que será modificado
├── modulos/                    # Diretório contendo os módulos com as funções de análise
│   ├── init.py
│   ├── contagem.py
│   ├── caracteres.py
│   ├── estrutura.py
│   ├── formatacao.py
│   └── frequencia.py
└── README.md                   # Este arquivo

## 🚀 Sua Tarefa como Contribuidor

1.  **Clone o Repositório:**
    ```bash
    git clone git@github.com:alcantaraolucas/text-analyzer.git
    cd analisador_projeto
    ```

2.  **Crie uma Nova Branch:**
    Crie uma branch com um nome descritivo para a funcionalidade que você irá adicionar (ex: `feature/integrar-contagem-caracteres` ou `aluno-joao/adicionar-maiusculas`).
    ```bash
    git checkout -b nome-da-sua-branch
    ```

3.  **Implemente a Funcionalidade:**
    * Você receberá uma tarefa específica para integrar uma funcionalidade de um dos módulos pré-existentes no diretório `modulos/`.
    * Sua principal modificação será no arquivo `analisador_texto.py`.
    * Você precisará:
        1.  Adicionar a declaração de `import` necessária para trazer a função do módulo apropriado.
        2.  Chamar a função importada dentro da função `main()` do `analisador_texto.py`, passando o `texto_exemplo`.
        3.  Adicionar um comando `print()` para exibir o resultado da análise de forma clara.

4.  **Adicione e Faça Commit das Suas Alterações:**
    ```bash
    git add analisador_texto.py
    git commit -m "feat: Integra funcionalidade de [descrição da sua tarefa]"
    ```
    (Ex: `feat: Integra contagem de caracteres com espaços`)

5.  **Envie Suas Alterações para o Repositório Remoto:**
    ```bash
    git push origin nome-da-sua-branch
    ```

6.  **Abra um Pull Request (PR):**
    * Vá para a página do repositório no GitHub.
    * Você verá uma notificação para criar um Pull Request a partir da sua branch recém-enviada. Clique nela.
    * Adicione um título e uma breve descrição ao seu PR (se necessário) e crie-o, direcionando-o para a branch principal (`main` ou `master`).

7.  **Participe da Revisão e Resolva Conflitos:**
    * Outros podem revisar seu código (em um cenário real).
    * **Importante:** É provável que surjam conflitos de merge quando seu PR tentar ser integrado à branch principal, especialmente se outros colegas já tiverem mergeado alterações no mesmo arquivo (`analisador_texto.py`).
    * Siga as instruções do monitor para resolver esses conflitos localmente, fazer commit da resolução e atualizar seu PR.

## 🛠️ Módulos de Funcionalidades Disponíveis

O diretório `modulos/` contém as seguintes funcionalidades prontas para serem integradas:

* `modulos.contagem`:
    * `contar_palavras(texto)`: Conta o número de palavras. (Já integrado no base)
* `modulos.caracteres`:
    * `contar_caracteres_com_espacos(texto)`: Conta caracteres, incluindo espaços.
    * `contar_caracteres_sem_espacos(texto)`: Conta caracteres, excluindo espaços.
* `modulos.estrutura`:
    * `contar_linhas(texto)`: Conta o número de linhas.
    * `contar_sentencas(texto)`: Conta o número de sentenças (baseado em `.`, `!`, `?`).
* `modulos.formatacao`:
    * `converter_para_maiusculas(texto)`: Converte o texto para maiúsculas.
    * `converter_para_minusculas(texto)`: Converte o texto para minúsculas.
* `modulos.frequencia`:
    * `obter_frequencia_palavras(texto)`: Retorna um dicionário com a frequência de cada palavra.

## ▶️ Como Executar o Script

Após clonar o repositório e (opcionalmente) fazer suas modificações, você pode executar o script principal com:

```bash
python analisador_texto.py

Divirtam-se aprendendo e colaborando! Não hesitem em pedir ajuda ao monitor.
