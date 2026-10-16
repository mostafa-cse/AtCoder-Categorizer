# Problem Analysis: AtCoder-arc033_3 — Data Structure

**Problem ID**: `AtCoder-arc033_3`  
**Contest**: `arc033`  
**Rating / Difficulty**: 1641  
**URL**: https://atcoder.jp/contests/arc033/tasks/arc033_3  
**VJudge Tag**: `[problem:AtCoder-arc033_3]`  
**Category File**: [`../categories/data_structures/fenwick_binary_lifting_kth_element.md`](../categories/data_structures/fenwick_binary_lifting_kth_element.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Fenwick Tree`  
- **Topic (Skill)**: `Binary Lifting on Fenwick Tree for K-th Smallest Element`  

---

## 1. Problem Statement & Key Idea
An initially empty set of integers. Process Q queries: 1) insert integer x (x <= 200,000); 2) find and remove the X-th smallest element currently in the set.

**Key Insight**: Maintain a frequency array using a Fenwick tree of size 200,000. Finding the X-th smallest element is finding the smallest index idx such that prefix_sum(idx) >= X, done via binary lifting directly on the Fenwick tree in O(log MAX).

## 2. Core Observation & Invariant
Each Fenwick node tree[idx] already stores the sum of a power-of-two interval. Jumping powers of two down from 1 << 18 allows finding the X-th element in a single O(log MAX) pass without standard binary search overhead.

## 3. Step-by-Step Algorithm
1. Initialize Fenwick tree of size MAX = 200,000.
2. For query 1 (insert x): fenwick.add(x, 1).
3. For query 2 (remove X-th smallest):
4.   idx = 0.
5.   For step from (1 << 18) down to 1:
6.     If idx + step <= MAX and fenwick.tree[idx + step] < X:
7.       idx += step;
8.       X -= fenwick.tree[idx];
9.   res = idx + 1.
10.   fenwick.add(res, -1).
11.   Print res.

## 4. Complexity Analysis
- **Time Complexity**: `O(Q log(MAX))`
- **Space Complexity**: `O(MAX)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX_VAL = 200000;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    // Binary lifting to find smallest index with prefix sum >= k
    int find_kth(int k) {
        int idx = 0;
        for (int step = (1 << 18); step > 0; step >>= 1) {
            if (idx + step <= n && tree[idx + step] < k) {
                idx += step;
                k -= tree[idx];
            }
        }
        return idx + 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    Fenwick bit(MAX_VAL);

    while (q--) {
        int type, x;
        cin >> type >> x;
        if (type == 1) {
            bit.add(x, 1);
        } else {
            int val = bit.find_kth(x);
            cout << val << "\n";
            bit.add(val, -1);
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Fenwick tree internal binary lifting for order statistics operations.
- **Reusable Pattern**: `Fenwick Binary Lifting: jump power-of-two intervals to find prefix sum threshold in O(log N).`
