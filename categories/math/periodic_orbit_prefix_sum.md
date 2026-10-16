# Periodic Orbit Prefix Sum Acceleration

**Domain**: `Math`  
**Subtopic**: `Cycle Detection`  

This workbook contains curated, high-quality competitive programming problems teaching **Periodic Orbit Prefix Sum Acceleration**.

---

## Curated Problems

### [problem:AtCoder-abc179_e] — Sequence Sum
- **Contest**: `abc179`
- **Rating / Difficulty**: 1175
- **Specific Skill**: Periodic Orbit Prefix Sum Acceleration
- **Individual Analysis**: [`../../analysis/AtCoder-abc179_e.md`](../../analysis/AtCoder-abc179_e.md)
- **Problem Statement Summary**: Given A_1 = X and A_{n+1} = A_n^2 mod M. Compute sum_{i=1}^N A_i for N <= 10^12, M <= 10^5.
- **Core Insight**: Track the first visit step of each value in visited[val]. Once a value repeats at step cur with previous visit at step prev: the cycle length is L = cur - prev. Divide remaining steps into full cycles and a partial remainder, computing the sum in O(M).
- **Complexity**: Time: `O(M)` | Space: `O(M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, x, m;
    if (!(cin >> n >> x >> m)) return 0;

    vector<int> visited(m, -1);
    vector<long long> seq;

    long long cur = x;
    int step = 0;

    while (step < n && visited[cur] == -1) {
        visited[cur] = step;
        seq.push_back(cur);
        cur = (cur * cur) % m;
        step++;
    }

    if (step == n) {
        long long total = 0;
        for (long long v : seq) total += v;
        cout << total << "\n";
        return 0;
    }

    int start_cycle = visited[cur];
    int cycle_len = step - start_cycle;

    long long total = 0;
    for (int i = 0; i < start_cycle; ++i) {
        total += seq[i];
    }

    long long cycle_sum = 0;
    for (int i = start_cycle; i < step; ++i) {
        cycle_sum += seq[i];
    }

    long long remaining_steps = n - start_cycle;
    total += (remaining_steps / cycle_len) * cycle_sum;

    long long tail = remaining_steps % cycle_len;
    for (int i = 0; i < tail; ++i) {
        total += seq[start_cycle + i];
    }

    cout << total << "\n";
    return 0;
}
```
