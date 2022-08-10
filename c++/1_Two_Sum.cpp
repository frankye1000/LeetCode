/*Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]*/

#include <iostream>
#include <vector>
using namespace std;
int main(){
    vector<int> nums={2,7,11,15};
    int target=9;

    vector<int> ans;
    for(int s=0;s<nums.size();s++){
        for(int t=s+1;t<nums.size();t++){
            if(nums[s]+nums[t]==target){
                ans.push_back(s);
                ans.push_back(t);
            }
        }
    }

    for(int j=0;j<ans.size();j++) cout<<ans[j]<<" ";

    return 0;
}
