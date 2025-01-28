import numpy as np
from statsmodels.tsa.stattools import coint, adfuller

class CointegrationPairsFinder:

    def __init__(self, data):
        self.data = data


    def find_cointegrated_pairs(self):
        n = self.data.shape[1]
        score_matrix = np.zeros((n, n))
        pvalue_matrix = np.ones((n, n))
        keys = self.data.keys()
        pairs = []
        for i in range(n):
            for j in range(i+1, n):
                S1 = self.data[keys[i]]
                S2 = self.data[keys[j]]
                result = coint(S1, S2)
                score = result[0]
                pvalue = result[1]
                score_matrix[i, j] = score
                pvalue_matrix[i, j] = pvalue
                pairs.append((keys[i], keys[j], pvalue))
        return score_matrix, pvalue_matrix, pairs

    # scores, pvalues, pairs = find_cointegrated_pairs(data)

    # pairs_sorted_by_pvalue = sorted(pairs, key=lambda x: x[2])

    # top_5_pairs = pairs_sorted_by_pvalue[:5]
    # for pair in top_5_pairs:
    #     print(f"Pair: {pair[0]} and {pair[1]}, P-value: {pair[2]}")