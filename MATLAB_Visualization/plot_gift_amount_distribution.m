clc;
clear;
close all;

hFig=figure;
set(hFig, 'Units','normalized', 'Position', [0.05 0.05 0.35 0.45])
mk_size=15;
ft_size=20;
line_width = 2;
bar_width = 0.5;
window_size = 1000;

load('GiftAmountInCSV.csv');
D=[0 24; 25 49; 50 99;100 499;500 999;1000 1499;1500 1999;2000 2499];
Distribution=zeros(8,1);
for count=1:size(GiftAmountInCSV,1)
    for range_count=1:size(D,1)
        if GiftAmountInCSV(count)>=D(range_count,1)&&GiftAmountInCSV(count)<=D(range_count,2)
            Distribution(range_count)=Distribution(range_count)+1;
        end
    end

end

bar(Distribution, bar_width);
hold on;
ylabel('Number of Donors','FontSize',ft_size)
xlabel('GiftAmount Range','FontSize',ft_size)
set(gca,'XLim',[0 9]);
set(gca,'XTick',[1 2 3 4 5 6 7 8]);
set(gca,'XTickLabel',{'0~25', '25~50', '50~100', '100~500', '500~1000','1000~1500','1500~2000', '2000~2500'}); 

set(gca,'FontSize',ft_size)

grid off;
box on;
