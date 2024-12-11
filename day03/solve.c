#include <stdio.h>
#include <ctype.h>
#include <cstring>

bool task2(char c,bool *check){
static int pointer2=0;
const char key2_1[]="do()",key2_2[]="don't()";
if(c==key2_2[pointer2] || c==key2_1[pointer2]){
   pointer2++;
   if(c==')')
      *check=(pointer2==strlen(key2_1)) ? 1 : 0;
}else
   pointer2=0;
return check;
}
int main(){
   char c=1;
   unsigned result=0,n1=0,n=0;
   int pointer=0;
   const char key[]="mul(*,*)";
   bool checking=true;;
   ///for pause saning purpose
   while(scanf("%c",&c) != EOF){
      //printf("\n%c=%c",c,key[pointer]);
      
      ///check for do/don't in task 2
         task2(c,&checking);
      ///if key is probably number
      if(checking){
      if(key[pointer]=='*'){
         // printf("[%c]",c);
         if(isdigit(c)){
            n1=n1*10+(int)(c-'0');
         }
         else if(c==','){
            n=n1;
            n1=0;
         }
         else if(c==')'){
            // printf("  {%u*%u}=%u\n",n,n1,n*n1);
            pointer=0;
            result+=n*n1;
            n=n1=0;
         }
         else{
            pointer=0;
            n=n1=0;
         }
      }
      ///if encounter correct key then
      else if(c==key[pointer]){
         pointer++;  
      }
      else{
         pointer=0;
         n=n1=0;
      }
      }
   }
   printf("%u\n",result);
   return 0;
}