package client;

import java.io.Serializable;

public class ClientUserInfo implements Serializable {
	String name=null;
	String msg=null;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getMsg() {
		return msg;
	}
	public void setMsg(String msg) {
		this.msg = msg;
	}
}
