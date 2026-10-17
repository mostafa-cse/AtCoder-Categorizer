# Monotonic Stack with Frequency/Last-Occurrence Tracking for Lexicographically Minimal Permutation

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Monotonic Queue / Deque`  

This workbook contains curated, high-quality competitive programming problems teaching **Monotonic Stack with Frequency/Last-Occurrence Tracking for Lexicographically Minimal Permutation**.

---

## Curated Problems

### `[problem:AtCoder-abc299_g]` — Minimum Permutation
- **Rating / Difficulty**: 2066
- **Contest**: `abc299`
- **Analysis**: [`analysis/AtCoder-abc299_g.md`](../../analysis/AtCoder-abc299_g.md)
- **Key Idea**: We use a monotonic stack and track the last occurrence index last_pos[x] of each value. When processing A[i] = x: if x is already in the stack, we skip it. Otherwise, while the stack is non-empty, top element y > x, and y appears again later in A (last_pos[y] > i), we pop y from the stack and unmark it. We then push x and mark it. The resulting stack contains the unique lexicographically smallest permutation.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(n);
    vector<int> last_pos(m + 1, -1);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        last_pos[a[i]] = i;
    }

    vector<int> st;
    vector<bool> in_st(m + 1, false);

    for (int i = 0; i < n; ++i) {
        int x = a[i];
        if (in_st[x]) continue;

        while (!st.empty() && st.back() > x && last_pos[st.back()] > i) {
            in_st[st.back()] = false;
            st.pop_back();
        }

        st.push_back(x);
        in_st[x] = true;
    }

    for (int i = 0; i < m; ++i) {
        cout << st[i] << (i == m - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
