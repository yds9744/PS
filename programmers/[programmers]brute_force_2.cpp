#include <string>
#include <vector>
#include <cstring>

using namespace std;

int solution(string numbers) {
    int answer = 0;
    
    // make prime list
    bool* prime = new bool[10000000];
    memset(prime, true, 10000000 * sizeof(bool));
    prime[0] = false;
    for(int i=2; i<10000000; i++){
        if(prime[i]){
            for(int j=i*2; j<10000000; j+=i){
                prime[j] = false;   
            }
        }
    }
    
    // nPr
    
    
    return answer;
}
