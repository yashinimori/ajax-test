import csv
import os
import matplotlib.pyplot as pyplot

class DataManager():
    raw_data = []
    filtered_data = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: []

    }
    group_age_range = {
        1: {'begin': 25,'end': 34},
        2: {'begin': 35,'end': 44},
        3: {'begin': 45,'end': 54},
        4: {'begin': 55,'end': 64},
        5: {'begin': 65,'end': 74},
        6: {'begin': 75,'end': 84}
    }
    def read_data(self):
        with open('storage/data/heart.csv') as f:
                self.raw_data = [{
                        'age':line[0],
                        'sex':line[1],
                        'cp':line[2],
                        'trtbps':line[3],
                        'chol':line[4],
                        'fbs':line[5],
                        'restecg':line[6],
                        'thalachh':line[7]
                        } for line in csv.reader(f)]
        self.raw_data.pop(0)

    def filter_and_group_data(self):
        for user in self.raw_data:
            if int(user['trtbps']) >= 140:
                for key, value in self.group_age_range.items():
                    if value['begin'] <= int(user['age']) <= value['end']:
                        self.filtered_data[key].append(user)


    def avarage_thalachh(self, group_number):
        sum = 0
        for user in self.filtered_data[group_number]:
            sum += int(user['thalachh'])
        if len(self.filtered_data[group_number]) == 0:
            return 0
        else:
            return sum/len(self.filtered_data[group_number])

    
    def create_diagram(self):
        figure = pyplot.figure(figsize=(6, 4))
        axes = figure.add_subplot()
        axes.set_xlabel('Возрастные группы')
        axes.set_ylabel('Среднее значение сердечного ритма')
        xaxis = list(data_manager.group_age_range.keys())
        yaxis = [self.avarage_thalachh(i) for i in list(data_manager.group_age_range.keys())]
        axes.bar(xaxis,yaxis)
        axes.grid()
        pyplot.savefig('storage/media/diagram.jpeg')
        print('Diagram saved to storage/media/diagram.jpeg')

if __name__ == '__main__':
    data_manager = DataManager()
    data_manager.read_data()
    data_manager.filter_and_group_data()
    data_manager.create_diagram()
    