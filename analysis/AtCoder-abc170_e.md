# Problem Analysis: AtCoder-abc170_e — Smart Infants

**Problem ID**: `AtCoder-abc170_e`  
**Contest**: `abc170`  
**Rating / Difficulty**: 1502  
**URL**: https://atcoder.jp/contests/abc170/tasks/abc170_e  
**VJudge Tag**: `[problem:AtCoder-abc170_e]`  
**Category File**: [`../categories/data_structures/dual_multiset_maxima_maintenance.md`](../categories/data_structures/dual_multiset_maxima_maintenance.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Multiset`  
- **Topic (Skill)**: `Dual Multiset (Multiset of Multiset Maxima) Dynamic Maintenance`  

---

## 1. Problem Statement & Key Idea
N infants with ratings belong to kindergartens 1..200000. Q events occur where infant C moves from kindergarten A to B. After each event, output the minimum of the highest rating of all non-empty kindergartens.

**Key Insight**: Maintain a multiset of ratings for each kindergarten, and a global multiset containing the maximum rating of every non-empty kindergarten.

## 2. Core Observation & Invariant
When infant C moves from kindergarten src to dst: remove infant rating from src multiset, update src's maximum in the global multiset. Add rating to dst multiset, update dst's maximum in the global multiset. Answer is *global_multiset.begin().

## 3. Step-by-Step Algorithm
1. Maintain array of multisets kg[200001], global multiset top_ratings, and infant locations loc[i], rating[i].
2. Populate initial ratings and global top_ratings.
3. For each query (infant c, new kindergarten dst):
4.   src = loc[c], val = rating[c].
5.   Erase old max of src and dst from top_ratings.
6.   Erase val from kg[src], insert val into kg[dst].
7.   Reinsert new max of src (if not empty) and dst into top_ratings.
8.   loc[c] = dst.
9.   Print *top_ratings.begin().

## 4. Complexity Analysis
- **Time Complexity**: `O(Q log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

const int MAX_K = 200005;

multiset<int> kg[MAX_K];
multiset<int> top_ratings;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> rating(n + 1), loc(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> rating[i] >> loc[i];
        kg[loc[i]].insert(rating[i]);
    }

    for (int i = 1; i < MAX_K; ++i) {
        if (!kg[i].empty()) {
            top_ratings.insert(*kg[i].rbegin());
        }
    }

    while (q--) {
        int c, dst;
        cin >> c >> dst;
        int src = loc[c];
        int val = rating[c];

        if (src == dst) {
            cout << *top_ratings.begin() << "\n";
            continue;
        }

        // Remove old max from top_ratings
        top_ratings.erase(top_ratings.find(*kg[src].rbegin()));
        if (!kg[dst].empty()) {
            top_ratings.erase(top_ratings.find(*kg[dst].rbegin()));
        }

        // Move infant
        kg[src].erase(kg[src].find(val));
        kg[dst].insert(val);
        loc[c] = dst;

        // Reinsert new max
        if (!kg[src].empty()) {
            top_ratings.insert(*kg[src].rbegin());
        }
        top_ratings.insert(*kg[dst].rbegin());

        cout << *top_ratings.begin() << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Two-level hierarchical multiset maintenance for dynamic group extrema.
- **Reusable Pattern**: `Dual Multiset Maintenance: inner multisets per group + global multiset of inner extrema.`
