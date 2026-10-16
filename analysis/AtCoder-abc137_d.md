# Problem Analysis: AtCoder-abc137_d — Summer Vacation

**Problem ID**: `AtCoder-abc137_d`  
**Contest**: `abc137`  
**Rating / Difficulty**: 1313  
**URL**: https://atcoder.jp/contests/abc137/tasks/abc137_d  
**VJudge Tag**: `[problem:AtCoder-abc137_d]`  
**Category File**: [`../categories/basics/reverse_time_greedy_priority_queue.md`](../categories/basics/reverse_time_greedy_priority_queue.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Reverse Time Greedy with Max-Heap Priority Queue`  

---

## 1. Problem Statement & Key Idea
N jobs. Job i takes 1 day of work and pays B_i yen A_i days after being chosen. You have M days until summer vacation ends. Maximize total rewards (rewards must be received by day M).

**Key Idea**: A job started on day d (1 <= d <= M) is paid by day M if and only if d + A_i <= M + 1, which means A_i <= M - d + 1 (the job delay is <= remaining days).

## 2. Core Observation & Invariant
Process days in REVERSE from day M down to 1. On day d, the time left until vacation ends is rem = M - d + 1. All jobs with delay A_i == rem become newly eligible to be scheduled! Add their rewards B_i to a max-heap. Pop the single highest available reward in the heap to be performed on day d.

## 3. Step-by-Step Algorithm
1. Group jobs by delay A_i into buckets jobs[A_i].
2. Initialize priority_queue<int> pq (max-heap).
3. Initialize total_reward = 0.
4. For day_left from 1 to M: for job reward B in jobs[day_left]: pq.push(B); if (!pq.empty()): total_reward += pq.top(), pq.pop().
5. Output total_reward.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + M log N)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> jobs(m + 1);
    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        if (a <= m) {
            jobs[a].push_back(b);
        }
    }

    priority_queue<int> pq;
    long long total_reward = 0;

    for (int rem = 1; rem <= m; ++rem) {
        for (int reward : jobs[rem]) {
            pq.push(reward);
        }
        if (!pq.empty()) {
            total_reward += pq.top();
            pq.pop();
        }
    }

    cout << total_reward << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Reverse time sweep with priority queue scheduling.
- **Reusable Pattern**: `Deadline scheduling in reverse: push newly eligible jobs, pop max reward.`
