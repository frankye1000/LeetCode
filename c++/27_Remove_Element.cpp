#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int> nums={0,1,2,2,3,0,4,2};
    int val=2;
    int s=0,t=nums.size()-1;
    int ans=nums.size();
    
    for(int i=0;i<nums.size();i++){
        if(nums[i]==val) ans--;
    }
    cout<<ans<<endl;

    while(s<t){
        if(nums[s]==val && nums[t]!=val){
            nums[s]=nums[t];
            s++;
            t--;
        }
        if(nums[s]!=val){
            s++;
        }
        if(nums[t]==val){
            t--;
        }
    }
    
    for(int i=0;i<=nums.size()-1;i++){
        cout<<nums[i];
    }




    return 0;
}