# Basic Constructive Algorithms

**Domain**: `Basics`  
**Subtopic**: `Greedy and Constructive`  

This workbook contains curated, high-quality competitive programming problems teaching **Basic Constructive Algorithms**.

---

## Curated Problems

### `[problem:AtCoder-arc183_b]` — Near Assignment
- **Rating / Difficulty**: 2118
- **Contest**: `arc183`
- **Analysis**: [`analysis/AtCoder-arc183_b.md`](../../analysis/AtCoder-arc183_b.md)
- **Key Idea**: If A == B, answer is trivially Yes. Otherwise, every value in B must exist in A (values cannot be created from nothing). Furthermore, since an assignment A_i = A_j overwrites a value, values can only replicate without losing variety if B contains at least one duplicate pair within distance K (i.e. exists i < j with B_i = B_j and j - i <= K). If no such nearby duplicate exists in B, every window of length K+1 has strictly distinct elements, making it impossible to perform any overwrite without permanently extinguishing a necessary value.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> a(n), b(n);
    vector<bool> in_a(n + 1, false);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        in_a[a[i]] = true;
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }

    if (a == b) {
        cout << "Yes\n";
        return;
    }

    for (int i = 0; i < n; ++i) {
        if (!in_a[b[i]]) {
            cout << "No\n";
            return;
        }
    }

    vector<int> last_pos(n + 1, -1);
    bool has_near_dup = false;
    for (int i = 0; i < n; ++i) {
        if (last_pos[b[i]] != -1 && i - last_pos[b[i]] <= k) {
            has_near_dup = true;
            break;
        }
        last_pos[b[i]] = i;
    }

    if (has_near_dup) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```
