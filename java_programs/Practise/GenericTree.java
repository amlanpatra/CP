import java.util.*;

public class GenericTree {
    public static class Node {
        int data;
        ArrayList<Node> children = new ArrayList<Node>();

        Node(int data) {
            this.data = data;

        }
    }

    public static void levelOrder(Node root) {
        Queue<Node> queue = new ArrayDeque<Node>();
        queue.add(root);

        while (queue.size() > 0) {
            Node temp = queue.remove();

            System.out.print(temp.data + " ");
            for (Node child : temp.children) {
                queue.add(child);
            }
        }
        System.out.println(".");
    }

    public static void main(String[] args) {
        Node root = new Node(10);

        Node twenty = new Node(20);
        root.children.add(twenty);

        Node thirty = new Node(30);
        root.children.add(thirty);

        Node forty = new Node(40);
        root.children.add(forty);

        Node fifty = new Node(50);
        twenty.children.add(fifty);

        Node sixty = new Node(60);
        twenty.children.add(sixty);

        Node seventy = new Node(70);
        thirty.children.add(seventy);

        Node eighty = new Node(80);
        thirty.children.add(eighty);

        Node ninety = new Node(90);
        thirty.children.add(ninety);

        Node hundred = new Node(100);
        forty.children.add(hundred);

        Node hundred_ten = new Node(110);
        eighty.children.add(hundred_ten);

        Node hundred_twenty = new Node(120);
        eighty.children.add(hundred_twenty);

        levelOrder(root);

    }
}