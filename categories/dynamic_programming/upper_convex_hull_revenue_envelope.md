# Convex Hull Trick (CHT) and Dynamic CHT

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Convex Hull Trick (CHT)`  

This workbook contains curated, high-quality competitive programming problems teaching **Convex Hull Trick (CHT) and Dynamic CHT**.

---

## Curated Problems

### `[problem:AtCoder-abc289_g]` — Shopping in AtCoder store
- **Rating / Difficulty**: 2109
- **Contest**: `abc289`
- **Analysis**: [`analysis/AtCoder-abc289_g.md`](../../analysis/AtCoder-abc289_g.md)
- **Key Idea**: Sort base valuations descending: B_1 >= B_2 >= ... >= B_N. If you target selling to the top i customers, the optimal price is P = B_i + C_j, yielding total revenue i * (B_i + C_j) = i * C_j + i * B_i. This is a linear function of C_j with slope m_i = i and y-intercept c_i = i * B_i. Finding the maximum revenue over all i in [1, N] for each query C_j is the upper convex hull envelope of lines with strictly increasing slopes, solved via the classic Convex Hull Trick.
- **Time Complexity**: `O(N log N + M log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Line {
    long long m, c;
    long long eval(long long x) const {
        return m * x + c;
    }
};

bool is_redundant(const Line& l1, const Line& l2, const Line& l3) {
    return (__int128)(l1.c - l2.c) * (l3.m - l2.m) <= (__int128)(l2.c - l3.c) * (l2.m - l1.m);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> b(n);
    for (int i = 0; i < n; ++i) cin >> b[i];

    sort(b.rbegin(), b.rend());

    vector<Line> hull;
    for (int i = 1; i <= n; ++i) {
        Line cur = { (long long)i, (long long)i * b[i - 1] };
        while (hull.size() >= 2 && is_redundant(hull[hull.size() - 2], hull.back(), cur)) {
            hull.pop_back();
        }
        hull.push_back(cur);
    }

    for (int j = 0; j < m; ++j) {
        long long c;
        cin >> c;

        int low = 0, high = (int)hull.size() - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (hull[mid].eval(c) < hull[mid + 1].eval(c)) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        cout << hull[low].eval(c) << (j + 1 == m ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
