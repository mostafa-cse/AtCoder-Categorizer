# Problem Analysis: AtCoder-arc118_d — D. Hamiltonian Cycle

**Problem ID**: `AtCoder-arc118_d`  
**Contest**: `arc118`  
**Rating / Difficulty**: 2448  
**URL**: https://atcoder.jp/contests/arc118/tasks/arc118_d  
**VJudge Tag**: `[problem:AtCoder-arc118_d]`  
**Category File**: [`../categories/graph_theory/hamiltonian_cycle_cayley_grid.md`](../categories/graph_theory/hamiltonian_cycle_cayley_grid.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Hamiltonian Path`  
- **Topic (Skill)**: `Hamiltonian Path and Cycle`  

---

## 1. Problem Statement & Key Idea
Construct a Hamiltonian cycle on the Cayley graph of $(\mathbb{Z}/P\mathbb{Z})^\times$ with generator set $\{a, a^{-1}, b, b^{-1}\}$.

## 2. Core Observation & Invariant
Let $n = \text{ord}(a)$ and $m = \min \{ m \ge 1 \mid b^m \in \langle a \rangle \}$. The generated subgroup has size $n \cdot m$. A Hamiltonian cycle exists iff $n \cdot m = P - 1$. Since $P - 1$ is even, at least one of $n, m$ is even (swap $a, b$ if necessary so $m$ is even). The elements form an $n \times m$ grid $(i, j) \leftrightarrow a^i b^j$. On this grid, traverse rows $1 \dots n-1$ in 2-column serpentine blocks, step to $(0, m-1)$, and return along row 0 to $(0, 0)$.

## 3. Step-by-Step Algorithm
1. 1. If $P = 2$, return `Yes\n1 1`.
2. 2. Compute $n = \text{ord}(a)$ and minimum $m \ge 1$ with $b^m \in \langle a \rangle$.
3. 3. If $n \cdot m \ne P - 1$, output `No`.
4. 4. If $n > 1$ and $m$ is odd, swap $a$ and $b$ and recompute $n, m$.
5. 5. If $n = 1$ or $m = 1$, output 1D power cycle.
6. 6. Otherwise, traverse the $n \times m$ grid in 2-column blocks covering rows $1 \dots n-1$, ascend to $(0, m-1)$, and walk left to $(0, 0)$.
7. 7. Map grid coordinates to $a^r b^c \pmod P$ and output the sequence.

## 4. Complexity Analysis
- **Time Complexity**: `O(P)`
- **Space Complexity**: `O(P)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long P, a, b;
    if (!(cin >> P >> a >> b)) return 0;
    if (P == 2) {
        cout << "Yes\n1 1\n";
        return 0;
    }

    auto get_n_m = [&](long long a_val, long long b_val, int &n, int &m, vector<int> &in_H) {
        in_H.assign(P, 0);
        long long cur = a_val % P;
        n = 1;
        in_H[1] = 1;
        while (cur != 1) {
            in_H[cur] = 1;
            cur = (cur * a_val) % P;
            n++;
        }
        long long cur_b = b_val % P;
        m = 1;
        while (!in_H[cur_b]) {
            cur_b = (cur_b * b_val) % P;
            m++;
            if (m > P) break;
        }
    };

    int n, m;
    vector<int> in_H;
    get_n_m(a, b, n, m, in_H);

    if (1LL * n * m != P - 1) {
        cout << "No\n";
        return 0;
    }

    if (n > 1 && m > 1 && m % 2 != 0) {
        swap(a, b);
        get_n_m(a, b, n, m, in_H);
    }

    vector<long long> path;
    if (n == 1) {
        long long val = 1;
        for (int i = 0; i < m; ++i) {
            path.push_back(val);
            val = (val * b) % P;
        }
        path.push_back(1);
    } else if (m == 1) {
        long long val = 1;
        for (int i = 0; i < n; ++i) {
            path.push_back(val);
            val = (val * a) % P;
        }
        path.push_back(1);
    } else {
        vector<pair<int, int>> coords;
        coords.push_back({0, 0});
        for (int k = 0; k < m / 2; ++k) {
            int col_l = 2 * k;
            int col_r = 2 * k + 1;
            if (k > 0) coords.push_back({1, col_l});
            else coords.push_back({1, 0});
            for (int r = 2; r < n; ++r) coords.push_back({r, col_l});
            coords.push_back({n - 1, col_r});
            for (int r = n - 2; r >= 1; --r) coords.push_back({r, col_r});
        }
        coords.push_back({0, m - 1});
        for (int c = m - 2; c >= 1; --c) coords.push_back({0, c});
        coords.push_back({0, 0});

        vector<long long> pow_a(n, 1), pow_b(m, 1);
        for (int i = 1; i < n; ++i) pow_a[i] = (pow_a[i - 1] * a) % P;
        for (int j = 1; j < m; ++j) pow_b[j] = (pow_b[j - 1] * b) % P;

        for (auto &p : coords) {
            path.push_back((pow_a[p.first] * pow_b[p.second]) % P);
        }
    }

    cout << "Yes\n";
    for (int i = 0; i < (int)path.size(); ++i) {
        cout << path[i] << (i + 1 == (int)path.size() ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
