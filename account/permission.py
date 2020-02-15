# from rest_framework import permissions, response
#
# class GroupBasePermission(permissions.BasePermission):
#
#     group_name = ""
#
#     def has_permission(self, request, view):
#         """
#         Should simply return, or raise a 403 response.
#         """
#         print ('self.group_name == ', self.group_name)
#         try:
#             request.user.groups.get(name=self.group_name)
#             return True
#         except:
#             print ('group does not exist')
#             msg = ('Permission denied.')
#             #data = {'detail': six.text_type(msg)}
#             #return Response(data, status=status.HTTP_403_FORBIDDEN)
#             return response.Response('NOT')
#
#
# class HRAdminGroupPermission(GroupBasePermission):
#     """
#         Checks to see if a user is in a particular group
#     """
#
#     group_name = "HR Admin"
