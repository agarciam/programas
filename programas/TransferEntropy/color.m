load TransferBubble.txt

h = imagesc(TransferBubble)
%  set(h,'edgecolor','none')
set(gca,'YDir','reverse');

%%%%%%%%  COLOR PALLETE %%%%%%%%%%%%
w = [1 1 1];    % start
b = [0 0 1];    % end (Blue)
p = [0 0 0.5625];  % Dark Blue 
red = [1 0 0];   % Dark Red

% colormap of size 64-by-3, ranging from white -> blue
c = zeros(1024,3);
for i=1:3
    c(:,i) = linspace(w(i), red(i), 1024); %linspace (linear?)
end

colormap(hot)
%  %  str = {'AORD';'ATX';'BSESN';'KLSE';'FCHI';'GDAXI';'CCSI';'FTSE';'HSI';'BVSP';
%  %  'MXX';'JKSE';'KS11';'MERV';'N225';'GSPC';'STI';'SSMI';'TWII';'TA100'};
%  str = {'IPC_MEXICO','SP500','MERVAL','IBOVESPA','FTSE_UK_INDEX','CAC_40','SWISS_MARKET_INDEX','DAX_INDEX','ATX_INDEX',...
%  'EGX_EGYPT','TEL_AVIV_STOCK','BSE_SENSEX','JAKARTA_STOCK','BURSA_MALAYSIA','STRAITS_TIMES_INDEX','HANG_SENG_INDEX',...
%  'TAIWAN_STOCK','KOSPI','NIKKEI_INDEX','ALL_ORDINARIES','MEXBOL','SPX','MERVAL','IBOV','UKX','CAC','SMI','DAX','ATX',...
%  'CASE','TA-25','SENSEX','JCI','FBMKLCI','FSSTI','HSI','TWSE','KOSPI','NKY','AS51'};
%  
%  set(gca, 'YTickLabel',str, 'YTick',1:numel(str))
%  set(gca,'XTick',[0:5:40]) 
%  set(gca,'fontsize',10)
%  set(gca,'FontName', 'Helvetica')
%  set(gcf, 'PaperPositionMode', 'manual');
%  set(gcf, 'PaperUnits', 'inches');
%  set(gcf, 'PaperPosition', [2 1 10 6]);
%  set(gca,'Xlabel','POLARITY  ->  RETURNS')
%  set(gca,'title','TRANSFER ENTROPY')

brighten(0)
h=colorbar;
set(h,'fontsize',16);
set(h,'FontName','Helvetica');
%  
%  print -color -depsc transfer.eps
print -djpg transfer_kraskov_sort_delay_k3.jpg;