# Basic Greedy Algorithms

**Domain**: `Basics`  
**Subtopic**: `Greedy and Constructive`  

This workbook contains curated, high-quality competitive programming problems teaching **Basic Greedy Algorithms**.

---

## Curated Problems

### `[problem:AtCoder-aising2020_e]` — Camel Train
- **Rating / Difficulty**: 2133
- **Contest**: `aising2020`
- **Analysis**: [`analysis/AtCoder-aising2020_e.md`](../../analysis/AtCoder-aising2020_e.md)
- **Key Idea**: Every camel gives base happiness min(L_i, R_i). Camels with L_i > R_i provide an extra bonus L_i - R_i if placed by deadline K_i. Camels with R_i > L_i provide an extra bonus R_i - L_i if placed after K_i (which is equivalent to deadline N - K_i from the right). These two sets of camels can be scheduled independently. For each group, we iterate deadlines from 1 to N, maintaining a min-heap of accepted bonuses: if the heap size exceeds deadline k, we pop the smallest bonus (regret greedy).
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;

    long long base_ans = 0;
    vector<vector<long long>> left_camels(n + 1);
    vector<vector<long long>> right_camels(n + 1);

    for (int i = 0; i < n; ++i) {
        int k;
        long long l, r;
        cin >> k >> l >> r;
        base_ans += min(l, r);

        if (l > r) {
            left_camels[k].push_back(l - r);
        } else if (r > l) {
            int right_k = n - k;
            right_camels[right_k].push_back(r - l);
        }
    }

    priority_queue<long long, vector<long long>, greater<long long>> pq_l;
    for (int k = 1; k <= n; ++k) {
        for (long long diff : left_camels[k]) {
            pq_l.push(diff);
        }
        while ((int)pq_l.size() > k) {
            pq_l.pop();
        }
    }
    while (!pq_l.empty()) {
        base_ans += pq_l.top();
        pq_l.pop();
    }

    priority_queue<long long, vector<long long>, greater<long long>> pq_r;
    for (int k = 1; k <= n; ++k) {
        for (long long diff : right_camels[k]) {
            pq_r.push(diff);
        }
        while ((int)pq_r.size() > k) {
            pq_r.pop();
        }
    }
    while (!pq_r.empty()) {
        base_ans += pq_r.top();
        pq_r.pop();
    }

    cout << base_ans << "\n";
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
