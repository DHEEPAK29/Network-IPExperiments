# Bandwidth tests via iperf command

![image](https://github.com/user-attachments/assets/7bf7cafe-46ba-4495-8575-72754974ed7b)

![image](https://github.com/user-attachments/assets/e16eddcb-4862-4c7b-bedd-2bb3682c6551)

sudo mn
R:
![image](https://github.com/user-attachments/assets/ba5301af-136a-4b58-a327-5e4af38ca698)

  
Then in the mininet terminal, run:
h2 iperf -s &
h1 iperf -t 10 -c 10.0.0.2

![image](https://github.com/user-attachments/assets/b45942a0-731f-49f0-a722-a283ee897138)

h1 ping -c 3 h2

![image](https://github.com/user-attachments/assets/8bf016f4-c7ab-4039-b12b-45050a1b436d)

quit

![image](https://github.com/user-attachments/assets/24fb128c-0238-4dfc-b8ed-855de3027af2)

sudo mn --link tc,bw=10,delay=10ms

Then in the mininet terminal:
iperf:
h2 iperf -s &
h1 iperf -t 10 -c 10.0.0.2

After iperf finishes, run:
h1 ping -c 3 h2

 

