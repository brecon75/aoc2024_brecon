#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;

// disgustingly inefficient code, but it works
// also it uses the stable_sort func, which is basically cheating

int line_count = 1373;
int rule_count = 1176;
int updates_count = 197;
int rules[2][1176];
vector<int> updates[197];
vector<int> incorrect_ids;

int check_update(const vector<int>& fupdates, int index);
bool compare(int a, int b);

int main() {
    int temp;
    for (int i = 1; i <= line_count; i++) {
        if (i <= rule_count) {
            cin >> rules[0][i-1];
            cin >> rules[1][i-1];
        } else {
            if (i == rule_count + 1) {
                cin.ignore();
            }
            string line;
            getline(cin, line);
            if (line.empty()) continue; // Skip empty lines
            stringstream ss(line);
            while (ss >> temp) {
                updates[i - rule_count - 1].push_back(temp);
            }
        }
    }

    int correct_sum = 0;
    for (int i = 0; i < updates_count; i++) {
        correct_sum += check_update(updates[i], i);
    }
    cout << "Correct sum: " << correct_sum << endl;

    int incorrect_sum = 0;
    for (int i = 0; i < incorrect_ids.size(); i++) {
        int idx = incorrect_ids[i];
        stable_sort(updates[idx].begin(), updates[idx].end(), compare);
        incorrect_sum += updates[idx][updates[idx].size() / 2];
    }
    cout << "Incorrect sum: " << incorrect_sum << endl;

    return 0;
}

int check_update(const vector<int>& fupdates, int index) {
    for (int i = 1; i < fupdates.size(); i++) {
        vector<int> irules;
        for (int j = 0; j < rule_count; j++) {
            if (fupdates[i] == rules[0][j]) irules.push_back(rules[1][j]);
        }
        for (int j = 0; j < i; j++) {
            for (int k = 0; k < irules.size(); k++) {
                if (fupdates[j] == irules[k]) {
                    incorrect_ids.push_back(index); // Use the index of the update
                    return 0;
                }
            }
        }
    }
    return fupdates[fupdates.size() / 2];
}

bool compare(int a, int b) {
    for (int i = 0; i < rule_count; i++) {
        if (rules[0][i] == a && rules[1][i] == b) {
            return true;
        }
        if (rules[0][i] == b && rules[1][i] == a) {
            return false;
        }
    }
    return false; // Leave the order unchanged if no rule is found
}