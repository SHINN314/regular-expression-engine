def subset_construction(Q, Sigma, delta, I, F):
    """NFAからDFAに変換するアルゴリズム。
    
    Parameters
    ----------
    Q : set
        NFAの状態集合。
    Sigma : set
        NFAのアルファベット。
    delta : dict
        NFAの状態遷移関数。ここでは状態と文字が与えられて時に、そこから遷移できるすべての状態の集合を返す。
    I : set
        NFAの初期状態の集合。
    F : set
        NFAの受理状態の集合
    
    Returns
    -------"""
    Q_d = set()         # DFAの状態集合
    delta_d = dict()    # DFAの状態遷移関数
    F_d = set()         # DFAの初期状態

    queue = {frozenset(I)}
    dfa_states = {frozenset(I): 0}

    while len(queue) != 0:
        dstate = queue.pop()        # DFAの状態を一意に定めるキー
        Q_d.add(dfa_states[dstate])

        if dstate & F:
            # DFAの状態とNFAの受理状態集合の積が空でないとき、それをDFAの受理状態集合に加える
            F_d.add(dfa_states[dstate])

        for sigma in Sigma:
            dnext = set()
            
            for q in dstate:
                # dstateに属する状態からsigmaが与えられたときに遷移できる状態をすべて集める
                dnext |= set(delta[(q, sigma)])
                
            dnext = frozenset(dnext) # immutableに変換

            if len(dnext) == 0:
                continue
            if not dnext in dfa_states:
                queue.add(dnext)
                new_state = len(dfa_states)
                dfa_states[dnext] = new_state

            delta_d[(dfa_states[dstate], sigma)] = dfa_states[dnext] # DFA上の状態dfa_state[dstate]と文字sigmaを受け取って、別のDFA上の状態dfastates[dnext]に遷移

        return Q_d, Sigma, delta_d, 0, F_d