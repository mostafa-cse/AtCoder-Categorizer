# Functional Graph Cycle Detection with Large K (K up to 10^100000)

**Domain**: `Basics`  
**Subtopic**: `Functional Graphs`  

This workbook contains curated, high-quality competitive programming problems teaching **Functional Graph Cycle Detection with Large K (K up to 10^100000)**.

---

## Curated Problems

### `[problem:AtCoder-abc030_d]` — Strange Dictionary
- **Rating / Difficulty**: 1586
- **Contest**: `abc030`
- **Analysis**: [`analysis/AtCoder-abc030_d.md`](../../analysis/AtCoder-abc030_d.md)
- **Key Idea**: The path from a eventually enters a cycle of length L_cycle after a tail of length L_tail <= N. If K <= L_tail, simulate directly. Otherwise, compute (K - L_tail) % L_cycle using big-integer modular reduction and take that many steps along the cycle.
- **Time Complexity**: `O(N + |K|)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a;
    string K_str;
    if (!(cin >> n >> a >> K_str)) return 0;

    vector<int> b(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> b[i];
    }

    vector<int> path;
    vector<int> step_at(n + 1, -1);

    int curr = a;
    int step = 0;

    while (step_at[curr] == -1) {
        step_at[curr] = step++;
        path.push_back(curr);
        curr = b[curr];
    }

    int tail_len = step_at[curr];
    int cycle_len = step - tail_len;

    // Check if K fits in simple integer <= tail_len
    if (K_str.size() <= 7) {
        long long k_val = stoll(K_str);
        if (k_val <= tail_len) {
            cout << path[k_val] << "\n";
            return 0;
        }
    }

    // Compute (K - tail_len) % cycle_len
    long long rem = 0;
    for (char c : K_str) {
        rem = (rem * 10 + (c - '0')) % cycle_len;
    }

    rem = (rem - (tail_len % cycle_len) + cycle_len) % cycle_len;

    int ans = path[tail_len + rem];
    cout << ans << "\n";
    return 0;
}
```
