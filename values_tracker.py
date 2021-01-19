class LastValuesTracker:

    def write_last_value(self, base_coin_abbreviation, last_coin_abbreviation, value):
        with open('last-values.txt', 'w') as file:
            file.write(f'{base_coin_abbreviation} <-> {last_coin_abbreviation} = {value}')

    def get_last_value(self, path):
        formatted_coins_information = []

        with open(path, 'r') as file:
            lines = file.readlines()

            for line in lines:
                line = line.replace(' <-> ', ' ').replace(' = ', ' ').split(' ')

                base_coin = line[0]
                last_coin = line[1]
                coins_rate = line[2]

                information = (base_coin, last_coin, coins_rate)

                formatted_coins_information.append(information)

        return formatted_coins_information

if __name__ == '__main__':
    tracker = LastValuesTracker()

    tracker.write_last_value('USD', 'BRL', 5.26)
    print(tracker.get_last_value('./last-values.txt'))
