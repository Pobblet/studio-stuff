monthly_fee = 24 /3  
tax_pct = 1.5#########################  ################## ##################
buy_sell_fee = 0.00

stock_name = "Some AI Stock seeing macines"  # later input or API
ticker = "SAS see" #later input even later api
buy_price = 3.12                   #######################  INPUT BUY PRICE HERE
sell_price = 3.02                  #######################  INPUT SELL PRICE HERE

print("\n")

shares_amount = 40 #input or based on availible funds ###### INPUT SHARES AMOUNT HERE
print("Stock name: " + stock_name)
print("Ticker: " + ticker)
print("Buy price £" + str(buy_price))
print("Sell price £" + str(sell_price))

print("\n")
##################################################################  INPUT STOPLOSS % HERE
#stoploss 7%
sl_p = 7
stoploss = buy_price /100 * sl_p 
print("Stop loss amount £" + str(stoploss))
stoploss_price = buy_price - stoploss
print("Stop loss price, sell at £" +str(stoploss_price))

spread = buy_price - sell_price
spread_pct = (spread / buy_price) * 100
print("Spread % "+str(spread_pct))
spread_cost = spread * shares_amount
print("Spread cost £" + str(spread_cost))

print("Amount of shares: "+str(shares_amount)) 
shares_cost = buy_price * shares_amount
print("Shares cost £" +str(shares_cost))

print("\n")

print("Buy Sell fee £"+str(buy_sell_fee))
share_cost_buy_sell_fee = shares_cost + buy_sell_fee
#print("Shares cost plus buy fee £"+str(share_cost_buy_sell_fee))      

tax_cost = share_cost_buy_sell_fee * (tax_pct / 100)
print("Tax amount £"+str(tax_cost))

total = share_cost_buy_sell_fee + tax_cost + spread_cost
#print("Total £"+str(total))

print("Monthly acc fee £"+str(monthly_fee))
total = total + monthly_fee
print("Exit buy Sell fee £"+str(buy_sell_fee))
all_charges = buy_sell_fee *2 +spread_cost + tax_cost + monthly_fee
print("All charges to trade £"+str(all_charges))
cost_to_buy = tax_cost + share_cost_buy_sell_fee + monthly_fee + buy_sell_fee + spread_cost
print("Total cost to buy £"+str(cost_to_buy))

#print("End.")
print("\n")
print("Breaking Even")

break_even_price = cost_to_buy / shares_amount 
print("Break even sell price: £"+str(break_even_price))

rise = break_even_price - sell_price 
break_even_pct = (rise / sell_price)*100 
print("Break even %: " + str(break_even_pct))   

print("\n")
print("\n")
print("Profit loss")
sell_price_out = 4.50  # later input or API#######################  INPUT SELL PRICE HERE
print("Sell price: £" + str(sell_price_out))
profit_loss = (sell_price_out - break_even_price) * shares_amount
gross = sell_price_out * shares_amount
print("Gross: £" + str(gross))
print("Profit/Loss: £" + str(profit_loss))
profit_pct = (profit_loss / cost_to_buy) * 100
print("Profit % " + str(profit_pct))

print("\n")




#forex 0.7%