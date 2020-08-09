with open('text_6.txt', 'r', encoding='utf-8') as syllabus:
    subject_dict = {} #словарь с названием предмета и общим количеством занятий
    for line in syllabus:
        line = line.split()
        sum_class = 0 #общее количество занятий конкретного предмета
        for i in range(len(line)-1):
            if line[i+1] != '-':
                s_num = ''  #строка, состоящая только из числового значения количества занятий
                for num in line[i+1]:
                    if num.isdigit():
                        s_num = s_num + num
                sum_class += int(s_num)
        subject_dict.update({line[0]: sum_class})
    print(subject_dict)


