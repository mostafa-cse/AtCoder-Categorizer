# Digit BFS Queue Generation / Monotonic Transition

**Domain**: `Basics`  
**Subtopic**: `BFS / State Generation`  

This workbook contains curated, high-quality competitive programming problems teaching **Digit BFS Queue Generation / Monotonic Transition**.

---

## Curated Problems

### [problem:AtCoder-abc161_d] — Lunlun Number
- **Contest**: `abc161`
- **Rating / Difficulty**: 991
- **Specific Skill**: Digit BFS Queue Generation / Monotonic Transition
- **Individual Analysis**: [`../../analysis/AtCoder-abc161_d.md`](../../analysis/AtCoder-abc161_d.md)
- **Problem Statement Summary**: A positive integer is a 'Lunlun number' if the absolute difference between any two adjacent decimal digits is at most 1. Find the K-th smallest Lunlun number (K <= 10^5).
- **Core Insight**: Start with single digits 1..9 in a queue. Pop number x with last digit d = x % 10. The next valid Lunlun numbers extending x are obtained by appending d - 1 (if d > 0), d, and d + 1 (if d < 9). Because we push numbers in increasing order of value, popping K times yields the exact K-th smallest Lunlun number.
- **Complexity**: Time: `O(K)` | Space: `O(K)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    queue<long long> q;
    for (int i = 1; i <= 9; ++i) {
        q.push(i);
    }

    long long current = 0;
    for (int step = 0; step < k; ++step) {
        current = q.front();
        q.pop();

        int last = current % 10;
        if (last > 0) q.push(current * 10 + (last - 1));
        q.push(current * 10 + last);
        if (last < 9) q.push(current * 10 + (last + 1));
    }

    cout << current << "\n";
    return 0;
}
```
