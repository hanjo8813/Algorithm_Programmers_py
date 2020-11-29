import java.util.Arrays;
public class Solution {
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
	
	public static void main(String[] args) {
		String[] participant = {"marina","josipa","nikola","vinko","filipa"};
		String[] completion = {"josipa","filipa","marina","nikola"};
		System.out.println(solution(participant,completion));
	}
}
