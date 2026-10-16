# Problem Analysis: AtCoder-abc138_e — Strings of Impurity

**Problem ID**: `AtCoder-abc138_e`  
**Contest**: `abc138`  
**Rating / Difficulty**: 1257  
**URL**: https://atcoder.jp/contests/abc138/tasks/abc138_e  
**VJudge Tag**: `[problem:AtCoder-abc138_e]`  
**Category File**: [`../categories/strings/periodic_string_subsequence_search.md`](../categories/strings/periodic_string_subsequence_search.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Subsequences`  
- **Topic (Skill)**: `Periodic String Subsequence Matching via Position Binary Search`  

---

## 1. Problem Statement & Key Idea
Given string s and string t. Let s' be an infinite concatenation of s. Find the shortest prefix length of s' that contains t as a subsequence (or -1 if impossible).

**Key Idea**: Greedily match each character of t at the earliest possible appearance in s.

## 2. Core Observation & Invariant
Store 0-indexed positions of each character in s: pos[c]. Maintain current index in s: cur_pos. For character t[i]: binary search with std::upper_bound in pos[t[i]] for the first position > cur_pos. If found, advance cur_pos to that position. If not found, wrap around to the next copy of s (advance copy count) and set cur_pos to pos[t[i]][0].

## 3. Step-by-Step Algorithm
1. Store all occurrence indices for each character 'a'..'z' in s.
2. If any character in t has an empty occurrence list in s, output -1.
3. Initialize copies = 0, cur_pos = -1.
4. For each char c in t: find first index in pos[c] > cur_pos via upper_bound; if found: cur_pos = *it; else: copies++, cur_pos = pos[c][0].
5. Answer is copies * |s| + cur_pos + 1.

## 4. Complexity Analysis
- **Time Complexity**: `O(|s| + |t| log |s|)`
- **Space Complexity**: `O(|s|)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    vector<vector<int>> pos(26);
    for (int i = 0; i < (int)s.size(); ++i) {
        pos[s[i] - 'a'].push_back(i);
    }

    long long copies = 0;
    int cur_idx = -1;

    for (char c : t) {
        int char_code = c - 'a';
        if (pos[char_code].empty()) {
            cout << -1 << "\n";
            return 0;
        }

        auto it = upper_bound(pos[char_code].begin(), pos[char_code].end(), cur_idx);
        if (it != pos[char_code].end()) {
            cur_idx = *it;
        } else {
            copies++;
            cur_idx = pos[char_code][0];
        }
    }

    long long total_len = copies * (long long)s.size() + cur_idx + 1;
    cout << total_len << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Simulating infinite periodic string subsequence matching via upper_bound.
- **Reusable Pattern**: `Greedy subsequence in periodic s: upper_bound on character occurrence lists.`
