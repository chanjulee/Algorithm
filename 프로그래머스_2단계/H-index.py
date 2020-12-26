def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i]<i+1:
            return i #min(i,citations[i-1]) min할거없이 i...
    return len(citations) #min(len(citations),citations[-1])

citations = list(map(int,input().split()))
print(solution(citations))

'''
import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;    
        
        //내림차순 정렬
        Integer[] citations2 = new Integer[citations.length];
        for(int i=0;i<citations.length;i++){
            citations2[i]=(Integer)citations[i];
        }        
        Arrays.sort(citations2,Collections.reverseOrder());
        
        for(int i=0;i<citations2.length;i++){
            if(citations2[i]<=(i+1)){
                if(citations2[i]==(i+1)){
                    answer=citations2[i];
                    break;
                }else if(citations2[i-1]>i){
                    answer=i;
                    break;
                }else {
                    answer=citations2[i-1];
                    break;
                }
            }else{
                answer=citations2.length;
            }
        }        
        return answer;
    }
}
'''