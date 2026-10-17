#include <iostream>

using namespace std;

const long long MOD = 1e9 + 7;

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

    long long A, B, C;
    if (!(cin >> A >> B >> C)) return 0;

    // Denominator = (A * B + A * C - B * C) % MOD
    long long den = (A * B + A * C - B * C) % MOD;
    den = (den % MOD + MOD) % MOD;

    long long inv_den = mod_inv(den);

    // r = (B * C - A * B) / Den
    long long num_r = (B * C - A * B) % MOD;
    num_r = (num_r % MOD + MOD) % MOD;
    long long r = (num_r * inv_den) % MOD;

    // c = (B * C - A * C) / Den
    long long num_c = (B * C - A * C) % MOD;
    num_c = (num_c % MOD + MOD) % MOD;
    long long c = (num_c * inv_den) % MOD;

    cout << r << " " << c << "\n";
    return 0;
}
