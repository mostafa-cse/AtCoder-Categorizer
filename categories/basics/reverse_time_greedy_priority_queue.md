# Reverse Time Greedy with Max-Heap Priority Queue

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Reverse Time Greedy with Max-Heap Priority Queue**.

---

## Curated Problems

### [problem:AtCoder-abc137_d] — Summer Vacation
- **Contest**: `abc137`
- **Rating / Difficulty**: 1313
- **Specific Skill**: Reverse Time Greedy with Max-Heap Priority Queue
- **Individual Analysis**: [`../../analysis/AtCoder-abc137_d.md`](../../analysis/AtCoder-abc137_d.md)
- **Problem Statement Summary**: N jobs. Job i takes 1 day of work and pays B_i yen A_i days after being chosen. You have M days until summer vacation ends. Maximize total rewards (rewards must be received by day M).
- **Core Insight**: Process days in REVERSE from day M down to 1. On day d, the time left until vacation ends is rem = M - d + 1. All jobs with delay A_i == rem become newly eligible to be scheduled! Add their rewards B_i to a max-heap. Pop the single highest available reward in the heap to be performed on day d.
- **Complexity**: Time: `O(N log N + M log N)` | Space: `O(N + M)`
- **Verified C++ Implementation**:
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
