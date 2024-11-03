from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.models import JobPosting
from api.serializers import JobPostingSerializer
from rest_framework import status
from drf_spectacular.utils import extend_schema

class JobPostingAPI(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        job_postings = JobPosting.objects.all()
        serializer = JobPostingSerializer(job_postings, many=True)
        return Response(serializer.data)
    
    @extend_schema(request=JobPostingSerializer,
                   responses={201: JobPostingSerializer}
                   )
    def post(self, request):
        serializer = JobPostingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class JobPostingDetailsAPI(APIView):
    #permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return JobPosting.objects.get(pk=pk)
        except JobPosting.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    @extend_schema(request=JobPostingSerializer,
                   responses={200: JobPostingSerializer}
                   )
    def put(self, request, job_id: int):
        job_posting = self.get_object(job_id)
        serializer = JobPostingSerializer(job_posting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, job_id: int):
        job_posting = self.get_object(job_id)
        job_posting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
