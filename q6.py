import numpy as np
import matplotlib.pyplot as plt
from funcoes_markov import transition_matrix, sample

def solve_question_6():
    n_q6 = 25
    k_q6 = 100
    s0_q6 = 0
    num_samples_q6 = 1000
    print(f"\n--- Questão 6: Calculando estado médio para n={n_q6}, k={k_q6}, {num_samples_q6} amostras ---")
    tm_q6 = transition_matrix(n_q6)
    all_trajectories = np.zeros((num_samples_q6, k_q6 + 1))
    print(f"Gerando {num_samples_q6} trajetórias...")
    for i in range(num_samples_q6):
        if (i + 1) % 100 == 0:
            print(f"  Gerada trajetória {i + 1}/{num_samples_q6}")
        all_trajectories[i, :] = sample(tm_q6, k_q6, s0_q6)
    average_states_over_time = np.mean(all_trajectories, axis=0)
    time_steps = np.arange(k_q6 + 1)
    plt.figure(figsize=(12, 8))
    plt.plot(time_steps, average_states_over_time, marker=".", linestyle="-")
    plt.xlabel("Passo de Tempo (k)")
    plt.ylabel("Estado Médio")
    plt.title(f"Estado Médio da Cadeia de Markov vs. Tempo (n={n_q6}, {num_samples_q6} amostras)")
    plt.grid(True)
    plt.savefig("qsn6.png")
    print("Gráfico da Questão 6 guardado como qsn6.png")
    plt.close()

if __name__ == '__main__':
    print("--- Executando Questão 6 ---")
    solve_question_6()

