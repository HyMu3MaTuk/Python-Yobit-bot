#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#import time
#import urllib.request
#from socket import error as SocketError
#import errno
#try: response = urllib2.urlopen('https://gate.io').read()
#except SocketError as e:
#    if e.errno != errno.ECONNRESET:
#        raise # Not error we are looking for
#    pass # Handle error here.


from gateAPI import GateIO
import time
#import request
import re


# Заполнить APIKEY APISECRET
apikey = '1C52391F-AF41-472B-AB3A-1868D19F8264'
secretkey = '1226dbcac889c84a89e567a112949c7c5e743449e47c315ea5aa19d51ff7ebd7'
API_URL = 'data.gate.io'
gate = GateIO(API_URL,apikey,secretkey)

FEE = 0.2
PROFIT = 1.3
USD = 10
B = 8
S = 10
X = 2.5


BTC = 0.001
BAL = 10

while True:
    print('*'*50)
    print(time.asctime())
    
    
    # Все торговые пары
    #print (gate.pairs())

    #pairs = gate.pairs()
    #pai = re.findall(r'trx_usdt', pairs)
    #print (pai)


    # Market order parameters
    #print (gate.marketinfo())


    # Все торговые котировки
    # print (gate.tickers())


    # Single transaction market
    # print (gate.ticker('btc_usdt'))


    # The depth of the market for all pairs
    # print (gate.orderBooks())


    # Глубина рынка отдельных транзакций
	#print (gate.orderBook('bifi_usdt'))

#ОТМЕНА ВСЕХ ОРДЕРОВ (1- buy, 0, sell, -1 все)
	
	
    print (gate.cancelAllOrders('-1','bifi_usdt'))
    print (gate.cancelAllOrders('-1','bcd_usdt'))
    print (gate.cancelAllOrders('-1','trx_usdt'))
    print (gate.cancelAllOrders('-1','god_usdt'))
    print (gate.cancelAllOrders('-1','ada_usdt'))
    print (gate.cancelAllOrders('-1','btc_usdt'))
    print (gate.cancelAllOrders('-1','bch_usdt'))
    print (gate.cancelAllOrders('-1','eth_usdt'))
    print (gate.cancelAllOrders('-1','xrp_usdt'))
    time.sleep(1)
    

    '''
    orders = gate.openOrders()
    #print(orders)
    PI = re.findall(r'\d+[0-9]{8}', orders)
  #  print(PI)
    PIDs = PI[::2]
    PIX = re.findall(r'\w+_\w+', orders)
 #   print (PIX)
    #PAIRs = re.findall(r'\D+_', orders)
    #print (PAIRs)
    
    #for x in range(len(PIDs)):
    #   print (gate.getOrder('396081201','bcd_usdt')
    #for i in range(len(PIDs)):
        #print(PIDs(i))
    
    for i in range(len(PIDs)):
        print(gate.cancelOrder((PIDs[i]),'bifi_usdt'))
    for i in range(len(PIDs)):
        print(gate.cancelOrder((PIDs[i]),'bcd_usdt'))
    for i in range(len(PIDs)):
        print(gate.cancelOrder((PIDs[i]),'trx_usdt'))
    for i in range(len(PIDs)):
        print(gate.cancelOrder((PIDs[i]),'god_usdt'))
    for i in range(len(PIDs)):
        print(gate.cancelOrder((PIDs[i]),'ada_usdt'))
    for i in range(len(PIDs)):
        print(gate.cancelOrder((PIDs[i]),'btc_usdt'))
   '''
	
	# Get my 24 hours trade records
	#print (gate.mytradeHistory('bifi_usdt'))

# Detailed market transactions (Подробные рыночные операции (тренд ВВЕРХ/ВНИЗ))
	#print (gate.marketlist()['data'][0])
	


    
	#print(type(PIDs))
	#a = []
	#for i in range(int(input(PIDs))): a.append(int(input(PIDs)))
	#print(a)

    

	#n = int(input(PIDs))
	#q = len(PIDs)
	#print(q)
	#for i in range(len(PIDs)): num.append(PIDs[i])
	
	#print(i)
        
        
	
	#for int_var in x_range: range(0, q)
	
	
	#print (gate.cancelOrder('348307942','bifi_usdt'))
	
	

	

	

	#//Подсчет кол-ва ордеров

	#$open_orders = open_orders()
	#$orders = $open_orders['orders']
	#$num = join(',', array_keys($orders))
	#$type = $orders[$num]['type']
	#$pair = $orders[$num]['currencyPair']
	#$PIDs = join(',', array_keys($orders))
	#$PIDs = explode(',', $PIDs)
	#q = len($PIDs)
