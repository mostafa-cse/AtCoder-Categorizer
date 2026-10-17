# Problem Analysis: AtCoder-arc120_d — Bracket Score 2

**Problem ID**: `AtCoder-arc120_d`  
**Contest**: `arc120`  
**Rating / Difficulty**: 1996  
**URL**: https://atcoder.jp/contests/arc120/tasks/arc120_d  
**VJudge Tag**: `[problem:AtCoder-arc120_d]`  
**Category File**: [`../categories/basics/extremal_bracket_pairing_stack.md`](../categories/basics/extremal_bracket_pairing_stack.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy / Invariants`  
- **Topic (Skill)**: `Extremal Pairing Upper Bound Attainment via Sign-Alternating Bracket Stack`  

---

## 1. Problem Statement & Key Idea
Given array A of length 2N. Construct a balanced bracket sequence of length 2N (with N '(' and N ')') such that matching bracket pairs (i, j) maximize sum |A_i - A_j|.

The maximum possible value of sum |A_i - A_j| over ANY pairing is to pair the N smallest elements of A with the N largest elements of A (giving sum A_large - sum A_small). We can always achieve this theoretical maximum with a valid bracket sequence! Label the N smallest elements -1 and the N largest elements +1. Process from left to right using a stack: if current element has different sign than stack top, they can form a valid matched pair (the earlier gets '(', the later gets ')'); if same sign, push to stack.

## 2. Core Observation & Invariant
Because the total number of +1 and -1 are equal (N each), any prefix with excess elements of one sign can be matched with opposite signs without violation, achieving the global upper bound.

## 3. Step-by-Step Algorithm
1. Pair each A[i] with its original index i.
2. Sort elements by value ascending.
3. Label the first N elements as -1, and the remaining N elements as +1.
4. Iterate i from 0 to 2N - 1 maintaining a stack of indices:
5.   If stack is not empty and sign[i] != sign[stack.top()]:
6.     match stack.top() and i; ans[stack.top()] = '(', ans[i] = ')'; pop stack.
7.   Else: push i to stack.
8. Print ans string.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;

struct Element {
    long long val;
    int idx;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total = 2 * n;
    vector<Element> a(total);
    for (int i = 0; i < total; ++i) {
        cin >> a[i].val;
        a[i].idx = i;
    }

    sort(a.begin(), a.end(), [](const Element& x, const Element& y) {
        return x.val < y.val;
    });

    vector<int> sign(total);
    for (int i = 0; i < total; ++i) {
        if (i < n) sign[a[i].idx] = -1;
        else sign[a[i].idx] = 1;
    }

    string ans(total, ' ');
    stack<int> st;

    for (int i = 0; i < total; ++i) {
        if (!st.empty() && sign[st.top()] != sign[i]) {
            ans[st.top()] = '(';
            ans[i] = ')';
            st.pop();
        } else {
            st.push(i);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Proving an unconstrained extremal upper bound and constructing an exact balanced bracket match using a sign stack.
- **Reusable Pattern**: `Optimal Bracket Pairing: Split into bottom N (-1) and top N (+1); match opposite signs using stack.`
