clc;
clear;
close all;

hFig=figure;
set(hFig, 'Units','normalized', 'Position', [0.05 0.05 0.35 0.45])
mk_size=15;
ft_size=10;
line_width = 2;
bar_width = 0.5;
window_size = 1000;

fileID = fopen('Joined_Parsed.csv');
C = readtable('Joined_Parsed.csv')
fclose(fileID);
Send=table2array(C(:,2));
Receive=table2array(C(:,3));
GiftRecency=table2array(C(:,4));
GiftAmount=table2array(C(:,5));
Ratio=Receive./Send;
TotalRatio=sum(Receive)/sum(Send);
tri=delaunay(GiftRecency,GiftAmount);
trisurf(tri,GiftRecency,GiftAmount,Ratio);
xlabel('Gift Amount','FontSize',ft_size);
ylabel('Gift Recency','FontSize',ft_size);
zlabel('Receive and Send Ratio','FontSize',ft_size);
set(gca,'XTick',[1 3 5 7 9]);
set(gca,'XTickLabel',{'10~25','50~100','500~1000','2500+','5-10'})
set(gca,'YTick',[0 2 4 6]);
set(gca,'YTickLabel',{'0~12 month','15~35 month','49~60 month','73~84 month'});

