# Problem Analysis: AtCoder-abc299_g — Minimum Permutation

**Problem ID**: `AtCoder-abc299_g`  
**Contest**: `abc299`  
**Rating / Difficulty**: 2066  
**URL**: https://atcoder.jp/contests/abc299/tasks/abc299_g  
**VJudge Tag**: `[problem:AtCoder-abc299_g]`  
**Category File**: [`../categories/data_structures/monotonic_stack_lexicographical_permutation.md`](../categories/data_structures/monotonic_stack_lexicographical_permutation.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Monotonic Queue / Deque`  
- **Topic (Skill)**: `Monotonic Stack with Frequency/Last-Occurrence Tracking for Lexicographically Minimal Permutation`  

---

## 1. Problem Statement & Key Idea
Given a sequence A of length N containing numbers from 1 to M, where every number appears at least once. Find the lexicographically smallest subsequence of length M that contains each number from 1 to M exactly once.

**Key Idea**: We use a monotonic stack and track the last occurrence index last_pos[x] of each value. When processing A[i] = x: if x is already in the stack, we skip it. Otherwise, while the stack is non-empty, top element y > x, and y appears again later in A (last_pos[y] > i), we pop y from the stack and unmark it. We then push x and mark it. The resulting stack contains the unique lexicographically smallest permutation.

## 2. Core Observation & Invariant
A larger character y can be popped in favor of a smaller character x iff y appears again later in the sequence.

## 3. Step-by-Step Algorithm
1. Precompute last_pos[x] for every value x in 1..M.
2. Initialize an empty stack and a boolean array in_st.
3. Iterate i from 0 to N - 1 with x = A[i]:
4.   If in_st[x] is true, continue.
5.   While stack is not empty, stack.back() > x, and last_pos[stack.back()] > i: in_st[stack.back()] = false; stack.pop_back().
6.   Push x onto stack and set in_st[x] = true.
7. Output the M elements of the stack.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N + M)`

## 5. Core Algorithmic Skill & Learning Takeaway
Greedy subsequence construction using a monotonic stack with future availability validation.

**Reusable Pattern**: Smallest subsequence with unique characters: pop stack when top > current and top appears later.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(n);
    vector<int> last_pos(m + 1, -1);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        last_pos[a[i]] = i;
    }

    vector<int> st;
    vector<bool> in_st(m + 1, false);

    for (int i = 0; i < n; ++i) {
        int x = a[i];
        if (in_st[x]) continue;

        while (!st.empty() && st.back() > x && last_pos[st.back()] > i) {
            in_st[st.back()] = false;
            st.pop_back();
        }

        st.push_back(x);
        in_st[x] = true;
    }

    for (int i = 0; i < m; ++i) {
        cout << st[i] << (i == m - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```
