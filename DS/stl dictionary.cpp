#include <iostream>
#include <map>

int main() {
    std::map<std::string, int> myDictionary;
    myDictionary["apple"] = 5;
    myDictionary["banana"] = 3;
    myDictionary["orange"] = 8;
    myDictionary["grape"] = 12;
    std::cout << "Dictionary elements with values:" << std::endl;
    for (const auto& pair : myDictionary)
        std::cout << pair.first << ": " << pair.second << std::endl;
    return 0;
}
