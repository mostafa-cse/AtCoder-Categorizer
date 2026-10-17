# Tree DFS Minimax Game with Subtree Size Parity Inversion and Greedy Child Ordering

**Domain**: `Game Theory`  
**Subtopic**: `Tree Games / Minimax`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree DFS Minimax Game with Subtree Size Parity Inversion and Greedy Child Ordering**.

---

## Curated Problems

### `[problem:AtCoder-arc112_c]` — DFS Game
- **Rating / Difficulty**: 1913
- **Contest**: `arc112`
- **Analysis**: [`analysis/AtCoder-arc112_c.md`](../../analysis/AtCoder-arc112_c.md)
- **Key Idea**: Let f[u] be the net difference (mover - other) from subtree u. Node u gives +1 coin. If child v has even size sz[v], the same player gets the turn upon return. Thus first player greedily takes all even subtrees with f[v] > 0 first. Odd subtrees change the turn upon return; first player sorts odd subtrees to alternate picks greedily. Finally, even subtrees with negative values are consumed by whoever is left with the turn.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int n;
vector<vector<int>> adj;
vector<int> sz;
vector<int> f;

void dfs(int u) {
    sz[u] = 1;
    vector<int> even_pos;
    vector<int> even_neg;
    vector<int> odd;

    int base_val = 1;

    for (int v : adj[u]) {
        dfs(v);
        sz[u] += sz[v];
        if (sz[v] % 2 == 0) {
            if (f[v] > 0) {
                even_pos.push_back(f[v]);
            } else {
                even_neg.push_back(f[v]);
            }
        } else {
            odd.push_back(f[v]);
        }
    }

    for (int x : even_pos) {
        base_val += x;
    }

    sort(odd.begin(), odd.end());
    int sign = -1;
    for (int x : odd) {
        base_val += sign * x;
        sign = -sign;
    }

    for (int x : even_neg) {
        base_val += sign * x;
    }

    f[u] = base_val;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    sz.assign(n + 1, 0);
    f.assign(n + 1, 0);

    for (int i = 2; i <= n; ++i) {
        int p;
        cin >> p;
        adj[p].push_back(i);
    }

    dfs(1);

    int takahashi = (n + f[1]) / 2;
    cout << takahashi << "\n";
    return 0;
}
```