#ОТМЕНА ВСЕХ ОРДЕРОВ
	#do {
	#for ($x=0; $x<$q; $x++)
	#{
	#$num = $PIDs[$x];
	#$type = $orders[$num]['type'];
	#//$rate = $orders[$num]['rate'];
	#//$amount = $orders[$num]['amount'];
	#$pair = $orders[$num]['currencyPair'];
	#$ID = $orders[$num]['orderNumber'];
	#}

	#print_r("ORDER=>".$ID."\n");
	#print_r(cancel_order($ID));
	#} while (1 < $q--);
        #for ($x=0; $x<$q; $x++)
        #   {
        #   $order_id = $PIDs[$x];
        #   $pair = $return[$order_id]['pair'];
         #  $type = $return[$order_id]['type'];
         #  }
         
    depth_btc = gate.orderBook('btc_usdt')
    d_b_btc_usd = depth_btc['bids'][0][0]
    d_s_btc_usd = depth_btc['asks'][-1][0]
    v_btc_usd = round((d_b_btc_usd*0.025), 2) #ШАГ В СТАКАНЕ 2,5% ОТ ЦЕНЫ ПОКУПКИ
    print ('макс. цена покупки BTC_USDT', d_b_btc_usd)
    print ('мини. цена продажи BTC_USDT', d_s_btc_usd)
    f_btc_usd = round((FEE/100*d_s_btc_usd*2*PROFIT), 2)
    s_btc_usd = round(d_s_btc_usd - d_b_btc_usd, 2)
    proc_btc_usd = round((s_btc_usd/d_b_btc_usd)*100, 2)
    val_b_btc_usd = round(USD/d_b_btc_usd, 6)
    val_s_btc_usd = round(USD/d_s_btc_usd, 6)

    depth_bifi = gate.orderBook('bifi_usdt')
    d_b_bifi_usd = depth_bifi['bids'][0][0]
    d_s_bifi_usd = depth_bifi['asks'][-1][0]
    v_bifi_usd = round((d_b_bifi_usd*0.025), 4) #ШАГ В СТАКАНЕ 2,5% ОТ ЦЕНЫ ПОКУПКИ
    print ('макс. цена покупки BIFI_USDT', d_b_bifi_usd)
    print ('мин. цена продажи BIFI_USDT', d_s_bifi_usd)
    f_bifi_usd = round((FEE/100*d_s_bifi_usd*2*PROFIT), 4)
    s_bifi_usd = round(d_s_bifi_usd - d_b_bifi_usd, 4)
    proc_bifi_usd = round((s_bifi_usd/d_b_bifi_usd)*100, 4)
    val_b_bifi_usd = round(USD/d_b_bifi_usd, 6)
    val_s_bifi_usd = round(USD/d_s_bifi_usd, 6)
    
    depth_bcx = gate.orderBook('bcx_usdt')
    d_b_bcx_usd = depth_bcx['bids'][0][0]
    d_s_bcx_usd = depth_bcx['asks'][-1][0]
    v_bcx_usd = round((d_b_bcx_usd*0.025), 4) #ШАГ В СТАКАНЕ 2,5% ОТ ЦЕНЫ ПОКУПКИ
    print ('макс. цена покупки BCX_USDT', d_b_bcx_usd)
    print ('мин. цена продажи BCX_USDT', d_s_bcx_usd)
    f_bcx_usd = round((FEE/100*d_s_bcx_usd*2*PROFIT), 6)
    s_bcx_usd = round(d_s_bcx_usd - d_b_bcx_usd, 4)
    proc_bcx_usd = round((s_bcx_usd/d_b_bcx_usd)*100, 6)
    
    depth_trx = gate.orderBook('trx_usdt')
    d_b_trx_usd = depth_trx['bids'][0][0]
    d_s_trx_usd = depth_trx['asks'][-1][0]
    v_trx_usd = round((d_b_trx_usd*0.025), 4) #ШАГ В СТАКАНЕ 2,5% ОТ ЦЕНЫ ПОКУПКИ
    print ('макс. цена покупки TRX_USDT', d_b_trx_usd)
    print ('мини. цена продажи TRX_USDT', d_s_trx_usd)
    f_trx_usd = round((FEE/100*d_s_trx_usd*2*PROFIT), 5)
    s_trx_usd = round(d_s_trx_usd - d_b_trx_usd, 5)
    proc_trx_usd = round((s_trx_usd/d_b_trx_usd)*100, 5)
    val_b_trx_usd = round(USD/d_b_trx_usd, 6)
    val_s_trx_usd = round(USD/d_s_trx_usd, 6)

    depth_god = gate.orderBook('god_usdt')
    d_b_god_usd = depth_god['bids'][0][0]
    d_s_god_usd = depth_god['asks'][-1][0]
    v_god_usd = round((d_b_god_usd*0.025), 2) #ШАГ В СТАКАНЕ 2,5% ОТ ЦЕНЫ ПОКУПКИ
    print ('макс. цена покупки GOD_USDT', d_b_god_usd)
    print ('мини. цена продажи GOD_USDT', d_s_god_usd)
    f_god_usd = round((FEE/100*d_s_god_usd*2*PROFIT), 2)
    s_god_usd = round(d_s_god_usd - d_b_god_usd, 2)
    proc_god_usd = round((s_god_usd/d_b_god_usd)*100, 2)
    val_b_god_usd = round(USD/d_b_god_usd, 6)
    val_s_god_usd = round(USD/d_s_god_usd, 6)
    

    depth_eth = gate.orderBook('eth_usdt')
    d_b_eth_usd = depth_eth['bids'][0][0]
    d_s_eth_usd = depth_eth['asks'][-1][0]
    v_eth_usd = round((d_b_eth_usd*0.025), 2) #ШАГ В СТАКАНЕ 2,5% ОТ ЦЕНЫ ПОКУПКИ
    print ('макс. цена покупки ETH_USDT', d_b_eth_usd)
    print ('мини. цена продажи ETH_USDT', d_s_eth_usd)
    f_eth_usd = round((FEE/100*d_s_eth_usd*2*PROFIT), 2)
    s_eth_usd = round(d_s_eth_usd - d_b_eth_usd, 2)
    proc_eth_usd = round((s_eth_usd/d_b_eth_usd)*100, 2)
    val_b_eth_usd = round(USD/d_b_eth_usd, 6)
    val_s_eth_usd = round(USD/d_s_eth_usd, 6)

    depth_bch = gate.orderBook('bch_usdt')
    d_b_bch_usd = depth_bch['bids'][0][0]
    d_s_bch_usd = depth_bch['asks'][-1][0]
    v_bch_usd = round((d_b_bch_usd*0.025), 2) #ШАГ В СТАКАНЕ 2,5% ОТ ЦЕНЫ ПОКУПКИ
    print ('макс. цена покупки BCH_USDT', d_b_bch_usd)
    print ('мини. цена продажи BCH_USDT', d_s_bch_usd)
    f_bch_usd = round((FEE/100*d_s_bch_usd*2*PROFIT), 2)
    s_bch_usd = round(d_s_bch_usd - d_b_bch_usd, 2)
    proc_bch_usd = round((s_bch_usd/d_b_bch_usd)*100, 2)
    val_b_bch_usd = round(USD/d_b_bch_usd, 6)
    val_s_bch_usd = round(USD/d_s_bch_usd, 6)
	
    depth_bcd = gate.orderBook('bcd_usdt')
    d_b_bcd_usd = depth_bcd['bids'][0][0]
    d_s_bcd_usd = depth_bcd['asks'][-1][0]
    v_bcd_usd = round((d_b_bcd_usd*0.025), 3) #ШАГ В СТАКАНЕ 2,5% ОТ ЦЕНЫ ПОКУПКИ
    print ('макс. цена покупки BCD_USDT', d_b_bcd_usd)
    print ('мин. цена продажи BCD_USDT', d_s_bcd_usd)
    f_bcd_usd = round((FEE/100*d_s_bcd_usd*2*PROFIT), 3)
    s_bcd_usd = round(d_s_bcd_usd - d_b_bcd_usd, 3)
    proc_bcd_usd = round((s_bcd_usd/d_b_bcd_usd)*100, 3)
    val_b_bcd_usd = round(USD/d_b_bcd_usd, 6)
    val_s_bcd_usd = round(USD/d_s_bcd_usd, 6)

    depth_ada = gate.orderBook('ada_usdt')
    d_b_ada_usd = depth_ada['bids'][0][0]
    d_s_ada_usd = depth_ada['asks'][-1][0]
    v_ada_usd = round((d_b_ada_usd*0.025), 4) #ШАГ В СТАКАНЕ 2,5% ОТ ЦЕНЫ ПОКУПКИ
    print ('макс. цена покупки ADA_USDT', d_b_ada_usd)
    print ('мин. цена продажи ADA_USDT', d_s_ada_usd)
    f_ada_usd = round((FEE/100*d_s_ada_usd*2*PROFIT), 4)
    s_ada_usd = round(d_s_ada_usd - d_b_ada_usd, 4)
    proc_ada_usd = round((s_ada_usd/d_b_ada_usd)*100, 4)
    val_b_ada_usd = round(USD/d_b_ada_usd, 6)
    val_s_ada_usd = round(USD/d_s_ada_usd, 6)

    depth_xrp = gate.orderBook('xrp_usdt')
    d_b_xrp_usd = depth_xrp['bids'][0][0]
    d_s_xrp_usd = depth_xrp['asks'][-1][0]
    v_xrp_usd = round((d_b_xrp_usd*0.025), 4) #ШАГ В СТАКАНЕ 2,5% ОТ ЦЕНЫ ПОКУПКИ
    print ('макс. цена покупки XRP_USDT', d_b_xrp_usd)
    print ('мин. цена продажи XRP_USDT', d_s_xrp_usd)
    f_xrp_usd = round((FEE/100*d_s_xrp_usd*2*PROFIT), 4)
    s_xrp_usd = round(d_s_xrp_usd - d_b_xrp_usd, 4)
    proc_xrp_usd = round((s_xrp_usd/d_b_xrp_usd)*100, 4)
    val_b_xrp_usd = round(USD/d_b_xrp_usd, 6)
    val_s_xrp_usd = round(USD/d_s_xrp_usd, 6)

    print ('Cпред BTC/USDT =>>', proc_btc_usd, '%', 'ИЛИ', s_btc_usd)
    print ('Cпред ETH/USDT =>>', proc_eth_usd,'%', 'ИЛИ', s_eth_usd)
    print ('Cпред BIFI/USDT =>>', proc_bifi_usd, '%', 'ИЛИ', s_bifi_usd)
    print ('Cпред BCD/USDT =>>', proc_bcd_usd,'%', 'ИЛИ', s_bcd_usd)
