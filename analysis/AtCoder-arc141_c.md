# Problem Analysis: AtCoder-arc141_c — C. Bracket Manufacture

**Problem ID**: `AtCoder-arc141_c`  
**Contest**: `arc141`  
**Rating / Difficulty**: 2342  
**URL**: https://atcoder.jp/contests/arc141/tasks/arc141_c  
**VJudge Tag**: `[problem:AtCoder-arc141_c]`  
**Category File**: [`../categories/basics/bracket_sequence_permutation_reconstruction.md`](../categories/basics/bracket_sequence_permutation_reconstruction.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Reconstruct a valid bracket sequence from its lexicographically smallest and largest permutations. Adjacent inversions force bracket types, with greedy validation in $O(N)$.

## 2. Core Observation & Invariant
In the lexicographically smallest permutation $P$ derived from a valid bracket sequence $S$, consecutive pairs $(P_{2i-1}, P_{2i})$ with $P_{2i-1} > P_{2i}$ can only occur if $S[P_{2i-1}] = '('$ and $S[P_{2i}] = ')'$. In the lexicographically largest permutation $Q$, pairs $(Q_{2i-1}, Q_{2i})$ with $Q_{2i-1} < Q_{2i}$ force $S[Q_{2i-1}] = '('$ and $S[Q_{2i}] = ')'$. Any unspecified characters can be uniquely deduced, and then validated by greedy reconstruction.

## 3. Step-by-Step Algorithm
1. Scan $P$ in adjacent pairs: if $P_{2i-1} > P_{2i}$, set $S[P_{2i-1}] = '('$ and $S[P_{2i}] = ')'$.
2. Scan $Q$ in adjacent pairs: if $Q_{2i-1} < Q_{2i}$, set $S[Q_{2i-1}] = '('$ and $S[Q_{2i}] = ')'$.
3. Fill remaining unassigned positions with alternating brackets to maintain equal counts.
4. Simulate greedy reconstruction of $P$ and $Q$ from candidate string $S$ using stacks/queues in $O(N)$ time. If they match the input, output $S$; otherwise -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

bool simulate_P(const string& s, int n, const vector<int>& target_p) {
    vector<int> open_idx, close_idx;
    for (int i = 0; i < 2 * n; ++i) {
        if (s[i] == '(') open_idx.push_back(i);
        else close_idx.push_back(i);
    }
    if ((int)open_idx.size() != n || (int)close_idx.size() != n) return false;

    int i_o = 0, i_c = 0;
    int bal = 0;
    for (int step = 0; step < 2 * n; ++step) {
        bool can_open = (i_o < n);
        bool can_close = (i_c < n && bal > 0);
        int picked = -1;
        if (can_open && can_close) {
            if (open_idx[i_o] < close_idx[i_c]) {
                picked = open_idx[i_o++];
                bal++;
            } else {
                picked = close_idx[i_c++];
                bal--;
            }
        } else if (can_open) {
            picked = open_idx[i_o++];
            bal++;
        } else if (can_close) {
            picked = close_idx[i_c++];
            bal--;
        } else {
            return false;
        }
        if (picked + 1 != target_p[step]) return false;
    }
    return true;
}

bool simulate_Q(const string& s, int n, const vector<int>& target_q) {
    vector<int> open_idx, close_idx;
    for (int i = 0; i < 2 * n; ++i) {
        if (s[i] == '(') open_idx.push_back(i);
        else close_idx.push_back(i);
    }
    if ((int)open_idx.size() != n || (int)close_idx.size() != n) return false;

    int i_o = n - 1, i_c = n - 1;
    int bal = 0;
    for (int step = 0; step < 2 * n; ++step) {
        int rem_steps = 2 * n - step;
        bool can_open = (i_o >= 0 && bal + 2 <= rem_steps);
        bool can_close = (i_c >= 0 && bal > 0);
        int picked = -1;
        if (can_open && can_close) {
            if (open_idx[i_o] > close_idx[i_c]) {
                picked = open_idx[i_o--];
                bal++;
            } else {
                picked = close_idx[i_c--];
                bal--;
            }
        } else if (can_open) {
            picked = open_idx[i_o--];
            bal++;
        } else if (can_close) {
            picked = close_idx[i_c--];
            bal--;
        } else {
            return false;
        }
        if (picked + 1 != target_q[step]) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(2 * n), q(2 * n);
    for (int i = 0; i < 2 * n; ++i) cin >> p[i];
    for (int i = 0; i < 2 * n; ++i) cin >> q[i];

    string s(2 * n, '?');

    for (int i = 0; i < n; ++i) {
        int u = p[2 * i] - 1;
        int v = p[2 * i + 1] - 1;
        if (u > v) {
            s[u] = '(';
            s[v] = ')';
        } else {
            if (s[u] == '?') s[u] = '(';
            if (s[v] == '?') s[v] = ')';
        }
    }

    for (int i = 0; i < n; ++i) {
        int u = q[2 * i] - 1;
        int v = q[2 * i + 1] - 1;
        if (u < v) {
            if (s[u] == ')') { cout << -1 << "\n"; return 0; }
            s[u] = '(';
            if (s[v] == '(') { cout << -1 << "\n"; return 0; }
            s[v] = ')';
        } else {
            if (s[u] == '?') s[u] = '(';
            if (s[v] == '?') s[v] = ')';
        }
    }

    for (char c : s) {
        if (c == '?') {
            cout << -1 << "\n";
            return 0;
        }
    }

    if (simulate_P(s, n, p) && simulate_Q(s, n, q)) {
        cout << s << "\n";
    } else {
        cout << -1 << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
