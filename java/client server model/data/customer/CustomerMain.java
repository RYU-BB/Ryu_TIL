package customer3;

import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class CustomerMain implements PublicConstants {
	public static void main(String[] args) throws NoSuchAlgorithmException {
		int menu = 0;
		Scanner sc = new Scanner(System.in);
		CustomerManagement manage = new CustomerManagement();
		if (!manage.connect())
			return;
		while (true) {
			do {
				for (int i = 0; i < MENU_NUM; i++)
					System.out.print(MENU[i]);
				menu = sc.nextInt();
			} while (menu < 0 || menu > MENU_NUM - 1);
			if (menu == PRINT_CUSTOMER_LIST)	
				manage.printCustomers();
			if (menu == REGISTER_NEW_CUSTOMER)	
				manage.registerNewCustomer();
			if (menu == MODIFY_CUSTOMER_INFO)	
				manage.modifyCustomerInfo();
			if (menu == MODIFY_CUSTOMER_POINT)	
				manage.modifyCustomerPoint();
			if (menu == LOOKUP_CUSTOMER_POINT)	
				manage.lookupCustomerPoint();
			if (menu == DELETE_CUSTOMER)
				manage.deleteCustomer();
				
			if (menu == EXIT) {
				sc.close();
				break;
			}
		}
	}

}
