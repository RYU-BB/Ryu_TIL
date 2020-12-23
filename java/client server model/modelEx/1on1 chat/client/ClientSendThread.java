package client;

import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.Scanner;

public class ClientSendThread implements Runnable,Constants {
	ObjectOutputStream out = null;
	Scanner sc = new Scanner(System.in);
	String userName=null;

	public ClientSendThread(String userName,ObjectOutputStream out) {
		this.out = out;
		this.userName=userName;
	}

	public void run() {
		try {
			
			
			while (true) {
				ClientUserInfo userInfo = new ClientUserInfo();
				userInfo.setName(userName);
				System.out.println(ENTER_MSG);
				userInfo.setMsg(sc.nextLine());
				if (userInfo.getMsg().equalsIgnoreCase(EXIT_MSG)) {
					out.writeObject(userInfo);
					out.flush();
					System.out.println(LOGOUT_MSG);
					break;
				} 
				out.writeObject(userInfo);
				out.flush();
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
