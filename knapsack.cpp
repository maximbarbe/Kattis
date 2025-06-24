#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <tuple>
#include <math.h>
using namespace std;


#define all(x) begin(x), end(x);

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double PI = acos(-1);

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int c, n, v, w;
    
    while (cin >> c >> n) {
        vi val;
        vi weights;
        for (int i = 0; i < n; i++) {
            cin >> v >> w;
            val.push_back(v);
            weights.push_back(w);
        }
        vector<vi> dp;
        dp.assign(n+1, vi());
        for (int i = 0; i <= n; i++) {
            dp[i].assign(c +1, 0);
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= c; j++) {
                if (j < weights[i - 1]) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = max(dp[i - 1][j], val[i - 1] + dp[i - 1][j - weights[i - 1]]);
                }
            }

        }
        vi items;
        int i = n;
        int j = c;
        while (i != 0 && j != 0) {
            if (weights[i - 1] > j) {
                i -= 1;
                continue;
            }
            if (dp[i][j] == dp[i - 1][j]) {
                i -= 1;
            } else {
                items.push_back(i - 1);
                j -= weights[i - 1];
                i -= 1;
            }
        }
        printf("%d\n", items.size());
        if (!items.empty()) {
            for (int i = 0; i < items.size() - 1; i++) {
                printf("%d ", items[i]);
            }
            printf("%d\n", items[items.size() - 1]);
        }


        

        

    }

}