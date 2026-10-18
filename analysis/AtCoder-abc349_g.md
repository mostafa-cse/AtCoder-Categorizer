# Problem Analysis: AtCoder-abc349_g — Palindrome Construction

**Problem ID**: `AtCoder-abc349_g`  
**Contest**: `abc349`  
**Rating / Difficulty**: 2655  
**URL**: https://atcoder.jp/contests/abc349/tasks/abc349_g  
**VJudge Tag**: `[problem:AtCoder-abc349_g]`  
**Category File**: [`../categories/data_structures_ds/palindrome_construction_dsu_dag.md`](../categories/data_structures_ds/palindrome_construction_dsu_dag.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `DSU / Union Find`  

---

## 1. Problem Statement & Key Idea
Constructing a positive integer sequence satisfying given palindrome radii requirements decomposes into equality constraints united via DSU (accelerated via Manacher-style jumps) and inequality constraints colored via a greedy DAG topological sort.

## 2. Core Observation & Invariant
For each index i with radius A[i], character pairs (i - k, i + k) for k = 1..A[i] must be equal, while if i - A[i] - 1 >= 0 and i + A[i] + 1 < N, the characters at i - A[i] - 1 and i + A[i] + 1 must be strictly unequal. Unite equal indices using DSU, skipping already-united components using a maximum-reach pointer. Create a directed inequality graph between DSU components and assign minimal positive integers greedily via mex/topological order.

## 3. Step-by-Step Algorithm
1. 1. Initialize DSU for N vertices.
2. 2. For each i, unite pairs (i - k, i + k) for k = 1..A[i], using Manacher skip-ahead to avoid redundant unifications.
3. 3. Add inequality edges between endpoints where palindrome condition terminates.
4. 4. Check for contradictory self-loops or cycles in the equality/inequality graph.
5. 5. Greedily assign positive values using topological sort / mex.
6. 6. Output 'Yes' and the sequence, or 'No' if impossible.

## 4. Complexity Analysis
- **Time Complexity**: `O(N alpha(N))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int ri = find(i), rj = find(j);
        if (ri != rj) parent[ri] = rj;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }

    DSU dsu(N);

    // Manacher-style interval DSU union
    int R = 0, C = 0;
    for (int i = 1; i <= N; ++i) {
        int r = i + A[i];
        int start_d = 1;
        if (i < R) {
            start_d = max(1, R - i + 1);
        }
        for (int d = start_d; d <= A[i]; ++d) {
            dsu.unite(i - d, i + d);
        }
        if (r > R) {
            R = r;
            C = i;
        }
    }

    // Inequality constraints
    vector<vector<int>> adj(N + 1);
    for (int i = 1; i <= N; ++i) {
        int a = A[i];
        int l = i - a - 1;
        int r = i + a + 1;
        if (l >= 1 && r <= N) {
            int rl = dsu.find(l);
            int rr = dsu.find(r);
            if (rl == rr) {
                cout << "No\n";
                return 0;
            }
            adj[rl].push_back(rr);
            adj[rr].push_back(rl);
        }
    }

    // Greedy mex coloring in order of positions 1 to N
    vector<int> color(N + 1, 0);
    vector<int> vis_tag(N + 2, 0);

    for (int i = 1; i <= N; ++i) {
        int root = dsu.find(i);
        if (color[root] == 0) {
            for (int neighbor : adj[root]) {
                if (color[neighbor] != 0 && color[neighbor] <= N + 1) {
                    vis_tag[color[neighbor]] = root;
                }
            }
            int c = 1;
            while (vis_tag[c] == root) {
                c++;
            }
            color[root] = c;
        }
    }

    cout << "Yes\n";
    for (int i = 1; i <= N; ++i) {
        cout << color[dsu.find(i)] << (i == N ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
