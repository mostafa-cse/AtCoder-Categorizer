# Binary Search

**Domain**: `Basics`  
**Subtopic**: `Leveraging Monotonicity`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search**.

---

## Curated Problems

### `[problem:AtCoder-agc029_c]` — Lexicographic constraints
- **Rating / Difficulty**: 2103
- **Contest**: `agc029`
- **Analysis**: [`analysis/AtCoder-agc029_c.md`](../../analysis/AtCoder-agc029_c.md)
- **Key Idea**: Binary search on the alphabet size K. If A_1 < A_2 < ... < A_N is strictly increasing, K = 1 is trivially sufficient. For K >= 2, we can greedily make each string S_i the lexicographically smallest string strictly greater than S_{i-1} of length A_i. If A_i > A_{i-1}, we simply append '0's (implicit trailing zeros). If A_i <= A_{i-1}, we truncate the string to length A_i and increment it like a base-K integer at position A_i! Since lengths can be up to 10^9, we maintain non-zero digits using a stack of pairs (position, value in 1..K-1). If an increment carries past the first position, alphabet size K is impossible.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    bool non_decreasing = true;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (i > 0 && a[i] <= a[i - 1]) non_decreasing = false;
    }

    if (non_decreasing) {
        cout << 1 << "\n";
        return 0;
    }

    auto check = [&](int K) {
        vector<pair<int, int>> st;

        for (int i = 1; i < n; ++i) {
            if (a[i] > a[i - 1]) continue;

            while (!st.empty() && st.back().first > a[i]) {
                st.pop_back();
            }

            int pos = a[i];
            while (true) {
                if (pos == 0) return false;

                if (!st.empty() && st.back().first == pos) {
                    if (st.back().second + 1 < K) {
                        st.back().second++;
                        break;
                    } else {
                        st.pop_back();
                        pos--;
                    }
                } else {
                    st.push_back({pos, 1});
                    break;
                }
            }
        }
        return true;
    };

    int low = 2, high = n, ans = n;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```
