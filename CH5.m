%1-1
D1=[1 5];
D2=[1 2 2];
D=conv(D1,D2);
M=tf([1 -1],D);
pole(M)

%1-2
N=100
D=[1 -2 3 10]
M=tf(N,D)
pole(M)

%1-3
N=[10 20]
D=[1 8 7 0]
M=tf(N,D)
pole(M)
