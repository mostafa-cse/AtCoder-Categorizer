# Coordinate-Compressed Event Sweep / Imos Method

**Domain**: `Data Structures`  
**Subtopic**: `Difference Arrays`  

This workbook contains curated, high-quality competitive programming problems teaching **Coordinate-Compressed Event Sweep / Imos Method**.

---

## Curated Problems

### [problem:AtCoder-abc188_d] — Snuke Prime
- **Contest**: `abc188`
- **Rating / Difficulty**: 933
- **Specific Skill**: Coordinate-Compressed Event Sweep / Imos Method
- **Individual Analysis**: [`../../analysis/AtCoder-abc188_d.md`](../../analysis/AtCoder-abc188_d.md)
- **Problem Statement Summary**: N services are used from day a_i to b_i at cost c_i/day. A subscription to Snuke Prime costs C/day and covers all services. Find the minimum total cost across all days (a_i, b_i <= 10^9).
- **Core Insight**: Record difference events: +c_i at day a_i, and -c_i at day b_i + 1. Sort all distinct event days. For the interval [day_j, day_{j+1} - 1], the length is day_{j+1} - day_j and the daily cost is min(current_cost, C).
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long big_c;
    if (!(cin >> n >> big_c)) return 0;

    map<long long, long long> events;
    for (int i = 0; i < n; ++i) {
        long long a, b, c;
        cin >> a >> b >> c;
        events[a] += c;
        events[b + 1] -= c;
    }

    long long total_cost = 0;
    long long current_cost = 0;
    long long prev_day = 0;

    for (const auto& [day, delta] : events) {
        if (prev_day != 0) {
            total_cost += (day - prev_day) * min(current_cost, big_c);
        }
        current_cost += delta;
        prev_day = day;
    }

    cout << total_cost << "\n";
    return 0;
}
```
