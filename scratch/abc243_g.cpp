#include <iostream>
#include <vector>
#include <cmath>
#include <cstdint>

using namespace std;

const int MAX_M = 60000;
uint64_t f[MAX_M + 1];
uint64_t pref[MAX_M + 1];

uint64_t isqrt(uint64_t n) {
    uint64_t r = sqrt(n);
    while ((r + 1) * (r + 1) <= n) r++;
    while (r * r > n) r--;
    return r;
}

void precompute() {
    f[1] = 1;
    pref[1] = 1;
    for (uint64_t z = 2; z <= MAX_M; ++z) {
        uint64_t s = isqrt(z);
        f[z] = pref[s];
        pref[z] = pref[z - 1] + f[z];
    }
}

void solve() {
    uint64_t x;
    cin >> x;

    uint64_t r = isqrt(x);
    uint64_t k = isqrt(r);

    uint64_t ans = 0;
    for (uint64_t z = 1; z <= k; ++z) {
        uint64_t low = z * z;
        uint64_t high = min(r, (z + 1) * (z + 1) - 1);
        uint64_t cnt = high - low + 1;
        ans += pref[z] * cnt;
    }

    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
