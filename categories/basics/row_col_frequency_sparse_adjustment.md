# Row/Column Candy Count with Sparse Cell Adjustment

**Domain**: `Basics`  
**Subtopic**: `Frequency Counting`  

This workbook contains curated, high-quality competitive programming problems teaching **Row/Column Candy Count with Sparse Cell Adjustment**.

---

## Curated Problems

### `[problem:AtCoder-abc023_c]` — 収集王
- **Rating / Difficulty**: 1752
- **Contest**: `abc023`
- **Analysis**: [`analysis/AtCoder-abc023_c.md`](../../analysis/AtCoder-abc023_c.md)
- **Key Idea**: The total candies in cell (r, c)'s cross is row_cnt[r] + col_cnt[c] - (1 if candy at (r, c) else 0). Compute frequencies of candy counts across rows and columns. Initially assume independence: sum_{x=0}^K freq_row[x] * freq_col[K - x]. Then adjust for cells with candies.
- **Time Complexity**: `O(R + C + N)`
- **Space Complexity**: `O(R + C + N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Candy {
    int r, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, K;
    if (!(cin >> R >> C >> K)) return 0;

    int n;
    cin >> n;

    vector<Candy> candies(n);
    vector<int> row_cnt(R + 1, 0);
    vector<int> col_cnt(C + 1, 0);

    for (int i = 0; i < n; ++i) {
        cin >> candies[i].r >> candies[i].c;
        row_cnt[candies[i].r]++;
        col_cnt[candies[i].c]++;
    }

    vector<int> freq_r(n + 1, 0);
    vector<int> freq_c(n + 1, 0);

    for (int r = 1; r <= R; ++r) {
        if (row_cnt[r] <= n) freq_r[row_cnt[r]]++;
    }
    for (int c = 1; c <= C; ++c) {
        if (col_cnt[c] <= n) freq_c[col_cnt[c]]++;
    }

    long long ans = 0;
    for (int x = 0; x <= K; ++x) {
        int y = K - x;
        if (x <= n && y <= n) {
            ans += (long long)freq_r[x] * freq_c[y];
        }
    }

    for (int i = 0; i < n; ++i) {
        int sum_val = row_cnt[candies[i].r] + col_cnt[candies[i].c];
        if (sum_val == K) ans--;
        if (sum_val == K + 1) ans++;
    }

    cout << ans << "\n";
    return 0;
}
```
