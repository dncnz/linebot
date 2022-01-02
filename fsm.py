from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url, send_breakfast_message, send_hamberger_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_to_main_menu(self, event):
        text = event.message.text
        return text.lower() == "start" or text.lower() == "home"

    def is_going_to_breakfast(self, event):
        text = event.message.text
        return text.lower() == "1" or text.lower() == "b"

    def is_going_to_hamberger(self, event):
        text = event.message.text
        return text.lower() == "2" or text.lower() == "b"
    
    def is_going_to_b_info(self, event):
        text = event.message.text
        return text.lower() == "1" or text.lower() == "2" or text.lower() == "3" or text.lower() == "4" or text.lower() == "5" or text.lower() == "6"

    def is_going_to_b_price(self, event):
        text = event.message.text
        return text.lower() == "p1" or text.lower() == "p2" or text.lower() == "p3" or text.lower() == "p4" or text.lower() == "p5" or text.lower() == "p6"
    
    def is_going_to_b_health(self, event):
        text = event.message.text
        return text.lower() == "h1" or text.lower() == "h2" or text.lower() == "h3" or text.lower() == "h4" or text.lower() == "h5" or text.lower() == "h6"

    def is_going_to_h_info(self, event):
        text = event.message.text
        return text.lower() == "1" or text.lower() == "2" or text.lower() == "3" or text.lower() == "4" or text.lower() == "5" or text.lower() == "6"

    def is_going_to_h_price(self, event):
        text = event.message.text
        return text.lower() == "p1" or text.lower() == "p2" or text.lower() == "p3" or text.lower() == "p4" or text.lower() == "p5" or text.lower() == "p6"

    def is_going_to_h_health(self, event):
        text = event.message.text
        return text.lower() == "h1" or text.lower() == "h2" or text.lower() == "h3" or text.lower() == "h4" or text.lower() == "h5" or text.lower() == "h6"

    def on_enter_main_menu(selg, event):
        print("main menu")
        reply_token = event.reply_token
        send_text_message(reply_token, "歡迎使用麥當勞菜單瀏覽系統\n\n請選擇時段(輸入數字)\n\n1. 早餐（供應時間:5:00~10:30）\n\n2. 主餐(供應時間:早餐時段以外)")

    def on_enter_breakfast(self, event):
        print("I'm entering breakfast")
        reply_token = event.reply_token
        send_breakfast_message(reply_token)
        #self.go_back()

    def on_enter_hamberger(self, event):
        print("I'm entering hamberger")
        reply_token = event.reply_token
        send_hamberger_message(reply_token)
        #self.go_back()

    def on_enter_b_info(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text == '1':
            send_text_message(reply_token, "1號餐	豬肉滿福堡加蛋\n\n"+
                                            "香嫩柔軟的太陽蛋，絕配香煎豬肉片，還有熱騰騰融化的切達吉事，最後蓋上軟中帶勁的滿福麵包！吃滿福保好運、上班上學一切順利！\n\n"+
                                            "p1:查看價格\nh1:查看營養成份\nb:返回早餐選單")
        elif text == '2':
            send_text_message(reply_token, "2號餐	無敵豬肉滿福堡加蛋\n\n"+
                                            "吃無敵豬肉滿福堡給你無敵活力！兩層香煎豬肉片，與獨家氣蒸太陽蛋和切達吉事，最後蓋上軟中帶勁的滿福麵包，吃滿福，保好運，今天你最無敵！\n\n"+
                                            "p2:查看價格\nh2:查看營養成份\nb:返回早餐選單")
        elif text == '3':
            send_text_message(reply_token, "3號餐	火腿蛋堡\n\n"+
                                            "香煎火腿片配上特選洗選蛋，口感意外超級搭，再用濃郁切達吉事點綴，絕妙組合！讓早起有了蛋蛋正能量，今天就這樣吃吧！\n\n"+
                                            "p3:查看價格\nh3:查看營養成份\nb:返回早餐選單")
        elif text == '4':
            send_text_message(reply_token, "4號餐	吉事蛋堡\n\n"+
                                            "起床來點正能量！三段水溫洗淨的洗選蛋，烹調出口感軟嫩的太陽蛋，再搭配美國春麥製成的柔軟麵包，以及紐澳模範乳源製成的切達吉事，絕配組合讓蛋蛋正能量爆發！\n\n"+
                                            "p4:查看價格\nh4:查看營養成份\nb:返回早餐選單")
        elif text == '5':
            send_text_message(reply_token, "5號餐	經典大早餐\n\n"+
                                            "金黃滑嫩炒蛋，像在餐盤裡出太陽了，伴佐剛剛香煎呈盤的豬肉片，還有Q彈帶勁的滿福麵包，你可以個別品嘗，也可以任意隨心情巧搭，你是早晨美食藝術家，享受從早開始。\n\n"+
                                            "p5:查看價格\nh5:查看營養成份\nb:返回早餐選單")
        elif text == '6':
            send_text_message(reply_token, "6號餐	豬肉鬆餅\n\n"+
                                            "奶油球緩慢在熱騰騰鬆餅上融化，甜蜜蜜的糖漿與香煎豬肉片相遇，甜與鹹、鬆與綿，這一口你想怎麼吃？享受從早開始！\n\n"+
                                            "p6:查看價格\nh6:查看營養成份\nb:返回早餐選單")
    
    def on_enter_h_info(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text == '1':
            send_text_message(reply_token, "1號餐	大麥克\n\n"+
                                            "麥當勞永遠的一號餐， 全球狂熱50年， 紐澳100%雙層純牛肉， 淋上大麥克招牌醬料， 加上生菜、吉事、洋蔥、酸黃瓜， 美味層層堆疊，口感樂趣無窮。 從美國總統到素人都是鐵粉， 經濟學家還發明「大麥克指數」致敬，果然，只有大麥克，才是大麥克！\n\n"+
                                            "p1:查看價格\nh1:查看營養成份\nb:返回主餐選單")
        elif text == '2':
            send_text_message(reply_token, "2號餐	雙層牛肉吉事堡\n\n"+
                                            "紐澳雙層100%優質牛肉， 搭配雙層切達吉事片， 酸黃瓜、洋蔥在裡面， 芥末醬、番茄醬淋上去， 層出不窮的經典滋味， 真的沒在跟你客氣的。\n\n"+
                                            "p2:查看價格\nh2:查看營養成份\nb:返回主餐選單")
        elif text == '3':
            send_text_message(reply_token, "3號餐	嫩煎鷄腿堡\n\n"+
                                            "低熱量的清爽美味，捨我其誰。 獨特的BBQ風味醬，搭配多汁去骨鷄腿肉，以慢火嫩煎入味，意料之外的絕配。 加上大片牛番茄與三道水洗新鮮生菜，清爽感加乘，喜歡就醬吃，越吃越順口！\n\n"+
                                            "p3:查看價格\nh3:查看營養成份\nb:返回主餐選單")
        elif text == '4':
            send_text_message(reply_token, "4號餐	麥香鷄\n\n"+
                                            "清脆爽口新鮮生菜， 健康優質麥香鷄排， 淋上特製醬料， 通通夾進芝麻麵包， 熟悉的經典美味， 不只超值，更有品質。\n\n"+
                                            "p4:查看價格\nh4:查看營養成份\nb:返回主餐選單")
        elif text == '5':
            send_text_message(reply_token, "5號餐	麥克鷄塊(6塊)\n\n"+
                                            "大家都愛麥克鷄塊！ 100%嚴選健康優質鷄肉， 調配鷄胸和鷄腿黃金比例， 口感外酥內軟， 男女老少都愛吃， 每年熱銷超過3億片， 疊起來有6000棟台北101。 搭上經典的糖醋醬， 酸酸甜甜的越吃越順口。 你呢？今天麥克鷄塊了嗎？\n\n"+
                                            "p5:查看價格\nh5:查看營養成份\nb:返回主餐選單")
        elif text == '6':
            send_text_message(reply_token, "6號餐	勁辣鷄腿堡\n\n"+
                                            "整塊勁辣鷄腿排，未吃份量先得分。 滿滿生菜搭配特製美乃滋，口感豐富多層次。 芝麻漢堡蓋上去，一口咬下過足癮。 夠辣夠帶勁！意猶未盡、就是吃不膩。\n\n"+
                                            "p6:查看價格\nh5:查看營養成份\nb:返回主餐選單")

    def on_enter_b_price(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text == "p1" or text == "P1":
            send_text_message(reply_token, "1號餐	豬肉滿福堡加蛋\n\n"+
                                            "單點: $58\n"+"雞塊配餐: $108\n"+"薯餅配餐: $88\n"+"搭配義式研磨咖啡: $78\n"+"搭配$38指定飲料: $68\n\n"+
                                            "h1:查看營養成份   b:返回早餐選單")
        elif text == "p2" or text == "P2":
            send_text_message(reply_token, "2號餐	無敵豬肉滿福堡加蛋\n\n"+
                                            "單點: $78\n"+"雞塊配餐: $128\n"+"薯餅配餐: $108\n"+"搭配義式研磨咖啡: $110\n"+"搭配$38指定飲料: $88\n\n"+
                                            "h2:查看營養成份   b:返回早餐選單")
        elif text == "p3" or text == "P3":
            send_text_message(reply_token, "3號餐	火腿蛋堡\n\n"+
                                            "單點: $50\n"+"雞塊配餐: $100\n"+"薯餅配餐: $80\n"+"搭配義式研磨咖啡: $82\n"+"搭配$38指定飲料: $60\n\n"+
                                            "h3:查看營養成份   b:返回早餐選單")
        elif text == "p4" or text == "P4":
            send_text_message(reply_token, "4號餐	吉事蛋堡\n\n"+
                                            "單點: $32\n"+"雞塊配餐: $82\n"+"薯餅配餐: $62\n"+"搭配義式研磨咖啡: $64\n"+"搭配$38指定飲料: $42\n\n"+
                                            "h4:查看營養成份   b:返回早餐選單")
        elif text == "p5" or text == "P5":
            send_text_message(reply_token, "5號餐	經典大早餐\n\n"+
                                            "單點: $69\n"+"雞塊配餐: $119\n"+"薯餅配餐: $99\n"+"搭配義式研磨咖啡: $101\n"+"搭配$38指定飲料: $79\n\n"+
                                            "h5:查看營養成份   b:返回早餐選單")
        elif text == "p6" or text == "P6":
            send_text_message(reply_token, "6號餐	豬肉鬆餅\n\n"+
                                            "單點: $69\n"+"雞塊配餐: $119\n"+"薯餅配餐: $99\n"+"搭配義式研磨咖啡: $101\n"+"搭配$38指定飲料: $79\n\n"+
                                            "h6:查看營養成份   b:返回早餐選單")

    def on_enter_h_price(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text == "p1" or text == "P1":
            send_text_message(reply_token, "1號餐	大麥克\n\n"+
                                            "單點: $75\n"+"經典配餐: $130\n"+"清爽配餐: $130\n"+"勁脆配餐: $143\n"+"炫冰配餐: $160\n"+"豪吃配餐: $160\n\n"+
                                            "h1:查看營養成份   b:返回主餐選單")
        elif text == "p2" or text == "P2":
            send_text_message(reply_token, "2號餐	雙層牛肉吉事堡\n\n"+
                                            "單點: $65\n"+"經典配餐: $120\n"+"清爽配餐: $120\n"+"勁脆配餐: $133\n"+"炫冰配餐: $150\n"+"豪吃配餐: $150\n\n"+
                                            "h2:查看營養成份   b:返回主餐選單")
        elif text == "p3" or text == "P3":
            send_text_message(reply_token, "3號餐	嫩煎鷄腿堡\n\n"+
                                            "單點: $80\n"+"經典配餐: $135\n"+"清爽配餐: $135\n"+"勁脆配餐: $148\n"+"炫冰配餐: $165\n"+"豪吃配餐: $165\n\n"+
                                            "h3:查看營養成份   b:返回主餐選單")
        elif text == "p4" or text == "P4":
            send_text_message(reply_token, "4號餐	麥香鷄\n\n"+
                                            "單點: $45\n"+"經典配餐: $100\n"+"清爽配餐: $100\n"+"勁脆配餐: $113\n"+"炫冰配餐: $130\n"+"豪吃配餐: $130\n\n"+
                                            "h4:查看營養成份   b:返回主餐選單")
        elif text == "p5" or text == "P5":
            send_text_message(reply_token, "5號餐	麥克鷄塊(6塊)\n\n"+
                                            "單點: $64\n"+"經典配餐: $119\n"+"清爽配餐: $119\n"+"勁脆配餐: $132\n"+"炫冰配餐: $149\n"+"豪吃配餐: $149\n\n"+
                                            "h5:查看營養成份   b:返回主餐選單")
        elif text == "p6" or text == "P6":
            send_text_message(reply_token, "6號餐	勁辣鷄腿堡\n\n"+
                                            "單點: $75\n"+"經典配餐: $130\n"+"清爽配餐: $130\n"+"勁脆配餐: $143\n"+"炫冰配餐: $160\n"+"豪吃配餐: $160\n\n"+
                                            "h6:查看營養成份   b:返回主餐選單")
    
    def on_enter_b_health(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text == "h1" or text == "H1":
            send_text_message(reply_token, "1號餐	豬肉滿福堡加蛋\n\n"+
                                            "熱量 (Kcal): 389\n" + "蛋白質 (g): 24\n" + "脂肪 (g): 20\n" + "碳水化合物 (g): 28\n" + "糖 (g): 1.6\n" + "鈉 (mg): 781.3\n\n"+
                                            "p1:查看價格   b:返回早餐選單")
        elif text == "h2" or text == "H2":
            send_text_message(reply_token, "2號餐	無敵豬肉滿福堡加蛋\n\n"+
                                            "熱量 (Kcal): 509\n" + "蛋白質 (g): 32\n" + "脂肪 (g): 30\n" + "碳水化合物 (g): 28\n" + "糖 (g): 1.6\n" + "鈉 (mg): 1002.8\n\n"+
                                            "p2:查看價格   b:返回早餐選單")
        elif text == "h3" or text == "H3":
            send_text_message(reply_token, "3號餐	火腿蛋堡\n\n"+
                                            "熱量 (Kcal): 302\n" + "蛋白質 (g): 17\n" + "脂肪 (g): 13\n" + "碳水化合物 (g): 30\n" + "糖 (g): 5.2\n" + "鈉 (mg): 568.7\n\n"+
                                            "p3:查看價格   b:返回早餐選單")
        elif text == "h4" or text == "H4":
            send_text_message(reply_token, "4號餐	吉事蛋堡\n\n"+
                                            "熱量 (Kcal): 282\n" + "蛋白質 (g): 14\n" + "脂肪 (g): 12\n" + "碳水化合物 (g): 30\n" + "糖 (g): 4.9\n" + "鈉 (mg): 432.2\n\n"+
                                            "p4:查看價格   b:返回早餐選單")
        elif text == "h5" or text == "H5":
            send_text_message(reply_token, "5號餐	經典大早餐\n\n"+
                                            "熱量 (Kcal): 411\n" + "蛋白質 (g): 26\n" + "脂肪 (g): 22\n" + "碳水化合物 (g): 27\n" + "糖 (g): 1.3\n" + "鈉 (mg): 664.9\n\n"+
                                            "p5:查看價格   b:返回早餐選單")
        elif text == "h6" or text == "H6":
            send_text_message(reply_token, "6號餐	豬肉鬆餅\n\n"+
                                            "熱量 (Kcal): 439\n" + "蛋白質 (g): 16\n" + "脂肪 (g): 18\n" + "碳水化合物 (g): 53\n" + "糖 (g): 11\n" + "鈉 (mg): 932.8\n\n"+
                                            "p6:查看價格   b:返回早餐選單")                         


    def on_enter_h_health(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text == "h1" or text == "H1":
            send_text_message(reply_token, "1號餐   大麥克\n\n"+
                                            "熱量 (Kcal): 548\n" + "蛋白質 (g): 26\n" + "脂肪 (g): 28\n" + "碳水化合物 (g): 49\n" + "糖 (g): 7.1\n" + "鈉 (mg): 672.1\n\n"+
                                            "p1:價格   b:返回主餐選單")
        elif text == "h2" or text == "H2":
            send_text_message(reply_token, "2號餐	雙層牛肉吉事堡\n\n"+
                                            "熱量 (Kcal): 467\n" + "蛋白質 (g): 26\n" + "脂肪 (g): 25\n" + "碳水化合物 (g): 35\n" + "糖 (g): 6.3\n" + "鈉 (mg): 784.4\n\n"+
                                            "p2:價格   b:返回主餐選單")
        elif text == "h3" or text == "H3":
            send_text_message(reply_token, "3號餐	嫩煎鷄腿堡\n\n"+
                                            "熱量 (Kcal): 363\n" + "蛋白質 (g): 24\n" + "脂肪 (g): 12\n" + "碳水化合物 (g): 40\n" + "糖 (g): 11\n" + "鈉 (mg): 690.9\n\n"+
                                            "p3:價格   b:返回主餐選單")
        elif text == "h4" or text == "H4":
            send_text_message(reply_token, "4號餐	麥香鷄\n\n"+
                                            "熱量 (Kcal): 360\n" + "蛋白質 (g): 14\n" + "脂肪 (g): 16\n" + "碳水化合物 (g): 42\n" + "糖 (g): 4.6\n" + "鈉 (mg): 743.7\n\n"+
                                            "p4:價格   b:返回主餐選單")
        elif text == "h5" or text == "H5":
            send_text_message(reply_token, "5號餐	麥克鷄塊(6塊)\n\n"+
                                            "熱量 (Kcal): 270\n" + "蛋白質 (g): 16\n" + "脂肪 (g): 17\n" + "碳水化合物 (g): 13\n" + "糖 (g): 0\n" + "鈉 (mg): 427.6\n\n"+
                                            "p5:價格   b:返回主餐選單")
        elif text == "h6" or text == "H6":
            send_text_message(reply_token, "6號餐	勁辣鷄腿堡\n\n"+
                                            "熱量 (Kcal): 493\n" + "蛋白質 (g): 22\n" + "脂肪 (g): 24\n" + "碳水化合物 (g): 47\n" + "糖 (g): 4.3\n" + "鈉 (mg): 871.4\n\n"+
                                            "p6:價格   b:返回主餐選單")  

    #def on_exit_state3(self):
    #    print("Leaving state3")
