



# years=set()
# i=0
# with open('AAPL.csv', 'r') as fy:
#     csv_reader=fy.readlines()
#     for row in csv_reader:
#         if(i!=0):
#           years.add(row.split(',')[0].split('-')[2])
#         else:
#             i+=1
#     years_sort=years
#     years_sorted= sorted(years_sort)

# for i in years_sorted:
#     with open(f'AAPL_{i}.csv', 'w', encoding='UTF8', newline='') as f:
#      writer = csv.writer(f)
#
#     with open('AAPL.csv', 'r') as fh:
#       fh.readline()




import csv
from csv import DictReader
import datetime
import os
import concurrent
from concurrent.futures import ThreadPoolExecutor, wait


def aapl_filse(fpath):
    if not os.path.exists(fpath):
        raise FileNotFoundError()

    executor = ThreadPoolExecutor(max_workers=16)
    futures = []

    counter = 0
    line = []

    open_aa, vol, high, low, close, adjusted = 0, 0, 0, 0, 0, 0

    with open(fpath) as csv_file:
        reader = DictReader(csv_file)

        for item in reader:

            date = item['Date'][6:]

            if counter == 0:
                date_year = date

            if date == date_year:
                line.append(item)

                open_aa += float(item['Open'])
                vol += float(item['Volume'])
                high += float(item['High'])
                low += float(item['Low'])
                close += float(item['Close'])
                adjusted += float(item['Adjusted Close'])

                counter += 1
            else:
                avg = {'Date': 'Average', 'Low': low / counter, 'Open': open_aa / counter, 'Volume': vol / counter,
                      'High': high / counter, 'Close': close / counter, 'Adjusted Close': adjusted / counter}
                file_path = os.path.join(os.path.dirname(fpath), f"{os.path.splitext(fpath)[0]}_{date_year}.csv")

                futures.append(executor.submit(write_to_file, line, avg, file_path))

                open_aa = float(item['Open'])
                vol = float(item['Volume'])
                high = float(item['High'])
                low = float(item['Low'])
                close = float(item['Close'])
                adjusted = float(item['Adjusted Close'])

                line = [item]

                counter = 1

                date_year = date

        avg = {'Date': 'Average', 'Low': low / counter, 'Open': open_aa / counter, 'Volume': vol / counter,
               'High': high / counter, 'Close': close / counter, 'Adjusted Close': adjusted / counter}
        file_path = os.path.join(os.path.dirname(fpath), f"{os.path.splitext(fpath)[0]}_{date_year}.csv")

        futures.append(executor.submit(write_to_file, line, avg, file_path))
    done, not_done = wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
    print(f"done: {len(done)}")
    print(f"not done: {len(not_done)}")


def write_to_file(lines: list, avg: dict, file_path):
    with open(file_path, "w", newline="") as csv_f:
        writer = csv.DictWriter(csv_f, ['Date', 'Low', 'Open', 'Volume', 'High', 'Close', 'Adjusted Close'])
        writer.writeheader()
        for row in lines:
            writer.writerow(row)
        writer.writerow(avg)



if __name__ == '__main__':
    start = datetime.datetime.utcnow()
    aapl_filse('AAPL.csv')
    end = datetime.datetime.utcnow()
    print(f"Time took: {(end - start).total_seconds()}s")







