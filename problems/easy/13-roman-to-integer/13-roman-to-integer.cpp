
/*
LeetCode 13. Roman to Integer
Difficulty: easy
URL: https://leetcode.com/problems/roman-to-integer/

Решение добавлено: 2025-08-20
*/

#include <iostream>
#include <map> 

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        map<char, int> roman_symbols = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
        int result = 0;
        int cur_val = 0;
        int prev_val = 0;
        char sym;
        for(int i = s.size()-1; i >= 0; i--){
            sym = s[i];
            cur_val = roman_symbols[sym];
            if (cur_val < prev_val){
                result -= cur_val;
            }
            else result += cur_val;
            prev_val = cur_val;
        }
        
        return result;
    }
};


int main(){
    Solution sol;
    string input = "LVIII";
    int res = sol.romanToInt(input);
    cout << "result = " << res << endl;
}
