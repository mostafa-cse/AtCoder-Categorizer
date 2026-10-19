# Problem Analysis: AtCoder-codefestival_2016_qualA_e — E - LRU Puzzle

**Problem ID**: `AtCoder-codefestival_2016_qualA_e`  
**Contest**: `code-festival-2016-quala`  
**Rating / Difficulty**: 2723  
**URL**: https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_e  
**VJudge Tag**: `[problem:AtCoder-codefestival_2016_qualA_e]`  
**Category File**: [`../categories/graph_theory/lru_puzzle_topological_sort.md`](../categories/graph_theory/lru_puzzle_topological_sort.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Topological Sorting`  

---

## 1. Problem Statement & Key Idea
Given N arrays initially identical to (1, 2, ..., M), we perform Q operations where each operation chooses one array and moves element a_i to the front. Determine whether all N arrays can end up completely identical.

## 2. Core Observation & Invariant
If all operations were performed on a single array, looking at the operations in reverse order, elements appear in the final array in order of their last access, followed by untouched elements in increasing order 1..M. In the target array V, any trailing suffix that remains in increasing order does not need to be actively moved because untouched elements in each array are already in increasing order. Trimming this increasing suffix leaves a mandatory prefix of V that every array must construct. Simulating backwards, we track how many arrays have currently matched each prefix length of V, advancing an array whenever the corresponding operation a_i is encountered.

## 3. Step-by-Step Algorithm
1. 1. Scan operations A in reverse (from Q-1 down to 0) to collect the unique elements in order of their last occurrence into array V.
2. 2. Append all remaining elements in 1..M that never occurred in A in increasing order to V.
3. 3. Trim elements from the end of V while V has length >= 2 and V[size-2] < V[size-1], then pop one more element representing the suffix boundary.
4. 4. Maintain num[len], the count of arrays currently matching prefix length len of V, initialized with num[0] = N.
5. 5. Scan operations A in reverse: if num[ind[A[i]]] > 0, decrement num[ind[A[i]]] and increment num[ind[A[i]] + 1].
6. 6. Check if num[i] == 0 for all i < V.size(). If all arrays achieved length >= V.size(), output 'Yes', else 'No'.

## 4. Complexity Analysis
- **Time Complexity**: `O(M + Q)`
- **Space Complexity**: `O(M + Q)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, Q;
    if (!(cin >> N >> M >> Q)) return 0;

    vector<int> A(Q);
    for (int i = 0; i < Q; ++i) {
        cin >> A[i];
    }

    vector<int> did(M + 1, 0);
    vector<int> ind(M + 1, 0);
    vector<int> V;

    for (int i = Q - 1; i >= 0; --i) {
        did[A[i]]++;
        if (did[A[i]] == 1) {
            ind[A[i]] = V.size();
            V.push_back(A[i]);
        }
    }

    for (int i = 1; i <= M; ++i) {
        if (did[i] == 0) {
            ind[i] = V.size();
            V.push_back(i);
        }
    }

    while (V.size() >= 2 && V[V.size() - 2] < V[V.size() - 1]) {
        V.pop_back();
    }
    if (!V.empty()) {
        V.pop_back();
    }

    vector<int> num(M + 2, 0);
    num[0] = N;

    for (int i = Q - 1; i >= 0; --i) {
        int idx = ind[A[i]];
        if (num[idx] > 0) {
            num[idx]--;
            num[idx + 1]++;
        }
    }

    for (size_t i = 0; i < V.size(); ++i) {
        if (num[i] > 0) {
            cout << "No\n";
            return 0;
        }
    }

    cout << "Yes\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
