# Extremal Pairing Upper Bound Attainment via Sign-Alternating Bracket Stack

**Domain**: `Basics`  
**Subtopic**: `Greedy / Invariants`  

This workbook contains curated, high-quality competitive programming problems teaching **Extremal Pairing Upper Bound Attainment via Sign-Alternating Bracket Stack**.

---

## Curated Problems

### `[problem:AtCoder-arc120_d]` — Bracket Score 2
- **Rating / Difficulty**: 1996
- **Contest**: `arc120`
- **Analysis**: [`analysis/AtCoder-arc120_d.md`](../../analysis/AtCoder-arc120_d.md)
- **Key Idea**: The maximum possible value of sum |A_i - A_j| over ANY pairing is to pair the N smallest elements of A with the N largest elements of A (giving sum A_large - sum A_small). We can always achieve this theoretical maximum with a valid bracket sequence! Label the N smallest elements -1 and the N largest elements +1. Process from left to right using a stack: if current element has different sign than stack top, they can form a valid matched pair (the earlier gets '(', the later gets ')'); if same sign, push to stack.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;

struct Element {
    long long val;
    int idx;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total = 2 * n;
    vector<Element> a(total);
    for (int i = 0; i < total; ++i) {
        cin >> a[i].val;
        a[i].idx = i;
    }

    sort(a.begin(), a.end(), [](const Element& x, const Element& y) {
        return x.val < y.val;
    });

    vector<int> sign(total);
    for (int i = 0; i < total; ++i) {
        if (i < n) sign[a[i].idx] = -1;
        else sign[a[i].idx] = 1;
    }

    string ans(total, ' ');
    stack<int> st;

    for (int i = 0; i < total; ++i) {
        if (!st.empty() && sign[st.top()] != sign[i]) {
            ans[st.top()] = '(';
            ans[i] = ')';
            st.pop();
        } else {
            st.push(i);
        }
    }

    cout << ans << "\n";
    return 0;
}
```
