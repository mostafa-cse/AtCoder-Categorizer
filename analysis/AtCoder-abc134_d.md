# Problem Analysis: AtCoder-abc134_d — Preparing Boxes

**Problem ID**: `AtCoder-abc134_d`  
**Contest**: `abc134`  
**Rating / Difficulty**: 926  
**URL**: https://atcoder.jp/contests/abc134/tasks/abc134_d  
**VJudge Tag**: `[problem:AtCoder-abc134_d]`  
**Category File**: [`../categories/math/harmonic_back_substitution.md`](../categories/math/harmonic_back_substitution.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Constructive Algorithms`  
- **Topic (Skill)**: `Reverse Multiples Harmonic Greedy / Back-Substitution`  

---

## 1. Problem Statement & Key Idea
N boxes numbered 1..N. Choose whether to place a ball in box i (b_i in {0, 1}). For each i, the total balls in boxes that are multiples of i must have parity a_i. Output a valid assignment.

**Key Idea**: Multiples of i are always > i (for multiplier >= 2). Thus, box N has no other multiples in [1..N], forcing b_N = a_N uniquely.

## 2. Core Observation & Invariant
Determining b_i in decreasing order from N down to 1: when deciding b_i, all strict multiples 2i, 3i, 4i... have already been determined! Therefore, b_i is uniquely forced: b_i = (a_i XOR sum_{k >= 2} b_{k*i}) % 2. Total steps across all i is sum N/i = O(N log N).

## 3. Step-by-Step Algorithm
1. Iterate i from N down to 1.
2. Compute current sum of balls in strict multiples: sum = sum_{k=2}^{N/i} b[k * i].
3. Set b[i] = (a[i] ^ (sum % 2)).
4. Collect all indices i where b[i] == 1 and print count followed by indices.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<int> b(n + 1, 0);
    vector<int> chosen;

    for (int i = n; i >= 1; --i) {
        int sum = 0;
        for (int j = 2 * i; j <= n; j += i) {
            sum ^= b[j];
        }
        b[i] = a[i] ^ sum;
        if (b[i] == 1) {
            chosen.push_back(i);
        }
    }

    cout << chosen.size() << "\n";
    for (size_t i = 0; i < chosen.size(); ++i) {
        cout << chosen[i] << (i + 1 == chosen.size() ? '\n' : ' ');
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Back-substitution on triangular multiple systems in harmonic time.
- **Reusable Pattern**: `Harmonic back-substitution: iterate backwards N..1, checking multiples k*i.`
