# Two-Array Ascending/Descending Greedy Replacement

**Domain**: `Basics`  
**Subtopic**: `Greedy`  

This workbook contains curated, high-quality competitive programming problems teaching **Two-Array Ascending/Descending Greedy Replacement**.

---

## Curated Problems

### [problem:AtCoder-abc127_d] — Integer Cards
- **Contest**: `abc127`
- **Rating / Difficulty**: 887
- **Specific Skill**: Two-Array Ascending/Descending Greedy Replacement
- **Individual Analysis**: [`../../analysis/AtCoder-abc127_d.md`](../../analysis/AtCoder-abc127_d.md)
- **Problem Statement Summary**: You have N cards with values A_1, ..., A_N. You can perform M operations: replace up to B_j cards with value C_j. Maximize the total sum of cards.
- **Core Insight**: Sort A in ascending order. Sort the replacement operations (B_j, C_j) in descending order of C_j. Iterate through cards with pointer i: replace A[i] with C_j as long as A[i] < C_j and quota B_j is not exhausted. Terminate immediately once A[i] >= C_j.
- **Complexity**: Time: `O(N log N + M log M)` | Space: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Op {
    int b;
    long long c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<Op> ops(m);
    for (int i = 0; i < m; ++i) {
        cin >> ops[i].b >> ops[i].c;
    }

    sort(a.begin(), a.end());
    sort(ops.begin(), ops.end(), [](const Op& x, const Op& y) {
        return x.c > y.c;
    });

    int ptr = 0;
    for (const auto& op : ops) {
        if (ptr >= n || a[ptr] >= op.c) break;
        int count = op.b;
        while (ptr < n && count > 0 && a[ptr] < op.c) {
            a[ptr] = op.c;
            ptr++;
            count--;
        }
    }

    long long sum = 0;
    for (long long x : a) {
        sum += x;
    }

    cout << sum << "\n";
    return 0;
}
```
