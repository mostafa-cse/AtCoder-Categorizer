# Problem Analysis: AtCoder-abc161_d — Lunlun Number

**Problem ID**: `AtCoder-abc161_d`  
**Contest**: `abc161`  
**Rating / Difficulty**: 991  
**URL**: https://atcoder.jp/contests/abc161/tasks/abc161_d  
**VJudge Tag**: `[problem:AtCoder-abc161_d]`  
**Category File**: [`../categories/basics/digit_bfs_queue_generation.md`](../categories/basics/digit_bfs_queue_generation.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `BFS / State Generation`  
- **Topic (Skill)**: `Digit BFS Queue Generation / Monotonic Transition`  

---

## 1. Problem Statement & Key Idea
A positive integer is a 'Lunlun number' if the absolute difference between any two adjacent decimal digits is at most 1. Find the K-th smallest Lunlun number (K <= 10^5).

**Key Idea**: Lunlun numbers can be generated in strictly increasing order by digit length using a queue (Breadth-First Search).

## 2. Core Observation & Invariant
Start with single digits 1..9 in a queue. Pop number x with last digit d = x % 10. The next valid Lunlun numbers extending x are obtained by appending d - 1 (if d > 0), d, and d + 1 (if d < 9). Because we push numbers in increasing order of value, popping K times yields the exact K-th smallest Lunlun number.

## 3. Step-by-Step Algorithm
1. Initialize queue<long long> q with 1, 2, ..., 9.
2. Loop k times: pop x = q.front(). If current iteration is K, output x and exit.
3. Let last_digit = x % 10.
4. If last_digit > 0: push x * 10 + (last_digit - 1).
5. Push x * 10 + last_digit.
6. If last_digit < 9: push x * 10 + (last_digit + 1).

## 4. Complexity Analysis
- **Time Complexity**: `O(K)`
- **Space Complexity**: `O(K)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    queue<long long> q;
    for (int i = 1; i <= 9; ++i) {
        q.push(i);
    }

    long long current = 0;
    for (int step = 0; step < k; ++step) {
        current = q.front();
        q.pop();

        int last = current % 10;
        if (last > 0) q.push(current * 10 + (last - 1));
        q.push(current * 10 + last);
        if (last < 9) q.push(current * 10 + (last + 1));
    }

    cout << current << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Generating structured digits in lexicographical numerical order via BFS queue.
- **Reusable Pattern**: `Digit BFS: seed 1..9, pop x, push valid 10*x + (d + delta).`
