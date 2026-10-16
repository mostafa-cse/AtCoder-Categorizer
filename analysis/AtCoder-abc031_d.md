# Problem Analysis: AtCoder-abc031_d — Goroawase

**Problem ID**: `AtCoder-abc031_d`  
**Contest**: `abc031`  
**Rating / Difficulty**: 1688  
**URL**: https://atcoder.jp/contests/abc031/tasks/abc031_d  
**VJudge Tag**: `[problem:AtCoder-abc031_d]`  
**Category File**: [`../categories/basics/digit_string_length_search.md`](../categories/basics/digit_string_length_search.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Exhaustive Search`  
- **Topic (Skill)**: `Digit String Length Partition Search`  

---

## 1. Problem Statement & Key Idea
K digits 1..K (K <= 9). Each digit d corresponds to an unknown string S_d of length between 1 and 3. Given N pairs of (digit sequence v_i, string w_i). Find the string S_d for each digit d.

**Key Insight**: There are only K digits, and each digit has length in {1, 2, 3}. The search space of length assignments is at most 3^9 = 19,683! Exhaustively search all length combinations and verify against the N string equations.

## 2. Core Observation & Invariant
Once lengths len[1..K] are fixed, for each equation v_i -> w_i, check if sum_{d in v_i} len[d] == |w_i|. If so, parse w_i into candidate substring for each digit d. If all parsed substrings are mutually consistent across all N equations, the solution is uniquely found.

## 3. Step-by-Step Algorithm
1. Backtrack through all 3^K length combinations len[1..K] in {1, 2, 3}.
2. For each combination:
3.   valid = true.
4.   vector<string> candidate(K + 1, '').
5.   For each pair (v_i, w_i):
6.     Verify sum len[d] == |w_i|.
7.     Slice w_i according to lengths: if candidate[d] already set and != slice, invalid.
8.   If valid for all N pairs, print candidate[1..K] and terminate.

## 4. Complexity Analysis
- **Time Complexity**: `O(3^K * N * sum(|w|))`
- **Space Complexity**: `O(K)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int k, n;
vector<string> v_list, w_list;
int len[10];

bool check() {
    vector<string> ans(k + 1, "");
    for (int i = 0; i < n; ++i) {
        int expected_len = 0;
        for (char c : v_list[i]) {
            expected_len += len[c - '0'];
        }
        if (expected_len != (int)w_list[i].size()) return false;

        int pos = 0;
        for (char c : v_list[i]) {
            int d = c - '0';
            string sub = w_list[i].substr(pos, len[d]);
            pos += len[d];

            if (ans[d] == "") {
                ans[d] = sub;
            } else if (ans[d] != sub) {
                return false;
            }
        }
    }

    for (int d = 1; d <= k; ++d) {
        cout << ans[d] << "\n";
    }
    return true;
}

bool search_lens(int idx) {
    if (idx > k) {
        return check();
    }
    for (int l = 1; l <= 3; ++l) {
        len[idx] = l;
        if (search_lens(idx + 1)) return true;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> k >> n)) return 0;

    v_list.resize(n);
    w_list.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> v_list[i] >> w_list[i];
    }

    search_lens(1);
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Parameter length partition search followed by greedy consistency verification.
- **Reusable Pattern**: `Token Length Backtracking: 3^K search over token lengths + prefix verification.`
