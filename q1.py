import numpy as np
from funcoes_markov import transition_matrix

if __name__ == '__main__':
    print("--- Questão 1: Testando a função transition_matrix ---")
    # Teste para n=10
    tm_10 = transition_matrix(10)
    print('\nMatriz de transição para n=10:')
    print(tm_10)

    expected_tm_10 = np.array([
        [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0. ],
        [0.8, 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. ],
        [0. , 0.8, 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. ],
        [0. , 0. , 0.8, 0. , 0. , 0. , 0. , 0. , 0. , 0. ],
        [0. , 0. , 0. , 0.8, 0. , 0. , 0. , 0. , 0. , 0. ],
        [0. , 0. , 0. , 0. , 0.8, 0. , 0. , 0. , 0. , 0. ],
        [0. , 0. , 0. , 0. , 0. , 0.8, 0. , 0. , 0. , 0. ],
        [0. , 0. , 0. , 0. , 0. , 0. , 0.8, 0. , 0. , 0. ],
        [0. , 0. , 0. , 0. , 0. , 0. , 0. , 0.8, 0. , 0. ],
        [0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0.8, 1. ]
    ])
    print('\nMatriz de transição esperada para n=10:')
    print(expected_tm_10)

    if np.allclose(tm_10, expected_tm_10):
        print('\nTeste para n=10 passou!')
    else:
        print('\nTeste para n=10 falhou.')
        print('Diferença:')
        print(tm_10 - expected_tm_10)

    # Teste para n=3
    tm_3 = transition_matrix(3)
    print('\nMatriz de transição para n=3:')
    print(tm_3)

    expected_tm_3 = np.array([
        [0.2, 0.2, 0.0],
        [0.8, 0.0, 0.0],
        [0.0, 0.8, 1.0]
    ])
    print('\nMatriz de transição esperada para n=3:')
    print(expected_tm_3)

    if np.allclose(tm_3, expected_tm_3):
        print('\nTeste para n=3 passou!')
    else:
        print('\nTeste para n=3 falhou.')
        print('Diferença:')
        print(tm_3 - expected_tm_3)

