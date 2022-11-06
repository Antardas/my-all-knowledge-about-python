

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  vector<int> v;
  int t = 2;
  int n, q;

  for (int i = 0; i < t; i++) {
    cin >> n >> q;
    if (n == 0 && q == 0) {
      break;
    }
    v.clear();
    for (int j = 0; j < n; j++) {
      int x;
      cin >> x;
      v.push_back(x);
    }
    // sort the vector
    sort(v.begin(), v.end());
    cout << "CASE# " << i + 1 << ":" << endl;
    for (int j = 0; j < q; j++) {
      int x;
      cin >> x;
      //   loop over the vector if the element is find then print the element
      if (find(v.begin(), v.end(), x) != v.end()) {
        cout << x << " found at "
             << (find(v.begin(), v.end(), x) - v.begin()) + 1 << endl;
      } else {
        // if the element is not find then print the upper bound of the element
        cout << x << " not found" << endl;
      }
    }
  }

  return 0;
}