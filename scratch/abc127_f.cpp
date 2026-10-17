#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;

    priority_queue<long long> left_max;
    priority_queue<long long, vector<long long>, greater<long long>> right_min;
    long long sum_left = 0, sum_right = 0, sum_b = 0;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            long long a, b;
            cin >> a >> b;
            sum_b += b;

            if (left_max.empty() || a <= left_max.top()) {
                left_max.push(a);
                sum_left += a;
            } else {
                right_min.push(a);
                sum_right += a;
            }

            // Rebalance: left_max has size (total + 1) / 2
            while (left_max.size() > right_min.size() + 1) {
                long long val = left_max.top();
                left_max.pop();
                sum_left -= val;
                right_min.push(val);
                sum_right += val;
            }
            while (left_max.size() < right_min.size()) {
                long long val = right_min.top();
                right_min.pop();
                sum_right -= val;
                left_max.push(val);
                sum_left += val;
            }
        } else {
            long long x = left_max.top();
            long long ans = (x * (long long)left_max.size() - sum_left) +
                            (sum_right - x * (long long)right_min.size()) + sum_b;
            cout << x << " " << ans << "\n";
        }
    }

    return 0;
}
