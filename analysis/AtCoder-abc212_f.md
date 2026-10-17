# Problem Analysis: AtCoder-abc212_f — F. Greedy Takahashi

**Problem ID**: `AtCoder-abc212_f`  
**Contest**: `abc212`  
**Rating / Difficulty**: 2332  
**URL**: https://atcoder.jp/contests/abc212/tasks/abc212_f  
**VJudge Tag**: `[problem:AtCoder-abc212_f]`  
**Category File**: [`../categories/graph_theory/functional_bus_graph_binary_lifting.md`](../categories/graph_theory/functional_bus_graph_binary_lifting.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Lowest Common Ancestor (LCA)`  
- **Topic (Skill)**: `Binary Lifting and LCA`  

---

## 1. Problem Statement & Key Idea
Buses connect cities deterministically at discrete times. Each bus departure transitions to a unique subsequent bus, forming a functional graph. Binary lifting over bus transitions answers position queries at time $Z$ in $O(\log M)$ time.

## 2. Core Observation & Invariant
Because a person arriving at city $B_i$ at time $T_i$ must take the earliest departing bus with departure time $\ge T_i$, each bus $i$ has at most one deterministic successor bus. The bus transition system forms a directed functional forest.

## 3. Step-by-Step Algorithm
1. Sort bus departures per city. For each bus $i$, identify its unique deterministic successor bus via binary search on departure times $\ge T_i$.
2. Construct binary lifting table $up[k][i]$ over bus transitions up to $2^{20}$.
3. For each query $(X, Y, Z)$, locate Takahashi's first bus departing city $Y$ at time $\ge X$. If departure time $\ge Z$, output current city; otherwise, binary lift along the bus graph to find his location at time $Z$ in $O(\log M)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O((M + Q) \log M)`
- **Space Complexity**: `O(M \log M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Bus {
    int id;
    int u, v;
    long long s, t;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<Bus> buses(m);
    vector<vector<int>> city_buses(n + 1);

    for (int i = 0; i < m; ++i) {
        buses[i].id = i;
        cin >> buses[i].u >> buses[i].v >> buses[i].s >> buses[i].t;
        city_buses[buses[i].u].push_back(i);
    }

    for (int c = 1; c <= n; ++c) {
        sort(city_buses[c].begin(), city_buses[c].end(), [&](int a, int b) {
            return buses[a].s < buses[b].s;
        });
    }

    const int LOGN = 20;
    vector<vector<int>> up(LOGN, vector<int>(m, -1));

    for (int i = 0; i < m; ++i) {
        int v = buses[i].v;
        long long t_arr = buses[i].t;
        const auto &vec = city_buses[v];
        int l = 0, r = (int)vec.size() - 1;
        int nxt = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (buses[vec[mid]].s >= t_arr) {
                nxt = vec[mid];
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        up[0][i] = nxt;
    }

    for (int k = 1; k < LOGN; ++k) {
        for (int i = 0; i < m; ++i) {
            if (up[k - 1][i] != -1) {
                up[k][i] = up[k - 1][up[k - 1][i]];
            } else {
                up[k][i] = -1;
            }
        }
    }

    while (q--) {
        long long x, z;
        int y;
        cin >> x >> y >> z;

        const auto &vec = city_buses[y];
        int l = 0, r = (int)vec.size() - 1;
        int first_bus = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (buses[vec[mid]].s >= x) {
                first_bus = vec[mid];
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        if (first_bus == -1 || buses[first_bus].s >= z) {
            cout << y << "\n";
            continue;
        }

        int cur = first_bus;
        for (int k = LOGN - 1; k >= 0; --k) {
            if (up[k][cur] != -1 && buses[up[k][cur]].s < z) {
                cur = up[k][cur];
            }
        }

        if (z <= buses[cur].t) {
            cout << buses[cur].u << " " << buses[cur].v << "\n";
        } else {
            cout << buses[cur].v << "\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
