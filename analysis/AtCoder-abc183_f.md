# Problem Analysis: AtCoder-abc183_f — Confluence

**Problem ID**: `AtCoder-abc183_f`  
**Contest**: `abc183`  
**Rating / Difficulty**: 1586  
**URL**: https://atcoder.jp/contests/abc183/tasks/abc183_f  
**VJudge Tag**: `[problem:AtCoder-abc183_f]`  
**Category File**: [`../categories/data_structures/dsu_small_to_large_map_merging.md`](../categories/data_structures/dsu_small_to_large_map_merging.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `Disjoint Set Union with Small-to-Large Map Merging`  

---

## 1. Problem Statement & Key Idea
N students with classes C_1, ..., C_N. Process Q queries: 1) unite groups containing student x and student y; 2) count how many students in student x's group belong to class y.

**Key Insight**: Each DSU component maintains a frequency map `std::map<int, int>` of class counts. When uniting components, merge the smaller map into the larger map (small-to-large / sack heuristic).

## 2. Core Observation & Invariant
Each element is inserted into a new map at most O(log N) times. With map operations, total time is O(N log^2 N + Q log N). Queries are answered in O(log N) directly from the component root's map.

## 3. Step-by-Step Algorithm
1. Initialize DSU parent[i] = i, and maps class_count[i][C_i] = 1.
2. For query 1 (unite x, y):
3.   rx = find(x), ry = find(y).
4.   If rx == ry continue.
5.   If class_count[rx].size() < class_count[ry].size(), swap(rx, ry).
6.   parent[ry] = rx.
7.   For each (cls, cnt) in class_count[ry]: class_count[rx][cls] += cnt.
8.   class_count[ry].clear().
9. For query 2 (x, cls):
10.   rx = find(x).
11.   Print class_count[rx][cls].

## 4. Complexity Analysis
- **Time Complexity**: `O(N log^2 N + Q log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<map<int, int>> class_count;

    DSU(int n, const vector<int>& c) : parent(n + 1), class_count(n + 1) {
        for (int i = 1; i <= n; ++i) {
            parent[i] = i;
            class_count[i][c[i]] = 1;
        }
    }

    int find(int u) {
        return parent[u] == u ? u : parent[u] = find(parent[u]);
    }

    void unite(int u, int v) {
        int ru = find(u);
        int rv = find(v);
        if (ru == rv) return;

        if (class_count[ru].size() < class_count[rv].size()) {
            swap(ru, rv);
        }

        parent[rv] = ru;
        for (const auto& entry : class_count[rv]) {
            class_count[ru][entry.first] += entry.second;
        }
        class_count[rv].clear();
    }

    int query(int u, int cls) {
        int ru = find(u);
        auto it = class_count[ru].find(cls);
        return it != class_count[ru].end() ? it->second : 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> c(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> c[i];
    }

    DSU dsu(n, c);

    while (q--) {
        int type, x, y;
        cin >> type >> x >> y;
        if (type == 1) {
            dsu.unite(x, y);
        } else {
            cout << dsu.query(x, y) << "\n";
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Small-to-large merging heuristic applied to DSU components.
- **Reusable Pattern**: `DSU Map Merging: if map[u].size() < map[v].size() swap; merge v into u.`
