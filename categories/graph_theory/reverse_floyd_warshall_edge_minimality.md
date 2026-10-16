# Reverse Floyd-Warshall Strict Triangle Inequality Edge Minimality

**Domain**: `Graph Theory`  
**Subtopic**: `All-Pairs Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Reverse Floyd-Warshall Strict Triangle Inequality Edge Minimality**.

---

## Curated Problems

### `[problem:AtCoder-arc083_b]` — Restoring Road Network
- **Rating / Difficulty**: 1563
- **Contest**: `abc074`
- **Analysis**: [`analysis/AtCoder-arc083_b.md`](../../analysis/AtCoder-arc083_b.md)
- **Key Idea**: Reverse Floyd-Warshall! If A[i][j] > A[i][k] + A[k][j] for any k, the triangle inequality is violated (output -1). If A[i][j] == A[i][k] + A[k][j] for some k != i, j, edge (i, j) is redundant and can be omitted. Otherwise, edge (i, j) is strictly required.
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> A(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> A[i][j];
        }
    }

    // Check triangle inequality
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (A[i][j] > A[i][k] + A[k][j]) {
                    cout << -1 << "\n";
                    return 0;
                }
            }
        }
    }

    long long total_weight = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            bool redundant = false;
            for (int k = 0; k < n; ++k) {
                if (k != i && k != j) {
                    if (A[i][j] == A[i][k] + A[k][j]) {
                        redundant = true;
                        break;
                    }
                }
            }
            if (!redundant) {
                total_weight += A[i][j];
            }
        }
    }

    cout << total_weight << "\n";
    return 0;
}
```
