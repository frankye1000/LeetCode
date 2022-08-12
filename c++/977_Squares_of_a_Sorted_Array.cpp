#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){

    vector<int> nums={-7,-3,2,3,11};
    for(int i=0;i<nums.size();i++){
        nums[i] = nums[i]*nums[i];
    }

    sort(nums.begin(),nums.end());
    return 0;
}