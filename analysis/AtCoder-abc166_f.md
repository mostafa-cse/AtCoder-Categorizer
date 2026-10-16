# Problem Analysis: AtCoder-abc166_f — Three Variables Game

**Problem ID**: `AtCoder-abc166_f`  
**Contest**: `abc166`  
**Rating / Difficulty**: 1668  
**URL**: https://atcoder.jp/contests/abc166/tasks/abc166_f  
**VJudge Tag**: `[problem:AtCoder-abc166_f]`  
**Category File**: [`../categories/basics/greedy_lookahead_invariant_sum.md`](../categories/basics/greedy_lookahead_invariant_sum.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy Algorithms`  
- **Topic (Skill)**: `Greedy Lookahead with Invariant Sum Constrained State`  

---

## 1. Problem Statement & Key Idea
Three integers A, B, C with A + B + C <= 2. In N rounds, a string S_i in {'AB', 'BC', 'AC'} specifies two variables: increment one and decrement the other. Maintain all variables >= 0 throughout all N rounds, or output 'No'.

**Key Insight**: The sum A + B + C is strictly conserved! If sum == 0, impossible. If sum == 1: at each step, exactly one variable is positive and one is zero, leaving no choice. If sum == 2: when both variables are positive (1, 1), use 1-STEP LOOKAHEAD to increment the variable needed in the next round!

## 2. Core Observation & Invariant
When faced with choices (A=1, B=1) for query 'AB': looking at S_{i+1}, if S_{i+1} involves A, increment A (so A becomes 2 and can survive decrement in round i+1); else increment B.

## 3. Step-by-Step Algorithm
1. If A + B + C == 0, print 'No'.
2. Simulate round i from 0 to N - 1:
3.   Let variables be u and v.
4.   If val[u] == 0 and val[v] == 0: print 'No'.
5.   If val[u] == 0: increment u, decrement v, record u.
6.   Else if val[v] == 0: increment v, decrement u, record v.
7.   Else (val[u] == 1 and val[v] == 1):
8.     If i + 1 < N and (S[i+1][0] == u || S[i+1][1] == u): increment u, decrement v, record u.
9.     Else: increment v, decrement u, record v.
10. Print 'Yes', then all choices.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long val[3];
    if (!(cin >> n >> val[0] >> val[1] >> val[2])) return 0;

    vector<string> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }

    vector<char> moves;

    for (int i = 0; i < n; ++i) {
        int u = s[i][0] - 'A';
        int v = s[i][1] - 'A';

        if (val[u] == 0 && val[v] == 0) {
            cout << "No\n";
            return 0;
        }

        if (val[u] == 0) {
            val[u]++;
            val[v]--;
            moves.push_back('A' + u);
        } else if (val[v] == 0) {
            val[v]++;
            val[u]--;
            moves.push_back('A' + v);
        } else {
            // Both are positive (val[u] == 1, val[v] == 1)
            // Look ahead to next query
            if (i + 1 < n && (s[i + 1][0] - 'A' == u || s[i + 1][1] - 'A' == u)) {
                val[u]++;
                val[v]--;
                moves.push_back('A' + u);
            } else {
                val[v]++;
                val[u]--;
                moves.push_back('A' + v);
            }
        }
    }

    cout << "Yes\n";
    for (char c : moves) {
        cout << c << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: 1-step lookahead greedy tie-breaking under strict resource invariance.
- **Reusable Pattern**: `Conserved Sum Game Lookahead: when both variables > 0, increment the one needed next.`
