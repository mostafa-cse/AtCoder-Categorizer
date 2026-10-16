# Problem Analysis: AtCoder-arc065_a — Daydream

**Problem ID**: `AtCoder-arc065_a`  
**Contest**: `abc049`  
**Rating / Difficulty**: 930  
**URL**: https://atcoder.jp/contests/abc049/tasks/arc065_a  
**VJudge Tag**: `[problem:AtCoder-arc065_a]`  
**Category File**: [`../categories/strings/reverse_greedy_suffix_parsing.md`](../categories/strings/reverse_greedy_suffix_parsing.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Greedy Parsing`  
- **Topic (Skill)**: `Reverse Greedy Suffix Parsing / Ambiguity Inversion`  

---

## 1. Problem Statement & Key Idea
Determine whether string S can be formed by concatenating copies of 'dream', 'dreamer', 'erase', and 'eraser'.

**Key Idea**: Left-to-right parsing is ambiguous ('dream' is a prefix of 'dreamer', 'erase' of 'eraser'). However, right-to-left suffix matching is completely deterministic!

## 2. Core Observation & Invariant
Reversing S and the words ('maerd', 'remaerd', 'esare', 'resare'), or simply matching from the back: check if S ends with 'eraser' (6), 'erase' (5), 'dreamer' (7), or 'dream' (5). Suffixes never conflict when matched greedily.

## 3. Step-by-Step Algorithm
1. Maintain pointer pos = |S|.
2. While pos > 0:
3. Check if S[pos - len .. pos - 1] matches any of the 4 valid words.
4. If a match is found, pos -= len.
5. If no word matches, output 'NO' and exit.
6. If pos == 0, output 'YES'.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S|)`
- **Space Complexity**: `O(|S|)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    vector<string> words = {"dream", "dreamer", "erase", "eraser"};
    int pos = s.size();

    while (pos > 0) {
        bool matched = false;
        for (const string& w : words) {
            int len = w.size();
            if (pos >= len && s.substr(pos - len, len) == w) {
                pos -= len;
                matched = true;
                break;
            }
        }
        if (!matched) {
            cout << "NO\n";
            return 0;
        }
    }

    cout << "YES\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Resolving prefix ambiguities by inverting parsing direction.
- **Reusable Pattern**: `Suffix greedy stripping: match from the end to resolve prefix collisions.`
