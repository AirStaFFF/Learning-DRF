from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from jobs.serializers import JobOfferListSerializer, CompanyListSerializer
from jobs.models import jobOffer, Company

class JobOfferListApiView(APIView):

    def get(self, request):
        joboffers = jobOffer.objects.all()
        serializer = JobOfferListSerializer(joboffers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOfferListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobOfferDetailsApiView(APIView):

    def get_object(self, pk):
        offer = get_object_or_404(jobOffer, pk=pk)
        return offer

    def get(self, request, pk):
        offer = self.get_object(pk)
        serializer = JobOfferListSerializer(offer)
        return Response(serializer.data)

    def put(self, request, pk):
        offer = self.get_object(pk)
        serializer = JobOfferListSerializer(offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        offer = self.get_object(pk)
        offer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CompanyListApiView(APIView):

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanyListSerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanyListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailsApiView(APIView):

    def get_object(self, pk):
        company = get_object_or_404(Company, pk=pk)
        return company

    def get(self, request, pk):
         company = self.get_object(pk)
         serializer = CompanyListSerializer(company)
         return Response(serializer.data)

    def post(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanyListSerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)