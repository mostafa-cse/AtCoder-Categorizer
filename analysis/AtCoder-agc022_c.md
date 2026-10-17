# Problem Analysis: AtCoder-agc022_c — C. Remainder Game

**Problem ID**: `AtCoder-agc022_c`  
**Contest**: `agc022`  
**Rating / Difficulty**: 2176  
**URL**: https://atcoder.jp/contests/agc022/tasks/agc022_c  
**VJudge Tag**: `[problem:AtCoder-agc022_c]`  
**Category File**: [`../categories/miscellaneous/remainder_game_greedy_power_of_two_reachability.md`](../categories/miscellaneous/remainder_game_greedy_power_of_two_reachability.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Greedy Algorithms`  
- **Topic (Skill)**: `Exchange Arguments`  

---

## 1. Problem Statement & Key Idea
Transform array a into b using operations v <- v mod k at cost 2^k. Since costs are powers of 2, minimizing the sum corresponds to lexicographically minimizing the set of chosen moduli from largest to smallest. Greedily attempt to drop k from 50 down to 1, retaining k iff removing it destroys reachability from a_i to b_i.

## 2. Core Observation & Invariant
Moduli k > 50 are useless since all values are <= 50. Because cost is sum of 2^k, choosing 2^k is more expensive than any combination of smaller powers sum_{j < k} 2^j < 2^k. Thus, a greedy high-to-low elimination strategy is optimal. Reachability on the 51-node directed graph (u -> u mod m for allowed m) is checked in O(50 * V^2).

## 3. Step-by-Step Algorithm
1. Initialize allowed set of moduli S = {1, 2, ..., 50}.
2. Verify that b_i is reachable from a_i for all i using all moduli in S. If not, output -1.
3. For k = 50 down to 1: temporarily remove k from S. Check if reachability still holds for all pairs (a_i, b_i). If reachability breaks, k must be retained in S.
4. Output sum_{k in S} 2^k.

## 4. Complexity Analysis
- **Time Complexity**: `O(50 * (50 * V^2 + N))`
- **Space Complexity**: `O(V^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool check(const set<int>& allowed, const vector<int>& a, const vector<int>& b, int n) {
    vector<vector<int>> adj(51);
    for (int u = 0; u <= 50; ++u) {
        for (int k : allowed) {
            adj[u].push_back(u % k);
        }
    }

    vector<vector<bool>> reach(51, vector<bool>(51, false));
    for (int u = 0; u <= 50; ++u) {
        reach[u][u] = true;
        vector<int> q = {u};
        for (size_t idx = 0; idx < q.size(); ++idx) {
            int v = q[idx];
            for (int w : adj[v]) {
                if (!reach[u][w]) {
                    reach[u][w] = true;
                    q.push_back(w);
                }
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        if (!reach[a[i]][b[i]]) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N), B(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];

    set<int> allowed;
    for (int k = 1; k <= 50; ++k) allowed.insert(k);

    if (!check(allowed, A, B, N)) {
        cout << -1 << "\n";
        return 0;
    }

    for (int k = 50; k >= 1; --k) {
        allowed.erase(k);
        if (!check(allowed, A, B, N)) {
            allowed.insert(k);
        }
    }

    long long ans = 0;
    for (int k : allowed) {
        ans += (1LL << k);
    }
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
