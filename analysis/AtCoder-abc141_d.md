# Problem Analysis: AtCoder-abc141_d — Powerful Discount Tickets

**Problem ID**: `AtCoder-abc141_d`  
**Contest**: `abc141`  
**Rating / Difficulty**: 823  
**URL**: https://atcoder.jp/contests/abc141/tasks/abc141_d  
**VJudge Tag**: `[problem:AtCoder-abc141_d]`  
**Category File**: [`../categories/data_structures/max_heap_greedy_reduction.md`](../categories/data_structures/max_heap_greedy_reduction.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Queue & Priority Queue`  
- **Topic (Skill)**: `Max-Heap Greedy Reduction`  

---

## 1. Problem Statement & Key Idea
You have N items with prices A_1, ..., A_N and M discount tickets. Each ticket halves the price of an item: floor(X / 2). Find the minimum total cost to purchase all items.

**Key Idea**: Applying a discount ticket to price X saves X - floor(X / 2) = ceil(X / 2). Because ceil(X / 2) is monotonically non-decreasing in X, the maximum reduction is always achieved by halving the currently most expensive item.

## 2. Core Observation & Invariant
Using a max-heap (std::priority_queue<int>), we repeatedly extract the maximum price X, replace it with X / 2, and push it back, exactly M times.

## 3. Step-by-Step Algorithm
1. Push all N prices into a max-heap.
2. Repeat M times: pop top element x, push x / 2.
3. Sum all remaining elements in the heap and output.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) log N)`
- **Space Complexity**: `O(N)`

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

## 6. Editorial Comparison & Alignment
Direct alignment with official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Greedy diminishing-returns reduction using priority queues.
- **Reusable Pattern**: `Max-Heap greedy halving loop: pop x, push x / 2.`
