import java.rmi.Naming;
import java.util.Scanner;

public class ConcatClient {
    public static void main(String[] args) {
        try {
            // Lookup the remote object
            ConcatInterface stub = (ConcatInterface) Naming.lookup("rmi://localhost/ConcatService");

            // Get input from user
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter first string: ");
            String str1 = sc.nextLine();
            System.out.print("Enter second string: ");
            String str2 = sc.nextLine();

            // Call the remote method
            String result = stub.concatenate(str1, str2);

            // Display the result
            System.out.println("Concatenated Result: " + result);

        } catch (Exception e) {
            System.out.println("Client Error: " + e.getMessage());
        }
    }
}
