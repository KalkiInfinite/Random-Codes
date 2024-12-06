#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> mySet;

    while (true) {
        cout << "Menu:" << endl;
        cout << "1. Add element" << endl;
        cout << "2. Delete element" << endl;
        cout << "3. Display elements" << endl;
        cout << "4. Exit" << endl;

        int choice;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                int elementToAdd;
                cout << "Enter the element to add: ";
                cin >> elementToAdd;
                mySet.insert(elementToAdd);
                cout << "Element added successfully!" << endl;
                break;
            }
            case 2: {
                int elementToDelete;
                cout << "Enter the element to delete: ";
                cin >> elementToDelete;

                if (mySet.erase(elementToDelete)) {
                    cout << "Element deleted successfully!" << endl;
                } else {
                    cout << "Element not found in the set." << endl;
                }
                break;
            }
            case 3: {
                cout << "Set elements: ";
                for (const int& element : mySet) {
                    cout << element << " ";
                }
                cout << endl;
                break;
            }
            case 4:
                cout << "Exiting the program." << endl;
                return 0;

            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}
