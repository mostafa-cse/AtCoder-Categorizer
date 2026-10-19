# Problem Analysis: AtCoder-agc012_c — C - Tautonym Puzzle

**Problem ID**: `AtCoder-agc012_c`  
**Contest**: `agc012`  
**Rating / Difficulty**: 2731  
**URL**: https://atcoder.jp/contests/agc012/tasks/agc012_c  
**VJudge Tag**: `[problem:AtCoder-agc012_c]`  
**Category File**: [`../categories/basics/tautonym_puzzle_lis_constructive.md`](../categories/basics/tautonym_puzzle_lis_constructive.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Find a string s of integers from 1..100 with |s| <= 200 such that exactly N subsequences of s are 'good' (of the form y + y for |y| >= 1), where 1 <= N <= 10^{12}.

## 2. Core Observation & Invariant
Construct s as P + Q, where P = (1, 2, ..., k) and Q is a permutation of (1, 2, ..., k). Because each character in 1..k appears exactly once in P and once in Q, any good subsequence y + y must have its first copy in P and second copy in Q. Since P is sorted 1..k, y must be an INCREASING subsequence of Q! Thus, the number of good subsequences of s is precisely the number of non-empty increasing subsequences of Q. Appending an element to the right of Q doubles the count of increasing subsequences (including empty), while prepending an element to the left increments the count by 1. Using Horner's rule on the binary representation of N + 1, we construct Q with k <= 55 elements.

## 3. Step-by-Step Algorithm
1. 1. Write N + 1 in binary.
2. 2. Start with an empty sequence for the most significant bit.
3. 3. For each subsequent bit from MSB-1 down to 0:
4.    a. Insert a new element cur_val at the right (simulating doubling the count).
5.    b. If the bit is 1, insert a new element cur_val at the left (simulating adding 1).
6. 4. Assemble Q = Q_left + Q_right, and P = (1, 2, ..., k).
7. 5. Output length 2*k and sequence P + Q.

## 4. Complexity Analysis
- **Time Complexity**: `O(log N)`
- **Space Complexity**: `O(log N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N;
    if (!(cin >> N)) return 0;

    long long target = N + 1;
    vector<int> bits;
    while (target > 0) {
        bits.push_back(target & 1);
        target >>= 1;
    }
    reverse(bits.begin(), bits.end());

    int cur_val = 1;
    vector<int> Q_left;
    vector<int> Q_right;

    for (size_t i = 1; i < bits.size(); ++i) {
        Q_right.push_back(cur_val++);
        if (bits[i] == 1) {
            Q_left.push_back(cur_val++);
        }
    }

    reverse(Q_left.begin(), Q_left.end());
    vector<int> Q = Q_left;
    Q.insert(Q.end(), Q_right.begin(), Q_right.end());

    int k = cur_val - 1;
    vector<int> P(k);
    for (int i = 0; i < k; ++i) P[i] = i + 1;

    vector<int> s = P;
    s.insert(s.end(), Q.begin(), Q.end());

    cout << s.size() << "\n";
    for (size_t i = 0; i < s.size(); ++i) {
        cout << s[i] << (i + 1 == s.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
