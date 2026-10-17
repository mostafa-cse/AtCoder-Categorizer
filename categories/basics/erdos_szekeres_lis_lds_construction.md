# Erdős–Szekeres Extremal Permutation Construction (LIS = A, LDS = B)

**Domain**: `Basics`  
**Subtopic**: `Constructive`  

This workbook contains curated, high-quality competitive programming problems teaching **Erdős–Szekeres Extremal Permutation Construction (LIS = A, LDS = B)**.

---

## Curated Problems

### `[problem:AtCoder-arc091_c]` — LISDL
- **Rating / Difficulty**: 1889
- **Contest**: `arc091`
- **Analysis**: [`analysis/AtCoder-arc091_c.md`](../../analysis/AtCoder-arc091_c.md)
- **Key Idea**: By the Erdős–Szekeres theorem, a valid permutation exists iff A + B <= N + 1 and A * B >= N. If valid, decompose N into A blocks of sizes s_1..s_A where 1 <= s_i <= B and sum s_i = N. Within each block, write numbers in descending order; arrange blocks in ascending order.
- **Time Complexity**: `O(N)`
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

    long long n, a, b;
    if (!(cin >> n >> a >> b)) return 0;

    if (a + b > n + 1 || a * b < n) {
        cout << -1 << "\n";
        return 0;
    }

    vector<int> block_sizes(a, 1);
    block_sizes[0] = b;
    long long rem = n - (b + a - 1);

    for (int i = 1; i < a && rem > 0; ++i) {
        int add = min(rem, b - 1);
        block_sizes[i] += add;
        rem -= add;
    }

    vector<int> ans;
    int cur_val = 1;

    for (int sz : block_sizes) {
        vector<int> blk;
        for (int i = 0; i < sz; ++i) {
            blk.push_back(cur_val++);
        }
        reverse(blk.begin(), blk.end());
        for (int x : blk) ans.push_back(x);
    }

    for (int i = 0; i < n; ++i) {
        cout << ans[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
