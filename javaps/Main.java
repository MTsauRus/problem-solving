package javaps;
import java.io.*;
import java.util.*;

public class Main {
    
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {

        String org = "1234567890";

        char[] ch = org.toCharArray();
        int[] intArr = new int[org.length()];

        for (int i  = 0; i < org.length(); i++) {
            intArr[i] = (ch[i] - '0');
        }

        System.out.println(Arrays.toString(ch));
        System.out.println(Arrays.toString(intArr));
    }
}
  