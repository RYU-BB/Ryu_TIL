#pragma once
#include <stdio.h>
#include <stdlib.h>
#define MAX_STACK_SIZE	100
//^&*^&^*/////'""'''''''"""''"/*
/*////'''''''''''''''"""""""""{}{}{}{}{}{}{}"*/
#define Element	char
#define printElem(e) printf("(%c)", e)

typedef struct ArrayStack {
	Element	data[MAX_STACK_SIZE];
	int		top;
} Stack;

extern void error(char* str);
extern void initStack(Stack* s);
extern int isEmpty(Stack* s);
extern int isFull(Stack* s);
extern void push(Stack* s, Element e);
extern Element pop(Stack* s);
extern Element peek(Stack* s);
extern int size(Stack* s);
extern void display(Stack* s, char* msg);

