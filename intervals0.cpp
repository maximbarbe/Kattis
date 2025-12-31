#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <climits>
#include <sstream>
#include <math.h>
#include <list>
#include <tuple>
#include <queue>
#include <map>
#include <unordered_map>
#include <numeric>
using namespace std;


typedef unsigned long long ll;
typedef vector<int> vi;




int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k, a, b;
    cin >> n >> k;
    vi hours;
    hours.assign(25, 0);
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        for (int j = a; j < b; j++) {
            hours[j] ++;
        }
    }
    int res =0;
    for (int i = 0; i <= 24; i++) {
        if (hours[i] >= k) res ++;
    }
    cout << res << "\n";

}
