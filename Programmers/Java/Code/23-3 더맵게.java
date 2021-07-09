package javaCode;

import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
       
        // 배열을 우선순위큐로 변환
		// 자바의 우선순위큐는 힙으로 구현되어있음!!
        PriorityQueue<Integer> pq = new PriorityQueue<>();
		for(int s : scoville)
			pq.add(s);
        
        while(true) {
        	// 큐의 모든 값이 K를 넘는지 검사하고싶다? -> 맨앞에것만 검사하면됨.
        	if(pq.peek() >= K)
        		break;
        	// 못넘는데 값이 하나라면?
    		if(pq.size() == 1)
    		{
    			answer = -1;
    			break;
    		}
            // 검사 후 가장 작은 값으로 연산
    		pq.add(pq.poll()+2*pq.poll());
    		answer++;
    	}
        return answer;
    }

	public static void main(String[] args) {
	}
}
