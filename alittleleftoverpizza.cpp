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

    int n;
    int l = 0; int m = 0; int s = 0; int v;
    string t;
    cin >>n;
    
    for (int i = 0; i <n; i++) {
        cin >> t >> v;
        if (t == "S") {
            s += v;
        } else if (t == "M") {
            m += v;
        } else {
            l += v;
        }
    }

    cout << ceil((double) s/6.0) + ceil((double) m/8.0) + ceil((double) l/12.0) << endl;

}
