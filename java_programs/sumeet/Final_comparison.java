// final class cannot be inherited
final class Parent {
    // final variable cannot be changed after value is assigned
    public final int a;

    // final method cannot be overridden
    public final int getA() {
        return this.a;
    }

    // constructor initializes value of 'a'
    Parent(int y) {
        this.a = y; // now this value cannot be changed
    }
}

class Child extends Parent { // Parent class cannot be extended since its final

    Child(int y) {
        super(y);
    }

    // getA() method cannot be overridden since its final in Parent class
    public final int getA() {
        return this.getA() + 1;
    }
}

public class Final_comparison {
    public static void main(String[] args) {
        // instance variables
        Parent obj1 = new Parent(4);
        Parent obj2 = new Parent(8);

        System.out.println(obj1.getA()); // 4
        System.out.println(obj2.getA()); // 8

        obj1.a = 1; // cannot be done since final variable
        obj2.a = 2; // cannot be done since final variable

    }
}