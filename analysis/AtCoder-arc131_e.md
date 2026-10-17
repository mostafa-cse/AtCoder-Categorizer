# Problem Analysis: AtCoder-arc131_e — E. Christmas Wreath

**Problem ID**: `AtCoder-arc131_e`  
**Contest**: `arc131`  
**Rating / Difficulty**: 2314  
**URL**: https://atcoder.jp/contests/arc131/tasks/arc131_e  
**VJudge Tag**: `[problem:AtCoder-arc131_e]`  
**Category File**: [`../categories/basics/complete_graph_trichromatic_free_3partition.md`](../categories/basics/complete_graph_trichromatic_free_3partition.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Given $N$, color the edges of the complete graph $K_N$ with three colors (Red, Blue, White) such that each color appears on exactly $M/3$ edges and no triangle contains all three colors, or determine impossible.

## 2. Core Observation & Invariant
Assigning all edges $(i, j)$ ($i < j$) incident to vertex $j$ the same color $C_j$ guarantees that every triangle $(a, b, c)$ with $a < b < c$ has edges $(a, c)$ and $(b, c)$ of color $C_c$, completely preventing trichromatic triangles.

## 3. Step-by-Step Algorithm
1. Color the edges in stars from each vertex $j \in \{2, \dots, N\}$ of size $j - 1$.
2. This reduces the problem to partitioning the integers $\{1, 2, \dots, N-1\}$ into three subsets of equal sum $M / 3 = N(N-1) / 6$.
3. Solve the 3-partition via simple branch-and-bound backtracking in $O(3^{N/3})$ time for $N \le 50$, outputting the star coloring.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long m = 1LL * n * (n - 1) / 2;
    if (m % 3 != 0) {
        cout << "No\n";
        return 0;
    }

    long long target = m / 3;
    if (n - 1 > target) {
        cout << "No\n";
        return 0;
    }

    vector<int> items(n - 1);
    for (int i = 0; i < n - 1; ++i) {
        items[i] = n - 1 - i;
    }

    vector<int> c1, c2, c3;
    bool found = false;

    function<void(int, long long, long long, long long)> dfs = [&](int idx, long long s1, long long s2, long long s3) {
        if (found) return;
        if (s1 > target || s2 > target || s3 > target) return;
        if (idx == (int)items.size()) {
            if (s1 == target && s2 == target && s3 == target) {
                found = true;
            }
            return;
        }
        int v = items[idx];
        if (s1 + v <= target) {
            c1.push_back(v);
            dfs(idx + 1, s1 + v, s2, s3);
            if (found) return;
            c1.pop_back();
        }
        if (s2 + v <= target && s1 != s2) {
            c2.push_back(v);
            dfs(idx + 1, s1, s2 + v, s3);
            if (found) return;
            c2.pop_back();
        }
        if (s3 + v <= target && s2 != s3 && s1 != s3) {
            c3.push_back(v);
            dfs(idx + 1, s1, s2, s3 + v);
            if (found) return;
            c3.pop_back();
        }
    };

    dfs(0, 0, 0, 0);

    if (!found) {
        cout << "No\n";
        return 0;
    }

    cout << "Yes\n";
    vector<char> col(n + 1);
    for (int v : c1) col[v + 1] = 'R';
    for (int v : c2) col[v + 1] = 'B';
    for (int v : c3) col[v + 1] = 'W';

    for (int i = 1; i < n; ++i) {
        string row = "";
        for (int j = i + 1; j <= n; ++j) {
            row.push_back(col[j]);
        }
        cout << row << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
