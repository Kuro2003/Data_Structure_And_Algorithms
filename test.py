stack=[]
s=input()
s+="#"
answer=""
# for i in range(len(s)):
#     if not stack or stack[-1] == s[i]:
#         stack.append(s[i])
#     else:
#         answer += stack[-1]
#         count=0
#         while stack:
#             stack.pop()
#             count += 1
#         answer += str(count)
#         stack.append(s[i])
# print(answer)
print(not stack)