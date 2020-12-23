#pragma once
#include <stdio.h>
#include <stdlib.h>

typedef enum { false, true } bool;

extern bool commentChk(int* chk, char ch,int* singleQuotesChk,int* doubleQuotesChk);
extern bool commentsChk(int* chkStart,int* ChkEnd, char ch,int* singleQuotesChk,int* doubleQuotationChk);
extern bool singleQuotationChk(int* chk, char ch, int* doubleQuotationChk);
extern bool doubleQuotationChk(int* chk, char ch);