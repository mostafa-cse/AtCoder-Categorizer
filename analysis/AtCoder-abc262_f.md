# Problem Analysis: AtCoder-abc262_f — F. Erase and Rotate

**Problem ID**: `AtCoder-abc262_f`  
**Contest**: `abc262`  
**Rating / Difficulty**: 2334  
**URL**: https://atcoder.jp/contests/abc262/tasks/abc262_f  
**VJudge Tag**: `[problem:AtCoder-abc262_f]`  
**Category File**: [`../categories/data_structures/lexicographical_deletion_rotation_monotonic_stack.md`](../categories/data_structures/lexicographical_deletion_rotation_monotonic_stack.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Monotonic Data Structures`  
- **Topic (Skill)**: `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`  

---

## 1. Problem Statement & Key Idea
Find the lexicographically smallest permutation achievable by at most $K$ operations of deleting the first element or rotating the last element to the front. Evaluates 0 rotations vs optimal suffix minimum rotation via monotonic stack in $O(N)$.

## 2. Core Observation & Invariant
Rotating the array right by $r \ge 1$ positions requires $r$ operations, bringing $P[N-r]$ to the front. To minimize the leading element, $P[N-r]$ must be chosen as the minimum element in $P[N-K \dots N-1]$. The remaining budget $K - r$ is used greedily via a monotonic stack on the remaining prefix and suffix.

## 3. Step-by-Step Algorithm
1. Candidate 1 (0 rotations): run standard greedy deletion with budget $K$ on $P[0 \dots N-1]$ using a monotonic stack.
2. Candidate 2 ($r \ge 1$ rotations): find index $idx \in [N-K, N-1]$ minimizing $P[idx]$. Bring $P[idx \dots N-1]$ to the front; process it with monotonic stack, then process $P[0 \dots idx-1]$ with remaining deletion budget $K - (N - idx)$.
3. Compare Candidate 1 and Candidate 2 lexicographically in $O(N)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
    }

    // Option 1: 0 rotations, up to K deletions
    vector<int> st1;
    int del_left = k;
    for (int x : p) {
        while (!st1.empty() && del_left > 0 && st1.back() > x) {
            st1.pop_back();
            del_left--;
        }
        st1.push_back(x);
    }
    while (!st1.empty() && del_left > 0) {
        st1.pop_back();
        del_left--;
    }

    if (k == 0) {
        for (int i = 0; i < (int)st1.size(); ++i) {
            cout << st1[i] << (i + 1 == (int)st1.size() ? "" : " ");
        }
        cout << "\n";
        return 0;
    }

    // Option 2: 1 or more rotations
    // Find min element in suffix of length k: p[n-k .. n-1]
    int min_val = 1e9;
    int idx = -1;
    for (int i = n - k; i < n; ++i) {
        if (p[i] < min_val) {
            min_val = p[i];
            idx = i;
        }
    }

    // Suffix part p[idx .. n-1]: monotonic stack for free
    vector<int> st_suf;
    for (int i = idx; i < n; ++i) {
        int x = p[i];
        while ((int)st_suf.size() > 1 && st_suf.back() > x) {
            st_suf.pop_back();
        }
        if (st_suf.empty()) {
            st_suf.push_back(x);
        } else if (st_suf.back() < x) {
            st_suf.push_back(x);
        }
    }

    // Prefix part p[0 .. idx-1] with budget rem_del = k - (n - idx)
    int rem_del = k - (n - idx);
    vector<int> st_pref;
    for (int i = 0; i < idx; ++i) {
        int x = p[i];
        while (!st_pref.empty() && rem_del > 0 && st_pref.back() > x) {
            st_pref.pop_back();
            rem_del--;
        }
        st_pref.push_back(x);
    }

    vector<int> st2 = st_suf;
    for (int x : st_pref) {
        st2.push_back(x);
    }

    while (!st2.empty() && rem_del > 0) {
        st2.pop_back();
        rem_del--;
    }

    // Compare st1 and st2
    const vector<int> &ans = (st1 < st2 ? st1 : st2);
    for (int i = 0; i < (int)ans.size(); ++i) {
        cout << ans[i] << (i + 1 == (int)ans.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
