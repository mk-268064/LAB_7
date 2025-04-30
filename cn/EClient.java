import java.net.*;
import java.io.*;

public class EClient {
    public static void main(String[] args) throws IOException {
        try (Socket c = new Socket(InetAddress.getLocalHost(), 9000);
             PrintStream os = new PrintStream(c.getOutputStream());
             BufferedReader console = new BufferedReader(new InputStreamReader(System.in));
             BufferedReader server = new BufferedReader(new InputStreamReader(c.getInputStream()))) {
            String line;
            while ((line = console.readLine()) != null) {
                os.println(line);
                System.out.println("Server: " + server.readLine());
            }
        } catch (IOException e) {
            System.out.println("Socket Closed or Error: " + e);
        }
    }
}