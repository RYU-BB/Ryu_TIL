package client;

import java.io.IOException;
import java.io.ObjectInputStream;
import server.ServerUserInfo;

public class ClientReceiveThread implements Runnable,Constants{
	ObjectInputStream in;
	ServerUserInfo serverUser;
	
	public ClientReceiveThread(ObjectInputStream in){
		this.in = in;
	}
	
	public void run() {
		try {
			while (true) {
				serverUser = (ServerUserInfo)in.readObject();
				if(serverUser.getMsg().equalsIgnoreCase(EXIT_MSG)) {
					System.out.println(SERVER_LOGOUT_MSG);
					break;
				}
				System.out.println(serverUser.getName()+": "+serverUser.getMsg());
			}
		} catch (IOException e) {
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
