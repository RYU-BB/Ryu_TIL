package customer3;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.InputMismatchException;
import java.util.Scanner;

public class CustomerManagement implements PublicConstants {
	private String url;
	private String username;
	private String password;
	private String hashType;
	private String query;
	private Statement stmt;
	private Connection conn;
	Scanner sc;

	CustomerManagement() {
		this.sc = new Scanner(System.in);
		this.url = "jdbc:oracle:thin:@localhost:1521:xe";
		this.username = null;
		this.password = null;
		this.conn = null;
		this.hashType = "SHA-256";
		this.query = null;
		this.stmt = null;
	}

	public boolean connect() {
		System.out.print(DB_LOGIN_ID_MSG);
		this.username = sc.next();
		System.out.print(DB_LOGIN_PW_MSG);
		this.password = sc.next();

		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			conn = DriverManager.getConnection(this.url, this.username, this.password);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		if (conn == null) {
			System.out.println(DB_CONN_FAILED_MSG);
			return false;
		} else {
			System.out.println(DB_CONN_MSG);
			return true;
		}
	}

	/* ## 0. 고객 명단 출력 */
	public void printCustomers() {
		this.query = "SELECT * FROM " + DB_CUSTOMER_TABLE_NAME;
		try {
			this.stmt = this.conn.createStatement();
			ResultSet rs = this.stmt.executeQuery(query);
			while (rs.next()) {
				System.out.println(rs.getString(DB_CUSTOMER_TABLE_ATTRIBUTE[0]) + TAP
						+ rs.getString(DB_CUSTOMER_TABLE_ATTRIBUTE[1]) + TAP
						+ rs.getString(DB_CUSTOMER_TABLE_ATTRIBUTE[2]) + TAP
						+ rs.getString(DB_CUSTOMER_TABLE_ATTRIBUTE[3]) + TAP
						+ rs.getString(DB_CUSTOMER_TABLE_ATTRIBUTE[4]) + TAP
						+ rs.getInt(DB_CUSTOMER_TABLE_ATTRIBUTE[5]));
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	// 1
	public void registerNewCustomer() throws NoSuchAlgorithmException{
		Customer newCustomer = new Customer();
		boolean again = false;
		newCustomer.setCustomerId(this.inputCustomerId(false));
		do {
			if(again)
				System.out.println(PASSWD_MISMATCH_MSG);
			System.out.print(CUSTOMER_PW_ENTER_MSG);
			newCustomer.setCustomerPw(this.getHashValue(sc.next(), this.hashType));
			System.out.print(CUSTOMER_PW_CHECK_MSG);
			again = true;
		}while (!(newCustomer.getCustomerPw().contentEquals(this.getHashValue(sc.next(), this.hashType))));
		System.out.print(CUSTOMER_NAME_ENTER_MSG);
		newCustomer.setName(sc.next());
		System.out.print(CUSTOMER_GENDER_ENTER_MSG);
		newCustomer.setGender(sc.next());
		System.out.print(CUSTOMER_PN_ENTER_MSG);
		newCustomer.setPhoneNum(sc.next());
		newCustomer.setPoint(0);
		this.insertIntoDB(newCustomer);
	}
	
	/*INSERT DB*/
	private void insertIntoDB(Customer newCustomer) {
		this.query = "INSERT INTO " + DB_CUSTOMER_TABLE_NAME + " VALUES";
		try {
			this.stmt = this.conn.createStatement();
			this.query += "('" + newCustomer.getCustomerId() + "','" + newCustomer.getCustomerPw() + "','"
					+ newCustomer.getName() + "','" + newCustomer.getPhoneNum() + "','" + newCustomer.getGender() + "',"
					+ newCustomer.getPoint() + ")";
			this.stmt.executeUpdate(query);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		System.out.println("추가 완료");
	}

	// 2
	public void modifyCustomerInfo() {
		int inputArrtNo;
		String updateAttr = null, updateValue = null;
		String customerId = inputCustomerId(true);
		do {
			for (int arrtNo=0; arrtNo<DB_CUSTOMER_TABLE_ATTRIBUTE.length; arrtNo++) {
				System.out.println(arrtNo+" . "+DB_CUSTOMER_TABLE_ATTRIBUTE[arrtNo]);
			}
			System.out.print(UPDATE_CUSTOMER_ATTRIBUTE);
			inputArrtNo = sc.nextInt();
		} while (inputArrtNo < 0 || inputArrtNo > 6);
		if (inputArrtNo == CUSTOMER_ID)
			updateAttr = "CUSTOMER_ID";
		if (inputArrtNo == CUSTOMER_PW)
			updateAttr = "CUSTOMER_PW";
		if (inputArrtNo == CUSTOMER_NAME)
			updateAttr = "CUSTOMER_NAME";
		if (inputArrtNo == PHONE_NUM)
			updateAttr = "PHONE_NUM";
		if (inputArrtNo == GENDER)
			updateAttr = "GENDER";
		if (inputArrtNo == POINT)
			updateAttr = "POINT_";
		System.out.print(UPDATE_CUSTOMER_VALUE);
		updateValue = sc.next();
		updateIntoDB(DB_CUSTOMER_TABLE_NAME, customerId, updateAttr, updateValue);
	}

	/*UPDATE DB*/
	private void updateIntoDB(String table, String customerId, String updateAttr, String updateValue) {
		try {
			this.stmt = this.conn.createStatement();
			if (updateAttr.equalsIgnoreCase("POINT_"))
				this.query = "UPDATE " + table + " SET " + updateAttr + " = " + updateValue + " WHERE CUSTOMER_ID = '"
						+ customerId + "'";
			else
				this.query = "UPDATE " + table + " SET " + updateAttr + " = '" + updateValue + "' WHERE CUSTOMER_ID = '"
						+ customerId + "'";
			this.stmt.executeUpdate(query);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		System.out.println("업데이트 완료");
	}

	// 3
	public void modifyCustomerPoint() {
		this.printCustomers();
		String customerId = inputCustomerId(true);
		System.out.print("\n" + UPDATE_CUSTOMER_POINT);
		Integer updateValue = sc.nextInt();
		updateIntoDB(DB_CUSTOMER_TABLE_NAME, customerId, "POINT_", updateValue.toString());
	}

	// 4
	public void lookupCustomerPoint() {
		int menu =0;
		do {
			for(int i=0; i<POINT_MENU_NUM; i++) {
				System.out.print(LOOKUP_POINT_MENU[i]);
				}
			menu=sc.nextInt();
		} while (menu < 1 || menu > POINT_MENU_NUM-1);
		printCustomerPoint(menu);
	}
	
	/*DB POINT 조회*/
	public void printCustomerPoint(int menu) {
		if(menu==CUSTOMERS_POINT) {
		query = "SELECT CUSTOMER_NAME, POINT_ FROM " + DB_CUSTOMER_TABLE_NAME;
		try {
			this.stmt = this.conn.createStatement();
			ResultSet rs = this.stmt.executeQuery(this.query);
			while(rs.next()) {
				System.out.println(rs.getString("CUSTOMER_NAME") + "님의 포인트는 " + rs.getString("POINT_") + "입니다.");
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}	
		if(menu==CUSTOMER_POINT) {
		this.printCustomerPoint(CUSTOMERS_POINT);
		String customerId = inputCustomerId(true);
		query = "SELECT CUSTOMER_ID,CUSTOMER_NAME, POINT_ FROM " + DB_CUSTOMER_TABLE_NAME;
		try {
			this.stmt = this.conn.createStatement();
			ResultSet rs = this.stmt.executeQuery(this.query);
			while (rs.next()) {
				if (rs.getString("CUSTOMER_ID").equals(customerId))
					System.out.println(rs.getString("CUSTOMER_NAME") + "님의 포인트는 " + rs.getString("POINT_") + "입니다.");
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
		if(menu==GENDER_AVG_POINT) {
			String gender=null;
			boolean again=false;
			do {
				if(again)
					System.out.println(NOT_MATCH_GENDER_MSG);
				System.out.print(CUSTOMER_GENDER_ENTER_MSG);
				gender = sc.next();
				again=true;
			} while(!(gender.contentEquals(MALE)) && !(gender.contentEquals(FEMALE)));
			query = "SELECT AVG(POINT_) FROM " + DB_CUSTOMER_TABLE_NAME + " WHERE GENDER = '" + gender + "'";
			try {
				this.stmt = this.conn.createStatement();
				ResultSet rs = this.stmt.executeQuery(this.query);
				rs.next();
				System.out.println(gender + "성의 평균 포인트는 " + rs.getString("AVG(POINT_)") + "점 입니다.");
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
	
	// 5
	public void deleteCustomer() {
		int menu =0;
		do {
			for(int i=0; i<DELETE_CUSTOMER_MENU_NUM; i++) {
				System.out.print(DELETE_CUSTOMER_MENU[i]);
				}
			menu=sc.nextInt();
		} while (menu < 1 || menu > DELETE_CUSTOMER_MENU_NUM-1);
		deleteCustomerDB(menu);		
	}

	public void deleteCustomerDB(int menu) {
		if(menu==CUSTOMER_DELETE) {
			String customerId = inputCustomerId(true);
			query = "DELETE " + DB_CUSTOMER_TABLE_NAME + " WHERE CUSTOMER_ID = '" + customerId + "'";
			try {
				this.stmt = this.conn.createStatement();
				this.stmt.executeUpdate(query);
				
			} catch (SQLException e) {
				e.printStackTrace();
			}
			System.out.println("삭제 완료");
		}
		if(menu==ALL_CUSTOMER_DELETE) {
			String chk = null;
			boolean again = false;
			do {
				if(again) {
					System.out.println(CHK_FAILED);
					return;
				}
				System.out.println(ALL_DELETE_CHK_MSG);
				chk = sc.next();
				again=true;
			}while(!(chk.contentEquals("삭제하겠습니다")));
			query = "truncate table " + DB_CUSTOMER_TABLE_NAME;
			try {
				this.stmt = this.conn.createStatement();
				this.stmt.execute(query);
			} catch (SQLException e) {
				e.printStackTrace();
			}
			System.out.println("삭제완료!!!!");
		}
		}
		
	private String inputCustomerId(boolean existWant) {
		String customerId = null;
		boolean again = false;
		if (existWant) {
			do {
				if (again)
					System.out.println(NOT_FOUND_CUSTOMER_ID_MSG);
				System.out.print(CUSTOMER_ID_ENTER_MSG);
				customerId = sc.next();
				again = true;
			} while (!this.checkCustomerId(customerId));
		} else {
			do {
				if (again)
					System.out.println(CUSTOMER_ID_OVERLAP_MSG);
				System.out.print(CUSTOMER_ID_ENTER_MSG);
				customerId = sc.next();
				again = true;
			} while (this.checkCustomerId(customerId));
		}
		return customerId;
	}

	private boolean checkCustomerId(String customerId) {
		String query = "SELECT CUSTOMER_ID FROM " + DB_CUSTOMER_TABLE_NAME;
		String Id = null;
		Statement stmt;
		try {
			stmt = conn.createStatement();
			ResultSet rs = stmt.executeQuery(query);
			while (rs.next()) {
				if (rs.getString("CUSTOMER_ID").contentEquals(customerId))
					return true;
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return false;
	}

	private String getHashValue(String string, String hashType) throws NoSuchAlgorithmException {
		MessageDigest md;
		md = MessageDigest.getInstance(hashType);
		byte[] hashByte = md.digest(string.getBytes());
		StringBuffer buf = new StringBuffer();
		for (byte b : hashByte)
			buf.append(Integer.toString((b & 0xff) + 0x100, 16).substring(1));
		return buf.toString();
	}
}