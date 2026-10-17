#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> a(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> a[i][j];
        }
    }

    // s[i] in {+1, -1}
    vector<int> s(n, 1);

    while (true) {
        bool changed = false;
        for (int i = 0; i < n; ++i) {
            int current_contribution = 0;
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                current_contribution += a[i][j] * s[i] * s[j];
            }
            if (current_contribution < 0) {
                s[i] = -s[i];
                changed = true;
                break;
            }
        }
        if (!changed) break;
    }

    string ans = "";
    for (int i = 0; i < n; ++i) {
        ans += (s[i] == 1 ? 'X' : 'Y');
    }
    cout << ans << "\n";

    return 0;
}
