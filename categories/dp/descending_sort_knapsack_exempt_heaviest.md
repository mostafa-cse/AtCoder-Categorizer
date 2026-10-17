# Descending Sort Relaxation on Knapsack Boundary (Exempt Heaviest Item)

**Domain**: `Dynamic Programming`  
**Subtopic**: `Knapsack DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Descending Sort Relaxation on Knapsack Boundary (Exempt Heaviest Item)**.

---

## Curated Problems

### `[problem:AtCoder-arc042_c]` — おやつ
- **Rating / Difficulty**: 1746
- **Contest**: `arc042`
- **Analysis**: [`analysis/AtCoder-arc042_c.md`](../../analysis/AtCoder-arc042_c.md)
- **Key Idea**: Sort snacks by weight descending: a_1 >= a_2 >= ... >= a_N. If snack i is the heaviest item in the chosen subset, all other chosen snacks must come from {i+1, ..., N} and their sum of weights must be <= L.
- **Time Complexity**: `O(N * L)`
- **Space Complexity**: `O(L)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Item {
    int a, b;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, l;
    if (!(cin >> n >> l)) return 0;

    vector<Item> items(n);
    for (int i = 0; i < n; ++i) {
        cin >> items[i].a >> items[i].b;
    }

    sort(items.begin(), items.end(), [](const Item& x, const Item& y) {
        return x.a > y.a;
    });

    vector<int> dp(l + 1, 0);
    int max_ans = 0;

    for (int i = 0; i < n; ++i) {
        int best_prev = 0;
        for (int w = 0; w <= l; ++w) {
            best_prev = max(best_prev, dp[w]);
        }
        max_ans = max(max_ans, items[i].b + best_prev);

        for (int w = l; w >= items[i].a; --w) {
            dp[w] = max(dp[w], dp[w - items[i].a] + items[i].b);
        }
    }

    cout << max_ans << "\n";
    return 0;
}
```
