# Functional Graph Permutation Cycle Decomposition + Lucas Numbers

**Domain**: `Dynamic Programming`  
**Subtopic**: `Tree / Graph DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Functional Graph Permutation Cycle Decomposition + Lucas Numbers**.

---

## Curated Problems

### `[problem:AtCoder-abc247_f]` — Cards
- **Rating / Difficulty**: 1697
- **Contest**: `abc247`
- **Analysis**: [`analysis/AtCoder-abc247_f.md`](../../analysis/AtCoder-abc247_f.md)
- **Key Idea**: Model each card as an edge between P_i and Q_i. Because P and Q are permutations, every vertex has degree 2, so the graph decomposes into disjoint simple cycles! For each cycle of length L, the number of edge subsets covering all vertices is the Lucas number L_L.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n + 1), q(n + 1);
    for (int i = 1; i <= n; ++i) cin >> p[i];
    for (int i = 1; i <= n; ++i) cin >> q[i];

    vector<vector<int>> adj(n + 1);
    for (int i = 1; i <= n; ++i) {
        adj[p[i]].push_back(q[i]);
        adj[q[i]].push_back(p[i]);
    }

    // Precompute Lucas numbers
    vector<long long> lucas(n + 2);
    lucas[1] = 1;
    lucas[2] = 3;
    for (int i = 3; i <= n + 1; ++i) {
        lucas[i] = (lucas[i - 1] + lucas[i - 2]) % MOD;
    }

    vector<bool> visited(n + 1, false);
    long long ans = 1;

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            int cycle_len = 0;
            int curr = i;
            while (!visited[curr]) {
                visited[curr] = true;
                cycle_len++;
                // Move to next unvisited neighbor
                int next_node = -1;
                for (int nxt : adj[curr]) {
                    if (!visited[nxt]) {
                        next_node = nxt;
                        break;
                    }
                }
                if (next_node == -1) break;
                curr = next_node;
            }
            ans = (ans * lucas[cycle_len]) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
