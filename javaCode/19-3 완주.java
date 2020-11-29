package javaCode;

import java.util.*;

public class Solution {
	// 1번째 풀이
	public static String solution(String[] participant, String[] completion)
	{
		String answer = "";
		Arrays.sort(participant);
		Arrays.sort(completion);
		for(int i=0; i<participant.length; i++)
		{
			answer = participant[i];
			if (i == participant.length-1)
				break;
			else if(!participant[i].equals(completion[i]))
				break;
		}
		return answer;
	}
	// 2번째 풀이
	public static String solution2(String[] participant, String[] completion) {
		String answer = "";
		HashMap<String, Integer> hm = new HashMap<String, Integer>();
		// participant에서 이름별 등장횟수를 해쉬맵에 저장
		for (String p : participant) {
			if (!hm.containsKey(p))
				hm.put(p, 1);
			else {
				int n = hm.get(p) + 1;
				hm.put(p, n);
			}
		}
		// 해쉬맵에서 completion과 겹치는 이름(키)가 나오면 등장횟수 -1
		for (String c : completion) {
			int n = hm.get(c) - 1;
			hm.put(c, n);
		}
        // 등장횟수가 0이 아닌 이름은 완주 못한것.
		for (String s : hm.keySet()) {
			if (hm.get(s) != 0)
				answer = s;
		}
		return answer;
	}

	public static void main(String[] args) {
		String[] participant = { "marina", "josipa", "nikola", "vinko", "filipa" };
		String[] completion = { "josipa", "filipa", "marina", "nikola" };
		System.out.println(solution(participant, completion));
	}
}
