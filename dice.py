# import plotly.figure_factory as ff
# import random
#
# dice_result = []
# for i in range(0, 100):
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     dice_result.append(dice1 + dice2)
#
# fig = ff.create_distplot([dice_result], ["Result"])
# fig.show()


import random
import plotly.express as px
count = []
dice_result = []
for i in range(0, 100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_result.append(dice1 + dice2)
    count.append(i)

print(count,dice_result)

fig = px.bar(x=dice_result,y=count)
fig.show()
