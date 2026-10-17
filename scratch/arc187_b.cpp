#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> b(n + 1);
    int total_wildcards = 0;
    for (int i = 1; i <= n; ++i) {
        cin >> b[i];
        if (b[i] == -1) total_wildcards++;
    }

    // pref[i][v]: completions of 1..i where all elements >= v
    vector<vector<long long>> pref(n + 1, vector<long long>(m + 2, 0));
    for (int v = 1; v <= m + 1; ++v) pref[0][v] = 1;

    for (int i = 1; i <= n; ++i) {
        for (int v = 1; v <= m + 1; ++v) {
            long long choices = 0;
            if (b[i] == -1) {
                choices = max(0, m - v + 1);
            } else {
                choices = (b[i] >= v ? 1 : 0);
            }
            pref[i][v] = (pref[i - 1][v] * choices) % MOD;
        }
    }

    // suff[i][v]: completions of i..n where all elements < v
    vector<vector<long long>> suff(n + 2, vector<long long>(m + 2, 0));
    for (int v = 1; v <= m + 1; ++v) suff[n + 1][v] = 1;

    for (int i = n; i >= 1; --i) {
        for (int v = 1; v <= m + 1; ++v) {
            long long choices = 0;
            if (b[i] == -1) {
                choices = max(0, v - 1);
            } else {
                choices = (b[i] < v ? 1 : 0);
            }
            suff[i][v] = (suff[i + 1][v] * choices) % MOD;
        }
    }

    long long total_sequences = pref[n][1];
    long long ans = total_sequences;

    // For each boundary i in 1 .. n - 1:
    // A cut occurs if min(pref) >= v and max(suff) < v for some v
    // Equivalently: sum over v from 2 to m of (pref[i][v] - pref[i][v+1]) * suff[i+1][v]
    for (int i = 1; i < n; ++i) {
        for (int v = 2; v <= m; ++v) {
            long long min_is_v = (pref[i][v] - pref[i][v + 1] + MOD) % MOD;
            long long max_less_v = suff[i + 1][v];
            long long ways = (min_is_v * max_less_v) % MOD;
            ans = (ans + ways) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
