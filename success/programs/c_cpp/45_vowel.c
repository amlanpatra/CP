// Check vowel or consonant
#include<stdio.h>
int main(void)
{    
    char cha;
	printf("Enter a character : \n");
	scanf("%c",&cha);
	if (cha == 'a' || cha == 'e' ||cha == 'i' ||cha == 'o' ||cha == 'u' || cha == 'A' 
		||cha == 'E' ||cha == 'I' ||cha == 'O' ||cha == 'U')
	{
		printf("The character entered '%s' is a vowel",&cha);
	}
	else
	{
		printf("The character entered is a consonant");
	}
	

	return 0;
}