#    print ('Cпред BCX/USDT =>>', proc_bcx_usd, '%', 'ИЛИ', s_bcx_usd)
    print ('Cпред TRX/USDT =>>', proc_trx_usd, '%', 'ИЛИ', s_trx_usd)
    print ('Cпред GOD/USDT =>>', proc_god_usd,'%', 'ИЛИ', s_god_usd)
    print ('Cпред ADA/USDT =>>', proc_ada_usd,'%', 'ИЛИ', s_ada_usd)
    print ('Cпред BCH/USDT =>>', proc_bch_usd,'%', 'ИЛИ', s_bch_usd)
    print ('Cпред XRP/USDT =>>', proc_xrp_usd,'%', 'ИЛИ', s_xrp_usd)

    print ('Комиссия BTC/USDT =>>', f_btc_usd)
    print ('Комиссия ETH/USDT =>>', f_eth_usd)
    print ('Комиссия BIFI/USDT =>>', f_bifi_usd)
    print ('Комиссия BCD/USDT =>>', f_bcd_usd)
    print ('Комиссия BCX/USDT =>>', f_bcx_usd)
    print ('Комиссия TRX/USDT =>>', f_trx_usd)
    print ('Комиссия GOD/USDT =>>', f_god_usd)
    print ('Комиссия ADA/USDT =>>', f_ada_usd)
    print ('Комиссия BCH/USDT =>>', f_bch_usd)
    print ('Комиссия XRP/USDT =>>', f_xrp_usd)
	


 # Market trade history of individual pairs
	#print (gate.tradeHistory('bifi_usdt'))
	#history_bifi_usd = gate.tradeHistory('bifi_usdt')['data']['rate'][0]
	#print (history_bifi_usd)



    # Get account funds
    bal = gate.balances()
    #print (bal)
    s = re.split(r'"',  bal)
    print(s)
    
    bala_usd = float(s[13])
    bala_bch = float(s[9])
    bala_eth = float(s[45])
    bala_btc = float(s[53])
    bala_bcd = float(s[21])
    bala_bcx = float(s[25])
    bala_bifi = float(s[57])
    bala_trx = float(s[61])
    bala_god = float(s[33])
    bala_ada = float(s[49])
    bala_xrp = float(s[121])

    bal_usd = round(bala_usd, 6)
    bal_bch = round(bala_bch, 6)
    bal_eth = round(bala_eth, 6)
    bal_btc = round(bala_btc, 6)
    bal_bcd = round(bala_bcd, 6)
    bal_bcx = round(bala_bcx, 6)
    bal_bifi = round(bala_bifi, 6)
    bal_trx = round(bala_trx, 6)
    bal_god = round(bala_god, 6)
    bal_ada = round(bala_ada, 6)
    bal_xrp = round(bala_xrp, 6)

	
    bal_btc_usd = round(bal_btc*d_b_btc_usd, 3)
    bal_bch_usd = round(bal_bch*d_b_bch_usd, 3)
    bal_eth_usd = round(bal_eth*d_b_eth_usd, 3)
    bal_bcd_usd = round(bal_bcd*d_b_bcd_usd, 3)
    bal_bcx_usd = round(bal_bcx*d_b_bcx_usd, 3)
    bal_bifi_usd = round(bal_bifi*d_b_bifi_usd, 3)
    bal_trx_usd = round(bal_trx*d_b_trx_usd, 3)
    bal_god_usd = round(bal_god*d_b_god_usd, 3)
    bal_ada_usd = round(bal_ada*d_b_ada_usd, 3)
    bal_xrp_usd = round(bal_xrp*d_b_xrp_usd, 3)
	
    all_bal_usd = round(bal_btc_usd+bal_trx_usd+bal_ada_usd+bal_god_usd+bal_bch_usd+bal_eth_usd+bal_xrp_usd+bal_usd, 3)
    all_bal_btc = round(all_bal_usd/d_b_btc_usd, 6)
    all_bal_eth = round(all_bal_usd/d_b_eth_usd, 6)
    all_bal_bifi = round((bal_bcd_usd+bal_bifi_usd+all_bal_usd)/d_s_bifi_usd, 3)
    all_bal_bcd = round((bal_bcd_usd+bal_bifi_usd+all_bal_usd)/d_s_bcd_usd, 3)
	
    avg_bal_usd = round((all_bal_usd)/7, 3)
    print("БАЛАНС",s[11], "=>>", bal_usd)
    print("БАЛАНС",s[51], "=>>", bal_btc, 'ИЛИ', bal_btc_usd, 'USDT')
    print("БАЛАНС",s[7], "=>>", bal_bch, 'ИЛИ', bal_bch_usd, 'USDT')
    print("БАЛАНС",s[43], "=>>", bal_eth, 'ИЛИ', bal_eth_usd, 'USDT')
    print("БАЛАНС",s[19], "=>>", bal_bcd, 'ИЛИ', bal_bcd_usd, 'USDT')
    print("БАЛАНС",s[55], "=>>", bal_bifi, 'ИЛИ', bal_bifi_usd, 'USDT')
