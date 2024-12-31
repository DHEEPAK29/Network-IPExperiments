BGP with ipmininet


BGP keepalive + Wireshark

sudo python3 -m ipmininet.examples –-topo=simple_bgp_network 

![image](https://github.com/user-attachments/assets/952b7261-2739-4fdd-b05f-377d3766958f)

![image](https://github.com/user-attachments/assets/dc87cc48-1e5b-4738-91a8-f3a47c7d0c56)

eBGP- 192.168.0.1, fc00::1; iBGP- 192.168.2.2, fc00:0:2::2

mininet> as1r1 wireshark &

![image](https://github.com/user-attachments/assets/695ac865-963f-4c89-9449-b3c216604a42)
![image](https://github.com/user-attachments/assets/480812d8-f149-4ce2-b961-2ed888e8deb4)

BGP best path

![image](https://github.com/user-attachments/assets/f6500e3f-9331-47b8-804a-61415258fa0b)
![image](https://github.com/user-attachments/assets/efbfaa33-fbcd-4c94-9399-23c60269e9b5)

![image](https://github.com/user-attachments/assets/639d0087-14b7-45cb-a708-9282a15159ae)

