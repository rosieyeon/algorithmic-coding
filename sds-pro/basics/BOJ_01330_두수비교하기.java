package com.basics;

import java.util.Scanner;

public class BOJ_01330_두수비교하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        if (a>b) {
            System.out.println('>');
        } else if (a<b) {
            System.out.println('<');
        } else {
            System.out.println("==");
        }

    }
}
