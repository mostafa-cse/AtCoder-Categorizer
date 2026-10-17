# Problem Analysis: AtCoder-arc154_d — D. A + B > C ?

**Problem ID**: `AtCoder-arc154_d`  
**Contest**: `arc154`  
**Rating / Difficulty**: 2265  
**URL**: https://atcoder.jp/contests/arc154/tasks/arc154_d  
**VJudge Tag**: `[problem:AtCoder-arc154_d]`  
**Category File**: [`../categories/miscellaneous/interactive_permutation_comparator_merge_sort.md`](../categories/miscellaneous/interactive_permutation_comparator_merge_sort.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Interactive Problems`  
- **Topic (Skill)**: `Interactive Problems`  

---

## 1. Problem Statement & Key Idea
An unknown permutation $P$ of length $N \le 2000$ is hidden. We can ask at most 25,000 queries of the form '? i j k', asking if $P_i + P_j > P_k$. Recover the entire permutation $P$.

## 2. Core Observation & Invariant
First, locate the index $x$ where $P_x = 1$ in $N-1$ queries. Start with candidate $x = 1$. For $i = 2 \dots N$, query '? i i x' ($P_i + P_i > P_x$). If 'No', then $2 P_i \le P_x \implies P_i < P_x$, so update candidate $x \leftarrow i$. When $i$ hits the true position of $1$, $2(1) \le P_x$ is 'No' (since $P_x \ge 2$), so $x$ switches to the position of $1$, and never changes again since $2 P_k > 1$ for all other elements.
Once the index $x$ with $P_x = 1$ is known, querying '? b x a' tests $P_b + 1 > P_a \iff P_b \ge P_a$. Since all elements are distinct, this provides a strict comparison oracle between any two elements $P_a$ and $P_b$. Using standard merge sort on the remaining $N-1$ elements takes at most $(N-1) \lceil \log_2 (N-1) \rceil \le 22,000$ queries, well within the 25,000 query limit.

## 3. Step-by-Step Algorithm
1. Set $one\_idx = 1$.
2. For $i = 2 \dots N$, ask '? i i one_idx'. If response is 'No', set $one\_idx = i$.
3. Define comparator $comp(a, b)$: query '? b one_idx a'. Returns true if $P_a < P_b$.
4. Sort all indices $\{1, \dots, N\} \setminus \{one\_idx\}$ using in-place merge sort with comparator $comp$.
5. Assign $P[one\_idx] = 1$, and for sorted indices assign values $2, 3, \dots, N$ in increasing order.
6. Flush answer '! P_1 P_2 ... P_N'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N) \text{ queries}`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool query(int i, int j, int k) {
    cout << "? " << i << " " << j << " " << k << endl;
    string res;
    if (!(cin >> res) || res == "-1") exit(0);
    return res == "Yes";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    // Step 1: Find index of 1
    int one_idx = 1;
    for (int i = 2; i <= n; ++i) {
        if (!query(i, i, one_idx)) {
            one_idx = i;
        }
    }

    // Step 2: Compare elements using query(b, one_idx, a)
    // P_b + 1 > P_a <=> P_a < P_b
    auto comp = [&](int a, int b) {
        if (a == b) return false;
        return query(b, one_idx, a);
    };

    vector<int> a;
    for (int i = 1; i <= n; ++i) {
        if (i != one_idx) a.push_back(i);
    }

    vector<int> tmp(a.size());
    auto merge_sort = [&](auto self, int l, int r) -> void {
        if (r - l <= 1) return;
        int m = l + (r - l) / 2;
        self(self, l, m);
        self(self, m, r);
        int i = l, j = m, k = l;
        while (i < m && j < r) {
            if (comp(a[i], a[j])) {
                tmp[k++] = a[i++];
            } else {
                tmp[k++] = a[j++];
            }
        }
        while (i < m) tmp[k++] = a[i++];
        while (j < r) tmp[k++] = a[j++];
        for (int p = l; p < r; ++p) a[p] = tmp[p];
    };

    merge_sort(merge_sort, 0, (int)a.size());

    vector<int> ans(n + 1);
    ans[one_idx] = 1;
    for (size_t i = 0; i < a.size(); ++i) {
        ans[a[i]] = (int)(i + 2);
    }

    cout << "!";
    for (int i = 1; i <= n; ++i) {
        cout << " " << ans[i];
    }
    cout << endl;

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
