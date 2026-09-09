 

class Solution {
public:
    int minimumMoves(string s) {
        int n = s.size();
        int minMoves = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == 'O')
                continue;
            else {
                minMoves++;
                s[i] = 'O';
                if (i + 1 < n)
                    s[i + 1] = 'O';
                if (i + 2 < n)
                    s[i + 2] = 'O';
            }
        }

        return minMoves;
    }
};
