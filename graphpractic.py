import matplotlib.pyplot as plt
age_stud = ['0-10', '10-20', '20-30', '30-40', '40-50']
marks = [10, 40, 45, 80, 30]

# line chart
# plt.plot(age_stud, marks)
# bar chart
# plt.bar(age_stud, marks)
# scatter chart
plt.scatter(age_stud, marks)
plt.title('age marks')
plt.xlabel('age')
plt.ylabel('marks')
plt.show()