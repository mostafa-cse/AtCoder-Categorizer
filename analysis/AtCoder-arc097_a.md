# Problem Analysis: AtCoder-arc097_a — K-th Substring

**Problem ID**: `AtCoder-arc097_a`  
**Contest**: `abc097`  
**Rating / Difficulty**: 1108  
**URL**: https://atcoder.jp/contests/abc097/tasks/arc097_a  
**VJudge Tag**: `[problem:AtCoder-arc097_a]`  
**Category File**: [`../categories/strings/bounded_length_substring_kth.md`](../categories/strings/bounded_length_substring_kth.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Substring Ranking`  
- **Topic (Skill)**: `Bounded-Length Substring Generation for Small K-th Ranking`  

---

## 1. Problem Statement & Key Idea
Given string S and integer K (K <= 5). Find the K-th lexicographically smallest distinct substring of S.

**Key Idea**: The K-th lexicographically smallest distinct substring can have length at most K! (Any substring of length > K is preceded by its K prefixes, which are strictly smaller).

## 2. Core Observation & Invariant
Since K <= 5, we only need to extract all substrings of length 1, 2, ..., K. Insert them into a std::set<string> to automatically deduplicate and sort them in O(|S| * K^2), then retrieve the K-th element.

## 3. Step-by-Step Algorithm
1. Initialize std::set<string> subs.
2. For each starting index i in 0..|S|-1: for len in 1..K (such that i + len <= |S|): insert S.substr(i, len) into subs.
3. Advance iterator K - 1 times in subs.
4. Print the string.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| * K^2)`
- **Space Complexity**: `O(|S| * K)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    int k;
    if (!(cin >> s >> k)) return 0;

    set<string> subs;
    int n = s.size();

    for (int i = 0; i < n; ++i) {
        for (int len = 1; len <= k && i + len <= n; ++len) {
            subs.insert(s.substr(i, len));
        }
    }

    auto it = subs.begin();
    for (int i = 0; i < k - 1; ++i) {
        it++;
    }

    cout << *it << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bounding substring search length by K for small K-th lexicographical order.
- **Reusable Pattern**: `K-th smallest substring: only examine substrings of length <= K.`
