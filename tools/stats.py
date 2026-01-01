from scipy import stats

def t_test(a, b):
    return stats.ttest_ind(a, b)
