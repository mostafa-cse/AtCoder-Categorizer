# Floyd-Warshall + Permutation Search on Target Subsets

**Domain**: `Graph Theory`  
**Subtopic**: `All-Pairs Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Floyd-Warshall + Permutation Search on Target Subsets**.

---

## Curated Problems

### [problem:AtCoder-abc073_d] — joisino's travel
- **Contest**: `abc073`
- **Rating / Difficulty**: 1345
- **Specific Skill**: Floyd-Warshall + Permutation Search on Target Subsets
- **Individual Analysis**: [`../../analysis/AtCoder-abc073_d.md`](../../analysis/AtCoder-abc073_d.md)
- **Problem Statement Summary**: An undirected weighted graph with N towns and M roads. Joisino must visit R specific towns r_1, ..., r_R (R <= 8) in any order. Find the minimum total distance traveled.
- **Core Insight**: Because R <= 8, R! <= 8! = 40,320 permutations. For each permutation p of {r_1, ..., r_R}, the travel cost is sum_{i=0}^{R-2} dist[p[i]][p[i+1]]. The minimum over all R! permutations is the exact answer.
- **Complexity**: Time: `O(N^3 + R! * R)` | Space: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

const long long INF = 1e15;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, R;
    if (!(cin >> n >> m >> R)) return 0;

    vector<int> r(R);
    for (int i = 0; i < R; ++i) {
        cin >> r[i];
    }

    vector<vector<long long>> dist(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        dist[u][v] = min(dist[u][v], c);
        dist[v][u] = min(dist[v][u], c);
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    sort(r.begin(), r.end());
    long long ans = INF;

    do {
        long long cur = 0;
        for (int i = 0; i < R - 1; ++i) {
            cur += dist[r[i]][r[i + 1]];
        }
        ans = min(ans, cur);
    } while (next_permutation(r.begin(), r.end()));

    cout << ans << "\n";
    return 0;
}
```
