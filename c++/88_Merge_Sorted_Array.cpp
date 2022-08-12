#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    vector<int> nums1={1,2,3,0,0,0};
    vector<int> nums2={2,6,8};
    int m=3,n=3;

    if(n!=0){
        for(int i=m;i<m+n;i++){
            nums1[i]=nums2[i-m];
        }
        sort(nums1.begin(), nums1.end());   
    }
}
