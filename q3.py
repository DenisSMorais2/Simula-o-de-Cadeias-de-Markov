import numpy as np
import matplotlib.pyplot as plt
from funcoes_markov import transition_matrix, propagate

def solve_question_3():
    n_q3 = 10
    tm_q3 = transition_matrix(n_q3)
    p0_q3 = np.zeros(n_q3)
    p0_q3[0] = 1.0
    num_steps_to_plot = 10
    states = np.arange(n_q3)
    plt.figure(figsize=(12, 8))
    for k_step in range(1, num_steps_to_plot + 1):
        pk = propagate(p0_q3, k_step, tm_q3)
        plt.plot(states, pk, marker='o', linestyle='-', label=f'Passo {k_step}')
    plt.xlabel('Estado')
    plt.ylabel('Probabilidade')
    plt.title(f'Distribuição de Probabilidades por Estado após k Passos (n={n_q3})')
    plt.xticks(states)
    plt.legend()
    plt.grid(True)
    plt.savefig('qsn3.png')
    print('\nGráfico da Questão 3 guardado como qsn3.png')
    plt.close()

if __name__ == '__main__':
    print("--- Questão 3: Plotando distribuições de probabilidade ---")
    solve_question_3()

