# Problem Analysis: AtCoder-abc080_d — Recording

**Problem ID**: `AtCoder-abc080_d`  
**Contest**: `abc080`  
**Rating / Difficulty**: 1383  
**URL**: https://atcoder.jp/contests/abc080/tasks/abc080_d  
**VJudge Tag**: `[problem:AtCoder-abc080_d]`  
**Category File**: [`../categories/data_structures/channel_interval_merging_imos.md`](../categories/data_structures/channel_interval_merging_imos.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Difference Arrays`  
- **Topic (Skill)**: `Channel Interval Merging with Imos Difference Array`  

---

## 1. Problem Statement & Key Idea
N TV programs across C channels. Program i on channel c_i runs from s_i to t_i. A recorder must prepare 0.5s before a show (from s_i - 0.5 to t_i) unless recording consecutive shows on the SAME channel. Find minimum recorders needed.

**Key Idea**: For the same channel, any contiguous or touching recording intervals [s_1, t_1] and [t_1, t_2] can share the same recorder without re-preparing.

## 2. Core Observation & Invariant
First, for each channel independently, merge all adjacent intervals that touch (t_prev == s_next). Second, each merged interval requires a recorder from (start - 0.5) to end (scale times by 2 to integers: 2*s - 1 to 2*t). Apply standard 1D imos difference array over all merged intervals: find the maximum concurrent overlapping intervals.

## 3. Step-by-Step Algorithm
1. Group intervals by channel c.
2. For each channel: sort intervals and merge touching intervals [s1, t1] and [t1, t2].
3. For each merged interval: add +1 at 2*s - 1, and -1 at 2*t in imos array.
4. Prefix sum imos array, output maximum value.

## 4. Complexity Analysis
- **Time Complexity**: `O(MAX_TIME + N log N)`
- **Space Complexity**: `O(MAX_TIME)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Pre-merging intra-channel intervals before applying multi-channel imos sweeping.
- **Reusable Pattern**: `Intra-category interval merge -> global imos difference array concurrency.`
