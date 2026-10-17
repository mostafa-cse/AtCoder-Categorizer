#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

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

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    if (n > m + k) {
        cout << 0 << "\n";
        return 0;
    }

    int max_val = n + m + 5;
    vector<long long> fact(max_val), inv(max_val);
    fact[0] = 1;
    inv[0] = 1;
    for (int i = 1; i < max_val; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[max_val - 1] = mod_inv(fact[max_val - 1]);
    for (int i = max_val - 2; i >= 1; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
    };

    long long total = nCr(n + m, n);
    long long invalid = nCr(n + m, m + k + 1);

    long long ans = (total - invalid + MOD) % MOD;
    cout << ans << "\n";

    return 0;
}
