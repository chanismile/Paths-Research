
import controller
import datetime
import sys


if __name__ == '__main__':
    control = controller.Controller("../data/paths.pkl.xz",'../data/paths0.png')
    print("To filter by hours press 1. Provide 2 hours for range in hh:mm:ss format.\nTo filter by hours in specific date press 2. Provide 2 hours for range and date in dd-mm-yyyy format.\nTo filter by area press 3. Provide top-left point and bottom-right point in x,y format.\nTo filter by specific area press 4. Provide 2 indexes in x,y format.\npress 5 to exit program")
    choises_list = []

    def parse_to_hours_filter(choise):
        global choises_list
        try:
            choise, from_hour, to_hour = choise.split()
            hh1, mm1, ss1 = from_hour.split(':')
            hh2, mm2, ss2 = to_hour.split(':')

            choises_list.append(
                (int(choise), (datetime.time(int(hh1), int(mm1), int(ss1)), datetime.time(int(hh2), int(mm2), int(ss2)))))
        except ValueError:
            print("invalid details. enter 1 and 2 hours for range. try again")

    def parse_to_date_filter(choise):
        global choises_list
        try:
            choise, from_hour, to_hour, date = choise.split()
            hh1, mm1, ss1 = from_hour.split(':')
            hh2, mm2, ss2 = to_hour.split(':')
            dd, mm, yyyy = date.split('-')

            choises_list.append((int(choise), (
            datetime.time(int(hh1), int(mm1), int(ss1)), datetime.time(int(hh2), int(mm2), int(ss2)),
            datetime.date(int(yyyy), int(mm), int(dd)))))
        except ValueError:
            print("invalid details. enter 2 hours for range in hh:mm:ss format and date in dd-mm-yyyy format. try again")
    def parse_to_area_filter(choise):
        global choises_list
        try:
            choise, p1, p2 = choise.split()
            x1, y1 = p1.split(',')
            x2, y2 = p2.split(',')

            choises_list.append((int(choise), ((int(x1), int(y1)), (int(x2), int(y2)))))
        except ValueError:
            print("invalid details. enter top-left point and bottom-right point in x,y format. try again")

    def parse_to_specific_area_filter(choise):
        global choises_list
        try:
            split_choise = choise.split()
            indxs = [tuple(indx.split(',')) for indx in split_choise[1:]]

            choises_list.append((int(split_choise[0]), tuple(indxs)))
        except ValueError:
            print("invalid details. enter 2 indexes in x,y format. try again")

    while(True):
        choises_list = []
        choosing_filter = 1

        while choosing_filter == 1:
            choise = input('your choise:')
            if choise[0] == '1':
                parse_to_hours_filter(choise)

            elif choise[0] == '2':
                parse_to_date_filter(choise)

            elif choise[0] == '3':
                parse_to_area_filter(choise)

            elif choise[0] == '4':
                parse_to_specific_area_filter(choise)

            elif choise[0] == '5':
                print('bye')
                sys.exit()

            choosing_filter = int(input('Do you want another filter? Press 1, if not, press 2\n'))

        control.drow_by_filters(tuple(choises_list))
        ans = input('to add more filters press 1, new filters - press 2, previous filter - press 3\n')
        if ans == 2:
            control.reset_df_with_filter()
        elif ans == 3:
            control.previous_filter()