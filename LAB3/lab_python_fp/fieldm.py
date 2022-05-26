# Пример:
#goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price':
# 2000}, {'title': 'Диван для отдыха', 'price': 5300}
goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'color': 'black'}]

def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) > 1: out = dict()
        for key in args:
            if key in item.keys():
                if len(args) > 1: out[key] = item[key]
                else: yield item[key]
        if len(args) > 1: yield out

if __name__ == "__main__":
    for i in field(goods,  'price'):print(i)
    for i in field(goods,'title', 'price'): print(i)