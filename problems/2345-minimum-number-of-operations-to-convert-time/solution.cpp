class Solution {
public:
    int convertTime(string current, string correct) {
        int cur =
            stoi(current.substr(0, 2)) * 60 +
            stoi(current.substr(3, 2));

        int cor =
            stoi(correct.substr(0, 2)) * 60 +
            stoi(correct.substr(3, 2));

        int diff = cor - cur;

        int ans = 0;

        vector<int> ops = {60, 15, 5, 1};

        for (int x : ops) {
            ans += diff / x;
            diff %= x;
        }

        return ans;
    }
};
