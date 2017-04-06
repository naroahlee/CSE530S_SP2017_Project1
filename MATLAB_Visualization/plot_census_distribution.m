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

load('census_of_donors_campaign.csv');
D=[0 19.9; 20 39.9; 40 50.9;60 79.9;80 100];
Distribution=zeros(5,1);
for count=1:size(census_of_donors_campaign,1)
    for range_count=1:size(D,1)
        if census_of_donors_campaign(count,1)>=D(range_count,1)&&census_of_donors_campaign(count,1)<=D(range_count,2)
            Distribution(range_count)=Distribution(range_count)+1;
        end
    end

end

bar(Distribution, bar_width);
hold on;
ylabel('Number of Donors','FontSize',ft_size)
xlabel('Poverty Percentage Range','FontSize',ft_size)
set(gca,'XLim',[0.5 5.5]);
set(gca,'XTick',[1 2 3 4 5]);
set(gca,'XTickLabel',{'0~19.9', '20~39.9', '40~50.9', '60~79.9', '80~100'}); 
set(gca,'FontSize',ft_size)
grid off;
box on;


hFig=figure;
set(hFig, 'Units','normalized', 'Position', [0.05 0.05 0.35 0.45])
D=[0 50000; 50000 100000; 100000 150000;150000 200000;200000 250000];
Distribution=zeros(5,1);
for count=1:size(census_of_donors_campaign,1)
    for range_count=1:size(D,1)
        if census_of_donors_campaign(count,2)>=D(range_count,1)&&census_of_donors_campaign(count,2)<=D(range_count,2)
            Distribution(range_count)=Distribution(range_count)+1;
        end
    end

end
% figure;
% h=cdfplot(census_of_donors_campaign(:,2)');
bar(Distribution, bar_width);
hold on;
ylabel('Number of Donors','FontSize',ft_size)
xlabel('Estimated Income (thousand dollars)','FontSize',ft_size)
set(gca,'XLim',[0.5 5.5]);
set(gca,'XTick',[1 2 3 4 5]);
set(gca,'XTickLabel',{'0~49.9', '50~99.9', '100~149.9', '150~199.9', '200~250'}); 
set(gca,'FontSize',ft_size)
grid off;
box on;



hFig=figure;
set(hFig, 'Units','normalized', 'Position', [0.05 0.05 0.35 0.45])
load('census_of_donors_campaign.csv');
D=[0 19.9; 20 39.9; 40 50.9;60 79.9;80 100];
Distribution=zeros(5,1);
for count=1:size(census_of_donors_campaign,1)
    for range_count=1:size(D,1)
        if census_of_donors_campaign(count,3)>=D(range_count,1)&&census_of_donors_campaign(count,3)<=D(range_count,2)
            Distribution(range_count)=Distribution(range_count)+1;
        end
    end

end

bar(Distribution, bar_width);
hold on;
ylabel('Number of Donors','FontSize',ft_size)
xlabel('Age Range','FontSize',ft_size)
set(gca,'XLim',[0.5 5.5]);
set(gca,'XTick',[1 2 3 4 5]);
set(gca,'XTickLabel',{'0~19.9', '20~39.9', '40~50.9', '60~79.9', '80~100'}); 
set(gca,'FontSize',ft_size)
grid off;
box on;

