import java.util.Arrays;
import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 

class Main {  
  public static void main(String args[]) throws IOException { 
    InputStreamReader in = new InputStreamReader(System.in);
    BufferedReader br = new BufferedReader(in);
    String s = br.readLine();
    // "abracadabra"
    prefFunc(s);
  } 
  
public static int[] prefFunc(String s) {
    int[] pi = new int[s.length()];
    pi[0] = 0;
    int k = 0;
    for (int q = 1; q < s.length(); q++) {
        char cur_char = s.charAt(q);
        while (k > 0 && s.charAt(k) != cur_char) {
            k = pi[k-1];
        }
        if (s.charAt(k) == cur_char) {
            pi[q] = ++k;
        }
    }
    for (int i: pi) {
      System.out.print(i);
      System.out.print(" ");
    }
    System.out.println();
    return pi;
    } 
}