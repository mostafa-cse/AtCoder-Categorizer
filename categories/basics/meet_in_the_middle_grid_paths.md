# Meet-in-the-Middle on 2D Grid Paths

**Domain**: `Basics`  
**Subtopic**: `Meet-in-the-Middle`  

This workbook contains curated, high-quality competitive programming problems teaching **Meet-in-the-Middle on 2D Grid Paths**.

---

## Curated Problems

### `[problem:AtCoder-abc271_f]` — XOR on Grid Path
- **Rating / Difficulty**: 1669
- **Contest**: `abc271`
- **Analysis**: [`analysis/AtCoder-abc271_f.md`](../../analysis/AtCoder-abc271_f.md)
- **Key Idea**: The total path length is 2N - 1, meaning 2^(2N-2) paths (up to 2^38, impossible). Meet in the middle at the anti-diagonal r + c = N - 1 (paths of length N - 1 from (0, 0) and length N - 1 from (N-1, N-1)).
- **Time Complexity**: `O(2^(N-1) log(2^(N-1)))`
- **Space Complexity**: `O(N * 2^(N-1))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int n;
long long a[22][22];
map<long long, int> freq[22];
long long total_ans = 0;

void dfs_forward(int r, int c, long long cur_xor) {
    if (r + c == n - 1) {
        freq[r][cur_xor]++;
        return;
    }
    if (r + 1 < n) dfs_forward(r + 1, c, cur_xor ^ a[r + 1][c]);
    if (c + 1 < n) dfs_forward(r, c + 1, cur_xor ^ a[r][c + 1]);
}

void dfs_backward(int r, int c, long long cur_xor) {
    if (r + c == n - 1) {
        // Exclude a[r][c] since it was already included in forward path
        long long target = cur_xor ^ a[r][c];
        auto it = freq[r].find(target);
        if (it != freq[r].end()) {
            total_ans += it->second;
        }
        return;
    }
    if (r - 1 >= 0) dfs_backward(r - 1, c, cur_xor ^ a[r - 1][c]);
    if (c - 1 >= 0) dfs_backward(r, c - 1, cur_xor ^ a[r][c - 1]);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    for (int r = 0; r < n; ++r) {
        for (int c = 0; c < n; ++c) {
            cin >> a[r][c];
        }
    }

    dfs_forward(0, 0, a[0][0]);
    dfs_backward(n - 1, n - 1, a[n - 1][n - 1]);

    cout << total_ans << "\n";
    return 0;
}
```
