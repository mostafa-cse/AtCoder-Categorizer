# Max-Heap Greedy Reduction

**Domain**: `Data Structures`  
**Subtopic**: `Queue & Priority Queue`  

This workbook contains curated, high-quality competitive programming problems teaching **Max-Heap Greedy Reduction**.

---

## Curated Problems

### [problem:AtCoder-abc141_d] — Powerful Discount Tickets
- **Contest**: `abc141`
- **Rating / Difficulty**: 823
- **Specific Skill**: Max-Heap Greedy Reduction
- **Individual Analysis**: [`../../analysis/AtCoder-abc141_d.md`](../../analysis/AtCoder-abc141_d.md)
- **Problem Statement Summary**: You have N items with prices A_1, ..., A_N and M discount tickets. Each ticket halves the price of an item: floor(X / 2). Find the minimum total cost to purchase all items.
- **Core Insight**: Using a max-heap (std::priority_queue<int>), we repeatedly extract the maximum price X, replace it with X / 2, and push it back, exactly M times.
- **Complexity**: Time: `O((N + M) log N)` | Space: `O(N)`
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

    priority_queue<int> pq;
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        pq.push(a);
    }

    for (int i = 0; i < m; ++i) {
        int top = pq.top();
        pq.pop();
        pq.push(top / 2);
    }

    long long total_cost = 0;
    while (!pq.empty()) {
        total_cost += pq.top();
        pq.pop();
    }

    cout << total_cost << "\n";
    return 0;
}
```
