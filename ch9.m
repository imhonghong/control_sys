%porblem1
s1=tf([1,6],[1,8,24,32,0]);
rlocus(s1);
%bp @ -3.1,-7.3
%im-axis @ +-2.5j


%problem2
s2=tf([1,0,1/3],[1,0,1,0]);
rlocus(s2);

%problem3
s3=tf([1,0,1/9],[1,0,1,0]);
rlocus(s3);
%bp @-0.578

%problem4
s4=tf([1,0.01],[1,12,20,0,0]);
rlocus(s4);
%bp @ -0.94,-0.02

