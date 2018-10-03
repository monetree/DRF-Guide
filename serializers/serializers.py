from rest_framework import serializers
from .models import Company,Language,Frameworks,Technologies


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_name','started_from','country','email','website','ip','active','language')


class GetLanguageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Language
        fields = ('language_name','language_logo','created_on','latest_build_on','latest_version','company','technology')

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('language_name','language_logo','created_on','latest_build_on','latest_version','company','technology')


class GetFrameworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frameworks
        fields = '__all__'
        depth = 1

class FrameworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frameworks
        fields = '__all__'


class GetTechnologiesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Technologies
        fields = '__all__'

class TechnologiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Technologies
        fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super(TechnologiesSerializer, self).to_representation(instance)
    #     rep['language'] = instance.language
    #     return rep
