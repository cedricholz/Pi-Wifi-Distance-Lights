# import Utils as utils
#
# from firebase import firebase
#
# # url = utils.get_url()
# # firebase = firebase.FirebaseApplication(url, None)
#
# my_name = 'cedric'
#
# import time


# def add_member1_to_member2s_lamp_lighters(member1, member2):
#     lamp_lighters = get_lamp_lighters(member2)
#     lit_times = get_lit_times(member2)
#
#     cur_time = time.time()
#
#     if lamp_lighters == None:
#         lamp_lighters = [member1]
#         lit_times = [cur_time]
#     else:
#         if member1 in lamp_lighters:
#             index = lamp_lighters.index(member1)
#             lit_times[index] = cur_time
#         else:
#             lamp_lighters.append(member1)
#             lit_times.append(member1)
#
#     firebase.put('family_members', member2, {'lamp_lighters': lamp_lighters, 'lit_times': lit_times})
#
#
# def get_lamp_lighters(family_member):
#     return firebase.get('/family_members/' + family_member + '/lamp_lighters', None)
#
#
# def get_lit_times(family_member):
#     return firebase.get('/family_members/' + family_member + '/lit_times', None)

import time
print(time.time() - 1515270706.885412)