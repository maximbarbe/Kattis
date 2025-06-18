#pragma GCC optimize("Ofast") 
#pragma GCC target("avx,avx2,fma")


#include <iostream>
#include <iomanip>
#include <vector>
#include <tuple>
#include <algorithm>
#include <math.h>
#include <string>

using namespace std;

class UnionFind{
    private:
        vector<int> sets;
        vector<int> rank;
        


    public:
        int numberSets;
        UnionFind(int n) {
            numberSets = n;
            for (int i = 0; i < n; i++) {
                sets.push_back(i);
                rank.push_back(0);
                
            }
        }

        int find(int id) {
            if (sets[id] == id) {
                return id;
            }
            return find(sets[id]);
        }

        bool isSameSet(int id1, int id2) {
            return find(id1) == find(id2);
        }

        void Union (int id1, int id2) {
            int smaller = find(id1);
            int larger = find(id2);
            if (smaller == larger) {
                return;
            }
            if (rank[smaller] > rank[larger]) {
                swap(smaller, larger);
            } else if (rank[smaller] == rank[larger]) {
                rank[larger] += 1;
            }
            sets[smaller] = larger;
            numberSets --;
            return;
        }
};



int main() {
    int n, m;
    while (true) {
        cin >> n >> m;
        if (n == 0 && m == 0) {
            break;
        }
        UnionFind ufds = UnionFind(n);
        vector<tuple<int, int, int>> edges;
        int src, dest, weight;
        for (int i = 0; i < m;i++) {
            cin >> src >> dest >> weight;
            if (src > dest) {
                swap(src, dest);
            }
            edges.push_back(make_tuple(weight, src, dest));
        }
        if (m < n - 1) {
            cout << "Impossible" << endl;
            continue;
        }
        sort(edges.begin(), edges.end());
        int res = 0;
        vector<pair<int, int>> retained;
        for (int i = 0; i < m; i++) {
            if (ufds.numberSets == 1) {
                break;
            }
            if (!ufds.isSameSet(get<1>(edges[i]), get<2>(edges[i]))) {
                ufds.Union(get<1>(edges[i]), get<2>(edges[i]));
                retained.push_back({get<1>(edges[i]), get<2>(edges[i])});
                res += get<0>(edges[i]);
            }
        }
        sort(retained.begin(), retained.end());
        if (ufds.numberSets != 1) {
            cout << "Impossible" << endl;
        } else {
            cout << res << endl;
            for (int i = 0; i < retained.size(); i++) {
                cout << retained[i].first << " " << retained[i].second << endl;
            }
        }



    }
}