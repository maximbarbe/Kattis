#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <tuple>
#include <math.h>
#include <map>
using namespace std;


#define all(x) begin(x), end(x);

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double PI = acos(-1);

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int n, m, k;
    string s;
    cin >> n >> m;
    map<string, int> quals;
    for (int i = 0; i< n; i++) {
        cin >> s;
        quals[s] = 1;
    }
    for (int i = 0; i < m; i++) {
        int c = 0;
        cin >> k;
        for (int j = 0; j < k; j++) {
            cin >> s;
            c += quals[s];
        }
        if (c == k) {
            cout << "apply\n";
        } else {
            cout << "why bother?\n";
        }
    }
    

}