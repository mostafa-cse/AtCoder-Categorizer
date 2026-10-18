# Problem Analysis: AtCoder-agc065_c — C - Avoid Half Sum

**Problem ID**: `AtCoder-agc065_c`  
**Contest**: `agc065`  
**Rating / Difficulty**: 2414  
**URL**: https://atcoder.jp/contests/agc065/tasks/agc065_c  
**VJudge Tag**: `[problem:AtCoder-agc065_c]`  
**Category File**: [`../categories/game_theory/avoid_half_sum_odd_partition_parity.md`](../categories/game_theory/avoid_half_sum_odd_partition_parity.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
Determine whether there exists a decomposition $B_i + C_i = A_i$ such that no subset choice of $B_i$ or $C_i$ totals half the total sum $S/2$.

## 2. Core Observation & Invariant
Choosing $X_i \in \{B_i, C_i\}$ is equivalent to choosing $X_i \in \{0, D_i\}$ where $D_i = |B_i - C_i| \le A_i$ with $D_i \equiv A_i \pmod 2$. A half-sum subset is unavoidable if and only if every possible choice of $D$ can represent $S/2$. By induction, the necessary and sufficient condition for the existence of such avoiding $D$ is that there exists some index $i$ such that the number of odd integers among $A_1, \dots, A_N$ strictly less than $A_i$ is strictly less than $A_i - 1$.

## 3. Step-by-Step Algorithm
1. 1. Extract all odd numbers in $A$ and sort them.
2. 2. For each element $A_i$, use binary search (`std::lower_bound`) to count how many odd elements in $A$ are strictly less than $A_i$.
3. 3. If for any $i$, this count is strictly less than $A_i - 1$, output `Yes`.
4. 4. If all elements have count $\ge A_i - 1$, output `No`.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int N;
    if (!(cin >> N)) return;
    vector<long long> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    sort(A.begin(), A.end());

    vector<long long> odds;
    for (auto x : A) {
        if (x % 2 != 0) odds.push_back(x);
    }

    bool ok = false;
    for (int i = 0; i < N; ++i) {
        long long cnt = lower_bound(odds.begin(), odds.end(), A[i]) - odds.begin();
        if (cnt < A[i] - 1) {
            ok = true;
            break;
        }
    }
    if (ok) cout << "Yes\n";
    else cout << "No\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
