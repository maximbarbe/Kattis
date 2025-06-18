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
vector<int> items;
int backtrack(int cur, int idx, int maxWeight) {
    if (cache.find({cur, idx}) != cache.end()) {
        return cache[{cur, idx}];
    }
    if (idx == items.size()) {
        return cur;
    } else {
        if (cur + items[idx] > maxWeight) {
            int res = backtrack(cur, idx + 1, maxWeight);
            cache[{cur, idx}] = res;
            return res;
        } else {
            int res = max(backtrack(cur + items[idx], idx + 1, maxWeight), backtrack(cur, idx+1, maxWeight));
            cache[{cur, idx}] = res;
            return res;
        }
    }
}





int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int g,t,n;
    cin >> g >> t >> n;
    int maxWeights = ((g-t)/10)*9;
    int k;
    for (int i = 0; i < n;i++) {
        cin >> k;
        items.push_back(k);
    }
    cout << maxWeights - backtrack(0, 0, maxWeights) << endl;

}