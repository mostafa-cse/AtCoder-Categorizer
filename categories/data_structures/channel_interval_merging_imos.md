# Channel Interval Merging with Imos Difference Array

**Domain**: `Data Structures`  
**Subtopic**: `Difference Arrays`  

This workbook contains curated, high-quality competitive programming problems teaching **Channel Interval Merging with Imos Difference Array**.

---

## Curated Problems

### [problem:AtCoder-abc080_d] — Recording
- **Contest**: `abc080`
- **Rating / Difficulty**: 1383
- **Specific Skill**: Channel Interval Merging with Imos Difference Array
- **Individual Analysis**: [`../../analysis/AtCoder-abc080_d.md`](../../analysis/AtCoder-abc080_d.md)
- **Problem Statement Summary**: N TV programs across C channels. Program i on channel c_i runs from s_i to t_i. A recorder must prepare 0.5s before a show (from s_i - 0.5 to t_i) unless recording consecutive shows on the SAME channel. Find minimum recorders needed.
- **Core Insight**: First, for each channel independently, merge all adjacent intervals that touch (t_prev == s_next). Second, each merged interval requires a recorder from (start - 0.5) to end (scale times by 2 to integers: 2*s - 1 to 2*t). Apply standard 1D imos difference array over all merged intervals: find the maximum concurrent overlapping intervals.
- **Complexity**: Time: `O(MAX_TIME + N log N)` | Space: `O(MAX_TIME)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXT = 200005;

struct Show {
    int s, t;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, C;
    if (!(cin >> n >> C)) return 0;

    vector<vector<Show>> by_channel(C + 1);
    for (int i = 0; i < n; ++i) {
        int s, t, c;
        cin >> s >> t >> c;
        by_channel[c].push_back({s, t});
    }

    vector<int> diff(MAXT + 5, 0);

    for (int c = 1; c <= C; ++c) {
        if (by_channel[c].empty()) continue;
        sort(by_channel[c].begin(), by_channel[c].end(), [](const Show& a, const Show& b) {
            return a.s < b.s;
        });

        vector<Show> merged;
        merged.push_back(by_channel[c][0]);

        for (size_t i = 1; i < by_channel[c].size(); ++i) {
            if (by_channel[c][i].s == merged.back().t) {
                merged.back().t = by_channel[c][i].t;
            } else {
                merged.push_back(by_channel[c][i]);
            }
        }

        for (const auto& show : merged) {
            int start_scaled = 2 * show.s - 1;
            int end_scaled = 2 * show.t;
            diff[start_scaled]++;
            diff[end_scaled]--;
        }
    }

    int max_recorders = 0;
    int cur = 0;
    for (int t = 0; t <= MAXT; ++t) {
        cur += diff[t];
        max_recorders = max(max_recorders, cur);
    }

    cout << max_recorders << "\n";
    return 0;
}
```
