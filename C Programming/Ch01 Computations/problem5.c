#include <stdio.h>
#include <time.h>
#include <string.h>

int main()
{
    char userInput[6];
    int t1, t2, sec;

    printf("Commands:\n"
           "start..............Start a new timer\n"
           "lap................Print time elapsed\n"
           "stop...............Stop/exit the timer\n\n");

    // until user enters stop, loop continues
    while (strcmp("stop", userInput) != 0)
    {
        printf("Enter a command here->");
        scanf("%5s", &userInput);

        // stores time in variable when user enters start
        if (strcmp("start", userInput) == 0)
        {
            t1 = time(0);
            printf("Timer has been started...\n");
        }
        // display time elapsed when user enters lap/stop
        else if ((strcmp("lap", userInput) == 0) || (strcmp("stop", userInput) == 0))
        {
            t2 = time(0);
            sec = t2 - t1;

            // convert sec to hrs:min:sec. Modulus 60 used to display time
            int hr, min;
            min = sec / 60;
            hr = min / 60;

            // if statement avoids displaying time elapsed if timer was not started
            if (sec < 999999999) printf("time = %i:%i:%i\n", hr, min % 60, sec % 60);
        }
        else printf("Command not recognized\n");
    }
    printf("End of program");
    return 0;
}