#    print("БАЛАНС",s[23], "=>>", bal_bcx, 'ИЛИ', bal_bcx_usd, 'USDT')
    print("БАЛАНС",s[59], "=>>", bal_trx, 'ИЛИ', bal_trx_usd, 'USDT')
    print("БАЛАНС",s[31], "=>>", bal_god, 'ИЛИ', bal_god_usd, 'USDT')
    print("БАЛАНС",s[47], "=>>", bal_ada, 'ИЛИ', bal_ada_usd, 'USDT')
    print("БАЛАНС",s[119], "=>>", bal_xrp, 'ИЛИ', bal_xrp_usd, 'USDT')
	
    print ('OBTAINABLE USDT =>>', all_bal_usd)
    print ('OBTAINABLE BTC =>>', all_bal_btc)
    print ('OBTAINABLE ETH =>>', all_bal_eth)
    print ('OBTAINABLE BIFI =>>', all_bal_bifi)
    print ('OBTAINABLE BCD =>>', all_bal_bcd)
    print ('AVERAGE USDT =>>', avg_bal_usd)
	
    #bal_all = round(bal_usd + bal_bcd + bal_bifi, 3)
    #print(bal_all)
    #print (gate.marketinfo())
    #result = re.findall(r'\d+', bal)
		
    #print (result)
		
	

    #bal_bifi = bal['BIFI']
    #print ('BALANCE BIFI=>>', bal_bifi)
    # Получить адрес пополнения
    # print (gate.depositAddres('btc'))

    # Get recharge history
    # print (gate.depositsWithdrawals('1469092370','1569092370'))
		
	


