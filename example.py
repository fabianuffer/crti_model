import numpy as np
import matplotlib.pyplot as plt


def generate_example(omega):
    Gamma = np.array([[0, 1, 0.5], [0, 0, 0.5], [0, 0, 0]])
    A = np.array([100, 70, 20])
    l1 = np.array([-20 * omega, -10 * omega, -5 * omega])
    l2 = np.array([-30 * omega, -20 * omega, -10 * omega])
    R1 = np.array([[0, -12 * omega, -10 * omega], [12 * omega, 0, 2 * omega], [10 * omega, -2 * omega, 0]])
    R2 = np.zeros((3, 3))
    return Gamma, A.T, [l1.T, l2.T], [R1, R2]


def check_constraint(P, A, Ls, Rs):
    """This function should check the consistency of the input data
    e.g. in the ownership matrix there is not more than 100% ownership, ..."""
    pass


def bs_equation(P, A, Ls, Rs):
    n = Rs[0].shape[0]
    u = np.ones(n)
    S = []
    for L, R in zip(Ls, Rs):
        S.append(L + np.dot(R, u))
    return np.linalg.solve(np.identity(n) - P, A + sum(S))


def insolvency_equation(P, A, Ls, Rs, Sigma_s):
    n = Rs[0].shape[0]
    u = np.ones(n)
    S = []
    for L, R, sigma in zip(Ls, Rs, Sigma_s):
        R_plus = np.maximum(R, 0)
        R_minus = np.minimum(R, 0)
        Temp = np.diag(L + np.dot(R_minus, u)) + R_plus
        S.append(np.dot(Temp, np.ones(n) - sigma))
    return np.linalg.solve(np.identity(n) - P, A + sum(S))


def is_admissible(G, Sigma_s):
    g_bigger_zero = [g > 0 for g in G]
    if all(g_bigger_zero):
        return True
    # Check for other possible admissible solution
    return False


def find_admissible_solution(P, A, Ls, Rs):
    S = len(Ls)
    n = Rs[0].shape[0]

    #TODO: Implement the iteration
    Sigma_s = [np.zeros(n) for _ in range(S)]
    G = insolvency_equation(P, A, Ls, Rs, Sigma_s)
    print is_admissible(G, Sigma_s)
    print G


def plot_balance_sheets(participation, asset, ext_liabilites, int_transactions):
    """ Implement picture of page 10 in presentation"""
    pass

if __name__ == "__main__":
    if False:
        # Solution for example with omega = 1
        participation, asset, ext_liabilites, int_transactions = generate_example(1)
        print bs_equation(participation, asset, ext_liabilites, int_transactions)

    if False:
        # Plot for omega between 0 and 2, there is no insolvency
        Gs = []
        omegas = np.linspace(0, 2, 100)
        for omega in omegas:
            participation, asset, ext_liabilites, int_transactions = generate_example(omega)
            G = bs_equation(participation, asset, ext_liabilites, int_transactions)
            Gs.append(G)
        plt.plot(omegas, Gs)
        plt.legend(('Company 1', 'Company 2', 'Company 3'))
        plt.show()

    participation, asset, ext_liabilites, int_transactions = generate_example(3.5)
    find_admissible_solution(participation, asset, ext_liabilites, int_transactions)