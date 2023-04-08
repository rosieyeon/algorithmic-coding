package com.basics;

import java.util.Scanner;

public class BOJ_25304_영수증 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int total = sc.nextInt();
        int n = sc.nextInt();
        int price = 0;

        for (int i = 0; i<n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            price += a*b;
        }

        if (price == total) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