# ОРДЕРА НА ПОКУПКУ
    # print (gate.buy('etc_btc','0.001','123'))



    #if (bal_usd >= 3*USD and s_bcx_usd >= f_bcx_usd and avg_bal_usd+BAL >= bal_bcx_usd): gate.buy('bcx_usdt', d_b_bcx_usd, BCX)
    #elif (bal_usd >= 3*USD and s_bcx_usd >= f_bcx_usd and proc_bcx_usd >= 2): gate.buy('bcx_usdt', d_b_bcx_usd, BCX)
    #elif (bal_usd >= 3*USD and avg_bal_usd+BAL >= bal_bcx_usd): gate.buy('bcx_usdt', d_b_bcx_usd-f_bcx_usd, BCX)
	

    #if($bal_rur > 100 && $s_usd_rur > $f_usd_rur)
    #{$val_usd2 = round($bal_rur*0.348/(2*$d_s_usd_rur+$f_usd_rur), 5);
    #print_r("ХОРОШИЙ СПРЕД, КУПИТЬ ".$val_usd2." USD\n");
    #$buy_usd = $BTCeAPI->makeOrder($val_usd2, 'usd_rur', BTCeAPI::DIRECTION_BUY, $d_b_usd_rur-0.3);}

	#elseif ($bal_rur > 100)
	#{$val_usd2 = round($bal_rur*0.348/(2*$d_s_usd_rur+$f_usd_rur), 5);
	#print_r("КУПИТЬ ".$val_usd2." USD\n");
	#buy_usd = $BTCeAPI->makeOrder($val_usd2, 'usd_rur', BTCeAPI::DIRECTION_BUY, $d_b_usd_rur-0.3);}

    if (bal_btc >= B*BTC and s_btc_usd >= f_btc_usd and BAL <= bal_usd):
        gate.buy('btc_usdt', d_b_btc_usd+0.01, val_b_btc_usd)
    elif (bal_btc >= B*BTC and BAL <= bal_usd):
        gate.buy('btc_usdt', d_b_btc_usd-f_btc_usd, val_b_btc_usd)

    if (bal_usd >= B*USD and s_eth_usd >= f_eth_usd and BAL >= bal_eth_usd):
        gate.buy('eth_usdt', d_b_eth_usd+0.01, val_b_eth_usd)
    elif (bal_usd >= B*USD and bal_eth_usd < 2*BAL and proc_eth_usd >= X):
        gate.buy('eth_usdt', d_b_eth_usd+0.01, val_b_eth_usd)
    elif (bal_usd >= B*USD and BAL >= bal_eth_usd):
        gate.buy('eth_usdt', d_b_eth_usd-f_eth_usd, val_b_eth_usd)	

    if (bal_usd >= B*USD and s_trx_usd >= f_trx_usd and BAL >= bal_trx_usd):
        gate.buy('trx_usdt', d_b_trx_usd+0.00001, val_b_trx_usd)
    elif (bal_usd >= B*USD and bal_trx_usd < 2*BAL and proc_trx_usd >= X):
        gate.buy('trx_usdt', d_b_trx_usd+0.00001, val_b_trx_usd)
    elif (bal_usd >= B*USD and BAL >= bal_trx_usd):
        gate.buy('trx_usdt', d_b_trx_usd-f_trx_usd, val_b_trx_usd)

    if (bal_usd >= B*USD and s_ada_usd >= f_ada_usd and BAL >= bal_ada_usd):
        gate.buy('ada_usdt', d_b_ada_usd+0.0001, val_b_ada_usd)
    elif (bal_usd >= B*USD and bal_ada_usd < 2*BAL and proc_ada_usd >= X):
        gate.buy('ada_usdt', d_b_ada_usd+0.0001, val_b_ada_usd)
    elif (bal_usd >= B*USD and BAL >= bal_ada_usd):
        gate.buy('ada_usdt', d_b_ada_usd-f_ada_usd, val_b_ada_usd)

    time.sleep(1)
        
    if (bal_usd >= B*USD and s_xrp_usd >= f_xrp_usd and BAL >= bal_xrp_usd):
        gate.buy('xrp_usdt', d_b_xrp_usd+0.0001, val_b_xrp_usd)
    elif (bal_usd >= B*USD and bal_xrp_usd < 2*BAL and proc_xrp_usd >= X):
        gate.buy('xrp_usdt', d_b_xrp_usd+0.0001, val_b_xrp_usd)
    elif (bal_usd >= B*USD and BAL >= bal_xrp_usd):
        gate.buy('xrp_usdt', d_b_xrp_usd-f_xrp_usd, val_b_xrp_usd)
        
    if (bal_usd >= B*USD and s_god_usd >= f_god_usd and BAL >= bal_god_usd):
        gate.buy('god_usdt', d_b_god_usd+0.01, val_b_god_usd)
    elif (bal_usd >= B*USD and bal_god_usd < 2*BAL and proc_god_usd >= X):
        gate.buy('god_usdt', d_b_god_usd+0.01, val_b_god_usd)
    elif (bal_usd >= B*USD and BAL >= bal_god_usd):
        gate.buy('god_usdt', d_b_god_usd-f_god_usd, val_b_god_usd)
        
    if (bal_usd >= B*USD and s_bch_usd >= f_bch_usd and BAL >= bal_bch_usd):
        gate.buy('bch_usdt', d_b_bch_usd+0.01, val_b_bch_usd)
    elif (bal_usd >= B*USD and bal_bch_usd < 2*BAL and proc_bch_usd >= X):
        gate.buy('bch_usdt', d_b_bch_usd+0.01, val_b_bch_usd)
    elif (bal_usd >= B*USD and BAL >= bal_bch_usd):
        gate.buy('bch_usdt', d_b_bch_usd-f_bch_usd, val_b_bch_usd)


    if (bal_usd >= B*USD and s_bifi_usd >= f_bifi_usd and bal_bifi_usd <= bal_bcd_usd+BAL):
        gate.buy('bifi_usdt', d_b_bifi_usd+0.0001, val_b_bifi_usd)
    elif (bal_usd >= B*USD and s_bifi_usd >= f_bifi_usd and proc_bifi_usd >= X):
        gate.buy('bifi_usdt', d_b_bifi_usd+0.0001, val_b_bifi_usd)
    #elif (bal_usd >= B*USD and d_s_bifi_usd == d_b_bifi_usd+0.0001): gate.buy('bifi_usdt', d_b_bifi_usd+0.0001, BIFI)
    elif (bal_usd >= B*USD and bal_bifi_usd <= bal_bcd_usd+BAL):
        gate.buy('bifi_usdt', d_b_bifi_usd-f_bifi_usd, val_b_bifi_usd)
    #val_bifi_usd= round(bal_usd*0.998/(2*d_s_bifi_usd+f_bifi_usd), 4)
    #print('ХОРОШИЙ СПРЕД, ПОКУПАЮ', val_bifi_usd, 'BIFI ПО ЦЕНЕ', d_b_bifi_usd-0.0001, 'USDT')
	
    if (bal_usd >= B*USD and s_bcd_usd >= f_bcd_usd and bal_bcd_usd <= bal_bifi_usd+BAL):
        gate.buy('bcd_usdt', d_b_bcd_usd+0.001, val_b_bcd_usd)
    elif (bal_usd >= B*USD and s_bcd_usd >= f_bcd_usd and proc_bcd_usd >= X):
        gate.buy('bcd_usdt', d_b_bcd_usd+0.001, val_b_bcd_usd)
    #elif (bal_usd >= B*USD and d_s_bcd_usd == d_b_bcd_usd+0.001): gate.buy('bcd_usdt', d_b_bcd_usd+0.001, BCD)
    elif (bal_usd >= B*USD and bal_bcd_usd <= bal_bifi_usd+BAL):
        gate.buy('bcd_usdt', d_b_bcd_usd-f_bcd_usd, val_b_bcd_usd)
	
        	
