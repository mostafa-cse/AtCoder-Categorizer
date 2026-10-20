# Problem Analysis: AtCoder-abc427_g — G - Takahashi's Expectation 2

**Problem ID**: `AtCoder-abc427_g`  
**Contest**: `abc427`  
**Rating / Difficulty**: 2974  
**URL**: https://atcoder.jp/contests/abc427/tasks/abc427_g  
**VJudge Tag**: `[problem:AtCoder-abc427_g]`  
**Category File**: [`../categories/data_structures/present_sequence_canonicalization_mood_treap.md`](../categories/data_structures/present_sequence_canonicalization_mood_treap.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Balanced Binary Search Tree (BBST)`  
- **Topic (Skill)**: `Treap`  

---

## 1. Problem Statement & Key Idea
Takahashi maintains a sequence of present values under dynamic insertions and queries: an operation merges adjacent values if their difference is less than A, maintaining a canonical sparse sequence where P_{i+1} - P_i >= A. Compute Takahashi's expected mood across all query points.

## 2. Core Observation & Invariant
The canonical merge condition P_{i+1} - P_i >= A causes inserted points to propagate shifts and mergers to subsequent points. Because the merge rule is associative, the canonicalized sequence can be maintained in blocks of sizes that are powers of 2 (or a randomized Treap / binary lifting table). Queries perform binary searches on each block to locate the effective position and compute mood contributions in O(log^2 M).

## 3. Step-by-Step Algorithm
1. 1. Represent canonical sequence blocks using power-of-two merged segments.
2. 2. For each insertion, canonicalize the inserted value against existing blocks: if a gap is < A, merge and promote.
3. 3. For query points, binary search canonical blocks to determine Takahashi's mood and index offsets.
4. 4. Output the answer for each query.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log^2 M)`
- **Space Complexity**: `O(M log M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static constexpr long long MIN_SENTINEL = -8000000000000000000LL;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long A, B;
    if (!(cin >> n >> A >> B)) return 0;

    vector<long long> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
    }

    auto merge = [&](const vector<long long>& lhs, const vector<long long>& rhs) -> vector<long long> {
        long long L = lhs.size(), R = rhs.size();
        vector<long long> result;
        result.push_back(MIN_SENTINEL);
        result.reserve(L + R + 1);
        long long l = 0, r = 0;
        while (l < L || r < R) {
            if (l == L || (r < R && lhs[l] - r * B > rhs[r] - (L - l) * A)) {
                result.push_back(rhs[r++] - (L - l) * A);
            } else {
                result.push_back(max(result.back() + A, lhs[l++] - r * B));
            }
        }
        result.erase(result.begin());
        return result;
    };

    vector<vector<long long>> seq;

    auto append_seq = [&](auto self, vector<long long> elem) -> void {
        if (seq.empty() || seq.back().size() != elem.size()) {
            seq.push_back(move(elem));
        } else {
            auto lhs = move(seq.back());
            seq.pop_back();
            self(self, merge(lhs, elem));
        }
    };

    for (int i = 0; i < n; ++i) {
        append_seq(append_seq, vector<long long>{p[i]});
    }

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int type;
        long long X;
        cin >> type >> X;
        if (type == 1) {
            append_seq(append_seq, vector<long long>{X});
        } else {
            for (const auto& s : seq) {
                int sz = (int)s.size();
                int low = 0, high = sz;
                while (low < high) {
                    int mid = (low + high) / 2;
                    if (X > s[mid] + mid * B) {
                        low = mid + 1;
                    } else {
                        high = mid;
                    }
                }
                int cnt = low;
                X += sz * A - (long long)cnt * (A + B);
            }
            cout << X << "\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
