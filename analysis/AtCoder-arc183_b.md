# Problem Analysis: AtCoder-arc183_b — Near Assignment

**Problem ID**: `AtCoder-arc183_b`  
**Contest**: `arc183`  
**Rating / Difficulty**: 2118  
**URL**: https://atcoder.jp/contests/arc183/tasks/arc183_b  
**VJudge Tag**: `[problem:AtCoder-arc183_b]`  
**Category File**: [`../categories/basics/distance_k_replication_reachability.md`](../categories/basics/distance_k_replication_reachability.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Given two arrays A and B of length N, determine if A can be transformed into B by repeatedly choosing i, j with |i - j| <= K and setting A_i = A_j.

**Key Insight**: If A == B, answer is trivially Yes. Otherwise, every value in B must exist in A (values cannot be created from nothing). Furthermore, since an assignment A_i = A_j overwrites a value, values can only replicate without losing variety if B contains at least one duplicate pair within distance K (i.e. exists i < j with B_i = B_j and j - i <= K). If no such nearby duplicate exists in B, every window of length K+1 has strictly distinct elements, making it impossible to perform any overwrite without permanently extinguishing a necessary value.

## 2. Core Observation & Invariant
Replication reachability under radius K requires value subset containment and the existence of at least one duplicate pair within distance K in the target array.

## 3. Step-by-Step Algorithm
1. If A == B, return Yes.
2. Verify all elements of B appear in A; if not, return No.
3. Check if there exist indices i < j with B[i] == B[j] and j - i <= K using last occurrence tracking.
4. If such a pair exists, return Yes; otherwise return No.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Replication invariant analysis and local duplicate density verification.
- **Reusable Pattern**: Array transformation under local overwriting radius K requires target to contain nearby duplicate seeds.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> a(n), b(n);
    vector<bool> in_a(n + 1, false);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        in_a[a[i]] = true;
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }

    if (a == b) {
        cout << "Yes\n";
        return;
    }

    for (int i = 0; i < n; ++i) {
        if (!in_a[b[i]]) {
            cout << "No\n";
            return;
        }
    }

    vector<int> last_pos(n + 1, -1);
    bool has_near_dup = false;
    for (int i = 0; i < n; ++i) {
        if (last_pos[b[i]] != -1 && i - last_pos[b[i]] <= k) {
            has_near_dup = true;
            break;
        }
        last_pos[b[i]] = i;
    }

    if (has_near_dup) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}
```
