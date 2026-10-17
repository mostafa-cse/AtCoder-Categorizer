#include <iostream>

using namespace std;

const long long MOD = 1777777777;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long mod_inv(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    if (!(cin >> n >> k)) return 0;

    // 1. Compute C(N, K) % MOD
    long long num = 1;
    long long den = 1;
    for (long long i = 0; i < k; ++i) {
        num = (num * ((n - i) % MOD)) % MOD;
        den = (den * (i + 1)) % MOD;
    }
    long long c_nk = (num * mod_inv(den)) % MOD;

    // 2. Compute D_K % MOD (Montmort numbers)
    // D_0 = 1, D_1 = 0, D_i = (i - 1) * (D_{i-1} + D_{i-2}) % MOD
    long long d_prev2 = 1; // D_0
    long long d_prev1 = 0; // D_1
    long long d_cur = (k == 0 ? 1 : 0);

    for (long long i = 2; i <= k; ++i) {
        d_cur = ((i - 1) % MOD * (d_prev1 + d_prev2)) % MOD;
        d_prev2 = d_prev1;
        d_prev1 = d_cur;
    }

    long long ans = (c_nk * d_cur) % MOD;
    cout << ans << "\n";

    return 0;
}
