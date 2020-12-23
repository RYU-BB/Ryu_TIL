#include "CommentChk.h"

bool commentLineChk(int* chk, char ch,int* singleQuotationChk,int* doubleQuotationChk) {	// //주석체크값,현재문자,홑따옴표체크값,쌍따옴표체크값
	if ((*singleQuotationChk) == 1 || (*doubleQuotationChk) == 1) return false;				//따옴표내부면 return  false

	switch (*chk) {																			// //주석체크값비교 시작  0: 주석과 상관없는 상태 1:직전 문자가 /인 상태 2:연속으로 /를 두개 받아서 주석 상태
	case 0:																					// 0일때 현재문자가 / 라면 주석체크값 1증가
		if (ch == '/') (*chk)++;
		return false;
	case 1:																					// 1일때 현재문자가 /라면 주석체크값 1증가 아닐경우 0으로 감소
		if (ch == '/') (*chk)++;
		else *chk=0;
		return false;
	case 2:																					// 2일때 현재문자가 \n이라면 주석체크값 0으로 초기화 \n이 아니라면 return true;
		if (ch == '\n') {
			*chk = 0;
			return true;
		}
		else return true;
	}
}

bool commentsChk(int* ChkStart,int* ChkEnd,char ch, int* singleQuotationChk, int* doubleQuotationChk) { // /**/주석체크시작과끝,현재문자,홑따옴표체크값,쌍따옴표체크값
	if ((*singleQuotationChk) == 1 || (*doubleQuotationChk) == 1) return false;							//따옴표 내부면 return false;

	switch (*ChkStart) {																				// /* 비교시작 0: 주석과 관련없는 상태 1:직전문자가 /인상태 2: 연속으로 /*를 입력받아서 주석상태
	case 0:																								//0일때 현재문자가 /라면 주석체크값 1증가
		if (ch == '/') (*ChkStart)++;			
		return false;
	case 1:																								//1일때 현재문자가 *이라면 주석체크값 1증가 아닐경우 0으로 감소
		if (ch == '*') (*ChkStart)++;
		else *ChkStart=0;
		return false;
	case 2:																								//2일때 End값이 0이고 현재문자가 *이라면 end값 1증가
		if ((*ChkEnd)==0 && ch == '*') {																//end값이 1이고 현재문자가 / 라면 chk값 전부 0으로 초기화 아닐경우 end값 0으로 감소 및 return true;
			*ChkEnd = 1;
			return true;
		}

		if ((*ChkEnd) == 1 && ch == '/') {
			*ChkStart = 0;
			*ChkEnd = 0;
			return true;
		}
		else *ChkEnd = 0;
		return true;
	}
}

bool singleQuotationChk(int* chk, char ch, int* doubleQuotationChk) {									//체크값 현재문자 쌍따옴표체크값
	if ((*doubleQuotationChk) == 1) return false;														//쌍따옴표 내부면 return false;
																										
	switch(*chk) {																						//체크값비교시작 0: 따옴표와 관련없는 상태 1:따옴표내부
	case 0:																								//0일경우 현재문자가 '라면 체크값 1증가 return true;
		if (ch == "'") {
			(*chk)++;
			return true;
		}
		else return false;
	case 1:																								//1일경우 현재문자가 '라면 체크값 1감소 아닐경우 return true;
		if (ch == "'") {
			*chk = 0;
			return true;
		}
		else return true;
		}
}

bool doubleQuotationChk(int* chk, char ch) {									//체크값 현재문자 홑따옴표체크함수가 true일때 이 함수는 실행되지 않으므로 홑따옴표체크값을 비교해줄 필요가 없다.
	
	switch (*chk) {																//체크값 비교 시작 0: 따옴표와 관련없는 상태 1:따옴표내부
	case 0:																		//0일경우 현재문자가 '라면 체크값 1증가 return true;
		if (ch == '"') {	
			(*chk)++;
			return true;
		}
		else return false;
	case 1:																		//1일경우 현재문자가 '라면 체크값 1감소 아닐경우 return true;
		if (ch == '"') {
			*chk = 0;
			return true;
		}
		else return true;
	}
}