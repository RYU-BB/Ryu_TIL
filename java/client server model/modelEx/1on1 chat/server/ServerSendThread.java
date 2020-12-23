package server;

import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.Scanner;

import client.ClientUserInfo;

public class ServerSendThread implements Runnable, Constants {
	ObjectOutputStream out = null;
	Scanner sc = new Scanner(System.in);
	String userName=null;

	public ServerSendThread(String userName,ObjectOutputStream out) {
		this.out = out;
		this.userName=userName;
	}

	public void run() {
		try {
			
			
			while (true) {
				ServerUserInfo userInfo = new ServerUserInfo();
				userInfo.setName(userName);
				System.out.print(ENTER_MSG);
				userInfo.setMsg(sc.nextLine());
				if (userInfo.getMsg().equalsIgnoreCase(EXIT_MSG)) {
					out.writeObject(userInfo);
					out.flush();
					System.out.println(LOGOUT_MSG);
				} else {
					out.writeObject(userInfo);
					out.flush();
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
