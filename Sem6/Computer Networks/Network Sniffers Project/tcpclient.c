/* tcpclient.c */

#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>


/* 
 This code creates a client which establishes a connection with the malicious server generating worm attack
  */

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>



int main(int argc,char*argv[])
{
        int sock, bytes_recieved;  
        char send_data[1024],recv_data[1024];
        struct hostent *host;
        struct sockaddr_in server_addr;  
        host = gethostbyname(argv[1]);
        if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == -1) {				//creating a socket
            perror("Socket");
            exit(1);
        }
        server_addr.sin_family = AF_INET;     
        server_addr.sin_port = htons(5000);   
        server_addr.sin_addr = *((struct in_addr *)host->h_addr);
        bzero(&(server_addr.sin_zero),8); 
        if (connect(sock, (struct sockaddr *)&server_addr,sizeof(struct sockaddr)) == -1) 		// sending CONNECT request to the server
        {
            perror("Connect");
            exit(1);
        }
				printf("Hello\n");
        while(1)
        {
          bytes_recieved=recv(sock,recv_data,1024,0);		//receiving malicious data
          recv_data[bytes_recieved] = '\0';
           printf("\nRecieved data = %s " , recv_data);
           
        }   
}
