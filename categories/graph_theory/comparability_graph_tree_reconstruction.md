# Comparability Graph Tree Reconstruction and Component Decomposition

**Domain**: `Graph Theory`  
**Subtopic**: `Trees`  

This workbook contains curated, high-quality competitive programming problems teaching **Comparability Graph Tree Reconstruction and Component Decomposition**.

---

## Curated Problems

### `[problem:AtCoder-arc197_d]` — Ancestor Relation
- **Rating / Difficulty**: 2062
- **Contest**: `arc197`
- **Analysis**: [`analysis/AtCoder-arc197_d.md`](../../analysis/AtCoder-arc197_d.md)
- **Key Idea**: The matrix A represents the comparability graph of a tree poset rooted at 1. Vertex 1 must be connected to all vertices. Removing 1, the remaining vertices must partition into connected components representing independent subtrees attached to 1. Inside each component C, the root path before any branching consists of universal vertices (vertices connected to all vertices in C). If there are k universal vertices, they can be arranged in k! orders along the entrance chain. Removing them splits C into further disconnected subcomponents, which are solved recursively.
- **Time Complexity**: `O(N^2) per testcase`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 998244353;

long long fact[505];

void solve() {
    int n;
    cin >> n;
    vector<vector<int>> A(n + 1, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> A[i][j];
        }
    }

    for (int i = 1; i <= n; ++i) {
        if (A[1][i] == 0) {
            cout << 0 << "\n";
            return;
        }
    }

    auto solve_comp = [&](auto& self, const vector<int>& comp) -> long long {
        if (comp.empty()) return 1;
        vector<int> univ;
        for (int u : comp) {
            bool ok = true;
            for (int v : comp) {
                if (A[u][v] == 0) {
                    ok = false;
                    break;
                }
            }
            if (ok) univ.push_back(u);
        }
        if (univ.empty()) return 0;
        int k = univ.size();
        vector<bool> in_univ(n + 1, false);
        for (int u : univ) in_univ[u] = true;
        vector<int> rem;
        for (int u : comp) {
            if (!in_univ[u]) rem.push_back(u);
        }
        if (rem.empty()) return fact[k];

        vector<bool> visited(n + 1, false);
        long long ans = fact[k];
        for (int u : rem) {
            if (!visited[u]) {
                vector<int> sub_c;
                vector<int> q = {u};
                visited[u] = true;
                int head = 0;
                while (head < (int)q.size()) {
                    int cur = q[head++];
                    sub_c.push_back(cur);
                    for (int v : rem) {
                        if (A[cur][v] == 1 && !visited[v]) {
                            visited[v] = true;
                            q.push_back(v);
                        }
                    }
                }
                long long sub_res = self(self, sub_c);
                if (sub_res == 0) return 0;
                ans = (ans * sub_res) % MOD;
            }
        }
        return ans;
    };

    vector<int> rem;
    for (int i = 2; i <= n; ++i) rem.push_back(i);

    vector<bool> visited(n + 1, false);
    long long total_ans = 1;
    for (int u : rem) {
        if (!visited[u]) {
            vector<int> sub_c;
            vector<int> q = {u};
            visited[u] = true;
            int head = 0;
            while (head < (int)q.size()) {
                int cur = q[head++];
                sub_c.push_back(cur);
                for (int v : rem) {
                    if (A[cur][v] == 1 && !visited[v]) {
                        visited[v] = true;
                        q.push_back(v);
                    }
                }
            }
            long long sub_res = solve_comp(solve_comp, sub_c);
            if (sub_res == 0) {
                cout << 0 << "\n";
                return;
            }
            total_ans = (total_ans * sub_res) % MOD;
        }
    }
    cout << total_ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    fact[0] = 1;
    for (int i = 1; i <= 500; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```
