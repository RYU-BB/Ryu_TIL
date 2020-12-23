package client;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.Scanner;

public class ClientExecution implements Constants {
	
	public ClientExecution() {
		ObjectInputStream in = null;
		ObjectOutputStream out = null;
		Socket socket = null;
		
		try {
			socket = new Socket("localhost", 9999);
			Scanner sc= new Scanner(System.in);
			out = new ObjectOutputStream(socket.getOutputStream());
			
			ClientUserInfo userInfo = new ClientUserInfo();
			System.out.print("닉네임을 입력해주세요 >> ");
			userInfo.setName(sc.nextLine());
			userInfo.setMsg(ACCESS_MSG);
			
			out.writeObject(userInfo);
			out.flush();
			
			in = new ObjectInputStream(socket.getInputStream());
			Thread ClientSendThread = new Thread(new ClientSendThread(userInfo.getName(), out));
			Thread ClientReceiveThread = new Thread(new ClientReceiveThread(in));

			ClientSendThread.start();
			ClientReceiveThread.start();

		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}
}