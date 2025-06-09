#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include "math.h"
#include <queue>
#include <tuple>
using namespace std;


typedef long long ll;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    priority_queue<tuple<int, int>> queue;
    int a;
    for (int i = 0; i < n; i++) {
        cin >> a;
        if (a != 0) {
            queue.push({a, i + 1});
        }
        
    }
    vector<tuple<int, int>> moves = vector<tuple<int, int>>();
    int s1, i, s2, j;

    while (queue.size() != 0) {
        if (queue.size() ==1) {
            cout << "no" << endl;
            return 0;
        }
        tuple<int, int> first = queue.top();

        queue.pop();
        tuple<int, int> second = queue.top();
        s1 = get<0>(first);
        i = get<1>(first);
        s2 = get<0>(second);
        j = get<1>(second);
        s1 --;
        s2 --;
        queue.pop();
        
        moves.push_back({i, j});
        if (s1 != 0) {
            queue.push({s1, i});
        }
        if (s2 != 0) {
            queue.push({s2, j});
        }


    }
    cout << "yes"<<endl;
    for (auto [a, b]:moves) {
        cout << a << " " << b << endl;
    }
}