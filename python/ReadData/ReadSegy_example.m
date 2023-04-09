%利用ReadSegy函数读取地震数据
[data,SegyTraceHeaders,SegyHeader]=ReadSegy('./3.fcnt');

data=single(data); %转为单精度，以节省内存
[a,b]=size(data); %读取行列数，b为文件存储的地震数据的道数，a为每道的采样点总数

t=SegyHeader.time; %读取时间范围，单位为秒
dt=SegyHeader.dt/(1e6); %采样时间间隔
fs=1/dt; %采样频率

%其他操作
%其他操作
%其他操作

WriteSegyStructure('原segy文件完整路径+文件名',SegyHeader,SegyTraceHeaders,recon_data); %recon_data为待写数据，将待写数据重写入原文件
