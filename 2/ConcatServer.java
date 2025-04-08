import java.rmi.Naming;

public class ConcatServer {
    public static void main(String[] args) {
        try {
            // Just bind the remote object; do NOT createRegistry here
            ConcatImplementation obj = new ConcatImplementation();
            Naming.rebind("ConcatService", obj);

            System.out.println("Server is ready.");
        } catch (Exception e) {
            System.out.println("Server Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
