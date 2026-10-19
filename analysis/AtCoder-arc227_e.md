# Problem Analysis: AtCoder-arc227_e — Shift and XOR Switches

**Problem ID**: `AtCoder-arc227_e`  
**Contest**: `arc227`  
**Rating / Difficulty**: 2710  
**URL**: https://atcoder.jp/contests/arc227/tasks/arc227_e  
**VJudge Tag**: `[problem:AtCoder-arc227_e]`  
**Category File**: [`../categories/math/shift_xor_switches_linear_basis.md`](../categories/math/shift_xor_switches_linear_basis.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Vector Space and XOR Basis`  

---

## 1. Problem Statement & Key Idea
Switches with values A_i correspond to polynomial multiplication (1 + x^{A_i}) in F_2[x] mod x^N. Pressing two switches of value X reduces to pressing one switch of value 2X. Distinct switch sets uniquely characterize final sequences B. Grouping by odd parts d = A_i / 2^{v_2(A_i)} splits the problem into independent digit-DP problems on powers of two.

## 2. Core Observation & Invariant
For each odd part d, available switches are at levels k = 0..L-1. A bit string B is achievable iff at each step k, choosing bit B_k = 1 leaves available switches M >= 1, giving maximum next carry floor((M - B_k)/2). The set of available switch values at level k consists of at most 2 consecutive integers, allowing an O(L) DP per odd part.

## 3. Step-by-Step Algorithm
1. 1. Classify switches by odd part d = A_i / 2^p.
2. 2. For each odd integer d < N with L levels where d * 2^{L-1} < N:
3.    - Maintain map of (M -> count of bit strings).
4.    - For k = 0 to L - 2: branch B_k = 0 (carry floor(M/2)) and B_k = 1 (if M >= 1, carry floor((M-1)/2)).
5.    - At level L - 1: each node contributes 1 + (1 if M >= 1 else 0) ways.
6. 3. Multiply ways across all odd parts d modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

static const long long MOD = 998244353;

long long solve_class(const vector<int>& cnt) {
    int L = cnt.size();
    if (L == 0) return 1;

    map<int, long long> states;
    states[cnt[0]] = 1;

    for (int k = 0; k < L - 1; ++k) {
        int c_next = cnt[k + 1];
        map<int, long long> next_states;
        for (const auto& kv : states) {
            int M = kv.first;
            long long count = kv.second;

            // branch 0
            int m0 = c_next + M / 2;
            next_states[m0] = (next_states[m0] + count) % MOD;

            // branch 1
            if (M >= 1) {
                int m1 = c_next + (M - 1) / 2;
                next_states[m1] = (next_states[m1] + count) % MOD;
            }
        }
        states = move(next_states);
    }

    long long total = 0;
    for (const auto& kv : states) {
        int M = kv.first;
        long long count = kv.second;
        long long ways = 1 + (M >= 1 ? 1 : 0);
        total = (total + count * ways) % MOD;
    }
    return total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    map<int, vector<int>> by_odd;
    for (int i = 0; i < m; ++i) {
        int a;
        cin >> a;
        int odd = a;
        int p = 0;
        while (odd % 2 == 0) {
            odd /= 2;
            p++;
        }
        by_odd[odd].push_back(p);
    }

    long long ans = 1;

    for (int d = 1; d < n; d += 2) {
        int L = 0;
        while (1LL * d * (1LL << L) < n) {
            L++;
        }
        if (L == 0) continue;

        vector<int> cnt(L, 0);
        auto it = by_odd.find(d);
        if (it != by_odd.end()) {
            for (int p : it->second) {
                if (p < L) {
                    cnt[p]++;
                }
            }
        }

        long long ways = solve_class(cnt);
        ans = (ans * ways) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
