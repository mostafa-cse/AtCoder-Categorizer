# Problem Analysis: AtCoder-arc230_c — C. Buildings

**Problem ID**: `AtCoder-arc230_c`  
**Contest**: `arc230`  
**Rating / Difficulty**: 2947  
**URL**: https://atcoder.jp/contests/arc230/tasks/arc230_c  
**VJudge Tag**: `[problem:AtCoder-arc230_c]`  
**Category File**: [`../categories/dynamic_programming/building_visibility_cartesian_tree_dp.md`](../categories/dynamic_programming/building_visibility_cartesian_tree_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Given C_1, ..., C_{N-1} where C_x is the number of buildings visible from gap x + 0.5, count permutations of heights (H_1, ..., H_N) matching these counts modulo 998244353.

## 2. Core Observation & Invariant
The visibility vector C corresponds to the gap depths of the Cartesian tree of H. Removing the minimum element replaces two adjacent maximums x with x - 1, preserving the invariant sum_{i=0}^N 2^{-C_i} = 1. Thus 2^{-C_0} + 2^{-C_N} = 1 - sum_{i=1}^{N-1} 2^{-C_i}. Writing the remainder in binary yields at most 2 candidates for (C_0, C_N). For each candidate, verify and reconstruct the Cartesian tree using a stack in O(N) time. The number of permutations matching a Cartesian tree is N! / prod_v S_v, where S_v is subtree size.

## 3. Step-by-Step Algorithm
1. 1. Normalize 1 - sum_{i=1}^{N-1} 2^{-C_i} in binary to find candidates for (C_0, C_N) (at most 2).
2. 2. For each candidate (C_0, C_N), form full sequence C = (C_0, C_1, ..., C_N).
3. 3. Use a stack to simulate Cartesian tree construction: merge adjacent equal values x into x - 1 and accumulate node sizes.
4. 4. If stack reduces to single value 0 with N nodes, add N! / prod S_v to answer.
5. 5. Output sum of ways modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 998244353;

long long power_mod(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> c_mid(n - 1);
    int max_c = 0;
    for (int i = 0; i < n - 1; ++i) {
        cin >> c_mid[i];
        if (c_mid[i] > max_c) max_c = c_mid[i];
    }

    int max_val = max(max_c + 100, n + 100);
    vector<int> cnt(max_val + 1, 0);
    for (int x : c_mid) {
        cnt[x]++;
    }

    for (int k = max_val; k >= 1; --k) {
        cnt[k - 1] += cnt[k] / 2;
        cnt[k] %= 2;
    }

    if (cnt[0] > 0) {
        cout << 0 << "\n";
        return 0;
    }

    int L = -1;
    for (int k = max_val; k >= 1; --k) {
        if (cnt[k] == 1) {
            L = k;
            break;
        }
    }

    if (L == -1) {
        cout << 0 << "\n";
        return 0;
    }

    vector<int> r_powers;
    for (int k = 1; k < L; ++k) {
        if (cnt[k] == 0) {
            r_powers.push_back(k);
        }
    }
    r_powers.push_back(L);

    vector<pair<int, int>> cands;
    if (r_powers.size() == 1) {
        cands.push_back({r_powers[0] + 1, r_powers[0] + 1});
    } else if (r_powers.size() == 2) {
        cands.push_back({r_powers[0], r_powers[1]});
        cands.push_back({r_powers[1], r_powers[0]});
    } else {
        cout << 0 << "\n";
        return 0;
    }

    // Precompute factorials
    vector<long long> fac(n + 1, 1);
    for (int i = 1; i <= n; ++i) {
        fac[i] = (fac[i - 1] * i) % MOD;
    }

    auto try_tree = [&](const vector<int>& full_c) -> long long {
        vector<pair<int, int>> st; // (val, size)
        vector<int> subtrees;
        subtrees.reserve(n);

        for (int x : full_c) {
            int cur_val = x;
            int cur_sz = 0;
            while (!st.empty() && st.back().first == cur_val) {
                int prev_val = st.back().first;
                int prev_sz = st.back().second;
                st.pop_back();

                int node_sz = prev_sz + cur_sz + 1;
                subtrees.push_back(node_sz);
                cur_val = prev_val - 1;
                cur_sz = node_sz;
            }
            st.push_back({cur_val, cur_sz});
        }

        if (st.size() == 1 && st[0].first == 0 && (int)subtrees.size() == n) {
            long long prod = 1;
            for (int s : subtrees) {
                prod = (prod * s) % MOD;
            }
            long long ways = fac[n] * power_mod(prod, MOD - 2) % MOD;
            return ways;
        }
        return 0;
    };

    long long total_ans = 0;
    for (const auto& cand : cands) {
        vector<int> full_c;
        full_c.reserve(n + 1);
        full_c.push_back(cand.first);
        for (int x : c_mid) full_c.push_back(x);
        full_c.push_back(cand.second);

        total_ans = (total_ans + try_tree(full_c)) % MOD;
    }

    cout << total_ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
