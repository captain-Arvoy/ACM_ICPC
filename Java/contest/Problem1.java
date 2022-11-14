/*Question: https://leetcode.com/contest/weekly-contest-310/problems/most-frequent-even-element/   */
//The program though complete, but i don't know how to read array from input

import java.util.Scanner;
import java.math.*;
public class Problem1{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int array[];
        int size_for_frequency_array = Integer.MIN_VALUE;
        for (int i = 0; i < array.length; i++){
            if(size_for_frequency_array < array[i]){
                size_for_frequency_array = array[i];
            }
        }
        int frequency_array[] = new int[(size_for_frequency_array+1)];
        int most_frequent_number = Integer.MIN_VALUE;
        boolean flag = false;
        //debug //OY yeh toh print hi nahi ho raha
        System.out.println("Size of frequency array = "+frequency_array.length);
        for (int i = 0; i < array.length;i++){
            frequency_array[array[i]]++;
        }
        for (int i = 0; i < size_for_frequency_array;i++){
            if((i&1) == 0 && frequency_array[i] > 0){
                flag = true;
                if(most_frequent_number < frequency_array[i]){
                    most_frequent_number = i;
                }
                else if(most_frequent_number == frequency_array[i]){
                    most_frequent_number = Math.min(i,most_frequent_number);
                }
            }
        }
        if (flag == false){
            System.out.println("-1");
        } else{
            System.out.println("most frequent number= "+most_frequent_number);
        }
    /*Displaying frequency array*/for (int i = 0; i < frequency_array.length;i++){
        System.out.print(frequency_array[i]+" ");
    }
    System.out.println();
    }
}