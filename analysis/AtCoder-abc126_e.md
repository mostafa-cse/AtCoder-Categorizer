# Problem Analysis: AtCoder-abc126_e — 1 or 2

**Problem ID**: `AtCoder-abc126_e`  
**Contest**: `abc126`  
**Rating / Difficulty**: 1340  
**URL**: https://atcoder.jp/contests/abc126/tasks/abc126_e  
**VJudge Tag**: `[problem:AtCoder-abc126_e]`  
**Category File**: [`../categories/data_structures/dsu_parity_system_components.md`](../categories/data_structures/dsu_parity_system_components.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Disjoint Set Union`  
- **Topic (Skill)**: `System of Parity Constraints / DSU Component Count`  

---

## 1. Problem Statement & Key Idea
N cards with numbers 1 or 2. M clues: (X_i, Y_i, Z_i) means A_{X_i} + A_{Y_i} + Z_i is even. Find the minimum number of cards to reveal to determine all cards.

**Key Idea**: The equation A_X + A_Y = Z (mod 2) means knowing either A_X or A_Y uniquely determines the other.

## 2. Core Observation & Invariant
Each clue defines an undirected edge between card X and card Y in a knowledge graph. In any connected component, revealing the value of just ONE card determines the values of all other cards in that component! Therefore, the minimum cards needed equals the number of connected components in the graph.

## 3. Step-by-Step Algorithm
1. Initialize DSU on N vertices.
2. For each clue (x, y, z): unite(x, y).
3. Count distinct DSU roots.
4. Print the component count.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) * alpha(N))`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    int components;
    DSU(int n) : parent(n + 1), components(n) {
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
            components--;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    DSU dsu(n);
    for (int i = 0; i < m; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        dsu.unite(x, y);
    }

    cout << dsu.components << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Modeling linear GF(2) parity relations as connected components in DSU.
- **Reusable Pattern**: `Degrees of freedom in pairwise parity equations = number of DSU connected components.`
