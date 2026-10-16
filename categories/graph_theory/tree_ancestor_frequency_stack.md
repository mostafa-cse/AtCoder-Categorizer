# Tree Path Ancestor Frequency Stack Backtracking

**Domain**: `Graph Theory`  
**Subtopic**: `Tree DFS`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree Path Ancestor Frequency Stack Backtracking**.

---

## Curated Problems

### [problem:AtCoder-abc198_e] — Unique Color
- **Contest**: `abc198`
- **Rating / Difficulty**: 1161
- **Specific Skill**: Tree Path Ancestor Frequency Stack Backtracking
- **Individual Analysis**: [`../../analysis/AtCoder-abc198_e.md`](../../analysis/AtCoder-abc198_e.md)
- **Problem Statement Summary**: Given a tree rooted at vertex 1. Vertex i has color C_i. A vertex is 'good' if no vertex on the path from root 1 to v (excluding v) shares color C_v. Find all good vertices in ascending order.
- **Core Insight**: Maintain a global frequency array cnt[color] representing the number of active ancestors on the path from root to current node. When entering node u, check if cnt[C_u] == 0 (if so, u is good); increment cnt[C_u], recurse on children, and decrement cnt[C_u] on exit.
- **Complexity**: Time: `O(N log N)` | Space: `O(N + max_color)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXC = 100000;
vector<vector<int>> adj;
vector<int> color;
vector<int> freq;
vector<int> good;

void dfs(int u, int p) {
    if (freq[color[u]] == 0) {
        good.push_back(u);
    }
    freq[color[u]]++;

    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u);
        }
    }

    freq[color[u]]--;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    color.resize(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> color[i];
    }

    adj.resize(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    freq.assign(MAXC + 1, 0);
    dfs(1, 0);

    sort(good.begin(), good.end());
    for (int x : good) {
        cout << x << "\n";
    }

    return 0;
}
```
