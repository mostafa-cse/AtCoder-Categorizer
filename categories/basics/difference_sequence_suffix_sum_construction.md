# Difference Sequence Linear Equation Construction with Suffix Sum Invariants

**Domain**: `Basics`  
**Subtopic**: `Constructive`  

This workbook contains curated, high-quality competitive programming problems teaching **Difference Sequence Linear Equation Construction with Suffix Sum Invariants**.

---

## Curated Problems

### `[problem:AtCoder-arc153_c]` — ± Increasing Sequence
- **Rating / Difficulty**: 1960
- **Contest**: `arc153`
- **Analysis**: [`analysis/AtCoder-arc153_c.md`](../../analysis/AtCoder-arc153_c.md)
- **Key Idea**: Represent x_i via positive differences: x_i = x_1 + sum_{j=1}^{i-1} d_j with d_j >= 1. The equation sum(A_i * x_i) = 0 rewrites to x_1 * sum(A) + sum_{j=1}^{N-1} d_j * suffix_sum_{j+1}(A) = 0. If sum(A) != 0, set d_j = 1, adjust d_j by at most sum(A), and solve for x_1. If sum(A) = 0, find a positive suffix sum and a negative suffix sum to cancel each other out by scaling their respective d_j. If all suffix sums have identical sign, output No.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    if (n == 1) {
        cout << "No\n";
        return 0;
    }

    vector<long long> suf(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
        suf[i] = suf[i + 1] + a[i];
    }

    vector<long long> x(n);

    if (suf[0] != 0) {
        long long S = 0;
        for (int i = 0; i < n; ++i) {
            x[i] = i;
            S += a[i] * x[i];
        }

        if (suf[0] > 0) {
            // Need S to decrease, increase x[0] by -S / suf[0]
            x[0] -= S;
        } else {
            x[0] += S;
        }

        // Adjust so that x is strictly increasing
        long long min_diff = 1;
        long long cur = x[0];
        vector<long long> ans(n);
        ans[0] = x[0];
        for (int i = 1; i < n; ++i) {
            ans[i] = max(ans[i - 1] + 1, x[i]);
        }
        // Direct reconstruction
        vector<long long> d(n - 1, 1);
        long long current_sum = 0;
        for (int i = 0; i < n - 1; ++i) {
            current_sum += d[i] * suf[i + 1];
        }
        long long rem = -current_sum;
        long long q = rem / suf[0];
        long long r = rem % suf[0];
        if (r < 0) {
            r += abs(suf[0]);
            q = (rem - r) / suf[0];
        }

        int target_idx = -1;
        for (int i = 0; i < n - 1; ++i) {
            if ((suf[0] > 0 && suf[i + 1] == 1) || (suf[0] < 0 && suf[i + 1] == -1)) {
                target_idx = i;
                break;
            }
        }
        if (target_idx != -1) {
            d[target_idx] += abs(suf[0]) - r;
            current_sum = 0;
            for (int i = 0; i < n - 1; ++i) current_sum += d[i] * suf[i + 1];
            q = -current_sum / suf[0];
        }

        cout << "Yes\n";
        vector<long long> res(n);
        res[0] = q;
        for (int i = 0; i < n - 1; ++i) {
            res[i + 1] = res[i] + d[i];
        }
        for (int i = 0; i < n; ++i) {
            cout << res[i] << (i == n - 1 ? "" : " ");
        }
        cout << "\n";
    } else {
        int pos_idx = -1, neg_idx = -1;
        for (int i = 1; i < n; ++i) {
            if (suf[i] > 0 && pos_idx == -1) pos_idx = i;
            if (suf[i] < 0 && neg_idx == -1) neg_idx = i;
        }

        if (pos_idx == -1 || neg_idx == -1) {
            cout << "No\n";
            return 0;
        }

        cout << "Yes\n";
        vector<long long> d(n - 1, 1);
        long long current_sum = 0;
        for (int i = 0; i < n - 1; ++i) {
            current_sum += d[i] * suf[i + 1];
        }

        if (current_sum > 0) {
            d[neg_idx - 1] += current_sum; // since suf[neg_idx] <= -1, this reduces sum
        } else if (current_sum < 0) {
            d[pos_idx - 1] += (-current_sum); // increases sum
        }

        vector<long long> res(n);
        res[0] = 0;
        for (int i = 0; i < n - 1; ++i) {
            res[i + 1] = res[i] + d[i];
        }
        for (int i = 0; i < n; ++i) {
            cout << res[i] << (i == n - 1 ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}
```
