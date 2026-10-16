# Problem Analysis: AtCoder-abc170_d — Not Divisible

**Problem ID**: `AtCoder-abc170_d`  
**Contest**: `abc170`  
**Rating / Difficulty**: 1033  
**URL**: https://atcoder.jp/contests/abc170/tasks/abc170_d  
**VJudge Tag**: `[problem:AtCoder-abc170_d]`  
**Category File**: [`../categories/number_theory/sieve_multiples_marking.md`](../categories/number_theory/sieve_multiples_marking.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Sieve & Multiples`  
- **Topic (Skill)**: `Sieve Divisor Elimination / Multiples Marking`  

---

## 1. Problem Statement & Key Idea
Given an array A of N positive integers. Count the number of elements A_i such that A_i is not divisible by any other element A_j (j != i) in the array.

**Key Idea**: Instead of checking all pairs O(N^2), use a harmonic sieve: count frequencies of each number, and mark all strict multiples 2x, 3x, 4x... as eliminated.

## 2. Core Observation & Invariant
Let MAX = 10^6. An element x can be selected if and only if: (1) x appears exactly once in A; (2) no smaller element in A divides x. Marking multiples takes sum MAX/x = O(MAX log MAX).

## 3. Step-by-Step Algorithm
1. Count frequencies of all numbers in array: count[x].
2. Initialize boolean array eliminated[MAX + 1] to false.
3. For each x from 1 to MAX: if count[x] > 0: mark eliminated[2*x], eliminated[3*x]... as true; if count[x] > 1, mark eliminated[x] = true.
4. Count elements A[i] where !eliminated[A[i]].
5. Print the count.

## 4. Complexity Analysis
- **Time Complexity**: `O(MAX log MAX + N)`
- **Space Complexity**: `O(MAX)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 1000000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    vector<int> freq(MAX + 1, 0);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        freq[a[i]]++;
    }

    vector<bool> bad(MAX + 1, false);

    for (int x = 1; x <= MAX; ++x) {
        if (freq[x] > 0) {
            for (int mult = 2 * x; mult <= MAX; mult += x) {
                bad[mult] = true;
            }
            if (freq[x] > 1) {
                bad[x] = true;
            }
        }
    }

    int ans = 0;
    for (int x : a) {
        if (!bad[x]) {
            ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Harmonic sieve elimination for pairwise divisibility constraints.
- **Reusable Pattern**: `Harmonic multiples marking: for present x, mark 2x, 3x, 4x... as invalid.`
