import numpy as np
import matplotlib.pyplot as plt
from funcoes_markov import transition_matrix, propagate, sample

def solve_question_7():
    n_q7 = 25
    k_q7 = 100
    s0_q7 = 0
    num_samples_q7 = 1000
    print(f"\n--- Questão 7: Comparando amostragem com teoria para n={n_q7}, k={k_q7}, {num_samples_q7} amostras ---")
    tm_q7 = transition_matrix(n_q7)
    final_states_from_samples = np.zeros(num_samples_q7, dtype=int)
    print(f"Gerando {num_samples_q7} trajetórias e registando estados finais...")
    for i in range(num_samples_q7):
        if (i + 1) % 100 == 0:
            print(f"  Processada trajetória {i + 1}/{num_samples_q7}")
        trajectory = sample(tm_q7, k_q7, s0_q7)
        final_states_from_samples[i] = trajectory[-1]
    p0_q7 = np.zeros(n_q7)
    p0_q7[s0_q7] = 1.0
    theoretical_distribution_prob = propagate(p0_q7, k_q7, tm_q7)
    theoretical_distribution_counts = theoretical_distribution_prob * num_samples_q7
    plt.figure(figsize=(12, 8))
    bin_edges = np.arange(n_q7 + 1) - 0.5
    plt.hist(final_states_from_samples, bins=bin_edges, rwidth=0.8, label='Distribuição Amostrada (Histograma)', alpha=0.7, color='blue', density=False)
    states_axis = np.arange(n_q7)
    plt.plot(states_axis, theoretical_distribution_counts, marker='o', linestyle='-', color='red', label=f'Distribuição Teórica (Esperada x{num_samples_q7})')
    plt.xlabel('Estado Final')
    plt.ylabel(f'Contagem (de {num_samples_q7} amostras)')
    plt.title(f'Comparação: Distribuição de Estados Finais Amostrada vs. Teórica (n={n_q7}, k={k_q7})')
    plt.xticks(states_axis)
    plt.legend()
    plt.grid(True, axis='y')
    plt.savefig('qsn7.png')
    print('Gráfico da Questão 7 guardado como qsn7.png')
    plt.close()

if __name__ == '__main__':
    print("--- Executando Questão 7 ---")
    solve_question_7()

