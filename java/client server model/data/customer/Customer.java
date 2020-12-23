package customer3;

public class Customer {
	private String customerId = null;
	private String customerPw = null;
	private String phoneNum=null;
	private String name = null;
	private String gender = null;
	private int point = 0;
	
	/*Getter & Setter*/

	public String getPhoneNum() {
		return phoneNum;
	}
	public void setPhoneNum(String phoneNum) {
		this.phoneNum = phoneNum;
	}
	public String getCustomerId() {
		return customerId;
	}
	public void setCustomerId(String cusotmerId) {
		this.customerId = cusotmerId;
	}
	public String getCustomerPw() {
		return customerPw;
	}
	public void setCustomerPw(String customerPw) {
		this.customerPw = customerPw;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	public int getPoint() {
		return point;
	}
	public void setPoint(int point) {
		this.point = point;
	}
}
