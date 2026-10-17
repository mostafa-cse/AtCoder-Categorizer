# Problem Analysis: AtCoder-arc155_c — Even Sum Triplet

**Problem ID**: `AtCoder-arc155_c`  
**Contest**: `arc155`  
**Rating / Difficulty**: 2219  
**URL**: https://atcoder.jp/contests/arc155/tasks/arc155_c  
**VJudge Tag**: `[problem:AtCoder-arc155_c]`  
**Category File**: [`../categories/basics/even_sum_triplet_parity_invariant_permutations.md`](../categories/basics/even_sum_triplet_parity_invariant_permutations.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Determine whether sequence A can be transformed into B by repeatedly rearranging any three consecutive elements whose sum is even.

## 2. Core Observation & Invariant
Operations fall into two categories: three evens (permutes 3 adjacent evens) and two odds + one even (moves an even past two odds). The feasibility of the latter is an invariant across the sequence. If two-odd operations are impossible, odds cannot move and act as fixed walls, allowing each even segment of length >= 3 to be independently sorted. If two-odd operations are possible, all elements can be freely permuted except when the count of evens is exactly 2, in which case their relative order is invariant.

## 3. Step-by-Step Algorithm
1. 1. Check if multiset of A matches B. If not, output No.
2. 2. Check whether any 3-window has >= 2 odds and >= 1 even. If this differs between A and B, output No.
3. 3. If possible: if number of evens == 2, check whether the relative order of the two evens is identical in A and B; otherwise output Yes.
4. 4. If impossible: canonicalize A and B by sorting every contiguous block of evens of length >= 3, and verify whether canonicalized sequences are identical.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

bool can_type2(const vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 2; i++) {
        int odds = (arr[i] & 1) + (arr[i + 1] & 1) + (arr[i + 2] & 1);
        if (odds == 2) return true;
    }
    return false;
}

vector<int> canonicalize(const vector<int>& arr) {
    vector<int> res;
    vector<int> cur_even;
    for (int x : arr) {
        if (x & 1) {
            if (cur_even.size() >= 3) {
                sort(cur_even.begin(), cur_even.end());
            }
            for (int e : cur_even) res.push_back(e);
            cur_even.clear();
            res.push_back(x);
        } else {
            cur_even.push_back(x);
        }
    }
    if (cur_even.size() >= 3) {
        sort(cur_even.begin(), cur_even.end());
    }
    for (int e : cur_even) res.push_back(e);
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n), b(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];

    vector<int> sorted_a = a, sorted_b = b;
    sort(sorted_a.begin(), sorted_a.end());
    sort(sorted_b.begin(), sorted_b.end());
    if (sorted_a != sorted_b) {
        cout << "No\n";
        return 0;
    }

    bool c2_a = can_type2(a);
    bool c2_b = can_type2(b);
    if (c2_a != c2_b) {
        cout << "No\n";
        return 0;
    }

    if (c2_a) {
        vector<int> evens_a, evens_b;
        for (int x : a) if (!(x & 1)) evens_a.push_back(x);
        for (int x : b) if (!(x & 1)) evens_b.push_back(x);
        if (evens_a.size() == 2) {
            cout << (evens_a == evens_b ? "Yes\n" : "No\n");
        } else {
            cout << "Yes\n";
        }
    } else {
        vector<int> can_a = canonicalize(a);
        vector<int> can_b = canonicalize(b);
        cout << (can_a == can_b ? "Yes\n" : "No\n");
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
