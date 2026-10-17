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

    int R, C, X, Y, D, L;
    if (!(cin >> R >> C >> X >> Y >> D >> L)) return 0;

    int max_val = X * Y + 5;
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

    long long subgrid_ways = 0;

    for (int mask = 0; mask < 16; ++mask) {
        int t = (mask & 1);
        int b = ((mask >> 1) & 1);
        int l = ((mask >> 2) & 1);
        int r = ((mask >> 3) & 1);

        int dx = X - t - b;
        int dy = Y - l - r;

        if (dx < 0 || dy < 0) continue;
        int slots = dx * dy;
        if (slots < D + L) continue;

        long long ways = (nCr(slots, D) * nCr(slots - D, L)) % MOD;
        if (__builtin_parity(mask)) {
            subgrid_ways = (subgrid_ways - ways + MOD) % MOD;
        } else {
            subgrid_ways = (subgrid_ways + ways) % MOD;
        }
    }

    long long total_positions = (1LL * (R - X + 1) * (C - Y + 1)) % MOD;
    long long ans = (subgrid_ways * total_positions) % MOD;

    cout << ans << "\n";
    return 0;
}
