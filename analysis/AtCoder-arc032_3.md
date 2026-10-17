# Problem Analysis: AtCoder-arc032_3 — 仕事計画

**Problem ID**: `AtCoder-arc032_3`  
**Contest**: `arc032`  
**Rating / Difficulty**: 2014  
**URL**: https://atcoder.jp/contests/arc032/tasks/arc032_3  
**VJudge Tag**: `[problem:AtCoder-arc032_3]`  
**Category File**: [`../categories/dynamic_programming/lexicographically_smallest_interval_scheduling_dp.md`](../categories/dynamic_programming/lexicographically_smallest_interval_scheduling_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Lexicographically Smallest Maximum Interval Scheduling via Backward DP`  

---

## 1. Problem Statement & Key Idea
N jobs are given with start time S_i and end time E_i. Select the maximum number of non-overlapping jobs. If multiple sets achieve the maximum, choose the one whose sorted job indices are lexicographically smallest.

**Key Idea**: Standard interval scheduling finds the maximum count greedily by earliest deadline. To achieve the lexicographically smallest index sequence, we compute backward DP over time: dp[t] = pair(max_jobs_from_t, best_first_job_index). For each job i starting at S_i and ending at E_i, candidate state is (1 + dp[E_i].first, i). We relax dp[t] from T_max down to 0. Then, forward reconstruction from t = 0 greedily picks the recorded job index, jumping to its end time.

## 2. Core Observation & Invariant
Backward DP over timeline allows computing optimal suffix counts while breaking ties in favor of the minimum job index for lexicographical reconstruction.

## 3. Step-by-Step Algorithm
1. Group jobs by start time S_i.
2. Let T_max = 1,000,000.
3. Initialize dp[t] = {0, INF} for all t.
4. For t from T_max down to 0:
5.   dp[t] = dp[t + 1] (idle at time t).
6.   For each job starting at t with end E_i and id i:
7.     pair cand = {1 + dp[E_i].first, i};
8.     if cand.first > dp[t].first: dp[t] = cand;
9.     else if cand.first == dp[t].first: dp[t].second = min(dp[t].second, cand.second);
10. Reconstruct sequence: start at t = 0. While dp[t].first > 0: pick job = dp[t].second, advance t = E[job].
11. Print count and job sequence.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + T_max)`
- **Space Complexity**: `O(N + T_max)`

## 5. Core Algorithmic Skill & Learning Takeaway
Timeline backward DP for lexicographically optimal interval scheduling.

**Reusable Pattern**: Lexicographical Schedule Reconstruction: Backward DP state (max_count, min_id) + forward greedy hopping.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_T = 1000000;
const int INF = 1e9 + 7;

struct Job {
    int id;
    int end_t;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<Job>> jobs_at(MAX_T + 1);
    vector<int> end_of_job(n + 1);

    for (int i = 1; i <= n; ++i) {
        int s, e;
        cin >> s >> e;
        jobs_at[s].push_back({i, e});
        end_of_job[i] = e;
    }

    // dp[t] = {max_jobs, best_job_id}
    vector<pair<int, int>> dp(MAX_T + 2, {0, INF});

    for (int t = MAX_T; t >= 0; --t) {
        dp[t] = dp[t + 1]; // Option 1: do nothing at time t

        for (const auto& job : jobs_at[t]) {
            int count_after = 1 + dp[job.end_t].first;
            int job_id = job.id;

            if (count_after > dp[t].first) {
                dp[t] = {count_after, job_id};
            } else if (count_after == dp[t].first) {
                dp[t].second = min(dp[t].second, job_id);
            }
        }
    }

    vector<int> result;
    int cur_t = 0;
    while (dp[cur_t].first > 0) {
        int best_job = dp[cur_t].second;
        result.push_back(best_job);
        cur_t = end_of_job[best_job];
    }

    cout << result.size() << "\n";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i] << (i + 1 == result.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
