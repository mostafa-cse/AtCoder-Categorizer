# Block Simulation and Invariant Reversal

**Domain**: `Miscellaneous`  
**Subtopic**: `Ad-Hoc / Simulation`  

This workbook contains curated, high-quality competitive programming problems teaching **Block Simulation and Invariant Reversal**.

---

## Curated Problems

### `[problem:AtCoder-abc253_g]` — Swap Many Times
- **Rating / Difficulty**: 2051
- **Contest**: `abc253`
- **Analysis**: [`analysis/AtCoder-abc253_g.md`](../../analysis/AtCoder-abc253_g.md)
- **Key Idea**: The swaps are naturally partitioned into N-1 blocks, where block i contains N-i swaps: (i, i+1), ..., (i, N). We locate the block bL containing swap L and the block bR containing swap R. If bL == bR, we simulate the <= N swaps directly. If bL < bR, we simulate the partial suffix of block bL (<= N swaps), then apply an O(N) structural invariant for all full intermediate blocks i in [bL + 1, bR - 1]: executing all swaps for k consecutive full blocks i1 through i2 takes the last k elements P[N-k+1..N], reverses them, and places them at P[i1..i1+k-1], while shifting the remaining intermediate elements to the right. Finally, we simulate the partial prefix of block bR (<= N swaps).
- **Time Complexity**: `O(N)`
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

    long long n, l, r;
    if (!(cin >> n >> l >> r)) return 0;

    vector<int> a(n + 1);
    iota(a.begin(), a.end(), 0);

    long long cur = 0;
    int bL = -1, posL = -1;
    int bR = -1, posR = -1;

    for (int i = 1; i < n; ++i) {
        long long sz = n - i;
        if (bL == -1 && cur + sz >= l) {
            bL = i;
            posL = i + (l - cur);
        }
        if (bR == -1 && cur + sz >= r) {
            bR = i;
            posR = i + (r - cur);
        }
        cur += sz;
    }

    if (bL == bR) {
        for (int j = posL; j <= posR; ++j) {
            swap(a[bL], a[j]);
        }
    } else {
        for (int j = posL; j <= n; ++j) {
            swap(a[bL], a[j]);
        }
        int i1 = bL + 1, i2 = bR - 1;
        if (i1 <= i2) {
            int k = i2 - i1 + 1;
            vector<int> last_k(a.begin() + (n - k + 1), a.begin() + (n + 1));
            reverse(last_k.begin(), last_k.end());
            vector<int> mid(a.begin() + i1, a.begin() + (n - k + 1));
            for (int t = 0; t < k; ++t) a[i1 + t] = last_k[t];
            for (int t = 0; t < (int)mid.size(); ++t) a[i1 + k + t] = mid[t];
        }
        for (int j = bR + 1; j <= posR; ++j) {
            swap(a[bR], a[j]);
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << a[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
