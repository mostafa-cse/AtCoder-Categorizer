# Problem Analysis: AtCoder-abc128_e — Roadwork

**Problem ID**: `AtCoder-abc128_e`  
**Contest**: `abc128`  
**Rating / Difficulty**: 1840  
**URL**: https://atcoder.jp/contests/abc128/tasks/abc128_e  
**VJudge Tag**: `[problem:AtCoder-abc128_e]`  
**Category File**: [`../categories/data_structures/time_space_diagonal_projection_sweep_line.md`](../categories/data_structures/time_space_diagonal_projection_sweep_line.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Sweep-Line / Multiset`  
- **Topic (Skill)**: `Time-Space Diagonal Projection (S_i - X_i) Sweep-Line with Active Multiset`  

---

## 1. Problem Statement & Key Idea
N roadworks: roadwork i at position X_i blocks passage during time [S_i, T_i). Q people start at position 0 at departure times D_1 < D_2 < ... < D_Q, walking at speed 1. For each person, find where they are stopped, or -1.

**Key Insight**: A person departing at time D reaches position X at time D + X. They are blocked by roadwork i iff S_i <= D + X_i < T_i, which rearranges to S_i - X_i <= D < T_i - X_i. Thus, roadwork i acts on departure times in interval [S_i - X_i, T_i - X_i).

## 2. Core Observation & Invariant
Project events onto departure time axis D. Add X_i at S_i - X_i, remove X_i at T_i - X_i. For each departure D_j, the first blocking roadwork is min(X_i) in the active set, queryable via std::multiset in O(log N).

## 3. Step-by-Step Algorithm
1. Generate events:
2.   (S_i - X_i, +1, X_i): add roadwork
3.   (T_i - X_i, -1, X_i): remove roadwork
4.   (D_j, 0, query_id): query person
5. Sort events by time. If times tie, process +1 before 0, and 0 before -1.
6. Maintain multiset<long long> active.
7. For each event:
8.   if type == +1: active.insert(X_i);
9.   if type == -1: active.erase(active.find(X_i));
10.   if type == 0: ans[query_id] = active.empty() ? -1 : *active.begin();
11. Print all answers.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N + Q)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Diagonal coordinate transformation D = t - x reducing dynamic trajectory blocking to static sweep-line.
- **Reusable Pattern**: `Trajectory Sweep-Line: Project [S_i - X_i, T_i - X_i) intervals and query active min element.`
