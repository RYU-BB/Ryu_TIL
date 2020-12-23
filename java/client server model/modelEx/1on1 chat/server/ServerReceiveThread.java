package server;

import java.io.IOException;
import java.io.ObjectInputStream;
import client.ClientUserInfo;

public class ServerReceiveThread implements Runnable, Constants {
	ObjectInputStream in;
	ClientUserInfo clientUser;

	public ServerReceiveThread(ObjectInputStream in) {
		this.in = in;
	}

	public void run() {
		try {
			while (true) {
				clientUser = (ClientUserInfo)in.readObject();
				if (clientUser.getMsg().equalsIgnoreCase(EXIT_MSG)) {
					System.out.println(CLIENT_LOGOUT_MSG);
					break;
				}
				System.out.println(clientUser.getName() +": "+clientUser.getMsg());
			}
		} catch (IOException e) {
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
