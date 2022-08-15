#include<iostream>
#include<vector>
using namespace std;

int main(){
    int n=5;
    //這邊定義一個2D向量矩陣，第一個n，代表有幾列向量，第二個n代表有幾行向量，並初始化為0
    vector<vector<int>> matrix(n, vector<int> (n,0));  

    int loop=n/2, mid=n/2, startx=0, starty=0, step=n-1, number=1;

    for(int i=0;i<loop;i++){
        // 左至右
        for(int s=0; s<step;s++){
            matrix[startx][starty]=number;
            starty++;
            number++;
        }
        // 上至下
        for(int s=0; s<step;s++){
            matrix[startx][starty]=number;
            startx++;
            number++;
        }

        // 右至左
        for(int s=0; s<step;s++){
            matrix[startx][starty]=number;
            starty--;
            number++;
        }
        // 下至上
        for(int s=0; s<step;s++){
            matrix[startx][starty]=number;
            startx--;
            number++;
        }
        startx++;
        starty++;
        step-=2;
    }
    if(n%2!=0) matrix[mid][mid]=number;


    //print 結果
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<matrix[i][j]<<" ";
        }
        cout<<endl;
    }

    return 0;
}
