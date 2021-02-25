def delivery_info(delivery_file):
    """ Take in one day's melon delivery log and print a summary to the screen. 
    
    This function opens the specified file, parses the relevant information from 
    each line, and generates a summary that is printed to the screen. """
    the_file = open(delivery_file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon, count, amount = words    # unpack the list into specific variables

        print(f'Delivered {count} {melon}s for total of ${amount}')
    the_file.close()


# list the files to run through:
delivery_files = ['um-deliveries-20140519.txt','um-deliveries-20140520.txt','um-deliveries-20140521.txt']
# for each file in the list, print the day number and the delivery summary:
for i, delivery_file in enumerate(delivery_files):
    print(f'Day {i+1}')
    delivery_info(delivery_file)
