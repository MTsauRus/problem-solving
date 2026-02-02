package javaps;


public class Main {
    private static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node head;
    private int size;

    public Main() {
        this.head = null;
        this.size = 0;
    }

    // 1. 맨앞 삽입
    public void addFirst(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
        size++;
        
    }

    // 2. 맨 뒤 삽입
    public void addLast(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            size++;
            return;
        }

        Node curr = head;
        while (curr.next != null) {
            curr = curr.next; 
        } 
        curr.next = newNode;
        size++;
    }

    // 3. 중간 삽입
    public void add(int index, int data) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException();
        }

        if (index == 0) {
            addFirst(data);
            return;
        }

        Node newNode = new Node(data);
        Node prev = head;

        for (int i = 0; i < index-1; i++) {
            prev = prev.next;
        }

        newNode.next = prev.next;
        prev.next = newNode;

        size++;
    }

    // 4. 삭제
    // 해당 인덱스 노드 삭제
    public int remove(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }

        int removedData;

        if (index == 0) {
            removedData = head.data;
            head = head.next;
            size--;
            return removedData;
        } else {
            Node prev = head;
            for (int i = 0; i < index-1; i++) {
                prev = prev.next;
            }
            removedData = prev.next.data;
            prev.next = prev.next.next;
            size--;
            return removedData;
        }
    }

}