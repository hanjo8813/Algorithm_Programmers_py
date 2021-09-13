package prgrms.정렬_1_K번째수;

import java.util.*;
public class Solution {
	public static int[] solution(int[] array, int[][] commands) {
		int[] answer = new int[commands.length];
		int index=0;
        for(int[] c : commands)
        {
        	int start = c[0]-1;
        	int end = c[1];	
        	int num = c[2]-1;
        	int[] new_arr = new int[end-start];
    		for(int i=start; i<end; i++)
    		{
    			new_arr[i-start] = array[i];
    		}
    		Arrays.sort(new_arr);
    		answer[index] = new_arr[num];
    		index++;
        }
        return answer;
    }
	public static int[] solution2(int[] array, int[][] commands) {
		int[] answer = new int[commands.length];
		int index=0;
        for(int[] c : commands)
        {
        	int[] new_arr = Arrays.copyOfRange(array,c[0]-1,c[1]);
        	Arrays.sort(new_arr);
        	answer[index] = new_arr[c[2]-1];
        	index++;
        }
        return answer;
    }

	public static void main(String[] args) {
		int[] array = {1, 5, 2, 6, 3, 7, 4};
		int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
		System.out.println(solution(array, commands));
	}
}
