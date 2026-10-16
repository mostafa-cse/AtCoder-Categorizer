# Problem Analysis: AtCoder-abc188_d — Snuke Prime

**Problem ID**: `AtCoder-abc188_d`  
**Contest**: `abc188`  
**Rating / Difficulty**: 933  
**URL**: https://atcoder.jp/contests/abc188/tasks/abc188_d  
**VJudge Tag**: `[problem:AtCoder-abc188_d]`  
**Category File**: [`../categories/data_structures/coordinate_compressed_event_sweep.md`](../categories/data_structures/coordinate_compressed_event_sweep.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Difference Arrays`  
- **Topic (Skill)**: `Coordinate-Compressed Event Sweep / Imos Method`  

---

## 1. Problem Statement & Key Idea
N services are used from day a_i to b_i at cost c_i/day. A subscription to Snuke Prime costs C/day and covers all services. Find the minimum total cost across all days (a_i, b_i <= 10^9).

**Key Idea**: Daily service costs change only at boundary days a_i and b_i + 1. Between two consecutive event days, the total service cost per day is constant.

## 2. Core Observation & Invariant
Record difference events: +c_i at day a_i, and -c_i at day b_i + 1. Sort all distinct event days. For the interval [day_j, day_{j+1} - 1], the length is day_{j+1} - day_j and the daily cost is min(current_cost, C).

## 3. Step-by-Step Algorithm
1. Store events in map<long long, long long> diff.
2. For each service (a, b, c): diff[a] += c, diff[b + 1] -= c.
3. Iterate through sorted map: maintain running_cost.
4. For each consecutive pair of event days (prev_day, cur_day), add (cur_day - prev_day) * min(running_cost, C).
5. Update running_cost += event_delta and prev_day = cur_day.
6. Print total cost.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: 1D coordinate-compressed interval difference array (imos method) with event sweeping.
- **Reusable Pattern**: `Sweep-line over map events: accumulate (next_day - cur_day) * min(cost, cap).`
