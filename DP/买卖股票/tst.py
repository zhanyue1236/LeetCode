import math

# RSA moduli from the test cases
test_values = {
    'test_1': 953333060825698081,
    'test_2': 945317903580264283,
    'test_3': 935509797568519949,
    'test_4': 940163326125238723,
    'test_5': 948898143556552601
}

# Brute-force factorization
def factor_rsa_n(N):
    for i in range(2, int(math.isqrt(N)) + 1):
        if N % i == 0:
            return i, N // i
    return None, None

# Calculate and print each result one at a time
for name, N in test_values.items():
    print(f"Factoring {name}: N = {N}")
    p, q = factor_rsa_n(N)
    print(f"  p = {p}")
    print(f"  q = {q}")
    print()