#include<iostream>
#include<string>
#include<sstream>
using namespace std;

int main(){
    int x;
    cin>>x;
    string temp;
    stringstream ss;
    ss<<x;
    ss>>temp;
    int check = (temp.size()/2);
    int s=0;
    int t=temp.size()-1;
    bool ans=true;
    for(int i=0;i<check;i++){
        if(temp[s]!=temp[t]){
            ans=false;
            break;
        }
        s++;
        t--;
    }
    cout<<ans<<endl;
    return 0;
}