#pragma GCC optimize("Ofast") 
#pragma GCC target("avx,avx2,fma")



#include <iostream>
#include <iomanip>
#include <vector>
#include <tuple>
#include <algorithm>
#include <math.h>
#include <string>
#include <queue>
#include <string>
#include <unordered_map>
typedef long long ll;



using namespace std;






int main() {

    int n, m;
    while (cin >> n >>m) {
        vector<int>values;
        int k;
        for (int i = 0; i < m;i++){
            cin >> k;
            values.push_back(k);
        }
        vector<bool> dp;
        dp.assign(n + 1, false);
        dp[0] = false;
        for (int i = 1; i < n+1; i++) {
            bool winnable = false;
            for (auto val:values) {
                if (i - val >= 0) {
                    // If the first move causes the second player to reach an unwinnable position then he wins.
                    winnable = winnable || !dp[i - val];
                }
            }
            dp[i] = winnable;
        }
        if (dp[n] == true) {
            cout << "Stan wins" << endl;
        } else {
            cout << "Ollie wins" << endl;
        }
    }
}