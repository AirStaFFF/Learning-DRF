from rest_framework import serializers
from jobs.models import jobOffer, Company

class JobOfferListSerializer(serializers.ModelSerializer):

    class Meta:
        model = jobOffer
        fields = "__all__"

class CompanyListSerializer(serializers.ModelSerializer):

    offers = JobOfferListSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"

