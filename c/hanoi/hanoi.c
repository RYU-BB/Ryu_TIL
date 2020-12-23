#include <stdio.h>

void hanoi(int disk, char from, char midpoint, char to) {
   if (disk == 1) {
      printf("원판 %d를 %c기둥에서 %c기둥으로 옮겼습니다.\n", disk, from, to);
   }
   else {
      hanoi(disk - 1, from, to, midpoint);
      printf("원판 %d를 %c기둥에서 %c기둥으로 옮겼습니다.\n", disk, from, to);
      hanoi(disk - 1, midpoint, from, to);
   }
}

int main(void) {
   int disk;
   char A = 'A', B = 'B', C = 'C';

   printf("값을 입력해주세요 : ");
   scanf_s("%d", &disk);
   hanoi(disk, A, B, C);

   return 0;
}