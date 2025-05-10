import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rnd # rnd is used by sample, but sample is in funcoes_markov
from funcoes_markov import transition_matrix, sample

if __name__ == '__main__':
    print("\n--- Questão 5: Amostrando e plotando trajetórias ---")
    n_q5 = 10
    tm_q5 = transition_matrix(n_q5)
    k_q5 = 100  # O enunciado do teste pede 100 passos para o plot
    s0_q5 = 0

    plt.figure(figsize=(12, 8))
    num_trajectories_q5 = 20
    print(f"Gerando e plotando {num_trajectories_q5} trajetórias de {k_q5} passos para n={n_q5}...")
    for i in range(num_trajectories_q5):
        # A função sample já está em funcoes_markov.py
        states_trajectory = sample(tm_q5, k_q5, s0_q5)
        plt.plot(states_trajectory, label=f'Trajetória {i + 1}' if i < 5 else None)
    
    plt.xlabel("Passo (k)")
    plt.ylabel("Estado")
    plt.title(f"{num_trajectories_q5} Amostras de Trajetórias da Cadeia de Markov (n={n_q5}, k={k_q5}, s0={s0_q5})")
    plt.yticks(np.arange(n_q5))
    plt.grid(True, axis='y')
    if num_trajectories_q5 <= 10:
        plt.legend()
    plt.savefig("qsn5.png")
    print("Gráfico da Questão 5 guardado como qsn5.png")
    plt.close()

    # Exemplo de uma trajetória com k=20 (para n=10, s0=0) como no PDF:
    # rnd.seed(42) # Para reprodutibilidade, se necessário para um exemplo específico
    # print("\nExemplo de uma trajetória com k=20 (para n=10, s0=0):")
    # example_trajectory = sample(tm_q5, 20, s0_q5)
    # print(example_trajectory)

