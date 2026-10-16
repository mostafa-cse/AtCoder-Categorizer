# Problem Analysis: AtCoder-abc127_d — Integer Cards

**Problem ID**: `AtCoder-abc127_d`  
**Contest**: `abc127`  
**Rating / Difficulty**: 887  
**URL**: https://atcoder.jp/contests/abc127/tasks/abc127_d  
**VJudge Tag**: `[problem:AtCoder-abc127_d]`  
**Category File**: [`../categories/basics/two_array_greedy_replacement.md`](../categories/basics/two_array_greedy_replacement.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy`  
- **Topic (Skill)**: `Two-Array Ascending/Descending Greedy Replacement`  

---

## 1. Problem Statement & Key Idea
You have N cards with values A_1, ..., A_N. You can perform M operations: replace up to B_j cards with value C_j. Maximize the total sum of cards.

**Key Idea**: Each operation allows replacing smaller values with larger values. We should replace the smallest available cards with the largest available replacement values C_j.

## 2. Core Observation & Invariant
Sort A in ascending order. Sort the replacement operations (B_j, C_j) in descending order of C_j. Iterate through cards with pointer i: replace A[i] with C_j as long as A[i] < C_j and quota B_j is not exhausted. Terminate immediately once A[i] >= C_j.

## 3. Step-by-Step Algorithm
1. Sort A in ascending order.
2. Sort operations in descending order of replacement value C.
3. Use pointer i = 0. For each operation (B, C): while i < N and B > 0 and A[i] < C: A[i] = C, i++, B--.
4. If A[i] >= C, break early.
5. Output sum of elements of A.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + M log M)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Optimal replacement via dual sorted pointers.
- **Reusable Pattern**: `Greedy replacement: match smallest current elements against largest replacement values.`
