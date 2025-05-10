import numpy as np
import numpy.random as rnd

def transition_matrix(n):
    if n < 3:
        raise ValueError('O número de estados (n) deve ser pelo menos 3.')
    tm = np.zeros((n, n))
    if n > 1:
        rows_i_plus_1 = np.arange(1, n)
        cols_i = np.arange(n - 1)
        tm[rows_i_plus_1, cols_i] = 0.8
    if n > 1:
        tm[0, np.arange(n - 1)] = 0.2
    tm[0, n - 1] = 0.0
    tm[n - 1, n - 1] = 1.0
    return tm

def propagate(p0, k, tm):
    pk_iter = p0.copy()
    if pk_iter.ndim == 0:
        pk_iter = np.array([pk_iter])
    if pk_iter.ndim > 1 and pk_iter.shape[0] != 1 and (pk_iter.shape[1] == 1):
        pk_iter = pk_iter.T
    pk_iter = pk_iter.flatten()
    m_prime = tm.T
    for _ in range(k):
        pk_iter = np.dot(pk_iter, m_prime)
    return pk_iter

def sample(tm, k, s0):
    num_states = tm.shape[0]
    if tm.shape[0] != tm.shape[1]:
        raise ValueError('A matriz de transição deve ser quadrada.')
    if not 0 <= s0 < num_states:
        raise ValueError(f'Estado inicial s0={s0} fora do intervalo [0, {num_states - 1}]')
    trajectory = np.zeros(k + 1, dtype=int)
    trajectory[0] = s0
    current_state = s0
    for i in range(k):
        probabilities = tm[:, current_state]
        if not np.isclose(np.sum(probabilities), 1.0):
            probabilities = probabilities / np.sum(probabilities)
        next_state = rnd.choice(np.arange(num_states), p=probabilities)
        trajectory[i + 1] = next_state
        current_state = next_state
    return trajectory

