import java.io.*;import java.net.*;
public class Client {
 public static void main(String[] a)throws IOException{
  DatagramSocket s=new DatagramSocket();
  InetAddress ip=a.length==0?InetAddress.getLocalHost():InetAddress.getByName(a[0]);
  byte[] sd=new byte[1024],rd=new byte[1024];
  System.out.print("Enter the hostname : ");
  sd=new BufferedReader(new InputStreamReader(System.in)).readLine().getBytes();
  s.send(new DatagramPacket(sd,sd.length,ip,1362));
  DatagramPacket rp=new DatagramPacket(rd,rd.length);
  s.receive(rp);
  System.out.println("IP Address: "+new String(rp.getData()).trim());
  s.close();
 }
}