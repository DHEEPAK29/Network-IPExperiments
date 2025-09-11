#include <iostream>
#include <netdb.h>
#include <arpa/inet.h>

int main() {
    struct addrinfo hints = {}, *res;
    hints.ai_family = AF_INET; // IPv4

    if (getaddrinfo("example.com", NULL, &hints, &res) == 0) {
        struct sockaddr_in *ipv4 = (struct sockaddr_in *)res->ai_addr;
        char ipstr[INET_ADDRSTRLEN];
        inet_ntop(AF_INET, &(ipv4->sin_addr), ipstr, sizeof(ipstr));
        std::cout << "IP: " << ipstr << std::endl;
        freeaddrinfo(res);
    }
    return 0;
}
