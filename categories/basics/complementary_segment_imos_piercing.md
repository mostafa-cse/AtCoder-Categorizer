# Complementary Segment Imos / Minimum Cost Interval Piercing

**Domain**: `Basics`  
**Subtopic**: `Prefix Sums`  

This workbook contains curated, high-quality competitive programming problems teaching **Complementary Segment Imos / Minimum Cost Interval Piercing**.

---

## Curated Problems

### `[problem:AtCoder-abc017_3]` — High Score
- **Rating / Difficulty**: 1607
- **Contest**: `abc017`
- **Analysis**: [`analysis/AtCoder-abc017_3.md`](../../analysis/AtCoder-abc017_3.md)
- **Key Idea**: Invert the condition: pick which single jewel type j in 1..M is omitted. Any ruin containing jewel j cannot be used. We want to minimize the score of ruins containing jewel j.
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(M)`
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
    if (!(cin >> n >> m)) return 0;

    vector<long long> diff(m + 2, 0);
    long long total_score = 0;

    for (int i = 0; i < n; ++i) {
        int l, r;
        long long s;
        cin >> l >> r >> s;
        total_score += s;
        diff[l] += s;
        diff[r + 1] -= s;
    }

    long long cur_loss = 0;
    long long min_loss = 2e18;

    for (int j = 1; j <= m; ++j) {
        cur_loss += diff[j];
        min_loss = min(min_loss, cur_loss);
    }

    cout << total_score - min_loss << "\n";
    return 0;
}
```
