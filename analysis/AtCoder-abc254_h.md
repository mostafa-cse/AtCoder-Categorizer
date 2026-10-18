# Problem Analysis: AtCoder-abc254_h — Ex. Multiply or Divide by 2

**Problem ID**: `AtCoder-abc254_h`  
**Contest**: `abc254`  
**Rating / Difficulty**: 2499  
**URL**: https://atcoder.jp/contests/abc254/tasks/abc254_h  
**VJudge Tag**: `[problem:AtCoder-abc254_h]`  
**Category File**: [`../categories/data_structures_ds/multiply_or_divide_by_2_max_heap_trie.md`](../categories/data_structures_ds/multiply_or_divide_by_2_max_heap_trie.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Trie`  
- **Topic (Skill)**: `Trie on Strings and Bits`  

---

## 1. Problem Statement & Key Idea
Find minimum operations to transform multiset $A$ into $B$ using $x \leftarrow \lfloor x / 2 \rfloor$ and $x \leftarrow 2x$. Invert operations on $B$: multiplying an element in $A$ by 2 is equivalent to dividing an even element in $B$ by 2. Inspecting the strictly largest element $M \in A \cup B$: if $M \in A$ and $M > \max(B)$, $M$ cannot be matched without division, so $M \leftarrow \lfloor M / 2 \rfloor$. If $M \in B$ and $M > \max(A)$, $M$ must be formed by doubling, which requires $M$ to be even (if odd, impossible: output -1) and replaces $M$ with $M / 2$. A max-heap simulates this top-down reduction in $O((N + M) \log(\max A))$.

## 2. Core Observation & Invariant
Viewing numbers as binary strings in a bitwise Trie, dividing by 2 pops the lowest bit, while multiplying by 2 appends a 0. The longest binary string can only match by reducing its length. Greedily reducing the maximum element is optimal and prevents branching.

## 3. Step-by-Step Algorithm
1. 1. Insert all elements of $A$ into max-heap $pqA$, and elements of $B$ into max-heap $pqB$.
2. 2. While both heaps are non-empty:
3.    a. Let $topA = pqA.top()$ and $topB = pqB.top()$.
4.    b. If $topA == topB$, pop both (matched).
5.    c. If $topA > topB$, pop $topA$, push $\lfloor topA / 2 \rfloor$ into $pqA$, increment operations.
6.    d. If $topB > topA$: if $topB$ is odd, return -1. Otherwise pop $topB$, push $topB / 2$ into $pqB$, increment operations.
7. 3. Output the total operations count.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) \log(\max A))`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    priority_queue<int> pqA, pqB;
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        pqA.push(x);
    }
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        pqB.push(x);
    }

    long long ops = 0;
    while (!pqA.empty() && !pqB.empty()) {
        int topA = pqA.top();
        int topB = pqB.top();

        if (topA == topB) {
            pqA.pop();
            pqB.pop();
        } else if (topA > topB) {
            pqA.pop();
            pqA.push(topA / 2);
            ops++;
        } else {
            if (topB % 2 != 0) {
                cout << -1 << "\n";
                return 0;
            }
            pqB.pop();
            pqB.push(topB / 2);
            ops++;
        }
    }

    cout << ops << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
