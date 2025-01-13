#include <stdio.h>

int main(){
    int  c=10;
    int w=5;

   for( int i=0; i<w; i++)
{   
     if (i==0||i==w-1){

    for(int j=0;j<c;j++){
    printf("#");
    }
    }else{
        printf("#");
     
        for(int j=1;j<c-1;j++)
        {
            //if( j==0||j==c-1)
        printf("*");
        }
      
        printf("#");
     }
        printf("\n"); 
}
  

 return (0);
}