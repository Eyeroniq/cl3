import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

// This is the implementation of the remote interface
public class ConcatImplementation extends UnicastRemoteObject implements ConcatInterface {

    // Constructor must throw RemoteException
    protected ConcatImplementation() throws RemoteException {
        super();
    }

    // Implementation of the concatenate method
    public String concatenate(String s1, String s2) throws RemoteException {
        return s1 + s2;
    }
}
