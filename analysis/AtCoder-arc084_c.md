# Problem Analysis: AtCoder-arc084_c — Finite Encyclopedia of Integer Sequences

**Problem ID**: `AtCoder-arc084_c`  
**Contest**: `arc084`  
**Rating / Difficulty**: 2703  
**URL**: https://atcoder.jp/contests/arc084/tasks/arc084_c  
**VJudge Tag**: `[problem:AtCoder-arc084_c]`  
**Category File**: [`../categories/basics/finite_encyclopedia_median_sequence.md`](../categories/basics/finite_encyclopedia_median_sequence.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Basic Counting`  
- **Topic (Skill)**: `Permutations, Combinations and Basic Counting Problems`  

---

## 1. Problem Statement & Key Idea
Finding the ceil(X/2)-th lexicographically smallest sequence of length 1..N with elements in 1..K. If K is even, exactly half of all sequences start with <= K/2, so the median is K/2 followed by N-1 copies of K. If K is odd, sequences symmetric under x -> K+1-x are precisely the N prefixes of (K+1)/2... (K+1)/2, placing that sequence at rank X/2 + N/2. The median is reached by stepping backwards floor(N/2) times in lexicographical order in O(N) amortized time.

## 2. Core Observation & Invariant
Stepping one step backwards in lexicographical order: if the sequence ends in 1, pop the 1; otherwise, decrement the last element and append copies of K until length reaches N. This amortizes to O(1) per step.

## 3. Step-by-Step Algorithm
1. 1. If K is even: output K/2 followed by N-1 copies of K.
2. 2. If K is odd:
3.    - Start with sequence of N copies of (K+1)/2.
4.    - Repeat floor(N/2) times: if seq.back() == 1, pop_back(); else decrement seq.back() and while len < N, append K.
5.    - Print sequence.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, n;
    if (!(cin >> k >> n)) return 0;

    if (k % 2 == 0) {
        cout << k / 2;
        for (int i = 1; i < n; ++i) {
            cout << " " << k;
        }
        cout << "\n";
        return 0;
    }

    // K is odd
    int m = (k + 1) / 2;
    vector<int> seq(n, m);

    int steps = n / 2;
    for (int s = 0; s < steps; ++s) {
        if (seq.back() == 1) {
            seq.pop_back();
        } else {
            seq.back()--;
            while ((int)seq.size() < n) {
                seq.push_back(k);
            }
        }
    }

    for (size_t i = 0; i < seq.size(); ++i) {
        cout << seq[i] << (i + 1 == seq.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
