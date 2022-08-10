#include<iostream>
#include<vector>
using namespace std;


int binary_search(const vector<int> &nums, int target){
    int low=0;
    int high=nums.size()-1;

    while(low<=high){
        int mid=int((low+high)/2);
        if(nums[mid]==target) 
            return mid;
        else if(target>nums[mid]) 
            low=mid+1;
        else 
            high=mid-1;
    }
    return low;
}


int main(){
    vector<int> nums={1,3,5,6};
    int target=0;
    
    int ans;
    ans = binary_search(nums,target);
    cout<<ans<<endl;


    return 0;
}