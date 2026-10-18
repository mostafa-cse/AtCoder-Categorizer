# Problem Analysis: AtCoder-arc147_e — E. Examination

**Problem ID**: `AtCoder-arc147_e`  
**Contest**: `arc147`  
**Rating / Difficulty**: 2553  
**URL**: https://atcoder.jp/contests/arc147/tasks/arc147_e  
**VJudge Tag**: `[problem:AtCoder-arc147_e]`  
**Category File**: [`../categories/graph_theory/examination_halls_marriage_theorem_greedy.md`](../categories/graph_theory/examination_halls_marriage_theorem_greedy.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Matching`  
- **Topic (Skill)**: `Halls Theorem`  

---

## 1. Problem Statement & Key Idea
Students have score $A_i$ and need $B_i$. Swapping scores between students can make everyone graduate ($A'_i \ge B_i$) iff for all $x$, $\text{count}(A \ge x) \ge \text{count}(B \ge x)$ by Hall's Marriage Theorem. Students with $A_i < B_i$ are mandatory swaps. For students with $A_i \ge B_i$, we want to keep as many unchanged as possible. Each helper student $j$ added to the swap pool covers the deficit on interval $[B_j, A_j - 1]$.

## 2. Core Observation & Invariant
Sweep values from largest to smallest. Maintain suffix balance of scores. Helper students $j$ with $A_j \ge B_j$ become available when the sweep passes $A_j$; push their $B_j$ into a min-priority queue. Whenever the suffix balance falls below 0, pop the smallest $B_j$ from the queue to fix the deficit as far into the future as possible. If the queue is empty while balance $< 0$, no solution exists (output -1).

## 3. Step-by-Step Algorithm
1. 1. Check global feasibility: sort $A$ and $B$; if any sorted $A_k < B_k$, output -1.
2. 2. Collect distinct values of $A_i, B_i$ and sort descending.
3. 3. Mandatory students ($A_i < B_i$): contribute $+1$ at $A_i$ and $-1$ at $B_i$.
4. 4. Helper students ($A_i \ge B_i$): bucket by $A_i$ with value $B_i$.
5. 5. Sweep descending: push available helper $B_j$ into a min-priority queue.
6. 6. While running balance $< 0$: pop minimum $B_j$, add $+1$ to balance, decrement at $B_j$, and increment `helpers_used`.
7. 7. Output $N - (\text{mandatory} + \text{helpers\_used})$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n), b(n);
    vector<int> sa(n), sb(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> b[i];
        sa[i] = a[i];
        sb[i] = b[i];
    }

    sort(sa.begin(), sa.end());
    sort(sb.begin(), sb.end());
    for (int i = 0; i < n; ++i) {
        if (sa[i] < sb[i]) {
            cout << -1 << "\n";
            return 0;
        }
    }

    map<int, vector<int>> helpers_by_a;
    map<int, int> diff;
    vector<int> vals;

    int mandatory_count = 0;
    for (int i = 0; i < n; ++i) {
        vals.push_back(a[i]);
        vals.push_back(b[i]);
        if (a[i] < b[i]) {
            mandatory_count++;
            diff[a[i]]++;
            diff[b[i]]--;
        } else {
            helpers_by_a[a[i]].push_back(b[i]);
        }
    }

    sort(vals.begin(), vals.end(), greater<int>());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    priority_queue<int, vector<int>, greater<int>> min_pq;
    long long cur_sum = 0;
    int helpers_used = 0;

    for (int v : vals) {
        if (helpers_by_a.count(v)) {
            for (int b_val : helpers_by_a[v]) {
                min_pq.push(b_val);
            }
        }

        if (diff.count(v)) {
            cur_sum += diff[v];
        }

        while (cur_sum < 0) {
            if (min_pq.empty()) {
                cout << -1 << "\n";
                return 0;
            }
            int b_val = min_pq.top();
            min_pq.pop();
            helpers_used++;
            cur_sum++;
            diff[b_val]--;
        }
    }

    cout << n - (mandatory_count + helpers_used) << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
