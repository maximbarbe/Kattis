#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <map>
#include <tuple>
using namespace std;

typedef tuple<int, int,int> t;

map<pair<int, int>, int> cache;
string s;
int res(int i, int j) {
    if (cache.find({i,j}) != cache.end()) {
        return cache[{i, j}];
    } else {
        int res = 0;
        int x = i;
        int y = j;
        while (j < s.size() && s[i] == s[j]) {
            res ++;
            i ++;
            j ++;
        }
        cache[{x, y}] = res;
        return res;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> s;
    int i,j, n;
    cin >> n;
    for (int k = 0; k<n; k++) {
        cin >> i >> j;
        cout << res(i, j)<<endl;
    }
}