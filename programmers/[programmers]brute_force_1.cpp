#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> answers) {
    int supoza0[5] = {1, 2, 3, 4, 5};
    int supoza1[8] = {2, 1, 2, 3, 2, 4, 2, 5};
    int supoza2[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    int len[3] = {5, 8, 10};
    int score[3] = {0};
    
    for(int i=0; i<answers.size(); i++){
        if(answers[i] == supoza0[ i%len[0] ]) score[0]++;
        if(answers[i] == supoza1[ i%len[1] ]) score[1]++;
        if(answers[i] == supoza2[ i%len[2] ]) score[2]++;
    }
    
    int max = 0;
    if(score[max] < score[1]) max = 1;
    if(score[max] < score[2]) max = 2;
    
    //cout << score[0] << " " << score[1] << " " << score[2] << endl;
    
    vector<int> answer;
    if(score[max] == score[0]) answer.push_back(1);
    if(score[max] == score[1]) answer.push_back(2);
    if(score[max] == score[2]) answer.push_back(3);
    return answer;
}
