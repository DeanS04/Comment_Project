import csv
conferences = []


with open('teacher_comments.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    header = csvfile.readline().split(',')
    for row in data:
            conferences.append(row)


def course_description(course):
    '''Provides a class description for the relevant course.'''
    description_list = []
    intro = ''
    if course == 'Calculus AB':
        intro += "This semester in AP AB Calculus, we covered the topics of limits, continuity, and differentiation and began the study of integration, which we will continue into the second semester. In addition to daily homework and frequent quizzes, we had three in-class unit tests, a cumulative final exam, and two projects, one on predicting stock prices using derivatives and one on modeling fluid flow using related rates and Torricelli’s Law."
    if course == 'Chinese II':
        intro += '这个学期我们学了更难的东西。我们学了学校，汽车，还有电脑的汉子。我们也复习了不同的词语。We learned more difficult vocabulary this semester. Our vocabulary units included school, cars, and computers. We also reviewed some common grammar concepts. '
    return intro


def attributes(attribute_list):
    '''Returns a description of the student based upon at most three attributes given for said student.'''
    attribute = ''
    for row in attribute_list:
        if row == 'hard worker':
            attribute = 'You were a very hard worker this semester. You always tried to get everything done, no matter how long the assignment was. '
        if row == 'communicative':
            attribute += 'You were a very communicative student, which I appreciated very much. If you did have any issues or difficulties, you would not hestitate to reach out to me or ask a fellow student. '
        if row == 'slow paced learner':
            attribute += 'You did have some difficulty understanding some of the concepts, and I could tell you struggled with some of the assignments. Good job persevering through all the challenges. '
            if 'communicative' in row:
                attribute += 'You did communicate with me, though, which definitely helped your understanding of all the concepts. '
            else:
                attribute += 'I would recommend you meet with me more. That way I could help explain and guide you through some of the tough areas. '
        if row == 'humorous':
            attribute += 'I enjoyed your sense of humour and positive in my class. I felt it really made a positive difference every day. '
        if row == 'independent':
            attribute += "An attribute that I noticed in you was your independence. Not having to rely on others can be a useful skill, but don't hestitate to reach out to me or any of your friends if you ever have any questions or concerns."
        if row == 'fast paced learner':
            attribute += 'You learned and worked at a faster pace than some of the other students, which is totally okay. '
            if row[10] == 'N':
                'If you do ever have any questions, I am open C and D block, as well as office hours and sometimes after school.'
        if row == 'dependent':
            attribute += 'You were a dependent student, which is totally okay as we are studying very challenging topics, so it is natural to not understand things. Continue to ask for help where you need it. '
    return attribute


def grade_avg(grade_list):
    '''Returns an average total grade based upon given scores.'''
#     num_grades = []
#     letter_grades = []
    test_grade = (int(grade_list[0]) + int(grade_list[1]) + int(grade_list[2]))/3
    participation_grade = int(grade_list[3])
    midterm = int(grade_list[4])
    total_grade = (test_grade + participation_grade + midterm)/3
    if total_grade != int(total_grade):
        total_grade = int(total_grade)
    return total_grade


def participation(grade):
    '''Returns a description of the student's class participation.'''
    if grade < 60:
        participation_comment = f"You struggled to engage in class this semester. You frequently missed assignments and did not engage in class activities. You also didn't communicate with me, nor did you work well with your fellow classmates. I encourage you to try and get things turned in to me more often, and I want you to meet with me if you have any questions and aim to talk in class at least once per class. Your participation grade in class this semester is {grade}%. "
    if 60 <= grade < 80:
        participation_comment = f"Your participation this semester was good, but there is room for improvement. You tried to do most of the assignments and engage in class, and you would usually work well with your classmates and with me. I want you to try and turn in every assignment I give you and ask any questions you have during class time. Your participation grade this semester is {grade}%. "
    if grade >= 80:
        participation_comment = f"Your participation this semester was admirable. You tried your hardest to complete every assignment I assigned, even if it was particularly challenging. During class, you would not hestitate to contribute to discussions or ask questions. Your participation grade this semester is {grade}%. "
    return participation_comment


def grade_trends(grades):
    '''Returns a description of the student's grade trend based on he or her 4 exams.'''
    grow = "You faithfully completed the exams and fully engaged in the preparation of the exam. As a result of your hard work, your average score of the exams was " + str(sum(grades)/len(grades)) + "%. This score showed a professional understanding of the contents; thus you have received A's on most tests, including the test you scored "+ str(max(grades))+"%."
    improve = "You have a bit more difficulty on your performance of in-class exams; you have recieved B range score in most tests, including an " + str(grades[-1]) +"% of your final exam. I would encourage you to see me before the test to be more prepared for the tests, using office-hours. I can help you to understand the content in a deeper level. Although your average score was " + str(sum(grades)/len(grades)) +"%, I think with some extra help, you can improve your grade, and your understanding of the course material."
    partialgrow = "You showed a partial growth in your exam scores. You scored" + " "+ str(sum(grades)/len(grades)) + "% on average. Though the score did not reflect how you improved very much, your test scores show that you were improving each time. You also utilized office hour effectively. Thus, you have received A-'s on your exams, including the test you scored" + " "+ str(max(grades))+ "%."

    work = grow
    if sum(grades)/len(grades) > 80:
        work = grow
        if grades[4] < grades[1] or grades[4] < grades[2] or grades[4] < grades[3]:
            work = partialgrow


    else:
        work = improve

    return work


def suggestions(info_list):
    '''Gives feedback based upon the information previously provided for a given student.'''
    suggestion = ''
    if 'hard worker' in info_list:
        suggestion += 'Please maintain the same level of effort you are putting into this class! I can tell you are a very hard worker, and this is a trait that will help you both in this class and any future endeavours.'
    if 'communicative':
        suggestion += 'I want you to keep being communicative with me. I appreciate how you reach out to me if you have any questions or concerns. It is very important as a student to always be clear with your teacher and know everything that is going on. '
    if 'slow paced learner' in info_list:
        suggestion += "Just because you had a hard time grasping some of the subjects, don't get discouraged! The things we are learning are very challenging. I want you to keep trying with everything, and if you have any questions, remember, I'm (almost) always available!"
    if 'humorous' in info_list:
        suggestion += "Please keep up the positive energy you bring to class each day. Your bright mood and humour really do lighten up everybody's day."
    if 'independent' in info_list:
        suggestion += 'I suggest collaborating with both me and your classmates more. Working with someone else can help you understand the concept a different way and/or find easier ways to do something, especially if you are struggling with some of the concepts we are working on. '
    if 'fast paced learner' in info_list:
        suggestion += "I'm glad you have been understanding the topics so well. If you continue to quickly learn the class material, that is great, but if you find some of the things we do more challenging, don't be discouraged. "
    if 'dependent' in info_list:
        suggestion += 'You should continue seeking help like you do. I would recommend you try to tackle more of your challenges on your own before you seek help. '
    print(suggestion)


def comment_end(name, grades, course):
    text = ''
    grade = sum(grades)/len(grades)
    if course == 'Calculus AB':
        text += f'The jump in difficulty level from precalculus to AP Calculus is significant, and you have excelled with this increased challenge. You have earned an {grade} for the semester and I look forward to your continued success during the remainder of the year.'
    if course == 'Chinese II':
        text += f'The jump in difficulty level from Chinese I to Chinese II is significant, and you have excelled with this increased challenge. You have earned an {grade} for the semester and I look forward to your continued success during the remainder of the year.'
    return text


def comment_printer(student_info):
    '''Prints the comment for students in a given conference information list.'''
    text = ''
    course = student_info[4]
    grades = [int(student_info[5]), int(student_info[6]), int(student_info[7]), int(student_info[8]), int(student_info[9])]
    first_name = student_info[0]
    attribute_list = student_info[11:13]
    # Name
    text += f"*** {student_info[0]} {student_info[1]} ***\n\n"
    # Course description
    text += f"{course_description(course)}\n\n"
    # Grade trends
    text += f"{grade_trends(grades)} {participation(int(student_info[9]))}\n\n"
    # Personal attributes
    text += f"{attributes(attribute_list)}\n\n"
    # End of comment
    text += f"{comment_end(first_name, grades, course)}\n\n"
    text += '-----------------------------------------------------------------------------------------------'
    print(text)


def comment_generator(student_info):
    '''Generates a personalized comment for a given student.'''
    txtfile = f"Students/{student_info[0]}.txt"
    with open(txtfile, 'w') as fout:
        course = student_info[4]
        grades = [int(student_info[5]), int(student_info[6]), int(student_info[7]), int(student_info[8]), int(student_info[9])]
        first_name = student_info[0]
        attribute_list = student_info[11:13]
        fout.write(f"*** {student_info[0]} {student_info[1]} ***\n\n")
        fout.write(course_description(course) + '\n' + '\n')
        fout.write(grade_trends(grades) + participation(int(student_info[9])) + '\n' + '\n')
        fout.write(attributes(attribute_list) + '\n' + '\n')
        fout.write(comment_end(first_name, grades, course))


for student in conferences:
    comment_generator(student)


for student in conferences:
    comment_printer(student)