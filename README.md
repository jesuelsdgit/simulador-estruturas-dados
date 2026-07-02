# Simulador de Estruturas de Dados (Pilha e Fila)

Trabalho desenvolvido para a disciplina de Algoritmos e Estruturas de Dados. O projeto consiste em uma interface gráfica feita em Python (Streamlit) integrada com a lógica de manipulação e alocação dinâmica feita em C++. A comunicação entre o Python e o C++ é feita via linha de comando utilizando a biblioteca `subprocess`.

## Requisitos

Para rodar o projeto no Windows, é necessário ter instalado:
* Python 3
* Compilador G++ (MinGW / MSYS2) configurado no PATH
* Biblioteca Streamlit

## Como Rodar o Projeto

1. Certifique-se de estar na pasta do projeto e instale o Streamlit pelo terminal:

	pip install streamlit

2. Compile o código C++ para gerar o executável que o Python vai chamar:

	g++ estruturas.cpp -o estruturas.exe

3. Inicie a interface do Streamlit:

	python -m streamlit run app.py

O sistema vai abrir automaticamente uma aba no seu navegador padrão (geralmente no endereço `http://localhost:8501`).

## O que foi implementado

* **Estruturas Base:** Implementação de Pilha e Fila usando ponteiros e alocação dinâmica no C++.
* **Persistência:** Os dados inseridos não somem ao atualizar a página, pois são salvos em arquivos `.txt` locais pelo C++.
* **Visualização:** A interface gráfica renderiza a Pilha na vertical (mostrando o Topo) e a Fila na horizontal (mostrando Início e Fim).
* **Métricas:** O C++ calcula e devolve para a tela o tamanho atual, a soma dos elementos, além do maior e menor valor em tempo real.
* **Interface:** Opção de alternar entre tema claro e escuro direto na barra lateral.
