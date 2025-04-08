import java.rmi.Remote;
import java.rmi.RemoteException;

// This interface defines the remote method
public interface ConcatInterface extends Remote {
    String concatenate(String s1, String s2) throws RemoteException;
}
