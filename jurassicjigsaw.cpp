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
    int n, k;
    cin >> n >> k;
    UnionFind ufds = UnionFind(n);
    vector<string> seq;
    vector<tuple<int, int, int>> edges;
    string sequence;
    for (int i = 0; i < n; i++) {
        cin >> sequence;
        for (int j = 0; j < i;j++) {
            int diff = 0;
            for (int l = 0; l < k; l++) {
                if (sequence[l] != seq[j][l]) {
                    diff ++;
                }
            }
            edges.push_back(make_tuple(diff, j, i));
        }
        seq.push_back(sequence);
    }
    int res = 0;
    sort(edges.begin(), edges.end());
    vector<pair<int, int>> retained;
    for (int i = 0; i < edges.size(); i++) {
        if (ufds.numberSets == 1) {
            break;
        } else {
            if (!ufds.isSameSet(get<1>(edges[i]), get<2>(edges[i]))) {
                ufds.Union(get<1>(edges[i]), get<2>(edges[i]));
                res += get<0>(edges[i]);
                retained.push_back({get<1>(edges[i]), get<2>(edges[i])});
            }
        }
    }
    cout << res << endl;
    for (int i = 0; i < n - 1; i++) {
        cout << retained[i].first << " " << retained[i].second << endl;
    }
}