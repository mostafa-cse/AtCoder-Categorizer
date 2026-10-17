# Problem Analysis: AtCoder-arc065_b — Connectivity

**Problem ID**: `AtCoder-arc065_b`  
**Contest**: `arc065`  
**Rating / Difficulty**: 1996  
**URL**: https://atcoder.jp/contests/arc065/tasks/arc065_b  
**VJudge Tag**: `[problem:AtCoder-arc065_b]`  
**Category File**: [`../categories/data_structures/dual_dsu_joint_connectivity_hash_pairing.md`](../categories/data_structures/dual_dsu_joint_connectivity_hash_pairing.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `Dual Graph Joint Connectivity Counting via Component Root Hash Pairing`  

---

## 1. Problem Statement & Key Idea
N cities connected by two independent edge sets: K roads and L railways. Two cities p, q are jointly connected iff they can reach each other via roads AND via railways. For each city i, output the number of cities jointly connected to i.

Build two separate DSU structures: one for the road network and one for the railway network. City i belongs to road component root R_i = find_road(i) and railway component root T_i = find_rail(i). Two cities p, q are jointly connected iff R_p == R_q AND T_p == T_q. Thus, joint connectivity is an equivalence relation where each city's equivalence class is uniquely defined by the pair of canonical roots (R_i, T_i). Count frequencies of each pair using a hash map or sorting in O(N log N).

## 2. Core Observation & Invariant
Joint connectivity across multiple networks is the intersection of equivalence classes, uniquely keyed by the tuple of DSU component roots.

## 3. Step-by-Step Algorithm
1. Initialize DSU_road and DSU_rail for N cities.
2. Add all K roads to DSU_road.
3. Add all L railways to DSU_rail.
4. For each city i in 1..N: record signature pair (DSU_road.find(i), DSU_rail.find(i)).
5. Count occurrences of each signature pair using map.
6. For each city i: print count[signature[i]].

## 4. Complexity Analysis
- **Time Complexity**: `O((N + K + L) * alpha(N) + N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <map>

using namespace std;

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int v) {
        if (v == parent[v]) return v;
        return parent[v] = find(parent[v]);
    }
    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) parent[b] = a;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k, l;
    if (!(cin >> n >> k >> l)) return 0;

    DSU road(n), rail(n);

    for (int i = 0; i < k; ++i) {
        int u, v;
        cin >> u >> v;
        road.unite(u, v);
    }

    for (int i = 0; i < l; ++i) {
        int u, v;
        cin >> u >> v;
        rail.unite(u, v);
    }

    map<pair<int, int>, int> freq;
    vector<pair<int, int>> sig(n + 1);

    for (int i = 1; i <= n; ++i) {
        sig[i] = {road.find(i), rail.find(i)};
        freq[sig[i]]++;
    }

    for (int i = 1; i <= n; ++i) {
        cout << freq[sig[i]] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Equivalence relation intersection across multiple graphs using DSU root pairing.
- **Reusable Pattern**: `Multi-Network Connectivity: Hash/map pair of roots (find_1(u), find_2(u)) across networks.`
