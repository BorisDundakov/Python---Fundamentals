# version = [int(el) for el in input().split(".")]
#
# for index in range(len(version)):
#     if (version[2]) <= 8:
#         version[2] += 1
#     else:
#         if version[1] <= 8:
#             version[1] += 1
#             version[2] = 0
#         else:
#             version[0] += 1
#             version[1] = 0
#             version[2] = 0
#
#         break
#     break
# version = [str(element) for element in version]
# final = ".".join(version)
# print(final)


version_as_list = input().split(".")
version_as_int = int("".join(version_as_list)) + 1
new_version = list(str(version_as_int))
final = ".".join(new_version)
print(final)