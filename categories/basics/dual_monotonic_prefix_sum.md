# Dual Monotonic Prefix Sum Optimization

**Domain**: `Basics`  
**Subtopic**: `Two Pointers`  

This workbook contains curated, high-quality competitive programming problems teaching **Dual Monotonic Prefix Sum Optimization**.

---

## Curated Problems

### [problem:AtCoder-abc172_c] — Tsundoku
- **Contest**: `abc172`
- **Rating / Difficulty**: 930
- **Specific Skill**: Dual Monotonic Prefix Sum Optimization
- **Individual Analysis**: [`../../analysis/AtCoder-abc172_c.md`](../../analysis/AtCoder-abc172_c.md)
- **Problem Statement Summary**: Two desks have N books (times A_1..A_N) and M books (times B_1..B_M). Find the maximum number of books you can read from the tops of desks in total time <= K.
- **Core Insight**: Because reading times are positive, prefA and prefB are strictly increasing. As i increases, the maximum valid number of books j taken from desk B is monotonically non-increasing. We can maintain j using two pointers in O(N + M).
- **Complexity**: Time: `O(N + M)` | Space: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> a(n), b(m);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < m; ++i) cin >> b[i];

    vector<long long> pa(n + 1, 0), pb(m + 1, 0);
    for (int i = 0; i < n; ++i) pa[i + 1] = pa[i] + a[i];
    for (int i = 0; i < m; ++i) pb[i + 1] = pb[i] + b[i];

    int max_books = 0;
    int j = m;

    for (int i = 0; i <= n; ++i) {
        if (pa[i] > k) break;
        while (j >= 0 && pa[i] + pb[j] > k) {
            j--;
        }
        if (j >= 0) {
            max_books = max(max_books, i + j);
        }
    }

    cout << max_books << "\n";
    return 0;
}
```
