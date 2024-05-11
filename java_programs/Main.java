import java.util.*;

public class Main {

    public static class Node {
        int data;
        ArrayList<Node> children = new ArrayList<Node>();

        Node(int val) {
            this.data = val;
        }
    }

    public static void levelOrder(Node root) {
        Queue<Node> queue = new ArrayDeque<Node>();
        queue.add(root);
        while (!queue.isEmpty()) {
            Node temp = queue.remove();
            System.out.print(temp.data + " ");
            for (Node node : temp.children) {
                queue.add(node);
            }
        }
        System.out.println(".");
    }

    public static void levelOrderLinewise(Node root) {
        Queue<Node> queue = new ArrayDeque<Node>();
        Queue<Node> cqueue = new ArrayDeque<Node>();
        queue.add(root);

        while (!queue.isEmpty()) {
            Node temp = queue.remove();
            System.out.print(temp.data + " ");

            for (Node child : temp.children) {
                cqueue.add(child);
            }
            if (queue.isEmpty()) {
                queue = cqueue;
                cqueue = new ArrayDeque<>();
                System.out.println(".");
            }
        }
    }

    public static void levelOrderLinewiseZigzag(Node root) {
        Deque<Node> queue = new ArrayDeque<Node>();
        Deque<Node> cqueue = new ArrayDeque<Node>();

        queue.add(root);
        int decider = 1;
        while (!queue.isEmpty()) {
            if (decider == 1) {
                Node temp = queue.remove();

                System.out.print(temp.data + " ");
                for (Node n : temp.children) {
                    cqueue.add(n);
                }
                if (queue.isEmpty()) {
                    queue = cqueue;
                    cqueue = new ArrayDeque<Node>();
                    System.out.println();
                    decider *= -1;
                }
            }

            else {
                Node temp = queue.removeLast();

                System.out.print(temp.data + " ");
                for (Node n : temp.children) {
                    cqueue.addFirst(n);
                }
                if (queue.isEmpty()) {
                    queue = cqueue;
                    cqueue = new ArrayDeque<Node>();
                    System.out.println();
                    decider *= -1;
                }
            }

        }

    }

    public static Node construct(int[] arr) {
        Stack<Node> stack = new Stack<Node>();
        Node root = null;

        for (int val : arr) {
            if (val != -1) {
                Node temp = new Node(val);
                stack.push(temp);
            } else {
                Node child = stack.pop();
                if (stack.size() > 0) {
                    Node parent = stack.peek();
                    parent.children.add(child);
                } else {
                    root = child;
                }
            }
        }
        return root;
    }

    public static void serialize(Node root, ArrayList<Integer> data) {

    }

    public static void main(String[] args) {

        int arr[] = { 10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1,
                -1 };
        Node root = construct(arr);
        levelOrderLinewise(root);
    }
}