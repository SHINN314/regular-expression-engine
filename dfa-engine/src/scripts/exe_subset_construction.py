from algorithms.dfa_engine import subset_construction

def main():
    Q_n = {0, 1, 2, 3, 4}
    Sigma_n = {0, 1}
    delta_n = {
        (0, 0) : {1, 2},
        (0, 1) : {},
        (1, 0) : {},
        (1, 1) : {1, 2, 3},
        (2, 0) : {4},
        (2, 1) : {},
        (3, 0) : {},
        (3, 1) : {},
        (4, 0) : {},
        (4, 1) : {}
    }
    I_n = {0}
    F_n = {3, 4}

    DFA = subset_construction(Q_n, Sigma_n, delta_n, I_n, F_n)
    print(DFA)
    