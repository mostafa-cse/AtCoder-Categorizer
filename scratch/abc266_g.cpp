#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

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

    int r, g, b, k;
    if (!(cin >> r >> g >> b >> k)) return 0;

    if (k > r || k > g) {
        cout << 0 << "\n";
        return 0;
    }

    int total_len = r + g + b + 5;
    vector<long long> fact(total_len), inv(total_len);
    fact[0] = 1;
    inv[0] = 1;
    for (int i = 1; i < total_len; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[total_len - 1] = mod_inv(fact[total_len - 1]);
    for (int i = total_len - 2; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
    };

    // 1. Arrange B 'B's, K 'X's, and (R - K) 'R's:
    long long ways1 = fact[b + r] * inv[b] % MOD * inv[k] % MOD * inv[r - k] % MOD;

    // 2. Distribute (G - K) 'G's into (1 + B + K) available slots:
    // C((G - K) + (1 + B + K) - 1, G - K) = C(G + B, G - K)
    long long ways2 = nCr(g + b, g - k);

    long long ans = (ways1 * ways2) % MOD;
    cout << ans << "\n";

    return 0;
}
