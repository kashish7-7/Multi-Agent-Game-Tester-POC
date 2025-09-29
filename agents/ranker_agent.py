

def rank_test_cases(test_cases):
    """
    Rank test cases and return top 10.
    For now, selects first 10; can later use AI scoring.
    """
    top_cases = test_cases[:10]
    print(f" Ranked top {len(top_cases)} test cases")
    return top_cases
