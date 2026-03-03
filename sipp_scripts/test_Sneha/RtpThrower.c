#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <pthread.h>

#define PORT 55000
#define MAXLINE 200
#define LOCAL_IP "10.133.36.30"
#define REMOTE_IP "10.133.39.186"

unsigned char rtp [] ={0x80,0x80,0x92,0xdb,0x00,0x00,0x00,0xa0,0x34,0x3d,0xa9,0x9b,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x7f,0xff,0xff,0x7f,0xff,0x7f,0x7f,0xff,0xff,0x7f,0x7f,0xff,0x7f,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xfe,0xff,0xff,0xfe,0x7e,0xfd,0x7d,0xfd,0x7e,0x75,0xfc,0x73,0x75,0xfe,0x71,0x7b,0x7e,0x7a,0xfc,0xfd,0xf9,0xfb,0xfb,0xf6,0xff,0xf9,0xf8,0x7c,0xfa,0xfd,0x7d,0xfc,0xff,0x7e,0xfe,0xfe,0xfe,0x7e,0xfd,0x7e,0x7d,0xfe,0x7c,0x7c,0x7d,0x7a,0x7b,0x7b,0x7c,0x7d,0x7f,0xfd,0xfb,0xf8,0xf5,0xf4,0xf1,0xf0,0xf1,0xf0,0xf2,0xf5,0xf7,0xfb,0xff,0x7a,0x76,0x71,0x6e,0x6d,0x6b,0x6b,0x6b,0x6b,0x6c,0x6e,0x70,0x75,0x7c,0xf9,0xf2,0xeb,0xe8,0xe3,0xdf,0xde,0xdb,0xe3,0xdf,0xe4,0x7e,0xf4,0x6f,0x62,0x66,0x5e,0x5e,0x5f,0x60};

unsigned char a = 0x34;
unsigned char recvRtp [MAXLINE];
void * senderThread (void *arg);
void * receiverThread (void *arg);
struct sockaddr_in localaddr, remoteaddr;

int main(int argc, char *argv[]) {
    int sockfd;
    char buffer[9];
    
    pthread_t sender, receiver;

    // Creating socket file descriptor
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&localaddr, 0, sizeof(localaddr));
    memset(&remoteaddr, 0, sizeof(remoteaddr));

    // Filling server information
    localaddr.sin_family = AF_INET;
    localaddr.sin_port = htons (PORT);
    inet_pton(AF_INET, LOCAL_IP, &localaddr.sin_addr.s_addr);
   
    remoteaddr.sin_family = AF_INET;
    remoteaddr.sin_port = htons (atoi(argv[1]));
    inet_pton(AF_INET, REMOTE_IP, &remoteaddr.sin_addr.s_addr);

    if (bind(sockfd, (const struct sockaddr *)&localaddr, sizeof(localaddr)) < 0 )
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    printf("[Size=%d][sockfd=%d]\n", sizeof(rtp), sockfd);
    pthread_create(&sender, NULL, senderThread, &sockfd);
    pthread_create(&receiver, NULL, receiverThread, &sockfd);

    /*int n, len;
    memcpy (buffer, &data, sizeof(unsigned int));
    memcpy (buffer+sizeof(unsigned int), &data2, sizeof(unsigned int));

    sendto(sockfd, (const char *)buffer, 8,
        MSG_CONFIRM, (const struct sockaddr *) &servaddr,
            sizeof(servaddr));
    printf("Hello message sent.\n");

    n = recvfrom(sockfd, (char *)buffer, MAXLINE,
                MSG_WAITALL, (struct sockaddr *) &servaddr,
                &len);
    buffer[n] = '\0';
    printf("Server : %s\n", buffer);*/
    pthread_join(sender, NULL);
    //pthread_join(receiver, NULL);

    close(sockfd);
    return 0;
}

void * senderThread (void *arg)
{
    int sockfd = *(int*)arg;
    printf ("SenderThread[%d]\n", sockfd);
    int len = sizeof(remoteaddr);
    sendto(sockfd, (const char *)rtp, sizeof(rtp), MSG_CONFIRM, (const struct sockaddr *)&remoteaddr, sizeof(remoteaddr));
    while (1)
    {
        sendto(sockfd, (const char *)rtp, sizeof(rtp), MSG_CONFIRM, (const struct sockaddr *)&remoteaddr, sizeof(remoteaddr));
        printf("packet sent\n");
        rtp[8] = ++a;
        sleep (8);
    }
return NULL;
}

void * receiverThread (void *arg)
{
    printf ("ReceiverThread\n");
    int sockfd = *(int*)arg;
    int len = sizeof(remoteaddr);
    int readLen = 0;
    while (1)
    {
        readLen = recvfrom(sockfd, (char *)recvRtp, MAXLINE, MSG_WAITALL, (struct sockaddr *) &remoteaddr, &len);
        recvRtp[readLen] = '\0';
        printf("Rtp Packet received [len=%d] [recvLen=%d]\n", len, readLen);
    }
return NULL;
}
