package 그래프.탐색.G4_소수경로;

import java.io.*;
import java.util.*;

public class Try1 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());

        for(int i=0; i<t; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            System.out.println(new Solution().solution(a, b));
        }
    }


    public static class Solution {

        public int target;
        public boolean[] isVisited;
        public int min;

        public String solution(int a, int b){
            target = b;
            isVisited = new boolean[10000];
            min = Integer.MAX_VALUE;

            char[] charArr = String.valueOf(a).toCharArray();
            int[] arr = new int[4];
            for(int i=0; i<4; i++){
                arr[i] = charArr[i] - '0';
            }

            isVisited[join(arr)] = true;
            dfs(0, arr);

            if(min == Integer.MAX_VALUE){
                return "Impossible";
            }
            return String.valueOf(min);
        }

        public void dfs(int depth, int[] arr){
            // System.out.println(Arrays.toString(arr));

            if(join(arr) == target){
                min = Math.min(min, depth);
                return;
            }
                        
            for(int i=0; i<4; i++){
                for(int j=0; j<10; j++){
                    if(i==0 && j==0){
                        continue;
                    }
                    int temp = arr[i];
                    arr[i] = j;
                    int num = join(arr);
                    if(isVisited[num] || !isPrime(num)){
                        continue;
                    }
                    isVisited[num] = true;
                    dfs(depth+1, arr);
                    isVisited[num] = false;
                    arr[i] = temp;
                }
            }
        }

        public int join(int[] arr){
            int result = 0;
            result += arr[0] * 1000;
            result += arr[1] * 100;
            result += arr[2] * 10;
            result += arr[3];
            return result;
        }

        public boolean isPrime(int num){
            if(num == 1){
                return false;
            }
            int sqrt = (int)Math.sqrt(num);
            for(int i=2; i<=sqrt; i++){
                if(num%i==0){
                    return false;
                }
            }
            return true;
        }

    }
    
}
