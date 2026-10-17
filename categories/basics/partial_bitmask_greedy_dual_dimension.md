# Partial Bitmask Enumeration with Greedy Sorting on Dual Dimension

**Domain**: `Basics`  
**Subtopic**: `Bitmask Enumeration`  

This workbook contains curated, high-quality competitive programming problems teaching **Partial Bitmask Enumeration with Greedy Sorting on Dual Dimension**.

---

## Curated Problems

### `[problem:AtCoder-abc018_4]` — バレンタインデー
- **Rating / Difficulty**: 1711
- **Contest**: `abc018`
- **Analysis**: [`analysis/AtCoder-abc018_4.md`](../../analysis/AtCoder-abc018_4.md)
- **Key Idea**: Since N <= 18, iterate over all C(N, P) subsets of girls using bitmasks. Once the girls are fixed, each boy's contribution is independent: sum all happiness values from the chosen girls to that boy. Greedily pick the Q boys with the highest happiness.
- **Time Complexity**: `O(C(N, P) * (R + M log M))`
- **Space Complexity**: `O(N + M + R)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int boy;
    int z;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, p, q, r;
    if (!(cin >> n >> m >> p >> q >> r)) return 0;

    vector<vector<Edge>> adj(n);
    for (int i = 0; i < r; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        --x; --y;
        adj[x].push_back({y, z});
    }

    int max_ans = 0;
    for (int mask = 0; mask < (1 << n); ++mask) {
        if (__builtin_popcount(mask) != p) continue;

        vector<int> boy_score(m, 0);
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                for (auto& e : adj[i]) {
                    boy_score[e.boy] += e.z;
                }
            }
        }

        sort(boy_score.rbegin(), boy_score.rend());
        int cur_score = 0;
        for (int j = 0; j < q; ++j) {
            cur_score += boy_score[j];
        }
        max_ans = max(max_ans, cur_score);
    }

    cout << max_ans << "\n";
    return 0;
}
```
