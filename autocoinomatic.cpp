#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <climits>
#include <sstream>
#include <list>
#include <tuple>
#include <queue>
#include <map>
#include <unordered_map>
#include <numeric>
using namespace std;


typedef unsigned long long ll;


void updateDP(vector<int> &dp, int value) {
    for (int i = value; i < 100001; i++) {
        dp[i] = min(dp[i], 1 + dp[i - value]);
    }
} 


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> dp(100001, 100001);
    unordered_map<int, bool> removed;
    dp[0] = 0;
    vector<int> values;
    vector<int> res;
    int n, m, di;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> di;
        values.push_back(di);
        
    }


    char c;
    int v;

    vector<pair<char, int>> commands;
    for (int i = 0; i < m; i++) {
        cin >> c >> v;
        if (c == 'X') {
            removed[v] = true;
        }
        commands.push_back(make_pair(c, v));
    }

    vector<int> kept;
    for (int i = 0; i < n; i++) {
        if (removed[values[i]] == false) {
            kept.push_back(values[i]);
        }
    }

    for (auto x:kept) {
        updateDP(dp, x);
    }

    for (int i = m - 1; i >=0; i--) {
        c = commands[i].first;
        v = commands[i].second;
        if (c == 'Q') {
            int query = dp[v];
            if (query == 100001) {
                res.push_back(-1);
            } else {
                res.push_back(query);
            }
        } else {
            updateDP(dp, v);
        }
    }

    for (int i = res.size() -1; i >= 0; i--) {
        cout << res[i] << endl;
    }

}
