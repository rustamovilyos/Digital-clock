# Цифровые часы
import sys,time
import sevseg


def clock():
    try:
        while True:
            print('\n' * 60)
            current_time = time.localtime()
            hours = str(current_time.tm_hour)
            minutes = str(current_time.tm_min)
            seconds = str(current_time.tm_sec)

            h_digits = sevseg.getSevSegStr(hours, 2)
            h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()

            m_digits = sevseg.getSevSegStr(minutes, 2)
            m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()

            s_digits = sevseg.getSevSegStr(seconds, 2)
            s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

            print(h_top_row + '   ' + m_top_row + '   ' + s_top_row)
            print(h_middle_row + ' * ' + m_middle_row + ' * ' + s_middle_row)
            print(h_bottom_row + ' * ' + m_bottom_row + ' * ' + s_bottom_row)
            print()
            print('Press Ctrl-C to quit.')

            while True:
                time.sleep(0.01)
                if time.localtime().tm_sec != current_time.tm_sec:
                    break
    except KeyboardInterrupt:
        print('Digital Clock stopped')
        sys.exit()


if __name__ == '__main__':
    clock()

