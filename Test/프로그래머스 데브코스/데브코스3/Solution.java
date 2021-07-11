package 데브코스3;

import java.util.*;

public class Solution {
	
	public static ArrayList<int[]> convertArrayToList(int[][] wires){
		ArrayList<int[]> new_list = new ArrayList<>();
		for(int[] wire : wires) {
			new_list.add(wire);
		}
		return new_list;
	}
	
	public static int DFS(int vertex, ArrayList<int[]> wires_list) {
		
		int count = 1;
		
		ArrayList<int[]> copy_list = new ArrayList<>();
		for(int[] wire : wires_list) {
			copy_list.add(wire);
		}
		
		for(int[] wire : wires_list) {
			if(vertex == wire[0]) {
				copy_list.remove(wire);
				count += DFS(wire[1], copy_list);
			}
			else if(vertex == wire[1]) {
				copy_list.remove(wire);
				count += DFS(wire[0], copy_list);
			}
		}
		
		return count;
	}
	
	public static int solution(int n, int[][] wires) {
		
		ArrayList<Integer> diff_list = new ArrayList<>();
		
		for(int i=0; i<wires.length; i++) {
			// 시작 정점
			int left_v = wires[i][0];
			int right_v = wires[i][1];
			
			// 간선 리스트 생성
			ArrayList<int[]> wires_list = new ArrayList<>();
			for(int[] wire : wires) {
				wires_list.add(wire);
			}
			wires_list.remove(i);
			
			int num_left = DFS(left_v, wires_list);
			int num_right = DFS(right_v, wires_list);
			diff_list.add(Math.abs(num_left - num_right));
		}
		
		int anwer = Collections.min(diff_list);
        return anwer;
    }
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 9;
		int[][] wires = { 
				{1,3},
				{2,3},
				{3,4},
				{4,5},
				{4,6},
				{4,7},
				{7,8},
				{7,9}
		};
		System.out.println(solution(n, wires));
		
		n = 4;
		wires = new int[][]{ 
				{1,2},
				{2,3},
				{3,4}
		};
		System.out.println(solution(n, wires));
	}
}
