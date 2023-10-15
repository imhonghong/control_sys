%1-1
D1=[1 5];
D2=[1 2 2];
D=conv(D1,D2);
M=tf([1 -1],D);
pole(M)
