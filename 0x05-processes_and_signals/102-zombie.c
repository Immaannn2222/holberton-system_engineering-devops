#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop
 *
 * Return:void
 */

int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
 * main- fucntion zombie
 *
 * Return: 0 on success
 */

int main(void)
{
pid_t _pid;
int i = 0;
while (i < 5)
{
_pid = fork();
if (_pid > 0)
{
printf("Zombie process created, PID: %d\n", _pid);
}
else
exit(0);
i++;
}
infinite_while();
return (0);
}
