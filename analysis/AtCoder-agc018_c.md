# Problem Analysis: AtCoder-agc018_c — C. Coins

**Problem ID**: `AtCoder-agc018_c`  
**Contest**: `agc018`  
**Rating / Difficulty**: 2618  
**URL**: https://atcoder.jp/contests/agc018/tasks/agc018_c  
**VJudge Tag**: `[problem:AtCoder-agc018_c]`  
**Category File**: [`../categories/basics/coins_exchange_sort_priority_queue.md`](../categories/basics/coins_exchange_sort_priority_queue.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Standard Template Library (STL)`  
- **Topic (Skill)**: `Priority Queue / Heap`  

---

## 1. Problem Statement & Key Idea
Given N = X + Y + Z people where person i has A_i gold, B_i silver, and C_i bronze coins. Select X people for gold, Y for silver, and Z for bronze to maximize total coins.

## 2. Core Observation & Invariant
Give everyone bronze coins as base sum sum C_i. Person i provides net gain A_i - C_i for gold and B_i - C_i for silver. By exchange argument, people chosen for gold lie to the left of people chosen for silver when sorted in descending order of (A_i - B_i).

## 3. Step-by-Step Algorithm
1. Sort people by (A_i - B_i) descending.
2. Compute prefix array pref[k]: maximum sum of X elements of (A_i - C_i) among first k people using a min-heap.
3. Compute suffix array suff[k]: maximum sum of Y elements of (B_i - C_i) among people from k to N using a min-heap.
4. Iterate split point k in [X, X+Z] and maximize pref[k] + suff[k+1].

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <numeric>
#include <algorithm>

using namespace std;

struct Person {
    long long A, B, C;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int X, Y, Z;
    if (!(cin >> X >> Y >> Z)) return 0;

    int N = X + Y + Z;
    vector<Person> people(N);
    long long base = 0;

    for (int i = 0; i < N; ++i) {
        cin >> people[i].A >> people[i].B >> people[i].C;
        base += people[i].C;
    }

    sort(people.begin(), people.end(), [](const Person& p1, const Person& p2) {
        return (p1.A - p1.B) > (p2.A - p2.B);
    });

    vector<long long> pref(N + 1, 0);
    priority_queue<long long, vector<long long>, greater<long long>> pq_min;
    long long cur_sum = 0;

    for (int i = 0; i < N; ++i) {
        long long val = people[i].A - people[i].C;
        pq_min.push(val);
        cur_sum += val;
        if ((int)pq_min.size() > X) {
            cur_sum -= pq_min.top();
            pq_min.pop();
        }
        if ((int)pq_min.size() == X) {
            pref[i + 1] = cur_sum;
        }
    }

    vector<long long> suff(N + 2, 0);
    while (!pq_min.empty()) pq_min.pop();
    cur_sum = 0;

    for (int i = N - 1; i >= 0; --i) {
        long long val = people[i].B - people[i].C;
        pq_min.push(val);
        cur_sum += val;
        if ((int)pq_min.size() > Y) {
            cur_sum -= pq_min.top();
            pq_min.pop();
        }
        if ((int)pq_min.size() == Y) {
            suff[i + 1] = cur_sum;
        }
    }

    const long long INF = 1e18;
    long long best = -INF;
    for (int k = X; k <= X + Z; ++k) {
        best = max(best, pref[k] + suff[k + 1]);
    }

    cout << (base + best) << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
