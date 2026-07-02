#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// A estrutura do nó é a mesma para Pilha e Fila (Alocação Dinâmica)
struct No {
    int Info; // Mudamos para int para alinhar direto com o Streamlit
    No *Lig;
};

// --- OPERAÇÕES DA PILHA (LIFO) ---
void Empilha(No* &Topo, int Elemento) {
    No *Aux = new No{Elemento, Topo};
    Topo = Aux;
}
bool Desempilha(No* &Topo, int &Valor) {
    if (!Topo) return false;
    No *Aux = Topo;
    Valor = Topo->Info;
    Topo = Topo->Lig;
    delete Aux;
    return true;
}

// --- OPERAÇÕES DA FILA (FIFO) ---
void InsereFila(No* &Com, No* &Fim, int Novo) {
    No *P = new No{Novo, NULL};
    if (!Com) Com = Fim = P;
    else { Fim->Lig = P; Fim = P; }
}
bool RetiraFila(No* &Com, No* &Fim, int &Valor) {
    if (!Com) return false;
    No *P = Com;
    Valor = P->Info;
    Com = Com->Lig;
    if (!Com) Fim = NULL;
    delete P;
    return true;
}

int main(int argc, char* argv[]) {
    if (argc < 3) return 1;

    string tipo = argv[1];    // "pilha" ou "fila"
    string comando = argv[2]; // "push", "pop" ou "status"
    string nomeArquivo = tipo + ".txt";

    No *Com = NULL, *Fim = NULL; // Usados pela Fila e Pilha (Com = Topo)

    // 1. CARREGA DADOS DO ARQUIVO
    ifstream arquivoEntrada(nomeArquivo);
    int x;
    while (arquivoEntrada >> x) {
        if (tipo == "fila") InsereFila(Com, Fim, x);
        else Empilha(Com, x); // Para a pilha, ler sequencialmente já mantém a ordem visual correta
    }
    arquivoEntrada.close();

    // 2. EXECUTA COMANDOS DO PYTHON
    if (comando == "push" && argc >= 4) {
        int val = stoi(argv[3]);
        if (tipo == "fila") InsereFila(Com, Fim, val);
        else Empilha(Com, val);
    } else if (comando == "pop") {
        int descarte;
        if (tipo == "fila") RetiraFila(Com, Fim, descarte);
        else Desempilha(Com, descarte);
    }

    // 3. CALCULA ESTATÍSTICAS E SALVA NO ARQUIVO (Tudo em um único loop)
    ofstream arquivoSaida(nomeArquivo);
    string elementos_str = "";
    int tam = 0, soma = 0, menor = 999, maior = -999;

    int valor;
    // Esvazia a estrutura para calcular e salvar
    while (tipo == "fila" ? RetiraFila(Com, Fim, valor) : Desempilha(Com, valor)) {
        arquivoSaida << valor << " ";
        tam++;
        soma += valor;
        if (valor < menor) menor = valor;
        if (valor > maior) maior = valor;
        
        // Formata a string para o Python (Inverte a ordem da pilha para exibição visual do topo)
        if (tipo == "pilha") elementos_str = to_string(valor) + (elementos_str.empty() ? "" : ",") + elementos_str;
        else elementos_str += to_string(valor) + ",";
    }
    arquivoSaida.close();
    if (!elementos_str.empty() && tipo == "fila") elementos_str.pop_back(); // Remove última vírgula da fila

    // 4. ENVIA RESPOSTA PARA O PYTHON
    if (tam == 0) cout << "VAZIA|0|0|0|0" << endl;
    else cout << elementos_str << "|" << tam << "|" << soma << "|" << menor << "|" << maior << endl;

    return 0;
}