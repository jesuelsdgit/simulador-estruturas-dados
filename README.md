Markdown
# Simulador Interativo de Estruturas de Dados (Pilha e Fila)

Este projeto apresenta uma aplicação web interativa desenvolvida com **Streamlit** (Python) que atua como front-end para algoritmos de estruturas de dados baseados em alocação dinâmica de memória em **C++**. A comunicação entre a interface gráfica e a lógica de baixo nível ocorre através de comunicação de processos via CLI (`subprocess`), atendendo aos requisitos da disciplina.

---

## 🛠️ Pré-requisitos e Dependências

Para compilar e executar este projeto localmente no Windows, você precisará de:

1. **Python 3.x** instalado.
2. Compilador **GCC/G++** (como o MSYS2/MinGW) configurado nas variáveis de ambiente (`PATH`) do sistema.
3. Biblioteca do **Streamlit** instalada no ambiente Python.

---

## 🚀 Instruções de Instalação e Execução

### 1. Clonar o Repositório
Caso queira baixar o projeto via terminal:
```bash
git clone [https://github.com/jesuelsdgit/simulador-estruturas-dados.git](https://github.com/jesuelsdgit/simulador-estruturas-dados.git)
cd simulador-estruturas-dados
2. Instalar as Dependências do Python
Instale o framework Streamlit executando o comando abaixo no terminal do seu sistema ou do VS Code:

Bash
pip install streamlit
## 3. Compilar O Código C++
O script Python busca especificamente pelo executável estruturas.exe na mesma pasta. Compile o arquivo-fonte em C++ utilizando o comando:

Bash
g++ estruturas.cpp -o estruturas.exe
4. Executar a Aplicação Web
Inicie o servidor local do Streamlit para abrir a interface no seu navegador padrão:

Bash
python -m streamlit run app.py
A aplicação abrirá automaticamente no endereço local, normalmente em http://localhost:8501.

📊 Funcionalidades Implementadas
Seleção Dinâmica: Alternância instantânea entre as estruturas de Pilha e Fila através da barra lateral.

Operações Fundamentais: Comandos interativos de Inserção (Push / Enqueue) e Remoção (Pop / Dequeue) que manipulam diretamente os nós na memória RAM via alocação dinâmica em C++.

Direção de Crescimento Visual: Conforme exigido no enunciado, a Pilha cresce e se comporta verticalmente (LIFO), enquanto a Fila se estrutura horizontalmente (FIFO), destacando os pontos de entrada e saída (topo, início e fim).

Métricas em Tempo Real: Exibição imediata das propriedades calculadas diretamente pelo back-end em C++:

Tamanho atual da estrutura.

Somatório de todos os valores presentes.

Identificação do menor valor contido.

Identificação do maior valor contido.

Persistência de Estado: Gravação e leitura síncrona em arquivos de texto locais (pilha.txt e fila.txt), garantindo a retenção e persistência dos dados entre as ações do usuário na interface web.

Customização de Interface: Botões integrados na barra lateral para alternância em tempo real entre o tema claro e o tema escuro (Dark Mode).
