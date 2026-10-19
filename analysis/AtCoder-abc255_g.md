# Problem Analysis: AtCoder-abc255_g — G - Constrained Nim

**Problem ID**: `AtCoder-abc255_g`  
**Contest**: `abc255`  
**Rating / Difficulty**: 2734  
**URL**: https://atcoder.jp/contests/abc255/tasks/abc255_g  
**VJudge Tag**: `[problem:AtCoder-abc255_g]`  
**Category File**: [`../categories/game_theory/constrained_nim_grundy.md`](../categories/game_theory/constrained_nim_grundy.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
We play Nim with N piles of sizes A_i <= 10^{18}. There are M forbidden moves: removing Y_i stones from a pile of size X_i is forbidden. Find which player wins under optimal play.

## 2. Core Observation & Invariant
By the Sprague-Grundy theorem, the game is equivalent to standard Nim with Grundy values g(A_i). Let S = {0, X_1, ..., X_M} be the set of critical pile sizes. If n not in S, no moves from n are forbidden, so g(n) = h(n-1) + 1, where h(n) = max_{0..n} g(i). Between critical points, g(n) = n - n_bar + h(n_bar), where n_bar is the predecessor in S. At each critical point n in S, the forbidden moves eliminate a small set of transitions. By tracking duplicate Grundy values in a frequency map, we can compute mex in O(deg(n)) per critical point. The total time to process S is O(M log M), and queries take O(log M).

## 3. Step-by-Step Algorithm
1. 1. Sort and deduplicate S = {0, X_1, ..., X_M}.
2. 2. Initialize g(0) = 0, h(0) = 0, and an empty extra_count frequency map.
3. 3. For each critical point n in S in ascending order:
4.    a. Compute h_before_n = h(n_prev) + (n - 1 - n_prev).
5.    b. Gather Grundy values of forbidden transitions from n: g(f_k) = g(X_i - Y_i).
6.    c. Find the minimum non-negative integer v whose frequency in 0..n-1 equals its forbidden count, yielding g(n).
7.    d. Update h(n) = max(h_before_n, g(n)), and if g(n) <= h_before_n, increment extra_count[g(n)].
8. 4. For each pile A_i, compute g(A_i) via binary search on S in O(log M).
9. 5. XOR-sum all g(A_i). If non-zero, output 'Takahashi', else 'Aoki'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log M + M log M)`
- **Space Complexity**: `O(M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    vector<pair<long long, long long>> forbi(M);
    vector<long long> S;
    S.push_back(0);

    for (int i = 0; i < M; ++i) {
        cin >> forbi[i].first >> forbi[i].second;
        S.push_back(forbi[i].first);
    }

    sort(S.begin(), S.end());
    S.erase(unique(S.begin(), S.end()), S.end());

    // Map X_i to list of X_i - Y_i
    sort(forbi.begin(), forbi.end());
    int forbi_idx = 0;

    map<long long, long long> g, h;
    g[0] = 0;
    h[0] = 0;

    map<long long, int> extra_count;

    auto get_g = [&](long long val) {
        auto it = upper_bound(S.begin(), S.end(), val);
        --it;
        long long n_bar = *it;
        if (val == n_bar) {
            return g[val];
        }
        return val - n_bar + h[n_bar];
    };

    for (size_t i = 1; i < S.size(); ++i) {
        long long n = S[i];
        long long n_prev = S[i - 1];

        long long h_before_n = h[n_prev] + (n - 1 - n_prev);

        // Gather forbidden transitions for n
        map<long long, int> f_g_counts;
        while (forbi_idx < M && forbi[forbi_idx].first == n) {
            long long f_val = forbi[forbi_idx].first - forbi[forbi_idx].second;
            long long gv = get_g(f_val);
            f_g_counts[gv]++;
            forbi_idx++;
        }

        // Check wiped candidates
        long long gn = -1;
        for (const auto& kv : f_g_counts) {
            long long v = kv.first;
            int req_cnt = kv.second;
            int tot_cnt = 0;
            if (v <= h_before_n) {
                tot_cnt = 1 + (extra_count.count(v) ? extra_count[v] : 0);
            }
            if (tot_cnt <= req_cnt) {
                if (gn == -1 || v < gn) {
                    gn = v;
                }
            }
        }

        if (gn == -1) {
            gn = h_before_n + 1;
        }

        g[n] = gn;
        long long hn = max(h_before_n, gn);
        h[n] = hn;

        if (gn <= h_before_n) {
            extra_count[gn]++;
        }
    }

    long long xor_sum = 0;
    for (int i = 0; i < N; ++i) {
        xor_sum ^= get_g(A[i]);
    }

    if (xor_sum != 0) {
        cout << "Takahashi\n";
    } else {
        cout << "Aoki\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
