#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>

using namespace std;



int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    multiset<int> problems;
    multiset<int>::iterator iter;
    int n, q, di;
    cin >> n >> q;
    for (int i = 0; i < n; i++) {
        cin >> di;
        problems.insert(di);
    }
    int t, d;
    for (int i = 0; i < q; i++) {
        cin >> t >> d;
        if (t == 1) {
            iter = problems.upper_bound(d);
            if (iter == problems.end()) {
                cout << -1 << endl;
            } else {
                cout << *iter << endl;
                problems.erase(iter);
            }
        } else {
            iter = problems.lower_bound(d);
            if (*iter == d) {
                cout << *iter << endl;
                problems.erase(iter);
            } else {
                if (iter == problems.begin() && *iter > d) {
                    cout << -1 << endl;
                } else {
                    iter --;
                    cout << *iter << endl;
                    problems.erase(iter);
                }
            }

        }
    }

}