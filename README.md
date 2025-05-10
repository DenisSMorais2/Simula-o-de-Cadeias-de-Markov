# Simulação de Cadeias de Markov

```bash
Este projeto implementa e analisa simulações de **Cadeias de Markov** discretas, com o objetivo de observar trajetórias, comportamento médio dos estados ao longo do tempo e comparar distribuições empíricas com distribuições teóricas. O projeto é dividido em várias "questões", cada uma abordando um aspecto da simulação.
```

## 📁 Estrutura do Projeto

markov_sim/
├── funcoes_markov.py
├── questao1.py
├── questao2.py
├── questao3.py
├── qsn4.png
├── qsn5.png
├── qsn6.png
├── qsn7.png
└── README.md

## 📦 Dependências

- Python 3.x
- numpy
- matplotlib

Instale as dependências com:

```bash
pip install numpy matplotlib
```
Descrição das Funções (em funcoes_markov.py):

def transition_matrix(n: int) -> np.ndarray:
    """Gera uma matriz de transição estocástica de dimensão n x n para uma cadeia de Markov."""

def sample(tm: np.ndarray, k: int, s0: int) -> np.ndarray:
    """Gera uma amostra de trajetória de k passos a partir do estado inicial s0 usando a matriz tm."""

def propagate(p0: np.ndarray, k: int, tm: np.ndarray) -> np.ndarray:
    """Propaga uma distribuição de probabilidade inicial p0 por k passos usando a matriz de transição."""

🔍 Questões
Questão 5 - Trajetórias Individuais
Gera e plota 20 trajetórias de uma cadeia de Markov de ordem n=10 com k=100 passos.

Todas as trajetórias começam no estado inicial `s0=0`.

Saída: `qsn5.png`.

Execute com:

```bash
python questao5.py
```

📊 Questão 6 - Estado Médio
Calcula o estado médio ao longo do tempo com base em 1000 amostras de trajetórias.

Usado para observar a tendência média do processo.

Parâmetros: `n=25, k=100, s0=0`.

Saída: `qsn6.png`.

Execute com:

```bash
python questao6.py
```

🧪 Questão 7 - Comparação com a Teoria
Compara a distribuição empírica dos estados finais após 100 passos com a distribuição teórica calculada por propagação.

Parâmetros: `n=25, k=100, s0=0, amostras=1000`.

Saída: `qsn7.png`.

Execute com:

```bash
python questao7.py
```

🖼 Exemplos de Saída
`qsn5.png`: Trajetórias individuais.

`qsn6.png`: Estado médio ao longo do tempo.

`qsn7.png`: Comparação entre distribuição amostrada e teórica.

📌 Notas Finais
A simulação assume cadeias de Markov homogêneas com espaço de estados finito e discreto.

As trajetórias são amostradas via transições probabilísticas definidas pela matriz tm.

🧠 Créditos
Este projeto foi desenvolvido como parte de um estudo sobre processos estocásticos e cadeias de Markov.
A função sample depende do módulo numpy.random, e a propagação usa multiplicação matricial com np.dot.

