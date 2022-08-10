#include<iostream>
#include<string>
#include<stack>
using namespace std;

// hint:use stack

int main(){
    string s;
    cin>>s;
    bool ans=true;
    stack<char> st;

    if(s[0]==')' || s[0]==']' || s[0]=='}'){
        ans=false;

    }else{
        for(int i=0; i<s.length(); i++){
            if(!st.empty() && st.top()=='(' && s[i]==')'){
                st.pop();
            }else if(!st.empty() && st.top()=='[' && s[i]==']'){
                st.pop();
            }else if(!st.empty() && st.top()=='{' && s[i]=='}'){
                st.pop();
            }else{
                st.push(s[i]);
            }
        }   
    }
    if(!st.empty()) ans=false;
    
    cout<<ans<<endl;
    
    return 0;
}