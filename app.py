import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Simulador de Estruturas MESTRADO", layout="centered")
st.title("🔄 ALGORITMOS E ESTRUTURAS DE DADOS: Pilha e Fila (C++ com Python)")

# Barra lateral para escolha da estrutura
tipo_estrutura = st.sidebar.selectbox(
    "Escolha a Estrutura de Dados:",
    ("pilha", "fila")
)

# Força o caminho correto do executável no Windows
EXEC_PATH = os.path.abspath("estruturas.exe")

# --- FUNÇÃO PARA CHAMAR O C++ ---
def chamar_cpp(comando, valor=""):
    if not os.path.exists(EXEC_PATH):
        return "ERRO: O arquivo estruturas.exe nao foi encontrado na pasta."
    
    # Monta a lista de argumentos para o subprocess
    args = [EXEC_PATH, tipo_estrutura, comando]
    if valor:
        args.append(str(valor))
        
    try:
        # Executa o C++ passando os argumentos de forma limpa
        resultado = subprocess.run(args, capture_output=True, text=True, check=True)
        return resultado.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"ERRO_CPP: {e.stderr}"

# --- EXECUÇÃO INICIAL (STATUS) ---
output_cpp = chamar_cpp("status")

# --- INTERFACE DE COMANDOS ---
col1, col2 = st.columns(2)

with col1:
    novo_valor = st.number_input("Digite um valor inteiro:", min_value=0, max_value=999, value=10)
    if st.button("Inserir (Push / Enqueue)", use_container_width=True):
        chamar_cpp("push", novo_valor)
        st.rerun()

with col2:
    st.write("###") 
    if st.button("Remover (Pop / Dequeue)", use_container_width=True):
        chamar_cpp("pop")
        st.rerun()

st.markdown("---")

# --- PROCESSAMENTO DOS DADOS VINDOS DO C++ ---
st.subheader(f"📊 Visualização da {tipo_estrutura.capitalize()}")

if not output_cpp or "VAZIA" in output_cpp or "ERRO" in output_cpp:
    st.info(f"A {tipo_estrutura} está vazia no momento. Adicione elementos acima!")
    tamanho, soma, menor, maior = 0, 0, "-", "-"
    dados_lista = []
else:
    try:
        partes = output_cpp.split("|")
        valores_str = partes[0]
        tamanho = partes[1]
        soma = partes[2]
        menor = partes[3]
        maior = partes[4]
        dados_lista = [int(x) for x in valores_str.split(",") if x.strip()]
    except Exception:
        st.error("Erro ao processar o retorno do C++.")
        tamanho, soma, menor, maior = 0, 0, "-", "-"
        dados_lista = []

# --- RENDERIZAÇÃO GRÁFICA ---
if dados_lista:
    if tipo_estrutura == "pilha":
        # Pilha cresce verticalmente (LIFO)
        for i, elem in enumerate(reversed(dados_lista)):
            if i == 0:
                st.markdown(f"🟩 **[ {elem} ]** ← `Topo (Entrada/Saída)`")
            else:
                st.markdown(f"⬛ [ {elem} ]")
    else:
        # Fila cresce horizontalmente (FIFO)
        fila_visual = ""
        for i, elem in enumerate(dados_lista):
            if i == 0:
                fila_visual += f"🟥 **[ {elem} ]** `Início (Saída)` ← "
            elif i == len(dados_lista) - 1:
                fila_visual += f"🟩 **[ {elem} ]** `Fim (Entrada)`"
            else:
                fila_visual += f"[ {elem} ] ← "
        if len(dados_lista) == 1:
            fila_visual = f"🟩🟥 **[ {dados_lista[0]} ]** `Início e Fim`"
        st.write(fila_visual)

st.markdown("---")

# --- CARDS DE ESTATÍSTICAS (MÉTRICAS DO C++) ---
st.subheader("📈 Propriedades Calculadas pelo C++")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Tamanho", str(tamanho))
c2.metric("Somatório", str(soma))
c3.metric("Menor Valor", str(menor))
c4.metric("Maior Valor", str(maior))