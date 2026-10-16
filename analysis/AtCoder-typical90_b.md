# Problem Analysis: AtCoder-typical90_b — Encyclopedia of Parentheses

**Problem ID**: `AtCoder-typical90_b`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 002)  
**Rating / Difficulty**: 800 (★3)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_b  
**VJudge Tag**: `[problem:AtCoder-typical90_b]`  
**Category File**: [`../categories/basics/recursive_backtracking.md`](../categories/basics/recursive_backtracking.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Backtracking & Recursion`  
- **Topic (Skill)**: `Recursive Backtracking & Prefix Balance Invariant`  

---

## 1. Problem Statement & Key Idea
Print all valid parentheses strings of length N in lexicographical order. N <= 16.

**Core Idea**: A parenthesis string is valid iff total '(' equals total ')' and in every prefix, count('(') >= count(')').

## 2. Core Observation & Invariant
Since N <= 16 is small, recursive backtracking placing '(' before ')' naturally generates all Catalan(N/2) valid strings in strict lexicographical order without sorting.

## 3. Step-by-Step Algorithm
1. If N is odd, return immediately (no valid strings).
2. Recursive DFS(s, open_count, close_count):
   - If len(s) == N: output s.
   - If open_count < N/2: DFS(s + '(', open_count + 1, close_count).
   - If close_count < open_count: DFS(s + ')', open_count, close_count + 1).

## 4. Complexity Analysis
Time: O(Catalan(N/2) * N), Space: O(N) recursion stack.

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>

using namespace std;

void dfs(string& s, int open_cnt, int close_cnt, int n) {
    if ((int)s.size() == n) {
        cout << s << "\n";
        return;
    }
    if (open_cnt < n / 2) {
        s.push_back('(');
        dfs(s, open_cnt + 1, close_cnt, n);
        s.pop_back();
    }
    if (close_cnt < open_cnt) {
        s.push_back(')');
        dfs(s, open_cnt, close_cnt + 1, n);
        s.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n % 2 != 0) return 0;

    string s;
    dfs(s, 0, 0, n);
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Backtracking or bitmask simulation checking Dyck path prefix non-negativity.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Parenthesis validity invariants, Dyck paths, and lexicographical recursive search without sorting.
- **Reusable Pattern**: `Prefix balance invariant backtracking.`

---
Back to [Recursive Backtracking & Prefix Balance Invariant](../categories/basics/recursive_backtracking.md) | [Categories Directory](../categories/README.md)