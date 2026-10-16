# Minimum Card Insertions = N - LIS(A) via Patience Sorting

**Domain**: `Dynamic Programming`  
**Subtopic**: `Longest Increasing Subsequence (LIS)`  

This workbook contains curated, high-quality competitive programming problems teaching **Minimum Card Insertions = N - LIS(A) via Patience Sorting**.

---

## Curated Problems

### `[problem:AtCoder-abc006_4]` — Playing Cards Insertion Sort
- **Rating / Difficulty**: 1696
- **Contest**: `abc006`
- **Analysis**: [`analysis/AtCoder-abc006_4.md`](../../analysis/AtCoder-abc006_4.md)
- **Key Idea**: Any card that is NOT moved must maintain its relative order with other unmoved cards, meaning the unmoved cards must form an increasing subsequence. To minimize moved cards, maximize unmoved cards: min operations = N - LIS(A).
- **Time Complexity**: `O(N log N)`
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

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> tails;
    for (int x : a) {
        auto it = lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) {
            tails.push_back(x);
        } else {
            *it = x;
        }
    }

    cout << n - tails.size() << "\n";
    return 0;
}
```
