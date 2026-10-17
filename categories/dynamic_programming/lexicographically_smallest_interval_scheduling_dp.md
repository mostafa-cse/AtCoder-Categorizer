# Lexicographically Smallest Maximum Interval Scheduling via Backward DP

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Lexicographically Smallest Maximum Interval Scheduling via Backward DP**.

---

## Curated Problems

### `[problem:AtCoder-arc032_3]` — 仕事計画
- **Rating / Difficulty**: 2014
- **Contest**: `arc032`
- **Analysis**: [`analysis/AtCoder-arc032_3.md`](../../analysis/AtCoder-arc032_3.md)
- **Key Idea**: Standard interval scheduling finds the maximum count greedily by earliest deadline. To achieve the lexicographically smallest index sequence, we compute backward DP over time: dp[t] = pair(max_jobs_from_t, best_first_job_index). For each job i starting at S_i and ending at E_i, candidate state is (1 + dp[E_i].first, i). We relax dp[t] from T_max down to 0. Then, forward reconstruction from t = 0 greedily picks the recorded job index, jumping to its end time.
- **Time Complexity**: `O(N + T_max)`
- **Space Complexity**: `O(N + T_max)`
- **Verified C++ Implementation**:
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
