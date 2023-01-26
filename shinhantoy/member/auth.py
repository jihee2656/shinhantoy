from django.contrib.auth.hashers import check_password
from .models import Member

class MemberAuth:
    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        if not username or not password:
            if request.user.is_authenticated:
                return request.user
            return None #None 생략해도 상관없음
                
        try:
            member = Member.objects.get(username=username)
        except Member.DoesNotExist:
            return None

        print (member, member.status)
        if check_password(password, member.password):
            if member.status == '일반':
                return member
        return None

    def get_user(self, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return None
        return member

