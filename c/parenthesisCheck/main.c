#include "ArrayStack.h"
#include "CommentChk.h"

int bracketChecker(char* filename) {
	// test {
	/* [[[ */

	int nLine = 1, nChar = 0,nCharLine = 0;	//줄,단어,한 줄당 단어
	int commentChk = 0, commentsChkStart = 0, commentsChkEnd = 0, sQuotationChk = 0, dQuotationChk=0; //     //주석 체크 ,  /*  */ 시작과 끝 체크 , 작은따옴표 체크, 큰 따옴표 체크
	char	ch, ch2;
	Stack	stack;

	FILE* fp = fopen(filename, "r");
	if (fp == NULL)
		error("Error: The file does not exist.\n");

	initStack(&stack);										//스택선언
	while ((ch = getc(fp)) != EOF) {
		nChar++;											//한번 읽을 때마다 단어수 추가
		nCharLine++;										//한번 읽을 때마다 한 줄에 있는 단어 수 추가

		/*주석상태확인함수는 두개의 입력을 연속으로 확인한 뒤 실행이 되므로 앞에서 먼저 실행시키고
		따옴표확인함수는 한개의 문자만 받아도 실행되므로 뒤로 둬서 주석상태일 때는 절대 실행되지 않도록 한다.*/

		if (commentLineChk(&commentChk, ch,&sQuotationChk,&dQuotationChk)) {	// //주석 체크 함수
			continue;															// 제일먼저 실행되는 함수이므로 예외처리는 함수내에서 따옴표만 해준다.
		}
		if (commentsChk(&commentsChkStart, &commentsChkEnd, ch,&sQuotationChk,&dQuotationChk)) {	// /**/ 주석 체크함수
			commentChk = 0;													// /**/ 주석내에 //가 있을 수 있으므로 주석체크변수를 계속 초기화해준다.
			continue;
		}
		if (singleQuotationChk(&sQuotationChk, ch, &dQuotationChk)) {
			commentChk = 0;													//따옴표 내에 //과 /**/이 존재할 수 있으므로 주석체크 변수를 계속 초기화해준다.
			commentsChkStart = 0;
			continue;
		}
		if (doubleQuotationChk(&dQuotationChk, ch)) {
			commentChk = 0;													//따옴표 내에 //과 /**/이 존재할 수 있으므로 주석체크 변수를 계속 초기화해준다.
			commentsChkStart = 0;
			continue;
		}

		if (ch == '\n') {													//줄이 바뀌면 nLine++ 및 라인별문자수를 0으로 초기화
			nLine++;
			nCharLine = 0;
		}

		if (ch == '(' || ch == '{' || ch == '[') {							//현재 문자가 여는 괄호일시 push
			push(&stack, ch);
		}
		if (ch == ')') {													//닫히는 괄호일시 ch2에 스택을pop시킨후 ch2가 짝이 맞는지 확인
			ch2 = pop(&stack);
			if (ch2 == '(') {
				continue;
			} else break;
		}
		if (ch == '}') {
			ch2 = pop(&stack);
			if (ch2 == '{') {
				continue;
			}
			else break;
		}
		if (ch == ']') {
			ch2 = pop(&stack);
			if (ch2 == '[') {
				continue;
			} else break;
			}
		}
	fclose(fp);
	printf("[%s] File check result:\n", filename);
	if (isEmpty(&stack) == 0)													//파일을 전부 검사했는데 스택이 비어있지않으면 오류
		printf("  Error found (#line=%d, #char=%d)\n\n", nLine, nCharLine);
	else
		printf("  Ok (#line=%d, #char=%d)\n\n", nLine, nChar);
	return isEmpty(&stack);
}
void main() {
	bracketChecker("ArrayStack.h");
	bracketChecker("ArrayStack.c");
	bracketChecker("BracketChecker.c");
}