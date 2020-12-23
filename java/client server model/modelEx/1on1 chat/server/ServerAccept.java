package server;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class ServerAccept implements Constants {
	ObjectInputStream in = null;
	ObjectOutputStream out = null;
	ServerSocket listener = null;
	Socket socket = null;
	Scanner sc=new Scanner(System.in);

	public ServerAccept() {
		try {
			listener = new ServerSocket(9999);
			System.out.println(WAIT_CONNECT_MSG);
			socket = listener.accept();
			System.out.println(CONNECT_MSG);
			out = new ObjectOutputStream(socket.getOutputStream());
			
			ServerUserInfo userInfo = new ServerUserInfo();
			System.out.print("닉네임을 입력해주세요 >> ");
			userInfo.setName(sc.nextLine());
			userInfo.setMsg(ACCESS_MSG);
			
			out.writeObject(userInfo);
			out.flush();
			
			in = new ObjectInputStream(socket.getInputStream());
			
			Thread ServerSendThread = new Thread(new ServerSendThread(userInfo.getName(),out));
			Thread ServerReceiveThread = new Thread(new ServerReceiveThread(in));
			ServerSendThread.start();
			ServerReceiveThread.start();
		} catch (Exception e) {
			e.printStackTrace();
		}

	}
}
