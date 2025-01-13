// #include<stdio.h>


// int main(){
//     char name[14];
//     int age; 
//         printf("ENTER YOUR INFORMATION\n");
//             fgets(name,sizeof(name),stdin);
//                 printf("\n");
//                 scanf("%d",&age);

//                     printf("MY INFORMATION \n %d %s",age,name);
//                     printf("\n");
// return(0);
// }

#include<stdio.h>
int main(){
int x,y;
int t;
    printf("ENTER FIRST NUM:","\n");
        scanf("%d",&x);
            printf("ENTER SECOUND NUM:","\n");
                scanf("%d",&y);
     int z;
     char q;
            printf("/n ENTER THE OPRATION :");
      
              // fgets(&q,1,stdin);
      scanf("%c",&q);

             switch(q)
            {
                case ('*'):
               { 
                z=x*y;
                    printf("%d",z);
                    printf("\n");
                    break;
               }case ('+'):
                {
                     z=x+y;
                printf("%d",z);
                    printf("\n");
                    break;
                }case('-'):
                 {  
                     z=x-y;               
                printf("%d",z);
                printf("\n");
                    break;
                 }case('/'):
                  { 
                      z=x/y;
                printf("%d",z);
                printf("\n");
                  }
                  default:
printf("WRONG CHOOSE");
            }
            return(0);


}