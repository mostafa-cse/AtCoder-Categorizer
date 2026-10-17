# Binary Search on Answer with Feasibility Deadline Verification

**Domain**: `Basics`  
**Subtopic**: `Binary Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Binary Search on Answer with Feasibility Deadline Verification**.

---

## Curated Problems

### `[problem:AtCoder-abc023_d]` — 射撃王
- **Rating / Difficulty**: 1843
- **Contest**: `abc023`
- **Analysis**: [`analysis/AtCoder-abc023_d.md`](../../analysis/AtCoder-abc023_d.md)
- **Key Idea**: Binary search on maximum height X. For height X, balloon i must be shot at time t <= floor((X - H_i) / S_i). This defines an exact deadline for each balloon. The schedule is feasible iff the number of balloons with deadline <= t does not exceed t + 1 for all t.
- **Time Complexity**: `O(N log(max_ans))`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Balloon {
    long long h, s;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Balloon> b(n);
    long long max_h = 0;
    for (int i = 0; i < n; ++i) {
        cin >> b[i].h >> b[i].s;
        max_h = max(max_h, b[i].h + (long long)n * b[i].s);
    }

    auto is_feasible = [&](long long x) -> bool {
        vector<int> count_limit(n, 0);

        for (int i = 0; i < n; ++i) {
            if (x < b[i].h) return false;
            long long t = (x - b[i].h) / b[i].s;
            if (t < n - 1) count_limit[t]++;
            else count_limit[n - 1]++;
        }

        int cum = 0;
        for (int t = 0; t < n; ++t) {
            cum += count_limit[t];
            if (cum > t + 1) return false;
        }
        return true;
    };

    long long low = 1, high = max_h, ans = max_h;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (is_feasible(mid)) {
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
