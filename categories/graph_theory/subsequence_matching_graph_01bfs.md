# Worst-Case Subsequence Matching on Graph via 0-1 BFS

**Domain**: `Graph Theory`  
**Subtopic**: `0-1 BFS`  

This workbook contains curated, high-quality competitive programming problems teaching **Worst-Case Subsequence Matching on Graph via 0-1 BFS**.

---

## Curated Problems

### `[problem:AtCoder-arc150_c]` — Path and Subsequence
- **Rating / Difficulty**: 1802
- **Contest**: `arc150`
- **Analysis**: [`analysis/AtCoder-arc150_c.md`](../../analysis/AtCoder-arc150_c.md)
- **Key Idea**: Every path contains S iff the path from 1 to N that matches the FEWEST elements of S matches all K elements. Find the minimum matched prefix length of S from 1 to N using 0-1 BFS.
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<int> s(k + 1);
    for (int i = 1; i <= k; ++i) cin >> s[i];

    vector<int> d(n + 1, INF);
    deque<int> dq;

    d[1] = (a[1] == s[1] ? 1 : 0);
    dq.push_front(1);

    while (!dq.empty()) {
        int u = dq.front();
        dq.pop_front();

        for (int v : adj[u]) {
            int w = (d[u] < k && a[v] == s[d[u] + 1]) ? 1 : 0;
            int next_d = d[u] + w;
            if (next_d < d[v]) {
                d[v] = next_d;
                if (w == 0) dq.push_front(v);
                else dq.push_back(v);
            }
        }
    }

    if (d[n] == k) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}
```
