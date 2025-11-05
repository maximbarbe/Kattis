
#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <unordered_map>
#include <math.h>
using namespace std;




int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int s, m, n, d, p, amt;
    cin >> s >> m >> n;
    string cmd;
    for (int i = 0; i<n; i++) {
        cin >> cmd;
        if (cmd == "DRIP") {
            cin >> d >> p;
            d = s * d;
            amt =  d /p;
            s += amt;
            d -= amt * p;
            m += d;
        } else {
            cin >> p;
            amt = m / p;
            s += amt;
            m -= amt * p;
        }
    }
    cout << s << endl << m << endl;
    
}