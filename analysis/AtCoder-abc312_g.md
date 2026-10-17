# Problem Analysis: AtCoder-abc312_g — Avoid Straight Line

**Problem ID**: `AtCoder-abc312_g`  
**Contest**: `abc312`  
**Rating / Difficulty**: 1819  
**URL**: https://atcoder.jp/contests/abc312/tasks/abc312_g  
**VJudge Tag**: `[problem:AtCoder-abc312_g]`  
**Category File**: [`../categories/combinatorics/tree_non_collinear_triplet_counting.md`](../categories/combinatorics/tree_non_collinear_triplet_counting.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Tree Algorithms`  
- **Topic (Skill)**: `Tree Non-Collinear Triplet Counting via Junction Center Decomposition`  

---

## 1. Problem Statement & Key Idea
Given a tree of N vertices. Count index triples (i, j, k) with 1 <= i < j < k <= N such that the unique simple paths between them do NOT all lie on a single simple path.

**Key Insight**: Three vertices i, j, k do NOT lie on a single path iff they branch out into three distinct components attached to a common center junction vertex u. For a vertex u, removing u splits the tree into components of sizes s_1, s_2, ..., s_d. The count of triplets centered at u is sum_{a < b < c} s_a * s_b * s_c.

## 2. Core Observation & Invariant
Using elementary symmetric polynomials, sum_{a < b < c} s_a s_b s_c is computed in O(d) per node using e_1, e_2, e_3 formulas, giving O(N) overall.

## 3. Step-by-Step Algorithm
1. Root tree at 1. Run DFS to compute subtree sizes sz[u].
2. For each vertex u:
3.   Gather component sizes s_1..s_d: child subtrees sz[v] and parent component N - sz[u].
4.   Compute e_1 = sum s_i, e_2 = sum_{i < j} s_i s_j = (e_1^2 - sum s_i^2) / 2.
5.   e_3 = (e_1 * e_2 - sum_{i < j} s_i s_j (s_i + s_j)) / 3 or directly sum_{i} s_i * (e_2 of rest).
6.   Sum e_3 over all vertices u.
7. Print total sum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int n;
vector<vector<int>> adj;
vector<int> sz;
long long total_ans = 0;

void dfs(int u, int p) {
    sz[u] = 1;
    vector<long long> comps;

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
            sz[u] += sz[v];
            comps.push_back(sz[v]);
        }
    }
    if (n - sz[u] > 0) {
        comps.push_back(n - sz[u]);
    }

    // Compute e_3 of comps
    long long s1 = 0, s2 = 0, s3 = 0;
    for (long long x : comps) {
        s1 += x;
        s2 += x * x;
        s3 += x * x * x;
    }

    long long e1 = s1;
    long long e2 = (e1 * e1 - s2) / 2;
    long long e3 = (e1 * e1 * e1 - 3 * e1 * s2 + 2 * s3) / 6;

    total_ans += e3;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    sz.assign(n + 1, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 0);

    cout << total_ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Decomposing tree non-collinear triplet metrics across junction vertices via elementary symmetric polynomials.
- **Reusable Pattern**: `Tree Junction Triplet Counting: sum e_3(component sizes) across all tree vertices.`
