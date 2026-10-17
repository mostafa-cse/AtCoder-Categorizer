# Binary Lifting on Permutations / Amidakuji Exponentiation

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Binary Lifting`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Lifting on Permutations / Amidakuji Exponentiation**.

---

## Curated Problems

### `[problem:AtCoder-abc013_4]` — 阿弥陀
- **Rating / Difficulty**: 1730
- **Contest**: `abc013`
- **Analysis**: [`analysis/AtCoder-abc013_4.md`](../../analysis/AtCoder-abc013_4.md)
- **Key Idea**: Traversing the ladder once forms a permutation P of {1, ..., N}. Traversing D times corresponds to computing P^D. Use binary lifting (doubling) over the permutation table up[k][i] = P^{2^k}(i).
- **Time Complexity**: `O(M + N log D)`
- **Space Complexity**: `O(N log D)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long d;
    if (!(cin >> n >> m >> d)) return 0;

    vector<int> a(m);
    for (int i = 0; i < m; ++i) {
        cin >> a[i];
    }

    vector<int> p(n + 1);
    iota(p.begin(), p.end(), 0);

    for (int i = m - 1; i >= 0; --i) {
        swap(p[a[i]], p[a[i] + 1]);
    }

    vector<vector<int>> up(31, vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        up[0][i] = p[i];
    }

    for (int k = 1; k < 31; ++k) {
        for (int i = 1; i <= n; ++i) {
            up[k][i] = up[k - 1][up[k - 1][i]];
        }
    }

    for (int i = 1; i <= n; ++i) {
        int cur = i;
        for (int k = 0; k < 31; ++k) {
            if ((d >> k) & 1) {
                cur = up[k][cur];
            }
        }
        cout << cur << "\n";
    }

    return 0;
}
```
