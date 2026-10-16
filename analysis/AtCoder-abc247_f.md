# Problem Analysis: AtCoder-abc247_f — Cards

**Problem ID**: `AtCoder-abc247_f`  
**Contest**: `abc247`  
**Rating / Difficulty**: 1697  
**URL**: https://atcoder.jp/contests/abc247/tasks/abc247_f  
**VJudge Tag**: `[problem:AtCoder-abc247_f]`  
**Category File**: [`../categories/dp/permutation_cycle_lucas_numbers.md`](../categories/dp/permutation_cycle_lucas_numbers.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Tree / Graph DP`  
- **Topic (Skill)**: `Functional Graph Permutation Cycle Decomposition + Lucas Numbers`  

---

## 1. Problem Statement & Key Idea
N cards, card i has P_i on front and Q_i on back (P and Q are permutations of 1..N). Choose a subset of cards such that every number 1..N appears at least once on either front or back of a chosen card. Find the number of valid card subsets, modulo 998244353.

**Key Insight**: Model each card as an edge between P_i and Q_i. Because P and Q are permutations, every vertex has degree 2, so the graph decomposes into disjoint simple cycles! For each cycle of length L, the number of edge subsets covering all vertices is the Lucas number L_L.

## 2. Core Observation & Invariant
Lucas numbers satisfy L_1 = 1, L_2 = 3, L_L = L_{L-1} + L_{L-2} for L >= 3 (derived from choosing non-adjacent unchosen edges on a circle). The total answer is the product of L_L over all connected cycle lengths L modulo 998244353.

## 3. Step-by-Step Algorithm
1. Build graph with edges (P_i, Q_i).
2. Precompute Lucas numbers: L[1] = 1, L[2] = 3; L[i] = (L[i-1] + L[i-2]) % MOD.
3. Decompose graph into connected components using DFS/DSU to find cycle lengths.
4. ans = 1.
5. For each cycle of length len: ans = (ans * L[len]) % MOD.
6. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n + 1), q(n + 1);
    for (int i = 1; i <= n; ++i) cin >> p[i];
    for (int i = 1; i <= n; ++i) cin >> q[i];

    vector<vector<int>> adj(n + 1);
    for (int i = 1; i <= n; ++i) {
        adj[p[i]].push_back(q[i]);
        adj[q[i]].push_back(p[i]);
    }

    // Precompute Lucas numbers
    vector<long long> lucas(n + 2);
    lucas[1] = 1;
    lucas[2] = 3;
    for (int i = 3; i <= n + 1; ++i) {
        lucas[i] = (lucas[i - 1] + lucas[i - 2]) % MOD;
    }

    vector<bool> visited(n + 1, false);
    long long ans = 1;

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            int cycle_len = 0;
            int curr = i;
            while (!visited[curr]) {
                visited[curr] = true;
                cycle_len++;
                // Move to next unvisited neighbor
                int next_node = -1;
                for (int nxt : adj[curr]) {
                    if (!visited[nxt]) {
                        next_node = nxt;
                        break;
                    }
                }
                if (next_node == -1) break;
                curr = next_node;
            }
            ans = (ans * lucas[cycle_len]) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Cycle decomposition of 2-regular permutation graphs with circular Lucas number independent set counting.
- **Reusable Pattern**: `Permutation Edge Cover on Cycles: answer = prod_{cycles} Lucas(cycle_length).`
