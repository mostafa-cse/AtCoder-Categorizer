# Time-Space Diagonal Projection (S_i - X_i) Sweep-Line with Active Multiset

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Sweep-Line / Multiset`  

This workbook contains curated, high-quality competitive programming problems teaching **Time-Space Diagonal Projection (S_i - X_i) Sweep-Line with Active Multiset**.

---

## Curated Problems

### `[problem:AtCoder-abc128_e]` — Roadwork
- **Rating / Difficulty**: 1840
- **Contest**: `abc128`
- **Analysis**: [`analysis/AtCoder-abc128_e.md`](../../analysis/AtCoder-abc128_e.md)
- **Key Idea**: A person departing at time D reaches position X at time D + X. They are blocked by roadwork i iff S_i <= D + X_i < T_i, which rearranges to S_i - X_i <= D < T_i - X_i. Thus, roadwork i acts on departure times in interval [S_i - X_i, T_i - X_i).
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N + Q)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

struct Event {
    long long time;
    int type; // +1 = add, 0 = query, -1 = remove
    long long val;
    int id;

    bool operator<(const Event& other) const {
        if (time != other.time) return time < other.time;
        return type > other.type; // process add (+1) before query (0) before remove (-1)
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<Event> events;

    for (int i = 0; i < n; ++i) {
        long long s, t, x;
        cin >> s >> t >> x;
        events.push_back({s - x, 1, x, -1});
        events.push_back({t - x, -1, x, -1});
    }

    for (int j = 0; j < q; ++j) {
        long long d;
        cin >> d;
        events.push_back({d, 0, 0, j});
    }

    sort(events.begin(), events.end());

    multiset<long long> active;
    vector<long long> ans(q);

    for (auto& ev : events) {
        if (ev.type == 1) {
            active.insert(ev.val);
        } else if (ev.type == -1) {
            active.erase(active.find(ev.val));
        } else {
            ans[ev.id] = active.empty() ? -1 : *active.begin();
        }
    }

    for (int j = 0; j < q; ++j) {
        cout << ans[j] << "\n";
    }

    return 0;
}
```
