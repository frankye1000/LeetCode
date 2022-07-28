"""
In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

Example 1:
Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately.
This poisoned status will last 2 seconds until the end of time point 2.
And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds.
So you finally need to output 4.
Example 2:
Input: [1,2], 2
Output: 3
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned.
This poisoned status will last 2 seconds until the end of time point 2.
However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status.
Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3.
So you finally need to output 3.
"""
## Time Limit Exceeded
# timeSeries = [1,4]
# duration = 2
#
# re = []
# for start in timeSeries:
#
#     for dur in range(duration):
#         end = start + 1
#         key = "start=%s,end=%s"%(start, end)
#
#         re.append(key)
#
#         start += 1
# print(len(set(re)))


## Time Limit Exceeded
# timeSeries = [1,2,3,4,5]
# duration = 3
#
# count = 0
# pointer = 0
#
# for j in range(len(timeSeries)):
#     start = timeSeries[j]
#     print("start = ", start)
#     for i in range(duration):
#         if start not in timeSeries[j+1:]:
#             count += 1
#             start += 1
#             print("count = ",count, "start = ",start)
#         else:
#             continue
#
# print(count)

timeSeries = [1,2,3,4,5]
duration = 3

total = duration * len(timeSeries)

for i in range(1, len(timeSeries)):
    if timeSeries[i] < timeSeries[i - 1] + duration:
        total -= timeSeries[i - 1] + duration - timeSeries[i]
print(total)


