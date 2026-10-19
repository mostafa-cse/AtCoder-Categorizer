# Problem Analysis: AtCoder-arc184_b — B - 123 Set

**Problem ID**: `AtCoder-arc184_b`  
**Contest**: `arc184`  
**Rating / Difficulty**: 2867  
**URL**: https://atcoder.jp/contests/arc184/tasks/arc184_b  
**VJudge Tag**: `[problem:AtCoder-arc184_b]`  
**Category File**: [`../categories/dynamic_programming/multiplicative_lattice_poset_grid_dominating_set.md`](../categories/dynamic_programming/multiplicative_lattice_poset_grid_dominating_set.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Given N <= 10^9, operation chooses x and adds x, 2x, 3x to set S. Find the minimum operations so {1, 2, ..., N} subset S.

## 2. Core Observation & Invariant
Decompose x = u * 2^a 3^b with gcd(u, 6) = 1. The problem decouples independently for each u <= N. For each u, we must cover the 2D lattice shape P(M) = {(a, b) | 2^a 3^b <= floor(N / u)}. There are only 306 distinct shapes P(M). Covering a shape is a minimum dominating set on the 2D multiplicative poset grid, solved via bitmask DP with superset Fast Zeta Transform (SOS DP).

## 3. Step-by-Step Algorithm
1. 1. Identify all 306 numbers of the form 2^a 3^b <= N to partition the domain of floor(N / u).
2. 2. For each unique shape defined by row heights h_a, compute min operations using bitmask DP: state s represents covered cells in column a.
3. 3. Use superset SOS DP to evaluate optimal transitions for all operation choices O in O(H * 2^H) time.
4. 4. Count the number of coprime-to-6 integers u yielding each shape via f(X) = X - floor(X/2) - floor(X/3) + floor(X/6).
5. 5. Sum (count * cost) across all shapes.

## 4. Complexity Analysis
- **Time Complexity**: `O(sum H_i 2^{H_i})`
- **Space Complexity**: `O(2^{max H})`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

const int INF = 1e9;

// Counts numbers in [1, X] coprime to 6
long long count_coprime_6(long long X) {
    if (X <= 0) return 0;
    return X - X / 2 - X / 3 + X / 6;
}

vector<int> get_profile(long long M) {
    vector<int> h;
    for (int a = 0; (1LL << a) <= M; ++a) {
        long long rem = M / (1LL << a);
        int b = 0;
        long long p3 = 1;
        while (p3 <= rem / 3) {
            p3 *= 3;
            b++;
        }
        h.push_back(b);
    }
    return h;
}

int solve_profile(const vector<int>& h) {
    if (h.empty()) return 0;
    int cur_H = h[0];
    int sz = 1 << (cur_H + 1);
    vector<int> dp(sz, INF);
    dp[0] = 0;

    for (size_t i = 0; i < h.size(); ++i) {
        int H = h[i];
        int next_H = (i + 1 < h.size()) ? h[i + 1] : -1;
        int cur_sz = 1 << (H + 1);

        // Superset SOS DP
        vector<int> F = dp;
        for (int b = 0; b <= H; ++b) {
            for (int mask = cur_sz - 1; mask >= 0; --mask) {
                if (!(mask & (1 << b))) {
                    F[mask] = min(F[mask], F[mask | (1 << b)]);
                }
            }
        }

        int next_sz = (next_H >= 0) ? (1 << (next_H + 1)) : 1;
        vector<int> next_dp(next_sz, INF);

        int all_mask = (1 << (H + 1)) - 1;
        int next_mask_filter = (next_H >= 0) ? ((1 << (next_H + 1)) - 1) : 0;

        for (int O = 0; O < cur_sz; ++O) {
            int covered = O | (O << 1);
            int req = (~covered) & all_mask;
            int cost = F[req] + __builtin_popcount(O);
            int nxt = O & next_mask_filter;
            if (cost < next_dp[nxt]) {
                next_dp[nxt] = cost;
            }
        }

        dp = move(next_dp);
    }

    return dp[0];
}

long long solve(long long N) {
    // Generate all 2^a * 3^b <= N
    vector<long long> vals;
    for (int a = 0; a < 32; ++a) {
        for (int b = 0; b < 22; ++b) {
            long long v = 1LL << a;
            long long p3 = 1;
            bool ok = true;
            for (int k = 0; k < b; ++k) {
                if (p3 > N / 3) { ok = false; break; }
                p3 *= 3;
            }
            if (!ok) continue;
            if (v > N / p3) continue;
            vals.push_back(v * p3);
        }
    }
    sort(vals.begin(), vals.end());

    map<vector<int>, int> memo;
    long long total_ans = 0;

    for (size_t i = 0; i < vals.size(); ++i) {
        long long vi = vals[i];
        long long vi_next = (i + 1 < vals.size()) ? vals[i + 1] : (N + 1);

        // u such that floor(N / u) is in [vi, vi_next - 1]:
        // vi <= floor(N / u) < vi_next
        // <=> N / vi_next < u <= N / vi
        long long L = N / vi_next;
        long long R = N / vi;
        long long num_u = count_coprime_6(R) - count_coprime_6(L);
        if (num_u == 0) continue;

        vector<int> h = get_profile(vi);
        int cost;
        auto it = memo.find(h);
        if (it != memo.end()) {
            cost = it->second;
        } else {
            cost = solve_profile(h);
            memo[h] = cost;
        }

        total_ans += num_u * cost;
    }

    return total_ans;
}

int main() {
    long long N;
    if (cin >> N) {
        cout << solve(N) << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
