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
typedef vector<int> vi;




int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,k;
    int a;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> a;
        if (a <= k) {
            cout << "1";
            k -= a;
        } else {
            cout << "0";
        }
    }
    cout << "\n";

}
