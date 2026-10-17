# Problem Analysis: AtCoder-agc035_c — C. Skolem XOR Tree

**Problem ID**: `AtCoder-agc035_c`  
**Contest**: `agc035`  
**Rating / Difficulty**: 2332  
**URL**: https://atcoder.jp/contests/agc035/tasks/agc035_c  
**VJudge Tag**: `[problem:AtCoder-agc035_c]`  
**Category File**: [`../categories/basics/xor_tree_bichromatic_constructive.md`](../categories/basics/xor_tree_bichromatic_constructive.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Construct a tree of $2N$ vertices with weights $1 \dots N, 1 \dots N$ where the path between $i$ and $N+i$ has XOR sum $i$. Star topology around 1 with pairs $(2k, 2k+1)$ and 3-basis decomposition solves for all non-powers of 2 in $O(N)$.

## 2. Core Observation & Invariant
If $N$ is a power of 2, the MSB of $N$ appears only in vertices $N$ and $N+N$, so the path between them cannot form an XOR sum of $N$, making construction impossible. For odd $N$ or non-power-of-2 even $N$, pairs $(2k, 2k+1)$ satisfy $2k \oplus (2k+1) = 1$, allowing a star hub at 1 to achieve paths of XOR $x$ for all $x$.

## 3. Step-by-Step Algorithm
1. If $N = 2^k$, output No.
2. Connect vertex 1 to 2, 2 to 3, 3 to $N+1$, $N+1$ to $N+2$, and $N+2$ to $N+3$.
3. For each pair $(2k, 2k+1) \le N$, connect 1 to $2k$, $2k$ to $2k+1$, 1 to $N+2k+1$, and $N+2k+1$ to $N+2k$.
4. If $N$ is even, decompose $N = u \oplus v \oplus 1$ with $u = N \& -N$ and $v = N \oplus u \oplus 1$, connecting $N$ to $u$ and $N+N$ to $N+v$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if ((n & (n - 1)) == 0) {
        cout << "No\n";
        return 0;
    }

    cout << "Yes\n";
    vector<pair<int, int>> edges;
    for (int k = 1; 2 * k + 1 <= n; ++k) {
        int u = 2 * k;
        int v = 2 * k + 1;
        edges.emplace_back(1, u);
        edges.emplace_back(u, v);
        edges.emplace_back(1, n + v);
        edges.emplace_back(n + v, n + u);
    }

    edges.emplace_back(3, n + 1);

    if (n % 2 == 0) {
        int u = n & -n;
        int v = n ^ u ^ 1;
        edges.emplace_back(n, u);
        edges.emplace_back(n + n, n + v);
    }

    for (auto &e : edges) {
        cout << e.first << " " << e.second << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
