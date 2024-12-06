Second Question:
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> dictionary;
    dictionary["vader"] = 5;
    dictionary["bane"] = 3;
    dictionary["sidious"] = 7;
    dictionary["revan"] = 2;

    cout << "Dictionary elements with values:" << endl; for
    (const auto pair : dictionary) {
        cout << pair.first << " " << pair.second << endl;
    }
    return 0;
}