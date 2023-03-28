
import yfinance as yf
import pandas as pd

# 定义要操作的多只股票代码
codes = ["0700.HK", "3690.HK", "2269.HK", "1810.HK", "1024.HK", "1211.HK"]

# 定义空的DataFrame用于保存所有股票的结果
all_data = pd.DataFrame()

for code in codes:
    # 获取基金数据
    data = yf.download(code, start='2022-01-01', end=None)

    # 计算移动平均线
    data['SMA_5'] = data['Close'].rolling(window=5).mean()
    data['SMA_30'] = data['Close'].rolling(window=30).mean()

    # 交易策略
    data['Signal'] = ''
    data['Position'] = None
    data['Buy_shares'] = None
    data['Sell_shares'] = None
    data['Buy_cash'] = None
    data['Sell_cash'] = None

    for i in range(1, len(data)):
        if data['SMA_5'][i] > data['SMA_30'][i] and data['SMA_5'][i - 1] <= data['SMA_30'][i - 1]:
            data.at[data.index[i], 'Signal'] = '买入'
            data.at[data.index[i], 'Position'] = 1
        elif data['SMA_5'][i] < data['SMA_30'][i] and data['SMA_5'][i - 1] >= data['SMA_30'][i - 1]:
            data.at[data.index[i], 'Signal'] = '卖出'
            data.at[data.index[i], 'Position'] = 0

    # 填充空值
    data['Position'].fillna(method='ffill', inplace=True)

    initial_cash = 100000  # 初始现金，可以根据需要调整
    shares = 0  # 持有股票数
    cash = initial_cash

    for i in range(1, len(data)):
        if data['Signal'][i] == '买入':
            shares_to_buy = cash // data['Close'][i]  # 使用现金购买尽可能多的股票
            buy_cash = shares_to_buy * data['Close'][i]
            data.at[data.index[i], 'Buy_shares'] = shares_to_buy
            data.at[data.index[i], 'Buy_cash'] = buy_cash
            shares += shares_to_buy
            cash -= buy_cash
        elif data['Signal'][i] == '卖出':
            sell_cash = shares * data['Close'][i]
            data.at[data.index[i], 'Sell_shares'] = shares
            data.at[data.index[i], 'Sell_cash'] = sell_cash
            cash += sell_cash
            shares = 0

# 计算投资组合的最终价值（包括现金和股票价值）
    final_value = cash + shares * data['Close'][-1]

    # 计算收益百分比
    return_percentage = (final_value - initial_cash) / initial_cash * 100
    print("{}收益百分比：{:.2f}%".format(code, return_percentage))


    print(data.tail(7))

    # 将数据保存到Excel文件
    data.to_excel('stock/'+code + "_fund_data.xlsx")
