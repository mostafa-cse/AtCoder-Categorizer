# Problem Analysis: AtCoder-abc115_d — Christmas

**Problem ID**: `AtCoder-abc115_d`  
**Contest**: `abc115`  
**Rating / Difficulty**: 1088  
**URL**: https://atcoder.jp/contests/abc115/tasks/abc115_d  
**VJudge Tag**: `[problem:AtCoder-abc115_d]`  
**Category File**: [`../categories/basics/recursive_burger_fractal_search.md`](../categories/basics/recursive_burger_fractal_search.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Divide and Conquer`  
- **Topic (Skill)**: `Recursive Burger Fractal Binary Search / Tree Size Division`  

---

## 1. Problem Statement & Key Idea
A Level-0 burger is a patty 'P'. A Level-L burger consists of 'B' + (Level-(L-1) burger) + 'P' + (Level-(L-1) burger) + 'B'. Find the number of patties 'P' in the bottom X layers of a Level-N burger (N <= 50, X <= total layers).

**Key Idea**: The structure of Level-L burger is completely recursive. Precompute total layers len[L] = 2 * len[L-1] + 3 and total patties pat[L] = 2 * pat[L-1] + 1.

## 2. Core Observation & Invariant
Binary search / divide and conquer on X: (1) if X == 1: bottom is 'B', 0 patties; (2) if X <= 1 + len[L-1]: lies in first half burger -> recurse on (L-1, X - 1); (3) if X == 2 + len[L-1]: covers bottom 'B' + entire first half + middle 'P' -> pat[L-1] + 1; (4) if X <= 2 + 2*len[L-1]: covers bottom + first half + middle 'P' + part of second half -> pat[L-1] + 1 + recurse(L-1, X - 2 - len[L-1]); (5) if X == len[L]: entire burger -> pat[L].

## 3. Step-by-Step Algorithm
1. Precompute len[L] and pat[L] arrays up to N = 50.
2. Write recursive function solve(L, X) matching the 5 interval cases.
3. Output solve(N, X).

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<long long> len_b(51), pat(51);

long long solve(int l, long long x) {
    if (l == 0) return (x > 0 ? 1 : 0);
    if (x <= 1) return 0;
    if (x <= 1 + len_b[l - 1]) {
        return solve(l - 1, x - 1);
    }
    if (x == 2 + len_b[l - 1]) {
        return pat[l - 1] + 1;
    }
    if (x <= 2 + 2 * len_b[l - 1]) {
        return pat[l - 1] + 1 + solve(l - 1, x - 2 - len_b[l - 1]);
    }
    return pat[l];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long x;
    if (!(cin >> n >> x)) return 0;

    len_b[0] = 1;
    pat[0] = 1;
    for (int i = 1; i <= n; ++i) {
        len_b[i] = 2 * len_b[i - 1] + 3;
        pat[i] = 2 * pat[i - 1] + 1;
    }

    cout << solve(n, x) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Divide and conquer size partitioning on recursively generated strings.
- **Reusable Pattern**: `Recursive structure division: match query prefix against precomputed segment lengths.`
