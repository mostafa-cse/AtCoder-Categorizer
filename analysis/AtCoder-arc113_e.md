# Problem Analysis: AtCoder-arc113_e — E - Rvom and Rsrev

**Problem ID**: `AtCoder-arc113_e`  
**Contest**: `arc113`  
**Rating / Difficulty**: 2789  
**URL**: https://atcoder.jp/contests/arc113/tasks/arc113_e  
**VJudge Tag**: `[problem:AtCoder-arc113_e]`  
**Category File**: [`../categories/basics/lexicographically_greatest_string_greedy_reduction.md`](../categories/basics/lexicographically_greatest_string_greedy_reduction.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Given a string S consisting of 'a' and 'b', you can repeatedly delete adjacent identical characters or invert/reverse substrings. Find the lexicographically largest string that can be formed.

## 2. Core Observation & Invariant
The operations allow cancelling pairs of 'a's and shifting 'b's forward. The optimal string consists of a maximal prefix of 'b's followed by minimal 'a's, or leading 'b's with specific trailing patterns. The exact trailing sequence depends on the total count of 'a's, whether the last character of S is 'a', and whether pairs of 'a's can be cancelled without destroying 'b' runs. By decomposing S into runs of 'a' and 'b', we can evaluate a small number of candidate optimal reductions and take the lexicographically maximum.

## 3. Step-by-Step Algorithm
1. 1. If S contains only 'a's, output '' if |S| is even, or 'a' if |S| is odd.
2. 2. Count total 'a's and 'b's. All 'b's can always be collected.
3. 3. Construct candidates:
4.    - Candidate 1: all 'b's followed by (total_a % 2) 'a's.
5.    - Candidate 2: all 'b's except possibly the last run, preserving suffix 'a's if advantageous.
6. 4. Lexicographically compare candidate strings.
7. 5. Output the maximum candidate.

## 4. Complexity Analysis
- **Time Complexity**: `O(|S|)`
- **Space Complexity**: `O(|S|)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void solve_test() {
    string s;
    if (!(cin >> s)) return;

    int ca = 0, cb = 0;
    for (char c : s) {
        if (c == 'a') ca++;
        else cb++;
    }

    if (cb == 0 || ca == 0) {
        cout << s << "\n";
        return;
    }

    if (s.back() == 'a') {
        int k = s.length();
        while (k > 0 && s[k - 1] == 'a') k--;

        int x = 0, y = 0;
        int cur_len = 0;
        for (int i = 0; i < k; ++i) {
            if (s[i] == 'a') {
                cur_len++;
            } else {
                if (cur_len == 1) x++;
                else if (cur_len >= 2) y++;
                cur_len = 0;
            }
        }
        if (cur_len == 1) x++;
        else if (cur_len >= 2) y++;

        int phi = x + 2 * y;
        int ops = (phi + 1) / 2;
        int t = ca - 2 * ops;

        string ans(cb, 'b');
        ans.append(t, 'a');
        cout << ans << "\n";
    } else {
        // Ends with 'b'
        if (ca % 2 == 0) {
            cout << string(cb, 'b') << "\n";
            return;
        }

        int k = s.length();
        while (k > 0 && s[k - 1] == 'b') k--;
        int trailing_b = (int)s.length() - k;

        if (trailing_b == 1) {
            cout << string(cb - 1, 'b') + "ab\n";
        } else if (trailing_b == 2) {
            cout << string(cb - 2, 'b') + "abb\n";
        } else {
            // trailing_b >= 3
            int first_b = s.find('b');
            if (first_b >= (int)s.length() - trailing_b) {
                cout << "a" + string(cb, 'b') << "\n";
                return;
            }

            // Check if "baa" appears in s[0 ... k]
            bool has_len_ge_2 = false;
            for (int i = 0; i <= k - 2; ++i) {
                if (s[i] == 'b' && s[i + 1] == 'a' && s[i + 2] == 'a') {
                    has_len_ge_2 = true;
                    break;
                }
            }

            int x = 0, y = 0;
            int cur_len = 0;
            for (int i = 0; i < k; ++i) {
                if (s[i] == 'a') {
                    cur_len++;
                } else {
                    if (cur_len == 1) x++;
                    else if (cur_len >= 2) y++;
                    cur_len = 0;
                }
            }
            if (cur_len == 1) x++;
            else if (cur_len >= 2) y++;

            int phi = x + 2 * y;
            int total_ops = 0;
            if (has_len_ge_2) {
                total_ops = (phi + 1) / 2;
            } else {
                if (phi % 2 == 1) {
                    total_ops = (phi + 1) / 2;
                } else {
                    total_ops = phi / 2 + 1;
                }
            }

            int a_ops = total_ops - 1;
            int t = ca - 2 * a_ops;

            string ans(cb - 2, 'b');
            ans.append(t, 'a');
            cout << ans << "\n";
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) {
            solve_test();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
