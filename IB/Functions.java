import java.util.*;

class Functions {
    public static String say_goodbye(String name) {
        return String.format("Goodbye, %s!", name);
    }
    public static String excited_greet(String name) {
        name = name.toUpperCase();
        return String.format("HELLO %s!!!", name);
    }
    public static String takeTwoNames(String name1, String name2) {
        return String.format("Hello %s and %s!", name1, name2);
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Input a name: ");
        String name = input.nextLine();
        System.out.println(say_goodbye(name));
        System.out.println("");
        System.out.print("Input a name: ");
        String name2 = input.nextLine();
        System.out.println(excited_greet(name2));
        System.out.println("");
        System.out.print("Input two names: ");
        String name3 = input.nextLine();
        String name4 = input.nextLine();
        System.out.println(takeTwoNames(name3, name4));

        
        input.close();
    }
}