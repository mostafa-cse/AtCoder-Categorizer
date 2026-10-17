# Raney's Lemma / Circular Prefix Balance on 2-Player Game

**Domain**: `Game Theory`  
**Subtopic**: `Raney's Lemma / Cyclic Shifts`  

This workbook contains curated, high-quality competitive programming problems teaching **Raney's Lemma / Circular Prefix Balance on 2-Player Game**.

---

## Curated Problems

### `[problem:AtCoder-arc138_c]` — Rotate and Play Game
- **Rating / Difficulty**: 1728
- **Contest**: `arc138`
- **Analysis**: [`analysis/AtCoder-arc138_c.md`](../../analysis/AtCoder-arc138_c.md)
- **Key Idea**: Assign +1 to the N/2 largest elements of A and -1 to the N/2 smallest elements. By Raney's Lemma, there is a cyclic shift where every prefix sum is strictly positive (or non-negative), allowing Takahashi to guarantee obtaining all N/2 largest elements.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, int>> a(n);
    long long total_top = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i].first;
        a[i].second = i;
    }

    sort(a.rbegin(), a.rend());

    vector<int> b(n, -1);
    for (int i = 0; i < n / 2; ++i) {
        b[a[i].second] = 1;
        total_top += a[i].first;
    }

    int min_pref = 0;
    int min_idx = -1;
    int cur_pref = 0;

    for (int i = 0; i < n; ++i) {
        cur_pref += b[i];
        if (cur_pref < min_pref) {
            min_pref = cur_pref;
            min_idx = i;
        }
    }

    int k = (min_idx + 1) % n;
    cout << k << " " << total_top << "\n";
    return 0;
}
```
