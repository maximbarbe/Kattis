#include <iostream>
#include <iomanip>
#include <vector>
#include <tuple>
#include <queue>
#include <unordered_map>
#include <math.h>
#include <algorithm>
using namespace std;




int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, v;
    double res = 0;
    long num;
    vector<int> a;
    vector<int> s;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> v;
        a.push_back(v);
    }
    for (int i = 0; i < n; i++) {
        cin >> v;
        s.push_back(v);
    }
    sort(s.begin(), s.end());
    long runningSum = 0;
    for (int i = 0; i < n; i++) {
        runningSum += s[n - 1 - i];
        res = max(res, (double)(runningSum + a[i]) / (double) (i + 1));
    }
    cout << setprecision(10) << fixed << res << endl;
}