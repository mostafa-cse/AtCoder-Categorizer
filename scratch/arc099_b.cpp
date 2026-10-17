#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

long long digit_sum(long long x) {
    long long s = 0;
    while (x > 0) {
        s += x % 10;
        x /= 10;
    }
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    long long cur = 1;
    vector<long long> pow10(16);
    pow10[0] = 1;
    for (int i = 1; i <= 15; ++i) {
        pow10[i] = pow10[i - 1] * 10;
    }

    for (int step = 0; step < k; ++step) {
        cout << cur << "\n";
        long long best_cand = cur + 1;
        double best_val = (double)best_cand / digit_sum(best_cand);

        for (int p = 0; p <= 14; ++p) {
            long long cand = cur + pow10[p];
            double val = (double)cand / digit_sum(cand);
            if (val < best_val) {
                best_val = val;
                best_cand = cand;
            }
        }
        cur = best_cand;
    }

    return 0;
}
