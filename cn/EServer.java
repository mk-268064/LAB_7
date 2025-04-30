import java.net.*;
import java.io.*;

public class EServer {
    public static void main(String[] args) throws IOException {
        try (ServerSocket s = new ServerSocket(9000);
             Socket c = s.accept();
             BufferedReader br = new BufferedReader(new InputStreamReader(c.getInputStream()));
             PrintStream ps = new PrintStream(c.getOutputStream())) {
            String line;
            while ((line = br.readLine()) != null) ps.println(line);
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}