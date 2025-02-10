from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from polygon.models import CompanyPolygon


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        return token

    def validate(self, attrs):
        

        data = super().validate(attrs)

        user = self.user

        data["user_id"] = user.id
        data["username"] = user.username
        data["email"] = user.email
        try:
            data["company_inn"] = user.companies_polygon.values_list('inn', flat=True)
        except:
            data["company_inn"] = None
        try:
            data["company_name"] = user.companies_polygon.values_list('name', flat=True)
        except:
            data["company_name"] = None        
        data["groups"] = user.groups.values_list('name', flat=True)

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer