# Problem Analysis: AtCoder-abc023_c — 収集王

**Problem ID**: `AtCoder-abc023_c`  
**Contest**: `abc023`  
**Rating / Difficulty**: 1752  
**URL**: https://atcoder.jp/contests/abc023/tasks/abc023_c  
**VJudge Tag**: `[problem:AtCoder-abc023_c]`  
**Category File**: [`../categories/basics/row_col_frequency_sparse_adjustment.md`](../categories/basics/row_col_frequency_sparse_adjustment.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Frequency Counting`  
- **Topic (Skill)**: `Row/Column Candy Count with Sparse Cell Adjustment`  

---

## 1. Problem Statement & Key Idea
An R x C grid has N candies at coordinates (r_i, c_i). Find the number of cells (r, c) such that the total candies in row r and column c equals K.

**Key Insight**: The total candies in cell (r, c)'s cross is row_cnt[r] + col_cnt[c] - (1 if candy at (r, c) else 0). Compute frequencies of candy counts across rows and columns. Initially assume independence: sum_{x=0}^K freq_row[x] * freq_col[K - x]. Then adjust for cells with candies.

## 2. Core Observation & Invariant
Iterate over all N candies: if row_cnt[r_i] + col_cnt[c_i] == K, decrement count by 1 (it was counted but actually has sum K - 1). If row_cnt[r_i] + col_cnt[c_i] == K + 1, increment count by 1 (its adjusted sum is K).

## 3. Step-by-Step Algorithm
1. Compute row_cnt[r] and col_cnt[c] for all rows and columns.
2. Build freq_row[x] and freq_col[y].
3. Initial answer ans = sum_{x=0}^K freq_row[x] * freq_col[K - x].
4. For each candy at (r_i, c_i):
5.   sum_cross = row_cnt[r_i] + col_cnt[c_i].
6.   if sum_cross == K: ans -= 1.
7.   if sum_cross == K + 1: ans += 1.
8. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(R + C + N)`
- **Space Complexity**: `O(R + C + N)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Independent 2D projection frequency multiplication followed by sparse point adjustments.
- **Reusable Pattern**: `Row/Column Independent Frequency: freq_r * freq_c minus sparse intersection correction.`
