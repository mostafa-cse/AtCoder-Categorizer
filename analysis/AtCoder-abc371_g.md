# Problem Analysis: AtCoder-abc371_g — G. Lexicographically Smallest Permutation

**Problem ID**: `AtCoder-abc371_g`  
**Contest**: `abc371`  
**Rating / Difficulty**: 2348  
**URL**: https://atcoder.jp/contests/abc371/tasks/abc371_g  
**VJudge Tag**: `[problem:AtCoder-abc371_g]`  
**Category File**: [`../categories/number_theory/permutation_cycle_crt_minimization.md`](../categories/number_theory/permutation_cycle_crt_minimization.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Modular Arithmetic`  
- **Topic (Skill)**: `Chinese Remainder Theorem (CRT)`  

---

## 1. Problem Statement & Key Idea
Find the lexicographically smallest permutation $A_{P^k(i)}$. Permutation cycle decomposition and greedy shift selection sequentially constrain $k$ across distinct cycle lengths via CRT and extended GCD in $O(N + D^2 \log N)$.

## 2. Core Observation & Invariant
Decompose permutation $P$ into disjoint cycles. To minimize $A$ lexicographically, we greedily determine the optimal shift $s_c$ for each cycle in increasing order of index $1 \dots N$. Each cycle of length $L$ restricts the exponent $k$ by $k \equiv s_c \pmod L$, which propagates constraints $k \equiv s_c \pmod{\gcd(L, L')}$ to all other cycle lengths $L'$ via Chinese Remainder Theorem.

## 3. Step-by-Step Algorithm
1. Find all disjoint cycles of $P$. Identify distinct cycle lengths (at most $\sqrt{2N} \approx 650$).
2. For each distinct length $L$, maintain modular constraints $k \equiv \text{rem}[L] \pmod{g[L]}$.
3. Process elements $i = 1 \dots N$: if $i$'s cycle $C$ is unchosen, search over valid shifts $s \in [0, |C|)$ satisfying $s \equiv \text{rem}[|C|] \pmod{g[|C|]}$ to minimize $A_{P^s(i)}$.
4. Fix $s^*$ for cycle $C$ and update $(g[L'], \text{rem}[L'])$ for all distinct lengths $L'$ via extended GCD / CRT in $O(N + D^2 \log N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + D^2 \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

long long extgcd(long long a, long long b, long long& x, long long& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long d = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> P(N + 1), A(N + 1);
    for (int i = 1; i <= N; ++i) cin >> P[i];
    for (int i = 1; i <= N; ++i) cin >> A[i];

    vector<bool> vis(N + 1, false);
    vector<vector<int>> cycles;
    vector<int> cycle_id(N + 1);
    vector<int> pos_in_cycle(N + 1);

    for (int i = 1; i <= N; ++i) {
        if (!vis[i]) {
            vector<int> cyc;
            int cur = i;
            while (!vis[cur]) {
                vis[cur] = true;
                pos_in_cycle[cur] = cyc.size();
                cycle_id[cur] = cycles.size();
                cyc.push_back(cur);
                cur = P[cur];
            }
            cycles.push_back(cyc);
        }
    }

    // Group cycle lengths
    vector<int> distinct_lengths;
    vector<bool> len_present(N + 1, false);
    for (const auto& cyc : cycles) {
        int L = cyc.size();
        if (!len_present[L]) {
            len_present[L] = true;
            distinct_lengths.push_back(L);
        }
    }

    // For each distinct length L, keep track of g[L] and rem[L]:
    // k = rem[L] (mod g[L])
    vector<int> g(N + 1, 1);
    vector<int> rem(N + 1, 0);

    vector<int> chosen_shift(cycles.size(), -1);

    for (int i = 1; i <= N; ++i) {
        int c_id = cycle_id[i];
        if (chosen_shift[c_id] != -1) continue;

        int L = cycles[c_id].size();
        int cur_g = g[L];
        int cur_r = rem[L];

        // Find shift s in [0, L) with s = cur_r (mod cur_g) that minimizes A[P^s(i)]
        int best_s = cur_r;
        int min_val = N + 1;
        int cur_pos = pos_in_cycle[i];

        for (int s = cur_r; s < L; s += cur_g) {
            int target_idx = cycles[c_id][(cur_pos + s) % L];
            int val = A[target_idx];
            if (val < min_val) {
                min_val = val;
                best_s = s;
            }
        }

        chosen_shift[c_id] = best_s;

        // Now update constraints for all distinct lengths
        for (int L2 : distinct_lengths) {
            int gcd_val = std::gcd(L2, L);
            int target_rem = best_s % gcd_val;

            // Solve: k = rem[L2] (mod g[L2]) and k = target_rem (mod gcd_val)
            long long x, y;
            long long d = extgcd(g[L2], gcd_val, x, y);
            if ((target_rem - rem[L2]) % d == 0) {
                long long step = gcd_val / d;
                long long mult = ((target_rem - rem[L2]) / d) % step;
                long long k_new = rem[L2] + (x % step * mult % step) * g[L2];
                long long new_g = (long long)g[L2] / d * gcd_val;
                k_new = (k_new % new_g + new_g) % new_g;
                g[L2] = new_g;
                rem[L2] = k_new;
            }
        }
    }

    vector<int> ans(N + 1);
    for (int c_id = 0; c_id < (int)cycles.size(); ++c_id) {
        int L = cycles[c_id].size();
        int s = rem[L];
        for (int p = 0; p < L; ++p) {
            int orig_elem = cycles[c_id][p];
            int mapped_elem = cycles[c_id][(p + s) % L];
            ans[orig_elem] = A[mapped_elem];
        }
    }

    for (int i = 1; i <= N; ++i) {
        cout << ans[i] << (i == N ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
