import java.net.*; 
import java.io.*;
import java.awt.image.*; 
import javax.imageio.*;
import javax.swing.*; 

class Server
{
    public static void main(String args[]) throws Exception
    {
        ServerSocket server = null; 
        Socket socket = null;
        
        try {
            server = new ServerSocket(4000); // Server waits on port 4000
            System.out.println("Server Waiting for image");
            
            socket = server.accept(); // Accept a connection from client
            System.out.println("Client connected."); 
            
            InputStream in = socket.getInputStream();
            DataInputStream dis = new DataInputStream(in); 
            
            // Read the image size sent by client
            int len = dis.readInt();
            System.out.println("Image Size: " + len / 1024 + "KB"); 
            
            byte[] data = new byte[len]; 
            dis.readFully(data);
            
            // Convert byte array to BufferedImage
            InputStream ian = new ByteArrayInputStream(data); 
            BufferedImage bImage = ImageIO.read(ian); 
            
            // Display image in a JFrame
            JFrame f = new JFrame("Server");
            ImageIcon icon = new ImageIcon(bImage); 
            JLabel l = new JLabel();
            l.setIcon(icon); 
            f.add(l);
            f.pack(); 
            f.setVisible(true);
            
        } catch (IOException e) {
            System.out.println("Exception: " + e.getMessage());
        } finally {
            // Ensure sockets are closed to avoid resource leaks
            if (socket != null && !socket.isClosed()) {
                socket.close(); 
            }
            if (server != null && !server.isClosed()) {
                server.close(); 
            }
            System.out.println("Server socket closed.");
        }
    }
}
