#include<iostream>
#include<vector>
using namespace std;
// slid window
int main(){
    int target=4;
    vector<int> nums={1,1,1};
    int i=0;
    int sum=0;
    int ans=INT32_MAX;
    for(int j=0;j<nums.size();j++){
        sum += nums[j];
        while(sum>=target){
            
            int len = j-i+1;
            cout<<"j= "<<j<<"i= "<<i<<"sum= "<<sum<<endl;
            if(ans>len) ans = len;
            sum-=nums[i];
            i++;
        }
    }
    if(ans==INT32_MAX) cout<<0<<endl;
    else cout<<ans<<endl;


    return 0; 
}

















