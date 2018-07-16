import os
import collections

LineResult = collections.namedtuple('LineResult',
                                    'street, city, zip, state, beds, baths, sq__ft, type, sale_date, price, latitude, longitude')


def main():
    print_header()
    data = load_csv_file()
    header = data.pop(0)
    print('Header: {},{},{},{},{},{},{},{},{},{},{},{}'.format(
        header.street,
        header.city,
        header.zip,
        header.state,
        header.beds,
        header.baths,
        header.sq__ft,
        header.type,
        header.sale_date,
        header.price,
        header.latitude,
        header.longitude
    ))
    meh = get_most_expensive_house(data)
    print('Most expensive house: {}-bed, {}-bath, house for ${} in {}'.format(meh.beds, meh.baths, meh.price, meh.city))
    leh = get_least_expensive_house(data)
    print('Least expensive house: {}-bed, {}-bath, house for ${} in {}'.format(leh.beds, leh.baths, leh.price, leh.city))
    ah = get_average_house(data)
    print('Average house: ${}, {} bed, {} bath'.format(ah[0], ah[1], ah[2]))


def print_header():
    print('--------------------------')
    print('       REAL ESTATE')
    print('--------------------------')
    print()


def load_csv_file():
    path = 'data/SacramentoRealEstateTransactions2008.csv'
    filename = os.path.abspath(path)
    print('Filename to load: {}'.format(filename))

    data = []
    with open(filename, 'r', encoding='utf-8') as file_in:
        for line in file_in:
            line_array = line.split(",")
            line_data = LineResult(
                street=line_array[0],
                city=line_array[1],
                zip=line_array[2],
                state=line_array[3],
                beds=line_array[4],
                baths=line_array[5],
                sq__ft=line_array[6],
                type=line_array[7],
                sale_date=line_array[8],
                price=line_array[9],
                latitude=line_array[10],
                longitude=line_array[11]
            )
            data.append(line_data)
    print('Loading from csv data file...done.')
    return data


def get_most_expensive_house(data):
    max_price = 0
    max_index = 0
    index = 0
    for d in data:
        current_price = int(d.price)
        if current_price > max_price:
            max_price = current_price
            max_index = index
        index += 1
    return data.pop(max_index)


def get_least_expensive_house(data):
    min_price = 1000000
    min_index = 0
    index = 0
    for d in data:
        current_price = int(d.price)
        if current_price < min_price:
            min_price = current_price
            min_index = index
        index += 1
    return data.pop(min_index)


def get_average_house(data):
    sum_price = 0
    sum_beds = 0
    sum_baths = 0
    count = 0
    for d in data:
        sum_price += int(d.price)
        sum_beds += int(d.beds)
        sum_baths += int(d.baths)
        count += 1
    ah = [sum_price/count, sum_beds/count, sum_baths/count]
    return ah


if __name__ == '__main__':
    main()
