# DP on Trees and DAGs

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Dp on Different Structures`  

This workbook contains curated, high-quality competitive programming problems teaching **DP on Trees and DAGs**.

---

## Curated Problems

### `[problem:AtCoder-abc368_e]` — Train Delay
- **Rating / Difficulty**: 2140
- **Contest**: `abc368`
- **Analysis**: [`analysis/AtCoder-abc368_e.md`](../../analysis/AtCoder-abc368_e.md)
- **Key Idea**: The connection condition is S_j + X_j >= max_{i: B_i = A_j, T_i <= S_j} (T_i + X_i). This is a longest-path DP on a DAG of train events. Sorting all departures and arrivals chronologically, each station maintains latest_arrival[city] = max (T_i + X_i). When train j departs city A_j at time S_j, its required delay is max(0, latest_arrival[A_j] - S_j). Upon arrival at B_j, it updates latest_arrival[B_j].
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Train {
    int id;
    int a, b;
    long long s, t;
};

struct Event {
    long long time;
    int type;
    int train_id;

    bool operator<(const Event& o) const {
        if (time != o.time) return time < o.time;
        return type < o.type;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long x1;
    if (!(cin >> n >> m >> x1)) return 0;

    vector<Train> trains(m + 1);
    vector<Event> events;

    for (int i = 1; i <= m; ++i) {
        trains[i].id = i;
        cin >> trains[i].a >> trains[i].b >> trains[i].s >> trains[i].t;
        events.push_back({trains[i].s, 1, i});
        events.push_back({trains[i].t, 0, i});
    }

    sort(events.begin(), events.end());

    vector<long long> X(m + 1, 0);
    X[1] = x1;

    vector<long long> latest_arrival(n + 1, 0);

    for (auto& ev : events) {
        int tid = ev.train_id;
        if (ev.type == 1) {
            if (tid != 1) {
                int city = trains[tid].a;
                X[tid] = max(0LL, latest_arrival[city] - trains[tid].s);
            }
        } else {
            int city = trains[tid].b;
            latest_arrival[city] = max(latest_arrival[city], trains[tid].t + X[tid]);
        }
    }

    for (int i = 2; i <= m; ++i) {
        cout << X[i] << (i == m ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
