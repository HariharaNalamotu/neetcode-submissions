class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        for (vector<char> row : board) {
            unordered_map<char, int> rowmap;
            for (char number : row) {
                rowmap[number]++;
                if (rowmap[number] > 1 && number!='.') {
                    return false;
                }
            }
        }

        for (int i = 0; i < 9; i++) {
            unordered_map<char, int> colmap;
            for (vector<char> row : board) {
                colmap[row[i]]++;
                if (colmap[row[i]] > 1 && row[i]!='.') {
                    return false;
                }
            }
        }

        for (int i = 0; i < 9; i = i+3) {
            for (int j = 0; j < 9; j = j+3) {
                unordered_map<char, int> boxmap;
                for (int rowoffset = 0; rowoffset < 3; rowoffset++) {
                    for (int coloffset = 0; coloffset < 3; coloffset++) {
                        boxmap[board[i+rowoffset][j+coloffset]]++;
                        if (boxmap[board[i+rowoffset][j+coloffset]] > 1 && board[i+rowoffset][j+coloffset]!='.') {
                            return false;
                        }
                    }
                }
            }
        }

        return true;
        
    }
};
