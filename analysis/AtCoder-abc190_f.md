# Problem Analysis: AtCoder-abc190_f — Shift and Inversions

**Problem ID**: `AtCoder-abc190_f`  
**Contest**: `abc190`  
**Rating / Difficulty**: 1321  
**URL**: https://atcoder.jp/contests/abc190/tasks/abc190_f  
**VJudge Tag**: `[problem:AtCoder-abc190_f]`  
**Category File**: [`../categories/data_structures/cyclic_shift_inversion_fenwick.md`](../categories/data_structures/cyclic_shift_inversion_fenwick.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Fenwick Tree`  
- **Topic (Skill)**: `Cyclic Shift Inversion Update via Fenwick Tree`  

---

## 1. Problem Statement & Key Idea
Given a permutation a_0, ..., a_{N-1} of 0..N-1. For each k from 0 to N-1, find the inversion number of the cyclically shifted sequence b_i = a_{(i + k) % N}.

**Key Idea**: Calculate the initial inversion count inv_0 using a Fenwick tree in O(N log N). Then update the inversion count in O(1) for each cyclic shift.

## 2. Core Observation & Invariant
When shifting the first element a_k to the back of the array: (1) a_k was previously before all other elements, forming a_k inversions with the elements smaller than a_k; (2) a_k is now placed after all other elements, forming (N - 1 - a_k) new inversions with elements larger than a_k! Thus, the inversion count updates by: inv_{k+1} = inv_k - a_k + (N - 1 - a_k).

## 3. Step-by-Step Algorithm
1. Compute initial inversions using Fenwick tree: inv = sum_{i=0}^{N-1} (i - bit.query(a[i])), bit.add(a[i] + 1).
2. Print initial inv.
3. For k = 0 to N - 2: inv += (N - 1 - a[k]) - a[k]; print inv.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, int val) {
        for (; i <= n; i += i & -i) tree[i] += val;
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    Fenwick bit(n);
    long long inv = 0;

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        inv += i - bit.query(a[i] + 1);
        bit.add(a[i] + 1, 1);
    }

    cout << inv << "\n";
    for (int k = 0; k < n - 1; ++k) {
        inv += (n - 1 - a[k]) - a[k];
        cout << inv << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: O(1) inversion count delta tracking under cyclic boundary shifts.
- **Reusable Pattern**: `Cyclic shift inversion delta: new_inv = old_inv - x + (N - 1 - x).`
