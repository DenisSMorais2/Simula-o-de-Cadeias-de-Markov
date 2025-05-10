import numpy as np
import matplotlib.pyplot as plt
from funcoes_markov import transition_matrix, propagate

def solve_question_4a():
    n_q4a = 10
    tm_q4a = transition_matrix(n_q4a)
    p0_q4a = np.zeros(n_q4a)
    p0_q4a[0] = 1.0
    target_prob = 0.5
    final_state_index = n_q4a - 1
    num_steps_val = 0
    current_prob_final_state = 0.0
    # pk = p0_q4a.copy() # Not needed here, propagate handles p0
    max_steps = 1000
    print(f"\n--- Questão 4a: Calculando passos para P(estado {final_state_index}) >= {target_prob} com n={n_q4a} ---")
    while current_prob_final_state < target_prob and num_steps_val <= max_steps:
        num_steps_val += 1
        pk_current = propagate(p0_q4a, num_steps_val, tm_q4a)
        current_prob_final_state = pk_current[final_state_index]
    if current_prob_final_state >= target_prob:
        print(f"Número de passos para P(estado {final_state_index}) >= {target_prob}: {num_steps_val}")
        print(f"Probabilidade no estado final no passo {num_steps_val}: {current_prob_final_state:.6f}")
        return num_steps_val
    else:
        print(f"Não foi possível atingir P(estado {final_state_index}) >= {target_prob} em {max_steps} passos.")
        print(f"Probabilidade no estado final no passo {max_steps}: {current_prob_final_state:.6f}")
        return -1

def num_steps(n):
    if n < 3:
        print(f"Aviso: n={n} é menor que 3. O comportamento pode não ser o esperado.")
    tm_q4b = transition_matrix(n)
    p0_q4b = np.zeros(n)
    p0_q4b[0] = 1.0
    target_prob = 0.5
    final_state_index = n - 1
    current_steps = 0
    current_prob_final_state = 0.0
    max_steps_limit = n * 50
    if n >= 30:
        max_steps_limit = n * 100 # Increased limit for larger n in original code
    while current_prob_final_state < target_prob and current_steps <= max_steps_limit:
        current_steps += 1
        pk_current = propagate(p0_q4b, current_steps, tm_q4b)
        current_prob_final_state = pk_current[final_state_index]
    if current_prob_final_state >= target_prob:
        return current_steps
    else:
        print(f"Para n={n}, não foi possível atingir P(estado {final_state_index}) >= {target_prob} em {max_steps_limit} passos.")
        print(f"Probabilidade no estado final no passo {max_steps_limit}: {current_prob_final_state:.6f}")
        return -1

def solve_question_4c():
    n_values = np.arange(10, 41)
    steps_values = []
    print("\n--- Questão 4c: Calculando num_steps para n de 10 a 40 ---")
    for n_val in n_values:
        print(f"Calculando para n={n_val}...")
        steps = num_steps(n_val)
        if steps == -1:
            print(f"Aviso: num_steps({n_val}) retornou falha (demorou demasiado). Usando NaN para o gráfico.")
            steps_values.append(np.nan)
        else:
            steps_values.append(steps)
        print(f"Para n={n_val}, passos = {steps}")
    
    valid_indices = ~np.isnan(steps_values)
    n_values_plot = n_values[valid_indices]
    steps_values_plot = np.array(steps_values)[valid_indices]

    plt.figure(figsize=(10, 6))
    plt.plot(n_values_plot, steps_values_plot, marker='o', linestyle='-')
    plt.xlabel("Número de Estados (n)")
    plt.ylabel("Número de Passos para P(final) >= 0.5")
    plt.title("Número de Passos vs. Tamanho da Cadeia (n)")
    plt.grid(True)
    plt.savefig("qsn4c.png")
    print("Gráfico da Questão 4c (linear) guardado como qsn4c.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.semilogy(n_values_plot, steps_values_plot, marker='o', linestyle='-')
    plt.xlabel("Número de Estados (n)")
    plt.ylabel("Número de Passos para P(final) >= 0.5 (escala log)")
    plt.title("Número de Passos vs. Tamanho da Cadeia (n) - Escala Semilog Y")
    plt.grid(True, which="both", ls="-")
    plt.savefig("qsn4c_semilogy.png")
    print("Gráfico da Questão 4c (semilog-y) guardado como qsn4c_semilogy.png")
    plt.close()

    print("\nInterpretação do gráfico semilogarítmico (Questão 4c):")
    print("O gráfico semilogarítmico (com o eixo Y em escala logarítmica) ajuda a visualizar se a relação")
    print("entre 'n' (número de estados) e o 'número de passos' é exponencial. Se o gráfico semilogarítmico")
    print("mostrar uma linha aproximadamente reta, isso sugere que o número de passos cresce exponencialmente")
    print("com 'n'. No nosso caso, se a linha for reta, significa que k ≈ a * b^n ou log(k) ≈ log(a) + n*log(b), ")
    print("onde 'k' é o número de passos. Um crescimento exponencial indica que o problema se torna")
    print("significativamente mais 'longo' (em termos de passos para atingir o critério) à medida que 'n' aumenta.")

if __name__ == '__main__':
    print("--- Executando Questão 4a ---")
    steps_q4a = solve_question_4a()

    print("\n--- Testando Questão 4b: num_steps(n) ---")
    steps_n10 = num_steps(10)
    print(f"Resultado de num_steps(10): {steps_n10} (Esperado: {steps_q4a if steps_q4a != -1 else 'similar a 4a'})")
    if steps_q4a != -1 and steps_n10 == steps_q4a:
        print("Teste num_steps(10) passou!")
    elif steps_q4a == -1 and steps_n10 == -1:
        print("Teste num_steps(10) consistente com falha de 4a (se aplicável).")
    else:
        print("Teste num_steps(10) falhou ou inconsistente com 4a!")

    steps_n5 = num_steps(5)
    print(f"Resultado de num_steps(5): {steps_n5}")
    if steps_n5 != -1:
        tm_5_check = transition_matrix(5)
        p0_5_check = np.zeros(5)
        p0_5_check[0] = 1.0
        pk_5_check = propagate(p0_5_check, steps_n5, tm_5_check)
        print(f"Verificação para n=5, P(S4) no passo {steps_n5}: {pk_5_check[4]:.6f}")
        # Check if this is the first step P(S4) >= 0.5
        prob_at_step_minus_1 = -1
        if steps_n5 > 1:
            prob_at_step_minus_1 = propagate(p0_5_check, steps_n5 - 1, tm_5_check)[4]
        
        if pk_5_check[4] >= 0.5 and (steps_n5 == 1 or prob_at_step_minus_1 < 0.5):
             print(f"Teste num_steps(5) parece correto (resultado: {steps_n5}).")
        else:
             print(f"Teste num_steps(5) pode ter problemas (resultado: {steps_n5}, P(S4)={pk_5_check[4]:.6f}, P(S4)@step-1={prob_at_step_minus_1:.6f}).")
    else:
        print("num_steps(5) retornou falha.")

    print("\n--- Executando Questão 4c ---")
    solve_question_4c()

