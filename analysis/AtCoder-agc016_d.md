# Problem Analysis: AtCoder-agc016_d — D. XOR Replace

**Problem ID**: `AtCoder-agc016_d`  
**Contest**: `agc016`  
**Rating / Difficulty**: 2910  
**URL**: https://atcoder.jp/contests/agc016/tasks/agc016_d  
**VJudge Tag**: `[problem:AtCoder-agc016_d]`  
**Category File**: [`../categories/miscellaneous/xor_multiset_swap_permutation_cycles.md`](../categories/miscellaneous/xor_multiset_swap_permutation_cycles.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Permutations`  
- **Topic (Skill)**: `Permutations and Permutation Cycles`  

---

## 1. Problem Statement & Key Idea
Given array A of length N and target array B. In one operation, replace A_i with the XOR sum of all elements in A. Find the minimum operations to transform A into B, or -1 if impossible.

## 2. Core Observation & Invariant
Append A_{N+1} = xor_sum(A) and B_{N+1} = xor_sum(B). Replacing A_i with the XOR sum is equivalent to swapping A_i and A_{N+1}! The multiset of values {A_1, ..., A_{N+1}} is completely invariant under operations. Transformation is possible iff multiset(A) == multiset(B). When possible, mismatched positions A_i != B_i define directed permutation cycles. Resolving C connected components requires (mismatched elements) + (C - 1) swaps if A_{N+1} is in a component, or + C if an extra swap is needed to bring A_{N+1} into the cycle.

## 3. Step-by-Step Algorithm
1. 1. Append A_{N+1} = xor_sum(A) and B_{N+1} = xor_sum(B).
2. 2. If sorted(A) != sorted(B), return -1.
3. 3. If A == B, return 0.
4. 4. Coordinate compress all values. For each i where A_i != B_i, add an undirected edge between A_i and B_i in a graph.
5. 5. Find the number of connected components C among non-isolated vertices.
6. 6. If A_{N+1} has degree > 0 (already in a component), ans = mismatches + C - 1; otherwise ans = mismatches + C.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> a(N), b(N);
    int ax = 0, bx = 0;
    for (int i = 0; i < N; ++i) {
        cin >> a[i];
        ax ^= a[i];
    }
    for (int i = 0; i < N; ++i) {
        cin >> b[i];
        bx ^= b[i];
    }

    if (a == b) {
        cout << 0 << "\n";
        return 0;
    }

    vector<int> a_all = a, b_all = b;
    a_all.push_back(ax);
    b_all.push_back(bx);

    vector<int> a_sorted = a_all, b_sorted = b_all;
    sort(a_sorted.begin(), a_sorted.end());
    sort(b_sorted.begin(), b_sorted.end());

    if (a_sorted != b_sorted) {
        cout << -1 << "\n";
        return 0;
    }

    vector<int> vals = a_all;
    vals.insert(vals.end(), b_all.begin(), b_all.end());
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    auto get_id = [&](int v) {
        return (int)(lower_bound(vals.begin(), vals.end(), v) - vals.begin());
    };

    int V = vals.size();
    DSU dsu(V);
    vector<bool> has_edge(V, false);
    int mismatches = 0;

    for (int i = 0; i < N; ++i) {
        if (a[i] != b[i]) {
            mismatches++;
            int u = get_id(a[i]);
            int v = get_id(b[i]);
            dsu.unite(u, v);
            has_edge[u] = true;
            has_edge[v] = true;
        }
    }

    vector<bool> comp_seen(V, false);
    int num_comps = 0;
    for (int i = 0; i < V; ++i) {
        if (has_edge[i]) {
            int root = dsu.find(i);
            if (!comp_seen[root]) {
                comp_seen[root] = true;
                num_comps++;
            }
        }
    }

    int start_id = get_id(ax);
    int extra = num_comps;
    if (has_edge[start_id]) {
        extra = num_comps - 1;
    }

    cout << mismatches + extra << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
