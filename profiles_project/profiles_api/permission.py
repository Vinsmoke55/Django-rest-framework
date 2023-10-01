from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
	"""allows user to edit their own profile"""
	def has_object_permission(self,request,view,obj):
		"""check user is trying to edit their own profile"""
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.id==request.user.id


class PostOwnStatus(permissions.BasePermission):
	"""allow user to update their own status"""

	def has_object_permission(self,request,view,obj):
		"""checks the user is trying to uupdaste their own status"""

		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.user_profile.id==request.user.id