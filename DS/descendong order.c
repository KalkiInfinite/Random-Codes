#include <iostream>
#include <set>
using namespace std;

struct DescendingOrder {
    bool operator()(int a, int b) const {
        return a > b;
    }
};

int main() {
    set<int, DescendingOrder> descendingSet;

    int num;
    while (true) {
        cout << "Enter a number (or enter -1 to stop): ";
        cin >> num;
        if (num == -1) {
            break;
        }
        descendingSet.insert(num);
    }

    cout << "Set elements in descending order: ";
    for (const int element : descendingSet) {
        cout << element << " ";
    }
    cout << endl;

    return 0;
}