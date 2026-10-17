# Velocity Profile Chmin Envelope via Bidirectional Relaxation on Doubled Grid

**Domain**: `Basics`  
**Subtopic**: `Continuous Optimization`  

This workbook contains curated, high-quality competitive programming problems teaching **Velocity Profile Chmin Envelope via Bidirectional Relaxation on Doubled Grid**.

---

## Curated Problems

### `[problem:AtCoder-abc076_d]` — AtCoder Express
- **Rating / Difficulty**: 1884
- **Contest**: `abc076`
- **Analysis**: [`analysis/AtCoder-abc076_d.md`](../../analysis/AtCoder-abc076_d.md)
- **Key Idea**: Discretize time into 0.5-second steps by doubling all times and speeds (t -> 2t, v -> 2v). The velocity profile v(t) must satisfy: (1) section speed limits, (2) start and end at 0, (3) v(t + 1) <= v(t) + 1, (4) v(t) <= v(t + 1) + 1. Initialize max allowable speed at each grid point and apply forward and backward chmin relaxation.
- **Time Complexity**: `O(sum t_i)`
- **Space Complexity**: `O(sum t_i)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> t(n), v(n);
    int total_t = 0;
    for (int i = 0; i < n; ++i) {
        cin >> t[i];
        total_t += t[i];
    }
    for (int i = 0; i < n; ++i) cin >> v[i];

    int steps = 2 * total_t;
    vector<double> max_v(steps + 1, 1e9);

    int cur_time = 0;
    for (int i = 0; i < n; ++i) {
        for (int step = cur_time; step <= cur_time + 2 * t[i]; ++step) {
            max_v[step] = min(max_v[step], (double)v[i]);
        }
        cur_time += 2 * t[i];
    }

    max_v[0] = 0;
    max_v[steps] = 0;

    // Forward pass
    for (int step = 1; step <= steps; ++step) {
        max_v[step] = min(max_v[step], max_v[step - 1] + 0.5);
    }

    // Backward pass
    for (int step = steps - 1; step >= 0; --step) {
        max_v[step] = min(max_v[step], max_v[step + 1] + 0.5);
    }

    double distance = 0;
    for (int step = 0; step < steps; ++step) {
        distance += (max_v[step] + max_v[step + 1]) * 0.5 * 0.5;
    }

    cout << fixed << setprecision(12) << distance << "\n";
    return 0;
}
```
