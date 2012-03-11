import numpy as np


def generate_example(omega):
    Gamma = np.array([[0, 1, 0.5], [0, 0, 0.5], [0, 0, 0]])
    A = np.array([100, 70, 20])
    l1 = np.array([-20 * omega, -10 * omega, -5 * omega])
    l2 = np.array([-30 * omega, -20 * omega, -10 * omega])
    R1 = np.array([[0, -12 * omega, -10 * omega], [12 * omega, 0, 2 * omega], [10 * omega, -2 * omega, 0]])
    R2 = np.zeros((3, 3))
    return Gamma, A.T, [l1.T, l2.T], [R1, R2]

def check_constraint(P, A, Ls, Rs):
    print 0


def bs_equation(P, A, Ls, Rs):
    u = np.ones(Rs[0].shape[0])
    S = []
    for L, R in zip(Ls, Rs):
        S.append(L + R * u)
    print sum(S) + A
    
    return 0


if __name__ == "__main__":
    participation, asset, ext_liabilites, int_transactions = generate_example(1)
    print participation
    print asset
    print ext_liabilites
    print int_transactions
    bs_equation(participation, asset, ext_liabilites, int_transactions)