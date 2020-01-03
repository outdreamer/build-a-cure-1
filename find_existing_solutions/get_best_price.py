import requests
import urllib.request
import time
from bs4 import BeautifulSoup

'''
to do:
- pull html
- sort html into just product text
- identify unique texts with dosages in them & match with price text
- standardize and return item with lowest price per unit & highest score
- add intl
- add lowest price with savings/coupon offer
- add identification of sub-compound quantities & ratios: '500mg Extract & Powder - 900mcg Hypericin'
- dose_item['keyword'] should be most common quantity keyword found
'''

order_sizes = ['mcg', 'mg', 'mL', 'g', 'kg']

def get_div_list(urls):
    ''' each item should have all relevant info for one product '''
    div_list = []
    for url in urls:
        print('url', url)
        response = requests.get(url)
        print('response', response)
        if response:
            print('response', response)
            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
                for text in soup.strings:
                    print('text', text)
                    quantity_count = sum([1 for order_size in order_sizes if order_size in text])
                    if quantity_count > 0:
                        new_lines = []
                        lines = text.split('\n')
                        for line in lines:
                            if line not in new_lines:
                                new_lines.append(line)
                        div_list.append('\n'.join(new_lines))
    if len(div_list) > 0:
        return div_list
    return False

def get_best_price_per_unit(div_list):
    products = {}
    ''' determine order of price & product dose divs '''
    div_list_text = '\n'.join(div_list)
    highest_size_count = 0
    for order_size in order_sizes:
        count = div_list_text.count(order_size)
        if count > highest_size_count:
            highest_size_count = count
    dose_item = {'name': 'total_dose_count', 'keyword': highest_size_count, 'direction': -1}
    price_item = {'name': 'price', 'keyword': '$', 'direction': 1}
    ordered_items = [dose_item, price_item]
    found_index = None
    
    for item in ordered_items:
        if item['keyword'] in div_list_text:
            found_index = div_list_text.index(item['keyword'])
            if found_index > -1:
                print('found index', found_index, 'of keyword', item['keyword'])
                break
    print('found_index', found_index)
    ''' re-order the ordered_items to ensure youre assigning 'first' to the first item '''
    new_ordered_items = [ordered_items[found_index]]
    for i, ordered_item in enumerate(ordered_items):
        if i != found_index:
            new_ordered_items.append(ordered_item)
    print('new', new_ordered_items)
    products = {}
    for i, text in enumerate(div_list):
        new_product = {}
        text_words = text.split(' ')
        for item in new_ordered_items:
            if item['keyword'] in text_words:
                add_word_index = i + item['direction']
                value = ' '.join(text_words[add_word_index:i]).strip() if add_word_index < i else ' '.join(text_words[i:add_word_index]).strip()
                if item['name'] == 'total_dose_count' and item['keyword'] in value:
                    other_words = text.split(value)
                    for other in other_words:
                        for count in other.split(' '):
                            if int(count):
                                count_index = i - item['direction']
                                count_keyword = text_words[count_index]
                                if count_keyword not in order_sizes and count_keyword != item['keyword']:
                                    ''' make sure this isnt a quantity of a sub component '''
                                    dose_value = ''.join([x for x in value if x in '0123456789.']).strip()
                                    value = str(int(count) * int(dose_value))
                new_product[item['name']] = value
        if new_product:
            for j, order_size in enumerate(order_sizes):
                if (j + 1) < len(order_sizes):
                    if order_size in div and order_sizes[j + 1] in div:
                        ''' found matching pair of consecutive quantities '''
                        small_value_index = div.index(order_size) + dose_item['direction']
                        converted_smaller = convert_to_grams(text_words[small_value_index], order_size)
                        large_value_index = div.index(order_sizes[j + 1]) + dose_item['direction']
                        converted_larger = convert_to_grams(text_words[large_value_index], order_sizes[j + 1])
                        new_product['dose'] = str(round((converted_smaller / converted_larger), 4))
            dose = ''.join([x for x in new_product['dose'] if x in '0123456789.'])
            price = ''.join([x for x in new_product['price'] if x in '0123456789.'])
            price_ratio = round(int(price)/int(dose), 2)
            if price_ratio not in products:
                products[price_ratio] = [new_product]
            else:
                products[price_ratio].append(new_product)
    print('products', products)
    max_ratio = max(products.keys())
    if max_ratio:
        print('max ratio', max_ratio, products[max_ratio])
        return products[max_ratio]
    return False

def convert_to_grams(value, size):
    value = int(value)
    if size in order_sizes:
        if size == 'mg':
            return round(value / 1000, 6)
        elif size == 'mcg':
            return round(value / 1000000, 6)
        elif size == 'g':
            return value
        else:
            print('conversion not supported for', value, size)
    return value

def get_best_price(product_name):
    urls = [] # add api sources for a product
    div_list = get_div_list(urls)
    if div_list:
        best_priced_products = get_best_price_per_unit(div_list)
        if best_priced_products:
            print('best_priced_products', best_priced_products)