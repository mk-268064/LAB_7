import java.io.*;import java.net.*;
public class Server {
 private static int indexOf(String[] a,String s){s=s.trim();for(int i=0;i<a.length;i++)if(a[i].equals(s))return i;return -1;}
 public static void main(String[] a)throws IOException{
  String[] h={"yahoo.com","gmail.com","cricinfo.com","facebook.com"},i={"68.180.206.184","209.85.148.19","80.168.92.140","69.63.189.16"};
  System.out.println("Press Ctrl + C to Quit");
  while(true){
   DatagramSocket s=new DatagramSocket(1362);
   byte[] sd=new byte[1021],rd=new byte[1021];
   DatagramPacket rp=new DatagramPacket(rd,rd.length);
   s.receive(rp);
   String q=new String(rp.getData()).trim();System.out.println("Request for host "+q);
   sd=(indexOf(h,q)!=-1?i[indexOf(h,q)]:"Host Not Found").getBytes();
   s.send(new DatagramPacket(sd,sd.length,rp.getAddress(),rp.getPort()));
   s.close();
  }
 }
}