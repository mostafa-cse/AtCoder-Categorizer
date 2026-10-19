# Problem Analysis: AtCoder-agc035_d — D. Add and Remove

**Problem ID**: `AtCoder-agc035_d`  
**Contest**: `agc035`  
**Rating / Difficulty**: 2902  
**URL**: https://atcoder.jp/contests/agc035/tasks/agc035_d  
**VJudge Tag**: `[problem:AtCoder-agc035_d]`  
**Category File**: [`../categories/dynamic_programming/reverse_tree_multiplier_interval_dp.md`](../categories/dynamic_programming/reverse_tree_multiplier_interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Given an array A of N cards, repeatedly choose three adjacent cards, eat the middle one, add its value to its two neighbors, and discard it, until 2 cards remain. Minimize the sum of the remaining two cards.

## 2. Core Observation & Invariant
Simulating forward is intractable because card values grow dynamically depending on previous choices. Instead, reverse the process: consider the LAST card k eaten among internal cards in interval (i, j). If card i has final multiplier c_i and card j has final multiplier c_j, then card k will contribute (c_i + c_j) * A_k to the final answer. Card k then splits the interval into subproblems (i, k) and (k, j), each inheriting the respective multiplier c_i + c_j for card k. This induces an interval DP with state (i, j, c_i, c_j).

## 3. Step-by-Step Algorithm
1. 1. Define recursive memoized function solve(i, j, ci, cj) returning the minimal cost of internal cards in range [i, j].
2. 2. Base case: if j - i == 1, return 0 (no internal cards left).
3. 3. Iterate over the last eaten card k in (i, j): cost = (ci + cj) * A[k] + solve(i, k, ci, ci + cj) + solve(k, j, ci + cj, cj).
4. 4. Memoize the state using a hash map or tuple lookup.
5. 5. Answer is A[1] + A[N] + solve(1, N, 1, 1).

## 4. Complexity Analysis
- **Time Complexity**: `O(4^N / N^{3/2}) states evaluated`
- **Space Complexity**: `O(2^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;

struct State {
    int L, R;
    ll cL, cR;
    bool operator<(const State& other) const {
        if (L != other.L) return L < other.L;
        if (R != other.R) return R < other.R;
        if (cL != other.cL) return cL < other.cL;
        return cR < other.cR;
    }
};

int N;
vector<ll> A;
map<State, ll> memo;

ll rec(int L, int R, ll cL, ll cR) {
    if (L + 1 == R) return 0;
    State s = {L, R, cL, cR};
    auto it = memo.find(s);
    if (it != memo.end()) return it->second;

    ll ans = -1;
    for (int k = L + 1; k < R; ++k) {
        ll cost = (cL + cR) * A[k] + rec(L, k, cL, cL + cR) + rec(k, R, cL + cR, cR);
        if (ans == -1 || cost < ans) {
            ans = cost;
        }
    }
    return memo[s] = ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;
    A.resize(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    ll ans = A[0] + A[N - 1] + rec(0, N - 1, 1, 1);
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
