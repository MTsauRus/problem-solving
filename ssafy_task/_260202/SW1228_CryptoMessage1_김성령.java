package ssafy_task._260202;

import java.io.*;
import java.util.*;

public class SW1228_CryptoMessage1_김성령 {

    static class Node {
        String data;
        Node next;

        public Node(String data) {
            this.data = data;
            this.next = null;
        }

    }
    static class MyLinkedList {
        Node head;
        int size;

        public MyLinkedList() {
            this.head = null;
            this.size = 0;
        }

        public void add(int index, String data) {
            Node newNode = new Node(data);

            if (index == 0) { // 맨앞에 넣는 경우
                newNode.next = head;
                head = newNode;
                size++;
                return;
            } else {
                Node prev = head;
                for (int i = 0; i < index - 1; i++) {
                    prev = prev.next;
                }
                newNode.next = prev.next;
                prev.next = newNode;
                size++;
                return;
            }
        }

        public void printFirst10(StringBuilder sb) {
            Node curr = head;
            for (int i = 0; i < 10; i++) {
                sb.append(curr.data).append(" ");
                curr = curr.next;
            }
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        for (int t = 1; t <= 10; t++) {
            MyLinkedList list = new MyLinkedList();

            int len = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < len; i++) {
                list.add(i, st.nextToken());
            }

            int N = Integer.parseInt(br.readLine()); 
            st = new StringTokenizer(br.readLine());

            for (int i = 0; i < N; i++) {
                String cmd = st.nextToken(); 
                int index = Integer.parseInt(st.nextToken());
                int count = Integer.parseInt(st.nextToken());

                for (int j = 0; j < count; j++) {
                    list.add(index + j, st.nextToken());
                }
            }

            sb.append("#").append(t).append(" ");
            list.printFirst10(sb);
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
