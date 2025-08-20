
/*
LeetCode 9. Palindrome Number
Difficulty: easy
URL: https://leetcode.com/problems/palindrome-number/

Решение добавлено: 2025-08-20
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        vector<int> digits;
        if (x < 0) {
            return false;
        }
        while (x > 0){
            digits.push_back(x % 10);
            x /=10;
        }
        int left = 0, right = digits.size() - 1;
        while(left < right){
            if (digits[left] != digits[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};


int main(){
    Solution sol;
    int x = -121;
    bool res = sol.isPalindrome(x);
    cout << res << endl;
    cout << (res ? "True" : "False") << endl;
}
