#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int total_floors = 2 * n;
    vector<int> a(n), b(n);
    vector<int> floor_type(total_floors + 1, 0); // 1: entry, 2: exit, 0: free
    vector<int> match_floor(total_floors + 1, 0);
    vector<bool> floor_used(total_floors + 1, false);

    bool possible = true;
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> b[i];
        if (a[i] != -1 && b[i] != -1 && a[i] >= b[i]) possible = false;
        if (a[i] != -1) {
            if (floor_used[a[i]]) possible = false;
            floor_used[a[i]] = true;
            floor_type[a[i]] = 1;
        }
        if (b[i] != -1) {
            if (floor_used[b[i]]) possible = false;
            floor_used[b[i]] = true;
            floor_type[b[i]] = 2;
        }
        if (a[i] != -1 && b[i] != -1) {
            match_floor[a[i]] = b[i];
            match_floor[b[i]] = a[i];
        }
    }

    if (!possible) {
        cout << "No\n";
        return 0;
    }

    vector<bool> dp(total_floors + 1, false);
    dp[0] = true;

    for (int r = 2; r <= total_floors; r += 2) {
        for (int l = 1; l < r; l += 2) {
            if (!dp[l - 1]) continue;
            int len = r - l + 1;
            int L = len / 2;

            bool valid = true;
            for (int k = 0; k < L; ++k) {
                int enter = l + k;
                int exit_f = l + k + L;

                if (floor_type[enter] == 2 || floor_type[exit_f] == 1) {
                    valid = false;
                    break;
                }
                if (match_floor[enter] != 0 && match_floor[enter] != exit_f) {
                    valid = false;
                    break;
                }
                if (match_floor[exit_f] != 0 && match_floor[exit_f] != enter) {
                    valid = false;
                    break;
                }
            }

            if (valid) {
                dp[r] = true;
                break;
            }
        }
    }

    cout << (dp[total_floors] ? "Yes" : "No") << "\n";
    return 0;
}
