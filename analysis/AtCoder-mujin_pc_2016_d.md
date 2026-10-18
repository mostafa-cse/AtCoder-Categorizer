# Problem Analysis: AtCoder-mujin_pc_2016_d — D. Parenthesis Sequence

**Problem ID**: `AtCoder-mujin_pc_2016_d`  
**Contest**: `mujin-pc-2016`  
**Rating / Difficulty**: 2404  
**URL**: https://atcoder.jp/contests/mujin-pc-2016/tasks/mujin_pc_2016_d  
**VJudge Tag**: `[problem:AtCoder-mujin_pc_2016_d]`  
**Category File**: [`../categories/data_structures/segment_tree_parenthesis_prefix_balance.md`](../categories/data_structures/segment_tree_parenthesis_prefix_balance.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree (Point Update Range Query)`  

---

## 1. Problem Statement & Key Idea
Determine whether a substring with '?' wildcards can be completed into a regular bracket sequence. A valid bracket sequence requires that the total balance is 0 and all prefix balances remain non-negative.

## 2. Core Observation & Invariant
To maximize the prefix balance everywhere, all '?' converted to '(' must appear as early as possible (before a split point mid), while all '?' converted to ')' must appear after mid. The prefix balance condition decomposes into two independent range minimum queries over prefix arrays.

## 3. Step-by-Step Algorithm
1. 1. For any query [l, r], verify length is even and calculate the required count of '(' wildcards.
2. 2. Find the transition index mid where '?' switches from '(' to ')' via prefix wildcard counts.
3. 3. Verify range minimum balance on [l, mid] with all '?' as '(' and on [mid+1, r] with all '?' as ')' using a Segment Tree or Sparse Table in O(1) per query.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N + Q)`
- **Space Complexity**: `O(N log N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    string s;
    cin >> s;

    vector<int> pref_open(n + 1, 0), pref_close(n + 1, 0), pref_q(n + 1, 0);
    vector<int> pref_L(n + 1, 0), pref_R(n + 1, 0);
    vector<int> q_pos;

    for (int i = 1; i <= n; i++) {
        char ch = s[i - 1];
        pref_open[i] = pref_open[i - 1] + (ch == '(' ? 1 : 0);
        pref_close[i] = pref_close[i - 1] + (ch == ')' ? 1 : 0);
        pref_q[i] = pref_q[i - 1] + (ch == '?' ? 1 : 0);
        if (ch == '?') q_pos.push_back(i);

        int val_L = (ch == '(' || ch == '?') ? 1 : -1;
        pref_L[i] = pref_L[i - 1] + val_L;

        int val_R = (ch == '(') ? 1 : -1;
        pref_R[i] = pref_R[i - 1] + val_R;
    }

    const int LOGN = 18;
    vector<vector<int>> st_L(LOGN, vector<int>(n + 1, 0));
    vector<vector<int>> st_R(LOGN, vector<int>(n + 1, 0));

    for (int i = 0; i <= n; i++) {
        st_L[0][i] = pref_L[i];
        st_R[0][i] = pref_R[i];
    }

    for (int j = 1; j < LOGN; j++) {
        int length = 1 << j;
        int half = 1 << (j - 1);
        for (int i = 0; i + length - 1 <= n; i++) {
            st_L[j][i] = min(st_L[j - 1][i], st_L[j - 1][i + half]);
            st_R[j][i] = min(st_R[j - 1][i], st_R[j - 1][i + half]);
        }
    }

    auto query_min_L = [&](int l, int r) -> int {
        if (l > r) return INF;
        int length = r - l + 1;
        int k = 31 - __builtin_clz(length);
        return min(st_L[k][l], st_L[k][r - (1 << k) + 1]);
    };

    auto query_min_R = [&](int l, int r) -> int {
        if (l > r) return INF;
        int length = r - l + 1;
        int k = 31 - __builtin_clz(length);
        return min(st_R[k][l], st_R[k][r - (1 << k) + 1]);
    };

    int q;
    cin >> q;
    while (q--) {
        int l, r;
        cin >> l >> r;
        int length = r - l + 1;
        if (length % 2 != 0) {
            cout << "No\n";
            continue;
        }

        int c1 = pref_open[r] - pref_open[l - 1];
        int c2 = pref_close[r] - pref_close[l - 1];
        int k1 = length / 2 - c1;
        int k2 = length / 2 - c2;
        if (k1 < 0 || k2 < 0) {
            cout << "No\n";
            continue;
        }

        if (k1 == 0) {
            int min_r = query_min_R(l, r);
            if (min_r >= pref_R[r]) {
                cout << "Yes\n";
            } else {
                cout << "No\n";
            }
        } else {
            int target = pref_q[l - 1] + k1;
            int idx = q_pos[target - 1];
            bool cond1 = (query_min_L(l, idx) >= pref_L[l - 1]);
            bool cond2 = (query_min_R(idx, r) >= pref_R[r]);
            if (cond1 && cond2) {
                cout << "Yes\n";
            } else {
                cout << "No\n";
            }
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
