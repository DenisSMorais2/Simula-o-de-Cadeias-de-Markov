import numpy as np
from funcoes_markov import transition_matrix, propagate

if __name__ == '__main__':
    print("\n--- Questão 2: Testando a função propagate ---")
    tm_q2 = transition_matrix(10)
    p0_q2 = np.zeros(10)
    p0_q2[0] = 1.0
    k_q2 = 30
    pk_q2 = propagate(p0_q2, k_q2, tm_q2)
    print(f'Distribuição após k={k_q2} passos, começando em p0={p0_q2}:')
    print(pk_q2)

    expected_pk_q2 = np.array([0.0816156 , 0.06787354, 0.05644353, 0.04694437, 0.03904617,
                               0.03247669, 0.02701094, 0.02246264, 0.01867741, 0.6074491 ])
    print('\nDistribuição esperada:')
    print(expected_pk_q2)

    if np.allclose(pk_q2, expected_pk_q2, atol=1e-07):
        print('\nTeste para propagate(p0, 30, tm_10) passou!')
    else:
        print('\nTeste para propagate(p0, 30, tm_10) falhou.')
        print('Diferença absoluta:', np.abs(pk_q2 - expected_pk_q2))
        print('Soma das probabilidades calculadas:', np.sum(pk_q2))
        print('Soma das probabilidades esperadas:', np.sum(expected_pk_q2))

