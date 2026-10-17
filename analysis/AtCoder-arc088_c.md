# Problem Analysis: AtCoder-arc088_c — Papple Sort

**Problem ID**: `AtCoder-arc088_c`  
**Contest**: `arc088`  
**Rating / Difficulty**: 2231  
**URL**: https://atcoder.jp/contests/arc088/tasks/arc088_c  
**VJudge Tag**: `[problem:AtCoder-arc088_c]`  
**Category File**: [`../categories/basics/papple_sort_palindrome_adjacent_swaps_greedy_fenwick.md`](../categories/basics/papple_sort_palindrome_adjacent_swaps_greedy_fenwick.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Find the minimum number of adjacent swaps to transform a string of length N <= 2 * 10^5 into a palindrome, or report -1 if impossible.

## 2. Core Observation & Invariant
A palindrome is possible iff at most one character has an odd frequency. In an optimal swap sequence, identical characters never cross each other. Processing characters greedily from left to right, we match each character with its rightmost available twin, assigning them symmetric target positions at the current outer boundaries. The minimum swaps to achieve this target configuration equals the inversion count of the target permutation, solvable in O(N log N) via Fenwick tree.

## 3. Step-by-Step Algorithm
1. 1. Check character frequencies; if more than 1 character has odd count, return -1.
2. 2. Store 0-indexed positions of each character in double-ended queues.
3. 3. Maintain left pointer L = 0 and right pointer R = N - 1.
4. 4. Scan original string from left to right:
5.    - If current character is the unique odd character's middle occurrence, assign target[i] = N / 2.
6.    - Otherwise, match S[i] with its rightmost unmatched twin j = pos[c].pop_back(), assigning target[i] = L++ and target[j] = R--.
7. 5. Compute inversions of the assigned target permutation using a Fenwick tree.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <deque>

using namespace std;

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;

    int n = s.length();
    vector<deque<int>> pos(26);
    for (int i = 0; i < n; ++i) {
        pos[s[i] - 'a'].push_back(i);
    }

    int odd_count = 0;
    int mid_idx = -1;
    for (int c = 0; c < 26; ++c) {
        if (pos[c].size() % 2 == 1) {
            odd_count++;
            mid_idx = pos[c][pos[c].size() / 2];
        }
    }

    if (odd_count > 1) {
        cout << -1 << "\n";
        return 0;
    }

    vector<int> target(n, -1);
    int L = 0, R = n - 1;

    for (int i = 0; i < n; ++i) {
        if (target[i] != -1) continue;
        int c = s[i] - 'a';
        if (i == mid_idx) {
            target[i] = n / 2;
            pos[c].pop_front();
            continue;
        }

        int j = pos[c].back();
        pos[c].pop_back();
        pos[c].pop_front();

        target[i] = L++;
        target[j] = R--;
    }

    Fenwick bit(n);
    long long inv = 0;
    for (int i = 0; i < n; ++i) {
        int val = target[i] + 1; // 1-based
        inv += i - bit.query(val);
        bit.add(val, 1);
    }

    cout << inv << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
