def delivery_info(delivery_file):
    the_file = open(delivery_file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]    # original file had an error here - index was set to 0
        amount = words[2]   # original file had an error here - index was set to 0

        print(f'Delivered {count} {melon}s for total of ${amount}')
    the_file.close()

delivery_files = ['um-deliveries-20140519.txt','um-deliveries-20140520.txt','um-deliveries-20140521.txt']
for i, delivery_file in enumerate(delivery_files):
    print(f'Day {i+1}')
    delivery_info(delivery_file)
