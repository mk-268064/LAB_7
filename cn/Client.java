import javax.swing.*; 
import java.net.*; 
import java.awt.image.*; 
import javax.imageio.*; 
import java.io.*;
import java.awt.image.BufferedImage; 
import java.io.ByteArrayOutputStream; 
import java.io.File;
import java.io.IOException; 
import javax.imageio.ImageIO;

public class Client
{
    public static void main(String args[]) throws Exception
    {
        Socket soc; 
        BufferedImage img = null; 
        
        // Connect to server at localhost:4000
        soc = new Socket("localhost", 4000); 
        System.out.println("Client is running.");
        
        try 
        {
            System.out.println("Reading image from disk.");
            img = ImageIO.read(new File("dhoni.jpg")); // Read the image file
            
            // Convert image to byte array
            ByteArrayOutputStream baos = new ByteArrayOutputStream(); 
            ImageIO.write(img, "jpg", baos);
            baos.flush();
            byte[] bytes = baos.toByteArray(); 
            baos.close(); 
            
            System.out.println("Sending image to server.");
            
            // Send image size and data to server
            OutputStream out = soc.getOutputStream(); 
            DataOutputStream dos = new DataOutputStream(out); 
            dos.writeInt(bytes.length); // Send image size
            dos.write(bytes, 0, bytes.length); // Send image data
            
            System.out.println("Image sent to server.");
            
            // Close the connection
            dos.close();
            out.close();
        }
        catch (Exception e)
        {
            System.out.println("Exception: " + e.getMessage());
            soc.close();
        }
        
        soc.close();
    }
}
