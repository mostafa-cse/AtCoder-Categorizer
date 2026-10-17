# Two Pointers

**Domain**: `Basics`  
**Subtopic**: `Leveraging Monotonicity`  

This workbook contains curated, high-quality competitive programming problems teaching **Two Pointers**.

---

## Curated Problems

### `[problem:AtCoder-agc048_c]` — Penguin Skating
- **Rating / Difficulty**: 2120
- **Contest**: `agc048`
- **Analysis**: [`analysis/AtCoder-agc048_c.md`](../../analysis/AtCoder-agc048_c.md)
- **Key Idea**: Shift coordinates by setting a_i = A_i - i and b_i = B_i - i. When penguins slide and cluster, contiguous blocks in a become equal to the anchor penguin's value! Therefore, the target sequence b can be formed if and only if each b_i can be matched to an occurrence of the identical value in a. Since penguins move either strictly leftward (b_i < a_i) or rightward (b_i > a_i), we can use two pointers to match each b_i with the closest matching value in a, accumulating total move steps.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long L;
    if (!(cin >> n >> L)) return 0;

    vector<long long> A(n + 2), B(n + 2);
    A[0] = 0; B[0] = 0;
    for (int i = 1; i <= n; ++i) cin >> A[i];
    for (int i = 1; i <= n; ++i) cin >> B[i];
    A[n + 1] = L + 1; B[n + 1] = L + 1;

    vector<long long> a(n + 2), b(n + 2);
    for (int i = 0; i <= n + 1; ++i) {
        a[i] = A[i] - i;
        b[i] = B[i] - i;
    }

    long long ans = 0;
    int j_left = 0, j_right = 0;

    for (int i = 1; i <= n; ++i) {
        if (a[i] == b[i]) continue;

        if (b[i] < a[i]) {
            while (j_left < i && a[j_left] < b[i]) {
                j_left++;
            }
            if (a[j_left] != b[i]) {
                cout << -1 << "\n";
                return 0;
            }
            ans += (i - j_left);
        } else {
            j_right = max(j_right, i);
            while (j_right <= n + 1 && a[j_right] < b[i]) {
                j_right++;
            }
            if (a[j_right] != b[i]) {
                cout << -1 << "\n";
                return 0;
            }
            ans += (j_right - i);
        }
    }

    cout << ans << "\n";
    return 0;
}
```
