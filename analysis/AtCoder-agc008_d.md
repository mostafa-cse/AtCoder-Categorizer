# Problem Analysis: AtCoder-agc008_d — K-th K

**Problem ID**: `AtCoder-agc008_d`  
**Contest**: `agc008`  
**Rating / Difficulty**: 2164  
**URL**: https://atcoder.jp/contests/agc008/tasks/agc008_d  
**VJudge Tag**: `[problem:AtCoder-agc008_d]`  
**Category File**: [`../categories/basics/earliest_deadline_first_multi_occurrence_scheduling.md`](../categories/basics/earliest_deadline_first_multi_occurrence_scheduling.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Greedy Algorithms`  

---

## 1. Problem Statement & Key Idea
Construct an array of length N^2 containing N copies of each 1..N such that the i-th occurrence of i is at index x_i. Solved by Earliest Deadline First (EDF) greedy scheduling.

## 2. Core Observation & Invariant
For each number i, exactly i-1 copies must appear before position x_i, and N-i copies must appear after position x_i. The prefix placement is an interval scheduling problem with deadlines x_i: processing i in increasing order of x_i and greedily placing copies in the leftmost available slots guarantees feasibility if one exists. Suffix placement is handled symmetrically from right to left in decreasing order of x_i.

## 3. Step-by-Step Algorithm
1. Place each fixed occurrence a[x_i] = i.
2. Sort elements in increasing order of x_i. For each element i, find the earliest i - 1 empty slots from left to right; if any slot index exceeds x_i, output "No".
3. Sort elements in decreasing order of x_i. For each element i, find the latest N - i empty slots from right to left; if any slot index is less than x_i, output "No".
4. If both passes succeed, output "Yes" and the resulting array a.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Element {
    int id;
    int x;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<Element> elems(n);
    vector<int> a(n * n + 1, 0);

    for (int i = 0; i < n; ++i) {
        elems[i].id = i + 1;
        cin >> elems[i].x;
        a[elems[i].x] = i + 1;
    }

    sort(elems.begin(), elems.end(), [](const Element& e1, const Element& e2) {
        return e1.x < e2.x;
    });

    int ptr = 1;
    for (const auto& e : elems) {
        int need = e.id - 1;
        for (int k = 0; k < need; ++k) {
            while (ptr <= n * n && a[ptr] != 0) ptr++;
            if (ptr > e.x) {
                cout << "No\n";
                return 0;
            }
            a[ptr] = e.id;
        }
    }

    sort(elems.begin(), elems.end(), [](const Element& e1, const Element& e2) {
        return e1.x > e2.x;
    });

    ptr = n * n;
    for (const auto& e : elems) {
        int need = n - e.id;
        for (int k = 0; k < need; ++k) {
            while (ptr >= 1 && a[ptr] != 0) ptr--;
            if (ptr < e.x) {
                cout << "No\n";
                return 0;
            }
            a[ptr] = e.id;
        }
    }

    cout << "Yes\n";
    for (int i = 1; i <= n * n; ++i) {
        cout << a[i] << (i == n * n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
