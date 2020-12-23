package customer3;

public interface PublicConstants {
	//MENU
	public static final int MENU_NUM = 8;
	public static final int POINT_MENU_NUM = 4;
	public static final int DELETE_CUSTOMER_MENU_NUM = 3;
	public static final int PRINT_CUSTOMER_LIST = 0;
	public static final int REGISTER_NEW_CUSTOMER = 1;
	public static final int MODIFY_CUSTOMER_INFO = 2;
	public static final int MODIFY_CUSTOMER_POINT = 3;
	public static final int LOOKUP_CUSTOMER_POINT = 4;
	public static final int DELETE_CUSTOMER = 5;
	public static final int EXIT = 6;
	
	//MODIFY MENU
	public static final int CUSTOMER_ID =0;
	public static final int CUSTOMER_PW =1;
	public static final int CUSTOMER_NAME =2;
	public static final int PHONE_NUM = 3;
	public static final int GENDER=4;
	public static final int POINT = 5;
	
	//POINT MENU
	public static final int CUSTOMERS_POINT =1;
	public static final int CUSTOMER_POINT =2;
	public static final int GENDER_AVG_POINT =3;
	
	//DELETE MENU
	public static final int CUSTOMER_DELETE = 1;
	public static final int ALL_CUSTOMER_DELETE = 2;
	
	//MAIN TITLE
	public static final String TITLE = "\\t### Customer Management Program ###\\n";
	public static final String[] MENU = {"## 0. 고객 명단 출력\n",
										 "## 1. 신규 고객 등록\n",
										 "## 2. 고객 정보 수정\n",
										 "## 3. 고객 포인트 수정\n",
										 "## 4. 고객 포인트 조회\n",
										 "## 5. 고객 삭제\n",
										 "## 6. 프로그램 종료\n",
										 ">> Input : "}; 
	public static final String[] LOOKUP_POINT_MENU = {"## 1. 전체고객포인트 출력\n",
														"## 2. 고객포인트 출력\n",
														"## 3. 성별 포인트평균 출력\n",
														">> input : "};
	public static final String[] DELETE_CUSTOMER_MENU = {"##1. 고객 삭제\n",
														"##2. 전체 고객 삭제\n",
														">> input : "};
	
	//MSG
	public static final String INT_MISMATCH_EXCEPT_MSG = "잘못입력했습니다!! 정수로 다시 입력해주세요.";
	public static final String NO_EXIST_CUSTOMER_MSG = "고객 명단이 없습니다!!";
	public static final String MODIFY_CUSTOMER_MSG = ">> 수정하고 싶은 고객님의 id를 입력하세요 : ";
	public static final String REGISTER_CUSTOMER_MSG = ">> 등록하고 싶은 고객님의 id를 입력하세요 : ";
	public static final String SEARCH_CUSTOMER_MSG = ">> 조회를 원하는 고객님의 고객 번호를 입력하세요 : ";
	public static final String DELETE_CUSTOMER_MSG = ">> 삭제를 원하는 고객님의 고객 번호를 입력하세요 : ";
	public static final String ID_OR_PW_FAILED = "아이디 또는 패스워드가 틀렸습니다. 다시 입력해주세요.";
	public static final String CUSTOMER_ID_OVERLAP_MSG = "이미 있는 아이디입니다. 다시 입력해주세요.";
	public static final String CUSTOMER_ID_ENTER_MSG = "아이디를 입력해주세요 >> ";
	public static final String CUSTOMER_PW_ENTER_MSG = "비밀번호를 입력해주세요 >> ";
	public static final String CUSTOMER_PW_CHECK_MSG = "비밀번호를 다시 입력해주세요 >>";
	public static final String CUSTOMER_NAME_ENTER_MSG = "이름을 입력해주세요 >> ";
	public static final String CUSTOMER_PN_ENTER_MSG = "핸드폰번호를 입력해주세요 >> ";
	public static final String CUSTOMER_GENDER_ENTER_MSG = "성별을 입력해주세요 (남/여)>> ";
	public static final String CUSTOMER_POINT_ENTER_MSG = "설정할 포인트를 입력해주세요 >> ";
	public static final String UPDATE_CUSTOMER_ATTRIBUTE = "변경할 속성을 선택해주세요 >>";
	public static final String UPDATE_CUSTOMER_VALUE = "변경할 값을 입력해주세요 >>";
	public static final String UPDATE_CUSTOMER_POINT = "변경할 포인트를 입력해주세요 >>";
	public static final String TAP = "\t";
	public static final String PASSWD_MISMATCH_MSG = "비밀번호가 서로 다릅니다.";
	public static final String NOT_FOUND_CUSTOMER_ID_MSG = "아이디를 찾을 수 없습니다.";
	public static final String NOT_MATCH_GENDER_MSG = "성별을 다시 입력해주세요. ";
	public static final String CHK_FAILED = "전체고객삭제를 취소합니다. ";
	public static final String ALL_DELETE_CHK_MSG = "정말 전체고객을 삭제하시겠습니까? 삭제를 원하면 '삭제하겠습니다'를 입력해주세요.";
	
	public static final String MALE = "남";
	public static final String FEMALE = "여";
	//DB
	public static final String DB_CUSTOMER_TABLE_NAME = "CUSTOMER_TABLE";
	public static final String DB_CUSTOMER_TABLE_ATTRIBUTE[] ={ "CUSTOMER_ID",
														    "CUSTOMER_PW",
														    "CUSTOMER_NAME",
														   	"PHONE_NUM",
														   	"GENDER",
															"POINT_"};
	public static final String DB_LOGIN_ID_MSG = "ORACLE ID >>";
	public static final String DB_LOGIN_PW_MSG = "ORACLE PW >>";
	public static final String DB_CONN_FAILED_MSG = "DATABASE 연결에 실패했습니다. 다시 시도해주세요.";
	public static final String DB_CONN_MSG = "DATABASE 연결에 성공했습니다.";
}