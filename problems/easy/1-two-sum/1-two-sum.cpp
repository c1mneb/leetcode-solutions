
/*
LeetCode 1. Two Sum
Difficulty: easy
URL: https://leetcode.com/problems/two-sum/

Решение добавлено: 2025-08-20
*/

#include <iostream>
#include <vector>
using namespace std;


vector<int> twoSum(vector<int>& nums, int target) {
    if (nums.empty()) {
        cout << "Vector is empty!" << endl;
        return {}; 
    }
    for(int i = 0; i < nums.size(); i++){
        for (int j = i+1; j < nums.size(); j++){
            if(nums[i] + nums[j] == target){
                return {i, j};
            }
        }
    }
    return {0, 0};
}

int main(){
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    cout << "Result: ";
    //twoSum(nums, target);
    vector<int> result = twoSum(nums, target);

    for (int i = 0; i < result.size(); i++){
        cout << result[i] << ", " ;
    }
    cout << endl;
    
}
