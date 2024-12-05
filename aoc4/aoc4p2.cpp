#include <iostream>
#include <vector>
#include <string>

// ./a.exe < input.txt

using namespace std;

int main() {
    vector<string> s;
    string temp;
    while (cin >> temp) {
        s.push_back(temp);
    }

    int count = 0;
    for (int i = 0; i < s.size() - 2; i++) {
        for (int j = 0; j < s[i].length() - 2; j++) {
            if ((s[i][j] == 'M' && s[i+1][j+1] == 'A' && s[i+2][j+2] == 'S' && s[i][j+2] == 'M' && s[i+2][j] == 'S') ||
                (s[i][j] == 'S' && s[i+1][j+1] == 'A' && s[i+2][j+2] == 'M' && s[i][j+2] == 'S' && s[i+2][j] == 'M') ||
                (s[i][j] == 'M' && s[i+1][j+1] == 'A' && s[i+2][j+2] == 'S' && s[i][j+2] == 'S' && s[i+2][j] == 'M') ||
                (s[i][j] == 'S' && s[i+1][j+1] == 'A' && s[i+2][j+2] == 'M' && s[i][j+2] == 'M' && s[i+2][j] == 'S')) {
                count++;
            }
        }
    }

    cout << count << endl;
    return 0;
}