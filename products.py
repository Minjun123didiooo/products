#讓使用者可重複輸入商品名稱、價錢，並存入清單

products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #'q'表示結束輸入商品
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])
