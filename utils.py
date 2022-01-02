import os

from linebot import LineBotApi, WebhookParser
from linebot.models import *


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_url(reply_token, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    img = ImageSendMessage(
        original_content_url = img_url,
        preview_image_url = img_url
    )
    line_bot_api.reply_message(reply_token, img)
    return 

def send_breakfast_message(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    carousel_template_message = TemplateSendMessage(
        alt_text = "早餐選單",
        template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url="https://www.mcdonalds.com/is/image/content/dam/tw/nutrition/nfl-product/product/products/sausage-mcmuffin-with-egg.jpg?$Product_Desktop$",
                    title = "1號餐	豬肉滿福堡加蛋",
                    text = "請輸入想查看的餐點數字!\n輸入home:返回用餐時段選擇",
                    actions = [
                        URIAction(
                            label = "詳細內容",
                            uri = "https://www.mcdonalds.com/tw/zh-tw/product/sausage-mcmuffin-with-egg.html"
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://www.mcdonalds.com/is/image/content/dam/tw/nutrition/nfl-product/product/products/mega-mcmuffin.jpg?$Product_Desktop$",
                    title = "2號餐	無敵豬肉滿福堡加蛋",
                    text = "請輸入想查看的餐點數字!\n輸入home:返回用餐時段選擇",
                    actions = [
                        URIAction(
                            label = "詳細內容",
                            uri = "https://www.mcdonalds.com/tw/zh-tw/product/mega-mcmuffin.html"
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://www.mcdonalds.com/is/image/content/dam/tw/nutrition/nfl-product/product/products/egg-burger-with-canadian-bacon.jpg?$Product_Desktop$",
                    title = "3號餐	火腿蛋堡",
                    text = "請輸入想查看的餐點數字!\n輸入home:返回用餐時段選擇",
                    actions = [
                        URIAction(
                            label = "詳細內容",
                            uri = "https://www.mcdonalds.com/tw/zh-tw/product/egg-burger-with-canadian-bacon.html"
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://www.mcdonalds.com/is/image/content/dam/tw/nutrition/nfl-product/product/products/egg-burger.jpg?$Product_Desktop$",
                    title = "4號餐	吉事蛋堡",
                    text = "請輸入想查看的餐點數字!\n輸入home:返回用餐時段選擇",
                    actions = [
                        URIAction(
                            label = "詳細內容",
                            uri = "https://www.mcdonalds.com/tw/zh-tw/product/egg-burger.html"
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://www.mcdonalds.com/is/image/content/dam/tw/nutrition/nfl-product/product/products/big-breakfast.jpg?$Product_Desktop$",
                    title = "5號餐	經典大早餐",
                    text = "請輸入想查看的餐點數字!\n輸入home:返回用餐時段選擇",
                    actions = [
                        URIAction(
                            label = "詳細內容",
                            uri = "https://www.mcdonalds.com/tw/zh-tw/product/big-breakfast.html"
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://www.mcdonalds.com/is/image/content/dam/tw/nutrition/nfl-product/product/products/hotcakes-with-sausage.jpg?$Product_Desktop$",
                    title = "6號餐	豬肉鬆餅",
                    text = "請輸入想查看的餐點數字!\n輸入home:返回用餐時段選擇",
                    actions = [
                        URIAction(
                            label = "詳細內容",
                            uri = "https://www.mcdonalds.com/tw/zh-tw/product/hotcakes-with-sausage.html"
                        ),
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template_message)
    return

def send_hamberger_message(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    carousel_template_message = TemplateSendMessage(
        alt_text = "主餐選單",
        template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url="https://www.mcdonalds.com/is/image/content/dam/tw/nutrition/nfl-product/product/products/EVM-01-Big-Mac.jpg?$Product_Desktop$",
                    title = "1號餐	大麥克",
                    text = "請輸入想查看的餐點數字!\n輸入home:返回用餐時段選擇",
                    actions = [
                        URIAction(
                            label = "詳細內容",
                            uri = "https://www.mcdonalds.com/tw/zh-tw/product/big-mac.html"
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://www.mcdonalds.com/is/image/content/dam/tw/nutrition/nfl-product/product/products/EVM-02-D-Cheeseburger.jpg?$Product_Desktop$",
                    title = "2號餐	雙層牛肉吉事堡",
                    text = "請輸入想查看的餐點數字!\n輸入home:返回用餐時段選擇",
                    actions = [
                        URIAction(
                            label = "詳細內容",
                            uri = "https://www.mcdonalds.com/tw/zh-tw/product/double-cheese-burger.html"
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://www.mcdonalds.com/is/image/content/dam/tw/nutrition/nfl-product/product/products/EVM-04-GBC.jpg?$Product_Desktop$",
                    title = "3號餐	嫩煎鷄腿堡",
                    text = "請輸入想查看的餐點數字!\n輸入home:返回用餐時段選擇",
                    actions = [
                        URIAction(
                            label = "詳細內容",
                            uri = "https://www.mcdonalds.com/tw/zh-tw/product/grilled-bbq-chicken-burger.html"
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://www.mcdonalds.com/is/image/content/dam/tw/nutrition/nfl-product/product/products/EVM-05-McChicken.jpg?$Product_Desktop$",
                    title = "4號餐	麥香鷄",
                    text = "請輸入想查看的餐點數字!\n輸入home:返回用餐時段選擇",
                    actions = [
                        URIAction(
                            label = "詳細內容",
                            uri = "https://www.mcdonalds.com/tw/zh-tw/product/mcchicken.html"
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://www.mcdonalds.com/is/image/content/dam/tw/nutrition/nfl-product/product/products/EVM-06-NGT6.jpg?$Product_Desktop$",
                    title = "5號餐	麥克鷄塊(6塊)",
                    text = "請輸入想查看的餐點數字!\n輸入home:返回用餐時段選擇",
                    actions = [
                        URIAction(
                            label = "詳細內容",
                            uri = "https://www.mcdonalds.com/tw/zh-tw/product/chicken-mcnuggets-6-pieces.html"
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://www.mcdonalds.com/is/image/content/dam/tw/nutrition/nfl-product/product/products/EVM-08-SCF.jpg?$Product_Desktop$",
                    title = "6號餐	勁辣鷄腿堡",
                    text = "請輸入想查看的餐點數字!\n輸入home:返回用餐時段選擇",
                    actions = [
                        URIAction(
                            label = "詳細內容",
                            uri = "https://www.mcdonalds.com/tw/zh-tw/product/spicy-chicken-filet-burger.html"
                        ),
                    ]
                )
                
            ]
        )
    )
    line_bot_api.reply_message(reply_token, carousel_template_message)
    return

"""
def send_button_message(id, text, buttons):
    pass
"""