#ОРДЕРА НА ПРОДАЖУ
    if (s_btc_usd >= f_btc_usd and BAL <= bal_btc_usd):
        gate.sell('btc_usdt', d_s_btc_usd-0.01, val_s_btc_usd), print('ХОРОШИЙ СПРЕД, ПРОДАЮ', val_s_btc_usd, 'BTC ПО ЦЕНЕ', d_s_btc_usd-0.01, 'USDT')
    elif (s_btc_usd >= f_btc_usd and bal_btc_usd >= BAL and proc_btc_usd >= X):
        gate.sell('btc_usdt', d_s_btc_usd-0.01, val_s_btc_usd), print('ХОРОШИЙ %, ПРОДАЮ', val_s_btc_usd, 'BTC ПО ЦЕНЕ', d_s_btc_usd-0.01, 'USDT')
    elif (BAL <= bal_btc_usd):
        gate.sell('btc_usdt', d_s_btc_usd + f_btc_usd, val_s_btc_usd), print('ПРОДАЮ',val_s_btc_usd, 'BTC ПО ЦЕНЕ', d_s_btc_usd+f_btc_usd, 'USDT')
    else: print('ДОСТАТОЧНО БАКСОВ ИЛИ МАЛО BTC')

    if (s_eth_usd >= f_eth_usd and BAL <= bal_eth_usd):
        gate.sell('eth_usdt', d_s_eth_usd-0.01, val_s_eth_usd), print('ХОРОШИЙ СПРЕД, ПРОДАЮ', val_s_eth_usd, 'ETH ПО ЦЕНЕ', d_s_eth_usd-0.01, 'USDT')
    elif (s_eth_usd >= f_eth_usd and bal_eth_usd >= BAL and proc_eth_usd >= X):
        gate.sell('eth_usdt', d_s_eth_usd-0.01, val_s_eth_usd), print('ХОРОШИЙ %, ПРОДАЮ', val_s_eth_usd, 'ETH ПО ЦЕНЕ', d_s_eth_usd-0.01, 'USDT')
    elif (BAL <= bal_eth_usd):
        gate.sell('eth_usdt', d_s_eth_usd + f_eth_usd, val_s_eth_usd), print('ПРОДАЮ',val_s_eth_usd, 'ETH ПО ЦЕНЕ', d_s_eth_usd+f_eth_usd, 'USDT')
    else: print('ДОСТАТОЧНО БАКСОВ ИЛИ МАЛО ETH')
	
    if (s_trx_usd >= f_trx_usd and BAL <= bal_trx_usd):
        gate.sell('trx_usdt', d_s_trx_usd-0.00001, val_s_trx_usd), print('ХОРОШИЙ СПРЕД, ПРОДАЮ', val_s_trx_usd, 'TRX ПО ЦЕНЕ', d_s_trx_usd-0.00001, 'USDT')
    elif (s_trx_usd >= f_trx_usd and bal_trx_usd >= BAL and proc_trx_usd >= X):
        gate.sell('trx_usdt', d_s_trx_usd-0.00001, val_s_trx_usd), print('ХОРОШИЙ %, ПРОДАЮ', val_s_trx_usd, 'TRX ПО ЦЕНЕ', d_s_trx_usd-0.00001, 'USDT')
    elif (BAL <= bal_trx_usd):
        gate.sell('trx_usdt', d_s_trx_usd + f_trx_usd, val_s_trx_usd), print('ПРОДАЮ',val_s_trx_usd, 'TRX ПО ЦЕНЕ', d_s_trx_usd+f_trx_usd, 'USDT')
    else: print('ДОСТАТОЧНО БАКСОВ ИЛИ МАЛО TRX')

    if (s_ada_usd >= f_ada_usd and BAL <= bal_ada_usd):
        gate.sell('ada_usdt', d_s_ada_usd-0.0001, val_s_ada_usd), print('ХОРОШИЙ СПРЕД, ПРОДАЮ', val_s_ada_usd, 'ADA ПО ЦЕНЕ', d_s_ada_usd-0.0001, 'USDT')
    elif (s_ada_usd >= f_ada_usd and bal_ada_usd >= BAL and proc_ada_usd >= X):
        gate.sell('ada_usdt', d_s_ada_usd-0.0001, val_s_ada_usd), print('ХОРОШИЙ %, ПРОДАЮ', val_s_ada_usd, 'ADA ПО ЦЕНЕ', d_s_ada_usd-0.0001, 'USDT')
    elif (BAL <= bal_ada_usd):
        gate.sell('ada_usdt', d_s_ada_usd + f_ada_usd, val_s_ada_usd), print('ПРОДАЮ',val_s_ada_usd, 'ADA ПО ЦЕНЕ', d_s_ada_usd+f_ada_usd, 'USDT')
    else: print('ДОСТАТОЧНО БАКСОВ ИЛИ МАЛО ADA')

    time.sleep(1)
    

    if (s_xrp_usd >= f_xrp_usd and BAL <= bal_xrp_usd):
        gate.sell('xrp_usdt', d_s_xrp_usd-0.0001, val_s_xrp_usd), print('ХОРОШИЙ СПРЕД, ПРОДАЮ', val_s_xrp_usd, 'XRP ПО ЦЕНЕ', d_s_xrp_usd-0.0001, 'USDT')
    elif (s_xrp_usd >= f_xrp_usd and bal_xrp_usd >= BAL and proc_xrp_usd >= X):
        gate.sell('xrp_usdt', d_s_xrp_usd-0.0001, val_s_xrp_usd), print('ХОРОШИЙ %, ПРОДАЮ', val_s_xrp_usd, 'XRP ПО ЦЕНЕ', d_s_xrp_usd-0.0001, 'USDT')
    elif (BAL <= bal_xrp_usd):
        gate.sell('xrp_usdt', d_s_xrp_usd + f_xrp_usd, val_s_xrp_usd), print('ПРОДАЮ',val_s_xrp_usd, 'XRP ПО ЦЕНЕ', d_s_xrp_usd+f_xrp_usd, 'USDT')
    else: print('ДОСТАТОЧНО БАКСОВ ИЛИ МАЛО XRP')
    
    if (s_god_usd >= f_god_usd and BAL <= bal_god_usd):
        gate.sell('god_usdt', d_s_god_usd-0.01, val_s_god_usd), print('ХОРОШИЙ СПРЕД, ПРОДАЮ', val_s_god_usd, 'GOD ПО ЦЕНЕ', d_s_god_usd-0.01, 'USDT')
    elif (s_god_usd >= f_god_usd and bal_god_usd >= BAL and proc_god_usd >= X):
        gate.sell('god_usdt', d_s_god_usd-0.01, val_s_god_usd), print('ХОРОШИЙ %, ПРОДАЮ', val_s_god_usd, 'GOD ПО ЦЕНЕ', d_s_god_usd-0.01, 'USDT')
    elif (BAL <= bal_god_usd):
        gate.sell('god_usdt', d_s_god_usd + f_god_usd, val_s_god_usd), print('ПРОДАЮ',val_s_god_usd, 'GOD ПО ЦЕНЕ', d_s_god_usd+f_god_usd, 'USDT')
    else: print('ДОСТАТОЧНО БАКСОВ ИЛИ МАЛО GOD')

    if (s_bch_usd >= f_bch_usd and BAL <= bal_bch_usd):
        gate.sell('bch_usdt', d_s_bch_usd-0.01, val_s_bch_usd), print('ХОРОШИЙ СПРЕД, ПРОДАЮ', val_s_bch_usd, 'BCH ПО ЦЕНЕ', d_s_bch_usd-0.01, 'USDT')
    elif (s_bch_usd >= f_bch_usd and bal_bch_usd >= BAL and proc_bch_usd >= X):
        gate.sell('bch_usdt', d_s_bch_usd-0.01, val_s_bch_usd), print('ХОРОШИЙ %, ПРОДАЮ', val_s_bch_usd, 'BCH ПО ЦЕНЕ', d_s_bch_usd-0.01, 'USDT')
    elif (BAL <= bal_bch_usd):
        gate.sell('bch_usdt', d_s_bch_usd + f_bch_usd, val_s_bch_usd), print('ПРОДАЮ',val_s_bch_usd, 'BCH ПО ЦЕНЕ', d_s_bch_usd+f_bch_usd, 'USDT')
    else: print('ДОСТАТОЧНО БАКСОВ ИЛИ МАЛО BCH')

    if (bal_usd <= S*USD and s_bifi_usd >= f_bifi_usd and S*USD <= bal_bcd_usd):
        gate.sell('bifi_usdt', d_s_bifi_usd - 0.0001, val_s_bifi_usd), print('ХОРОШИЙ СПРЕД, ПРОДАЮ', val_s_bifi_usd, 'BIFI ПО ЦЕНЕ', d_s_bifi_usd-0.0001, 'USDT')
    elif (bal_usd <= S*USD and S*USD <= bal_bifi_usd):
        gate.sell('bifi_usdt', d_s_bifi_usd + f_bifi_usd, val_s_bifi_usd), print('ПРОДАЮ',val_s_bifi_usd, 'BIFI ПО ЦЕНЕ ', d_s_bifi_usd+f_bifi_usd, 'USDT')
    else: print('ДОСТАТОЧНО БАКСОВ ИЛИ МАЛО BIFI')

    if (bal_usd <= S*USD and s_bcd_usd >= f_bcd_usd and S*USD <= bal_bcd_usd):
        gate.sell('bcd_usdt', d_s_bcd_usd - 0.001, val_s_bcd_usd), print('ХОРОШИЙ СПРЕД, ПРОДАЮ', val_s_bcd_usd, 'BCD ПО ЦЕНЕ', d_s_bcd_usd-0.001, 'USDT')
    elif (s_bcd_usd >= f_bcd_usd and proc_bcd_usd >= X):
        gate.sell('bcd_usdt', d_s_bcd_usd - 0.001, val_s_bcd_usd), print('ХОРОШИЙ %, ПРОДАЮ', val_s_bcd_usd, 'BCD ПО ЦЕНЕ', d_s_bcd_usd-0.001, 'USDT')
    elif (bal_usd <= S*USD and S*USD <= bal_bcd_usd):
        gate.sell('bcd_usdt', d_s_bcd_usd + f_bcd_usd, val_s_bcd_usd), print('ПРОДАЮ', val_s_bcd_usd, 'BCD ПО ЦЕНЕ', d_s_bcd_usd+f_bcd_usd, 'USDT')
    else: print('ДОСТАТОЧНО БАКСОВ ИЛИ МАЛО BCD')





	
    #if (bal_usd <= S*USD and s_bcx_usd >= f_bcx_usd and avg_bal_usd <= bal_bcx_usd+BAL): gate.sell('bcx_usdt', d_s_bcx_usd, BCX), print('ХОРОШИЙ СПРЕД, ПРОДАЮ', BCX, 'BCX ПО ЦЕНЕ', d_s_bcx_usd, 'USDT')
    #elif (s_bcx_usd >= f_bcx_usd and proc_bcx_usd >= X): gate.sell('bcx_usdt', d_s_bcx_usd, BCX), print('ХОРОШИЙ %, ПРОДАЮ', BCX, 'BCX ПО ЦЕНЕ', d_s_bcx_usd, 'USDT')
    #elif (bal_usd <= S*USD and avg_bal_usd <= bal_bcx_usd+BAL): gate.sell('bcx_usdt', d_s_bcx_usd + f_bcx_usd, BCD), print('ПРОДАЮ',BCX, 'BCX ПО ЦЕНЕ', d_s_bcx_usd+f_bcx_usd, 'USDT')
    #else: print('ДОСТАТОЧНО БАКСОВ ИЛИ МАЛО BCX')
	

    #Cancel order
    #print (gate.cancelOrder('348307942','bifi_usdt'))
		
	
    
		
	

    # Get order status
    # print (gate.getOrder('267040896','eth_btc'))
		
	

	
		
	
    # Отменить открытые ордера
    #print (gate.cancelAllOrders('0','bifi_usdt'))
		
	
    
        
    # withdraw
    # print (gate.withdraw('btc','88','your address'))

    time.sleep(60)
    
