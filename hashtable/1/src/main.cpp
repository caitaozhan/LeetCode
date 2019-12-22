#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

/*
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

class Solution 
{
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        vector<int> result;
        unordered_map<int, int> mymap;
        int length = nums.size();
        for(int i = 0; i < length; i++)
        {
            int find = target - nums[i];
            if(mymap.find(find) == mymap.end())
            {
                mymap[nums[i]] = i;
            }
            else
            {
                int j = mymap.find(find)->second;
                result.push_back(min(i, j));
                result.push_back(max(i, j));
                break;
            }
        }
        return result;
    }
};

int main() 
{
    
    vector<int> nums({2, 7, 11, 15});
    Solution s;
    vector<int> result = s.twoSum(nums, 9);
    for(auto i: result)
    {
        cout<<i<<" ";
    }
    cout<<endl;

    result = s.twoSum(nums, 22);
    for(auto i: result)
    {
        cout<<i<<" ";
    }
    cout<<endl;

    result = s.twoSum(nums, 18);
    for(auto i: result)
    {
        cout<<i<<" ";
    }
    cout<<endl;

}