# Minimum Swaps to Sort Finite-Alphabet Array via Directed Cycle Decomposition

**Domain**: `Graph Theory`  
**Subtopic**: `Cycle Decomposition`  

This workbook contains curated, high-quality competitive programming problems teaching **Minimum Swaps to Sort Finite-Alphabet Array via Directed Cycle Decomposition**.

---

## Curated Problems

### `[problem:AtCoder-abc302_g]` — Sort from 1 to 4
- **Rating / Difficulty**: 1891
- **Contest**: `abc302`
- **Analysis**: [`analysis/AtCoder-abc302_g.md`](../../analysis/AtCoder-abc302_g.md)
- **Key Idea**: Let cnt[u][v] be the number of indices where the actual array has value u but the sorted target array has value v. This forms a directed multigraph with 4 vertices. A cycle of length L fixes L elements using L - 1 swaps. To minimize swaps, maximize the number of cycles by greedily extracting 2-cycles, then 3-cycles, then 4-cycles.
- **Time Complexity**: `O(N + 4^4)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n), b(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        b[i] = a[i];
    }

    sort(b.begin(), b.end());

    int cnt[5][5] = {};
    for (int i = 0; i < n; ++i) {
        if (a[i] != b[i]) {
            cnt[a[i]][b[i]]++;
        }
    }

    long long swaps = 0;

    // 2-cycles
    for (int u = 1; u <= 4; ++u) {
        for (int v = u + 1; v <= 4; ++v) {
            int k = min(cnt[u][v], cnt[v][u]);
            swaps += k;
            cnt[u][v] -= k;
            cnt[v][u] -= k;
        }
    }

    // 3-cycles
    vector<int> p3 = {1, 2, 3, 4};
    for (int u = 1; u <= 4; ++u) {
        for (int v = 1; v <= 4; ++v) {
            for (int w = 1; w <= 4; ++w) {
                if (u != v && v != w && w != u) {
                    int k = min({cnt[u][v], cnt[v][w], cnt[w][u]});
                    swaps += 2LL * k;
                    cnt[u][v] -= k;
                    cnt[v][w] -= k;
                    cnt[w][u] -= k;
                }
            }
        }
    }

    // 4-cycles
    for (int u = 1; u <= 4; ++u) {
        for (int v = 1; v <= 4; ++v) {
            for (int w = 1; w <= 4; ++w) {
                for (int x = 1; x <= 4; ++x) {
                    if (u != v && v != w && w != x && x != u && u != w && v != x) {
                        int k = min({cnt[u][v], cnt[v][w], cnt[w][x], cnt[x][u]});
                        swaps += 3LL * k;
                        cnt[u][v] -= k;
                        cnt[v][w] -= k;
                        cnt[w][x] -= k;
                        cnt[x][u] -= k;
                    }
                }
            }
        }
    }

    cout << swaps << "\n";
    return 0;
}
```
