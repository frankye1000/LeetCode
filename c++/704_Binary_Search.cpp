#include<iostream>
#include<vector>
using namespace std;

int binary_search(vector<int> nums, int target){
        int low=0;
        int high=nums.size()-1;

        while(low<=high){
            int mid = int((low+high)/2);
            if(nums[mid]==target) return mid;
            else if(target>nums[mid]) low=mid+1;
            else high=mid-1;
        }
        return -1;
}
int main(){
    

    vector<int> nums={-1,0,3,5,9,12};
    int target=9;

    int ans = binary_search(nums,target);

    cout<<ans<<endl;


    return 0;
}